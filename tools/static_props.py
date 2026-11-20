#!/usr/bin/env python3
"""Keep static Action 0 cost/speed fallbacks in sync with the graphics callbacks.

NewGRF purchase callbacks (CB 0x36) are what OpenTTD uses in-game, but AIs such
as AAAHogEX read the static Action 0 properties.  Leaving 0x0B (cost factor) and
0x0C (speed) unset makes those AIs divide by zero, so every aircraft gets a
static fallback that mirrors its graphics-block value.

Usage:
    python tools/static_props.py --check   # CI: fail on missing/out-of-sync values
    python tools/static_props.py --write   # one-off migration / keep sources in sync
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GFX_DIR = ROOT / "src" / "gfx"

ITEM_RE = re.compile(r"(?m)^[ \t]*item\s*\(\s*FEAT_AIRCRAFT\s*,\s*([A-Za-z0-9_]+)\s*\)\s*\{")
PROPERTY_RE = re.compile(r"\bproperty\s*\{")
GRAPHICS_RE = re.compile(r"\bgraphics\s*\{")
COST_RE = re.compile(r"(?m)^[ \t]*cost_factor:\s*(\d+)\s*;")
SPEED_RE = re.compile(r"purchase_speed:\s*plane_speed_kmh\((\d+)\)")
RUNNING_RE = re.compile(r"(?m)^[ \t]*purchase_running_cost_factor:\s*(\d+)\s*;")
STATIC_COST_RE = re.compile(r"(?m)^[ \t]*cost_factor:\s*(\d+)\s*;")
STATIC_SPEED_RE = re.compile(r"(?m)^[ \t]*speed:\s*(\d+)\s*km/h\s*;")
STATIC_RUNNING_RE = re.compile(r"(?m)^[ \t]*running_cost_factor:\s*(\d+)\s*;")
STATIC_LINE_RE = re.compile(
    r"(?m)^[ \t]*(?:cost_factor|speed|running_cost_factor):[^\r\n]*(?:\r?\n|\r)?"
)


def find_matching_brace(text: str, open_idx: int) -> int:
    depth = 0
    for idx in range(open_idx, len(text)):
        char = text[idx]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return idx
    raise ValueError("unbalanced braces")


def find_main_item(text: str) -> tuple[int, int, str] | None:
    """Return (open_idx, close_idx, vehicle_id) for the item with a graphics block."""
    for match in ITEM_RE.finditer(text):
        open_idx = match.end() - 1
        close_idx = find_matching_brace(text, open_idx)
        block = text[open_idx : close_idx + 1]
        if GRAPHICS_RE.search(block):
            return open_idx, close_idx, match.group(1)
    return None


def parse_file(path: Path) -> dict:
    text = path.read_bytes().decode("utf-8")
    found = find_main_item(text)
    if found is None:
        raise ValueError(f"{path}: no aircraft item with a graphics block")
    item_open, item_close, vehicle_id = found
    block = text[item_open : item_close + 1]

    prop_match = PROPERTY_RE.search(block)
    gfx_match = GRAPHICS_RE.search(block)
    if prop_match is None or gfx_match is None:
        raise ValueError(f"{path}: item {vehicle_id} is missing property/graphics blocks")

    prop_open = block.find("{", prop_match.end() - 1)
    prop_close = find_matching_brace(block, prop_open)
    gfx_open = block.find("{", gfx_match.end() - 1)
    gfx_close = find_matching_brace(block, gfx_open)

    gfx_text = block[gfx_open + 1 : gfx_close]
    cost = COST_RE.search(gfx_text)
    speed = SPEED_RE.search(gfx_text)
    running = RUNNING_RE.search(gfx_text)
    if cost is None or speed is None or running is None:
        raise ValueError(
            f"{path}: item {vehicle_id} is missing cost_factor/purchase_speed/"
            f"purchase_running_cost_factor in its graphics block"
        )

    return {
        "path": path,
        "text": text,
        "vehicle_id": vehicle_id,
        "item_open": item_open,
        "item_close": item_close,
        "prop_open": item_open + prop_open,
        "prop_close": item_open + prop_close,
        "cost": int(cost.group(1)),
        "cruise": int(speed.group(1)),
        "running": int(running.group(1)),
    }


def check_file(parsed: dict) -> list[str]:
    path = parsed["path"]
    prop_text = parsed["text"][parsed["prop_open"] + 1 : parsed["prop_close"]]
    problems = []
    checks = (
        ("cost_factor", STATIC_COST_RE, min(parsed["cost"], 255)),
        ("speed (km/h)", STATIC_SPEED_RE, parsed["cruise"]),
        ("running_cost_factor", STATIC_RUNNING_RE, min(parsed["running"], 255)),
    )
    for label, regex, expected in checks:
        match = regex.search(prop_text)
        if match is None:
            problems.append(f"{path}: {parsed['vehicle_id']} missing static {label}")
        elif int(match.group(1)) != expected:
            problems.append(
                f"{path}: {parsed['vehicle_id']} static {label} is {match.group(1)}, "
                f"expected {expected}"
            )
    return problems


def write_file(parsed: dict) -> bool:
    text = parsed["text"]
    prop_text = text[parsed["prop_open"] + 1 : parsed["prop_close"]]
    newline = "\r\n" if "\r\n" in text else "\n"
    stripped = STATIC_LINE_RE.sub("", prop_text).rstrip()
    trailing = prop_text[len(prop_text.rstrip()) :]
    block = (
        f"{newline}    cost_factor: {min(parsed['cost'], 255)};"
        f"{newline}    speed: {parsed['cruise']} km/h;"
        f"{newline}    running_cost_factor: {min(parsed['running'], 255)};"
    )
    new_prop_text = stripped + block + trailing
    new_text = text[: parsed["prop_open"] + 1] + new_prop_text + text[parsed["prop_close"] :]
    if new_text == text:
        return False
    parsed["path"].write_bytes(new_text.encode("utf-8"))
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="fail on missing or out-of-sync values")
    mode.add_argument("--write", action="store_true", help="add or update the static values")
    args = parser.parse_args()

    files = sorted(GFX_DIR.rglob("*.pnml"))
    problems: list[str] = []
    changed = 0
    parsed_count = 0

    for path in files:
        try:
            parsed = parse_file(path)
        except ValueError as exc:
            problems.append(str(exc))
            continue
        parsed_count += 1
        if args.check:
            problems.extend(check_file(parsed))
        elif write_file(parsed):
            changed += 1

    if args.check:
        if problems:
            for problem in problems:
                print(f"[FAIL] {problem}")
            print(f"\n{len(problems)} problem(s) across {parsed_count} aircraft files.")
            return 1
        print(f"All {parsed_count} aircraft files have static cost/speed/running-cost fallbacks.")
        return 0

    print(f"Updated {changed} of {parsed_count} aircraft files.")
    if problems:
        for problem in problems:
            print(f"[FAIL] {problem}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
