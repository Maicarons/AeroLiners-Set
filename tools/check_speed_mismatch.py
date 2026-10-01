#!/usr/bin/env python3
"""Verify the aircraft speed convention across src/gfx/**/*.pnml.

Required invariant (see tools/fix_speed_constant.py):
  - every aircraft has a speed callback of the constant form:
        switch (FEAT_AIRCRAFT, SELF, <id>_speed, flight_state())
        {
          return plane_speed_kmh(CRUISE);
        }
  - the constant equals the file's purchase_speed value;
  - switches still using per-flight_state branches (12..13 / 15 / 18 /
    16..20 / 21..22) are reported as legacy and must be converted.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src" / "gfx"

RE_SPEED_SWITCH = re.compile(
    r"switch \(FEAT_AIRCRAFT, SELF, (\w+)_speed, flight_state\(\)\)\s*\{([^}]*)\}"
)
RE_PURCHASE = re.compile(r"purchase_speed:\s*plane_speed_kmh\(\s*(\d+)\s*\)")
RE_CONSTANT = re.compile(r"^\s*return\s+plane_speed_kmh\(\s*(\d+)\s*\)\s*;", re.M)


def main() -> int:
    files = sorted(ROOT.rglob("*.pnml"))
    ok = 0
    problems: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        switches = RE_SPEED_SWITCH.findall(text)
        if not switches:
            problems.append(f"{path}: no speed switch")
            continue
        pm = RE_PURCHASE.search(text)
        purchase = int(pm.group(1)) if pm else None
        if purchase is None:
            problems.append(f"{path}: no purchase_speed")
        for name, body in switches:
            m = RE_CONSTANT.match(body.strip()) if len(RE_CONSTANT.findall(body)) == 1 else None
            # only accept when the body is exactly one constant return (plus comments)
            returns = RE_CONSTANT.findall(body)
            if len(returns) != 1:
                problems.append(f"{path}: {name}_speed is not constant form ({len(returns)} returns)")
                continue
            if int(returns[0]) != purchase:
                problems.append(
                    f"{path}: {name}_speed constant {returns[0]} != purchase_speed {purchase}"
                )
                continue
            ok += 1
    print(f"aircraft files: {len(files)}, constant-form switches ok: {ok}")
    if problems:
        print(f"problems: {len(problems)}")
        for p in problems:
            print(f"  !! {p}")
        return 1
    print("all speed callbacks follow the constant-cruise convention")
    return 0


if __name__ == "__main__":
    sys.exit(main())
