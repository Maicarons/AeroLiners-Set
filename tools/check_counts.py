#!/usr/bin/env python3
"""Verify that hard-coded fleet counts in public-facing docs match reality.

The source of truth is generated automatically and stays in sync with the
source tree:

  * docs/aircraft/summary.json  -> aircraft / liveries / manufacturers
  * lang/*.lng                  -> interface language file count

This script greps the documented counts out of the public docs (README,
the docs site home pages, and the project-structure guide) and fails if any
of them disagrees with the source of truth. It is wired into CI
(.github/workflows/release.yml) so that expanding the fleet can never again
silently leave the public-facing counts stale.

Only numbers that appear *with their unit* are matched, so incidental
figures (e.g. the 65535 engine-pool limit, the 1743 sprite-PNG count, the
129 greyscale PNGs) are never flagged.

Run from anywhere; the repo root is derived from this file's location.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# metric -> regex used to extract the *documented* number from each file.
# Each regex must capture exactly the digit(s) that form the count.
CHECKS: dict[str, dict[str, str]] = {
    "README.md": {
        "aircraft": r"\*\*(\d+)\*\*\s*个机型",
        "liveries": r"\*\*(\d+)\*\*\s*种涂装",
        "manufacturers": r"\*\*(\d+)\*\*\s*家制造商",
        "languages": r"\*\*(\d+)\*\*\s*种界面语言文件",
    },
    "README.en.md": {
        "aircraft": r"\*\*(\d+)\*\*\s*aircraft models",
        "liveries": r"\*\*(\d+)\*\*\s*liveries",
        "manufacturers": r"\*\*(\d+)\*\*\s*manufacturers",
        "languages": r"\*\*(\d+)\*\*\s*interface language files",
    },
    "docs/index.md": {
        "aircraft": r"(\d+)\s*(?:款机型|种真实世界客机)",
        "liveries": r"(\d+)\s*种涂装",
        "languages": r"(\d+)\s*种语言文件",
    },
    "docs/en/index.md": {
        "aircraft": r"(\d+)\s*(?:real-world airliner|models)",
        "liveries": r"(\d+)\s*liveries",
        "languages": r"(\d+)\s*built-in language files",
    },
    "docs/guide/project-structure.md": {
        "aircraft": r"\*\*(\d+)\*\*\s*个机型",
        "liveries": r"逻辑涂装数\s*(\d+)",
        "languages": r"(\d+)\s*种语言文件",
    },
}


def load_truths() -> dict[str, int]:
    summary_path = REPO_ROOT / "docs" / "aircraft" / "summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    lang_count = len(list((REPO_ROOT / "lang").glob("*.lng")))
    return {
        "aircraft": int(summary["total_aircraft"]),
        "liveries": int(summary["total_liveries"]),
        "manufacturers": len(summary["manufacturers"]),
        "languages": lang_count,
    }


def main() -> int:
    truths = load_truths()
    print("Source of truth (generated from source tree):")
    for key, value in truths.items():
        print(f"  {key:14s} = {value}")

    failures = 0
    for rel_path, metrics in CHECKS.items():
        path = REPO_ROOT / rel_path
        if not path.exists():
            print(f"[SKIP] {rel_path}: file not found")
            continue
        text = path.read_text(encoding="utf-8")
        for metric, pattern in metrics.items():
            expected = truths[metric]
            matches = re.findall(pattern, text)
            if not matches:
                print(f"[MISSING]  {rel_path}: no '{metric}' count matched by /{pattern}/")
                failures += 1
                continue
            values = [int(m) for m in matches]
            if any(v != expected for v in values):
                print(
                    f"[MISMATCH] {rel_path}: '{metric}' documented as "
                    f"{[v for v in values if v != expected]} (all matches: {values}), "
                    f"expected {expected}"
                )
                failures += 1
            else:
                print(f"[OK]       {rel_path}: '{metric}' = {expected}")

    if failures:
        print(f"\nFAILED: {failures} count check(s) disagree with the source of truth.")
        print("Update the docs (or, if the source changed, regenerate summary.json).")
        return 1

    print("\nAll documented fleet counts match the source of truth.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
