#!/usr/bin/env python3
"""Fix in-flight speed (flight_state 16..20) to match purchase_speed.

Bug: every aircraft advertised purchase_speed / state-18 as cruise max,
but the speed callback returned a much lower value for states 16..20
(the actual in-flight range). Players therefore never reached the
displayed maximum (e.g. L-188: shown 591, actually capped at 373).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src" / "gfx"

RE_PURCHASE = re.compile(r"(purchase_speed:\s*plane_speed_kmh\(\s*)(\d+)(\s*\))")
RE_STATE18 = re.compile(r"(18:\s*return\s*plane_speed_kmh\(\s*)(\d+)(\s*\))")
RE_INFLIGHT = re.compile(r"(16\.\.20:\s*return\s*plane_speed_kmh\(\s*)(\d+)(\s*\))")


def fix_file(path: Path, dry_run: bool = False) -> tuple[bool, str | None]:
    text = path.read_text(encoding="utf-8", errors="replace")
    purchase = RE_PURCHASE.search(text)
    inflight = RE_INFLIGHT.search(text)
    if not purchase or not inflight:
        return False, f"missing purchase or inflight in {path.name}"

    target = int(purchase.group(2))
    current = int(inflight.group(2))
    if current == target:
        return False, None

    new_text = RE_INFLIGHT.sub(
        lambda m: m.group(1) + str(target) + m.group(3),
        text,
        count=1,
    )
    # keep state-18 in sync with purchase_speed as well
    s18 = RE_STATE18.search(new_text)
    if s18 and int(s18.group(2)) != target:
        new_text = RE_STATE18.sub(
            lambda m: m.group(1) + str(target) + m.group(3),
            new_text,
            count=1,
        )

    if not dry_run:
        path.write_text(new_text, encoding="utf-8", newline="\n")
    return True, f"{path.relative_to(ROOT.parent.parent)}: 16..20 {current} -> {target}"


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    changed = 0
    skipped = 0
    errors = []
    for path in sorted(ROOT.rglob("*.pnml")):
        text = path.read_text(encoding="utf-8", errors="replace")
        if "plane_speed_kmh" not in text:
            continue
        ok, msg = fix_file(path, dry_run=dry_run)
        if ok:
            changed += 1
            print(msg or "")
        elif msg:
            errors.append(msg)
        else:
            skipped += 1

    mode = "would change" if dry_run else "changed"
    print(f"\n{mode} {changed} files, already-ok {skipped}, problems {len(errors)}")
    for e in errors:
        print(f"  !! {e}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
