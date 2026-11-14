#!/usr/bin/env python3
"""AeroLiners Set release bundling: one implementation shared by CMake and CI.

Config: bundle.json (repo root) is the single source of truth for GRFID, version,
project name, GRF filename, bundled docs and archive naming. Every consumer
(CMakeLists.txt, .github/workflows/release.yml) calls this script instead of
duplicating that metadata.

Subcommands:
  info   [--key K]      print one resolved value (or all key=value lines)
  build                 write bin/<grfid>-<name>-<version>.tar and .tar.gz, then verify
  verify <tar> [--ref]  check layout, GRF ID, doc line endings and (optionally) MD5

BaNaNa / OpenTTD content-download layout:
  <grfid>-<name>-<version>.tar
    <name>-<version>/
      <grf_file>
      readme.txt  license.txt  changelog.txt
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import sys
import tarfile
import time
import zlib
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "bundle.json"
EPOCH_2000 = datetime(2000, 1, 1, tzinfo=timezone.utc)


class BundleError(Exception):
    pass


def load_config(path: Path) -> dict:
    if not path.is_file():
        raise BundleError(f"config not found: {path}")
    with path.open("r", encoding="utf-8") as fh:
        cfg = json.load(fh)
    for key in ("grfid", "name", "version", "grf_file", "nml_file", "src_file",
                "bin_dir", "docs_src_dir", "docs", "bundle_dir", "archive"):
        if key not in cfg:
            raise BundleError(f"bundle.json is missing required key: {key}")
    return cfg


def render(template: str, cfg: dict) -> str:
    return template.format(
        name=cfg["name"],
        version=cfg["version"],
        grfid=cfg["grfid"],
        grfid_text=cfg.get("grfid_text", ""),
    )


def repo_revision() -> int:
    """Days since 2000-01-01 UTC — the NewGRF internal version number."""
    return (datetime.now(timezone.utc) - EPOCH_2000).days


def resolve(cfg: dict) -> dict:
    bundle_dir = render(cfg["bundle_dir"], cfg)
    archive = render(cfg["archive"], cfg)
    archive_gz = archive + ".gz"
    bin_dir = cfg["bin_dir"]
    docs_src_dir = cfg["docs_src_dir"]
    docs = list(cfg["docs"])
    changelog = next((d for d in docs if "changelog" in d.lower()), "changelog.txt")
    return {
        "bundle_dir": bundle_dir,
        "archive": archive,
        "archive_gz": archive_gz,
        "archive_path": f"{bin_dir}/{archive}",
        "archive_gz_path": f"{bin_dir}/{archive_gz}",
        "grf_path": f"{bin_dir}/{cfg['grf_file']}",
        "nml_path": f"{bin_dir}/{cfg['nml_file']}",
        "src_path": cfg["src_file"],
        "changelog_path": f"{docs_src_dir}/{changelog}",
        "repo_revision": str(repo_revision()),
    }


def info_values(cfg: dict) -> dict:
    values = {k: str(v) for k, v in cfg.items() if not isinstance(v, (list, dict))}
    values["docs"] = " ".join(cfg["docs"])
    values.update(resolve(cfg))
    return values


PLACEHOLDER_RE = re.compile(r"\$" r"\{([A-Za-z0-9_]+)\}")


def render_doc(path: Path, placeholders: dict) -> bytes:
    if not path.is_file():
        raise BundleError(f"bundled doc not found: {path}")
    text = path.read_text(encoding="utf-8")

    def repl(match):
        return placeholders.get(match.group(1), match.group(0))

    text = PLACEHOLDER_RE.sub(repl, text)
    # BaNaNaS / OpenTTD tooling runs on Linux: always ship LF line endings.
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text.encode("utf-8")


def grfid_matches(data: bytes, expected_hex: str) -> bool:
    """Check the GRF ID (ACTION8) of a .grf file (Container 2 / 0 / 1)."""
    expected = bytes.fromhex(expected_hex)
    try:
        if data[:6] == b"\x00\x00GRF\x82":
            if data[6:10] != b"\x0d\x0a\x1a\x0a":
                raise ValueError("bad container 2 signature")
            body = data[15:] if data[14] == 0 else zlib.decompress(data[15:])
        elif data[:3] == b"GRF":
            body = data
        else:
            raise ValueError("not a GRF file (bad magic)")
        return body.find(b"\x08" + expected) != -1
    except (ValueError, zlib.error) as exc:
        print(f"  ERROR: cannot parse GRF container: {exc}")
        return False


def build(cfg: dict) -> int:
    vals = resolve(cfg)
    grf_abs = REPO_ROOT / vals["grf_path"]
    if not grf_abs.is_file():
        raise BundleError(f"GRF not found: {grf_abs} (build the GRF target first)")
    grf_bytes = grf_abs.read_bytes()
    md5 = hashlib.md5(grf_bytes).hexdigest()
    rev = vals["repo_revision"]
    placeholders = {
        "GRF_REVISION": rev,
        "GRF_MD5": md5,
        "VERSION": cfg["version"],
        "NEWGRF_VERSION": cfg["version"],
        "GRF_NAME": cfg.get("brand_en", cfg["name"]),
        "GRF_ID": cfg["grfid"],
        "GRF_FILE": cfg["grf_file"],
        "PROJECT_NAME": cfg["name"],
        "HOMEPAGE": cfg.get("homepage", ""),
        "LICENSE": cfg.get("license", ""),
    }
    docs_src = REPO_ROOT / cfg["docs_src_dir"]
    top = vals["bundle_dir"] + "/"
    members = [(top + cfg["grf_file"], grf_bytes)]
    for doc in cfg["docs"]:
        members.append((top + doc, render_doc(docs_src / doc, placeholders)))

    mtime = int(os.environ.get("SOURCE_DATE_EPOCH", str(int(time.time()))))
    out_tar = REPO_ROOT / vals["archive_path"]
    out_gz = REPO_ROOT / vals["archive_gz_path"]
    out_tar.parent.mkdir(parents=True, exist_ok=True)

    def write_tar(path: Path, mode: str) -> None:
        with tarfile.open(path, mode) as tf:
            di = tarfile.TarInfo(name=top)
            di.type = tarfile.DIRTYPE
            di.mode = 0o755
            di.mtime = mtime
            tf.addfile(di)
            for name, payload in members:
                ti = tarfile.TarInfo(name=name)
                ti.size = len(payload)
                ti.mode = 0o644
                ti.mtime = mtime
                ti.uid = 0
                ti.gid = 0
                ti.uname = ""
                ti.gname = ""
                tf.addfile(ti, io.BytesIO(payload))

    write_tar(out_tar, "w")
    write_tar(out_gz, "w:gz")

    print(f"Built: {vals['archive_path']} ({out_tar.stat().st_size} bytes)")
    print(f"Built: {vals['archive_gz_path']} ({out_gz.stat().st_size} bytes)")
    print(f"GRF revision: {rev}   GRF MD5: {md5}")
    print(f"Layout: {vals['bundle_dir']}/ -> {cfg['grf_file']} + {', '.join(cfg['docs'])}")

    rc = verify(cfg, out_tar, grf_abs, cfg["grfid"])
    rc |= verify(cfg, out_gz, grf_abs, cfg["grfid"])
    return rc


def verify(cfg: dict, bundle: Path, ref: Path | None, grfid: str) -> int:
    vals = resolve(cfg)
    expected_top = vals["bundle_dir"]
    expected_grf = cfg["grf_file"]
    expected_docs = list(cfg["docs"])
    print(f"Verifying {bundle} ...")
    ok = True
    grf_data = b""
    readme_data = b""
    with tarfile.open(bundle, "r:*") as tf:
        members = tf.getmembers()
        for m in members:
            n = m.name.replace("\\", "/")
            if n.startswith("/") or ".." in n.split("/"):
                print("  ERROR: unsafe member path: " + n)
                ok = False
        files = {m.name.replace("\\", "/"): m for m in members if m.isfile()}
        tops = sorted({n.split("/")[0] for n in files})
        if len(tops) != 1:
            print(f"  ERROR: expected exactly one top-level directory, got {tops}")
            ok = False
            top = tops[0] if tops else ""
        else:
            top = tops[0]
            if top != expected_top:
                print(f"  ERROR: top-level directory is '{top}', expected '{expected_top}'")
                ok = False
            else:
                print(f"  OK: top-level directory: {top}/")
        rel = {n[len(top) + 1:] for n in files if n.startswith(top + "/")}
        expected = set([expected_grf] + expected_docs)
        missing = sorted(expected - rel)
        if missing:
            print(f"  ERROR: missing files: {missing}")
            ok = False
        extra = sorted(rel - expected)
        if extra:
            print(f"  WARNING: unexpected extra files: {extra}")
        if not missing:
            print(f"  OK: required files present: {expected_grf}, {', '.join(expected_docs)}")
        grf_member = files.get(top + "/" + expected_grf)
        if grf_member is None:
            print(f"  ERROR: {expected_grf} not found in bundle")
            ok = False
        else:
            grf_data = tf.extractfile(grf_member).read()
        for doc in expected_docs:
            m = files.get(top + "/" + doc)
            if m is None:
                continue
            data = tf.extractfile(m).read()
            if b"\r" in data:
                print(f"  ERROR: {doc} contains CR bytes (must be LF-only)")
                ok = False
            if doc == "readme.txt":
                readme_data = data

    if grf_data:
        if grfid_matches(grf_data, grfid):
            print(f"  OK: GRF ID matches {grfid}")
        else:
            print(f"  ERROR: GRF ID does not match {grfid}")
            ok = False
        md5_in_tar = hashlib.md5(grf_data).hexdigest()
        if readme_data:
            if b"$" b"{GRF_MD5}" in readme_data or b"$" b"{GRF_REVISION}" in readme_data:
                print("  ERROR: readme.txt still has unsubstituted placeholders")
                ok = False
            elif md5_in_tar.encode() not in readme_data:
                print("  ERROR: readme.txt MD5 does not match the bundled GRF")
                ok = False
            else:
                print(f"  OK: readme.txt reports the bundled GRF MD5 ({md5_in_tar})")
        if ref is not None:
            ref_path = Path(ref)
            if not ref_path.is_file():
                print(f"  ERROR: reference GRF not found: {ref_path}")
                ok = False
            else:
                ref_md5 = hashlib.md5(ref_path.read_bytes()).hexdigest()
                if ref_md5 == md5_in_tar:
                    print(f"  OK: GRF MD5 matches reference ({ref_md5})")
                else:
                    print(f"  ERROR: GRF MD5 mismatch: bundle={md5_in_tar} ref={ref_md5}")
                    ok = False
    else:
        ok = False

    print("VERIFY RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="AeroLiners Set release bundling")
    parser.add_argument("--config", default=str(CONFIG_PATH), help="path to bundle.json")
    sub = parser.add_subparsers(dest="command", required=True)

    p_info = sub.add_parser("info", help="print resolved release metadata")
    p_info.add_argument("--key", help="print a single value; omit for all key=value lines")
    sub.add_parser("build", help="build tar + tar.gz and self-verify")
    p_verify = sub.add_parser("verify", help="verify an existing bundle")
    p_verify.add_argument("bundle", help="path to the .tar / .tar.gz bundle")
    p_verify.add_argument("--ref", help="reference .grf for MD5 comparison")
    p_verify.add_argument("--grfid", help="override expected GRF ID (8 hex digits)")

    args = parser.parse_args()
    try:
        cfg = load_config(Path(args.config))
        if args.command == "info":
            values = info_values(cfg)
            if args.key:
                if args.key not in values:
                    print(f"Unknown info key: {args.key}", file=sys.stderr)
                    print("Available: " + ", ".join(sorted(values)), file=sys.stderr)
                    return 2
                print(values[args.key])
            else:
                for k in sorted(values):
                    print(f"{k}={values[k]}")
            return 0
        if args.command == "build":
            return build(cfg)
        if args.command == "verify":
            grfid = args.grfid or cfg["grfid"]
            return verify(cfg, Path(args.bundle), Path(args.ref) if args.ref else None, grfid)
    except (BundleError, OSError, tarfile.TarError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 2


if __name__ == "__main__":
    sys.exit(main())
