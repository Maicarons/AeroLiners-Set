#!/usr/bin/env python3
"""Rewrite every aircraft speed callback to a constant cruise speed.

Background (see docs/guide and OpenTTD src/aircraft_cmd.cpp):
  - `graphics { speed: X_speed; }` is compiled by NML to callback 0x36
    (CBID_VEHICLE_MODIFY_PROPERTY) with var10 = the aircraft speed property.
  - OpenTTD evaluates that callback only inside UpdateAircraftCache(), i.e.
    at vehicle creation, airport state/position changes and savegame load,
    and caches the result in vcache.cached_max_speed.
  - A speed switch keyed on flight_state() therefore gets "stuck" on the
    value of whichever state was active at the last cache refresh:
      * in live play planes stayed at runway speed after liftoff;
      * after save/reload the cached value reset to cruise, so the
        runway/decision speed became the cruise speed.
  - The fix: return the cruise speed unconditionally. OpenTTD's native
    airport movement limits (SPEED_LIMIT_TAXI=50, APPROACH=230, HOLD=425,
    braking=50 km-ish/h) already provide realistic taxi/approach/braking
    slowdown, derived from the cruise speed, and are save/load stable.

The constant must equal the aircraft's purchase_speed (displayed cruise).
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
RE_CRUISE_IN_BLOCK = re.compile(r"plane_speed_kmh\(\s*(\d+)\s*\)")

MARKER = "speed-constant"

COMMENT = (
    "  // [speed-constant] 巡航速度恒定，不随飞行状态变化。\n"
    "  // OpenTTD 将速度属性回调（CB36）的结果缓存于 cached_max_speed，仅在载具\n"
    "  // 创建、机场状态切换和读档时刷新；按 flight_state 返回不同速度会让缓存\n"
    "  // 卡在旧值上（起飞后停在跑道速度；读档后跑道速度变成巡航速度）。\n"
    "  // 滑行/进近/刹车减速由游戏原生状态机按巡航速度自动派生，无需在此压低。\n"
)


def build_block(name: str, cruise: int) -> str:
    return (
        f"switch (FEAT_AIRCRAFT, SELF, {name}_speed, flight_state())\n"
        "{\n"
        f"{COMMENT}"
        f"  return plane_speed_kmh({cruise}); // cruise, keep in sync with purchase_speed\n"
        "}"
    )


def is_constant_form(body: str) -> bool:
    return MARKER in body


def fix_file(path: Path, dry_run: bool = False) -> tuple[bool, str | None]:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = RE_SPEED_SWITCH.search(text)
    if not m:
        return False, f"no speed switch in {path}"
    name, body = m.group(1), m.group(2)

    pm = RE_PURCHASE.search(text)
    if not pm:
        return False, f"no purchase_speed in {path}"
    cruise = int(pm.group(1))

    if is_constant_form(body):
        # Already fixed; only realign the constant if it drifted from purchase_speed.
        cm = RE_CRUISE_IN_BLOCK.search(body)
        if cm and int(cm.group(1)) == cruise:
            return False, None
        if not cm:
            return False, f"constant form but no plane_speed_kmh in {path}"
        new_block = build_block(name, cruise)
        if not dry_run:
            text = text[: m.start()] + new_block + text[m.end():]
            path.write_text(text, encoding="utf-8", newline="\n")
        return True, f"{path.relative_to(ROOT.parent.parent)}: realign {cm.group(1)} -> {cruise}"

    new_block = build_block(name, cruise)
    if not dry_run:
        text = text[: m.start()] + new_block + text[m.end():]
        path.write_text(text, encoding="utf-8", newline="\n")
    return True, f"{path.relative_to(ROOT.parent.parent)}: {name}_speed -> constant {cruise}"


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    changed = 0
    skipped = 0
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.pnml")):
        try:
            ok, msg = fix_file(path, dry_run=dry_run)
        except Exception as exc:  # pragma: no cover
            errors.append(f"{path}: {exc}")
            continue
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
    raise SystemExit(main())
