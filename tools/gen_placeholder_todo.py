"""从权威的中文占位 TODO 文档（docs/guide/placeholder-aircraft-todo.md）解析 71 款占位机数据，
机械生成英文版（docs/en/guide/placeholder-aircraft-todo.md），保证中英文数据一致。

解析内容：
  - 主表（71 行）：# / 机型(en) / 中文名 / 引入年 / 座级 / 航程 / 速度 / 成本 / donor / 优先级
  - 详情表（13–71 行）：# / 机型 / 源文件 / donor   （用于英文详情区的源文件路径）
  - 1–12 款源文件路径硬编码（中文详情区为散文，无表格）

用法:
    python tools/gen_placeholder_todo.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"G:/GitHub/AeroLiners-Set")
ZH = ROOT / "docs" / "guide" / "placeholder-aircraft-todo.md"
EN = ROOT / "docs" / "en" / "guide" / "placeholder-aircraft-todo.md"

# 1–12 款源文件路径（中文详情区为散文，无表格可解析）
SRC_1_12 = {
    "COMAC C909": "src/gfx/COMAC/C909/C909.pnml",
    "COMAC C919": "src/gfx/COMAC/C919/C919.pnml",
    "Airbus A220-300": "src/gfx/Airbus/A220/A220-300/A220-300.pnml",
    "Airbus A319neo": "src/gfx/Airbus/A320/A319neo/A319neo.pnml",
    "Airbus A321neo": "src/gfx/Airbus/A320/A321neo/A321neo.pnml",
    "Boeing 737 MAX 9": "src/gfx/Boeing/B737/B737MAX9/B737MAX9.pnml",
    "Boeing 737 MAX 10": "src/gfx/Boeing/B737/B737MAX10/B737MAX10.pnml",
    "Boeing 787-10": "src/gfx/Boeing/B787/B787-10/B787-10.pnml",
    "Airbus A330-900neo": "src/gfx/Airbus/A330/A330-900neo/A330-900neo.pnml",
    "Airbus A350-1000": "src/gfx/Airbus/A350/A350-1000/A350-1000.pnml",
    "Boeing 777X": "src/gfx/Boeing/B777/B777X/B777X.pnml",
    "Embraer E195-E2": "src/gfx/Embraer/E195/E195-E2/E195-E2.pnml",
}

MAIN_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*`([^`]+?)`\s*\|\s*(.+?)\s*\|\s*$"
)
DETAIL_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+?)`\s*\|\s*`([^`]+?)`\s*\|\s*$"
)

EMOJI_LEVEL = {"高": "High", "中": "Medium", "低": "Low"}


def parse(text: str):
    rows = []
    detail_src = {}
    for line in text.splitlines():
        m = MAIN_RE.match(line)
        if m:
            num, model, zh, year, seats, rng, speed, cost, donor, prio = m.groups()
            level = "Low"
            for k, v in EMOJI_LEVEL.items():
                if k in prio:
                    level = v
                    break
            emoji = prio.strip()[0] if prio.strip() else ""
            rows.append(
                {
                    "num": int(num),
                    "model": model.strip(),
                    "zh": zh.strip(),
                    "year": int(year),
                    "seats": int(seats),
                    "range": int(rng),
                    "speed": int(speed),
                    "cost": int(cost),
                    "donor": donor.strip(),
                    "emoji": emoji,
                    "level": level,
                }
            )
            continue
        d = DETAIL_RE.match(line)
        if d:
            num, model, src, donor = d.groups()
            detail_src[model.strip()] = src.strip()
    return rows, detail_src


def src_for(row, detail_src):
    m = row["model"]
    if m in SRC_1_12:
        return SRC_1_12[m]
    return detail_src.get(m, f"src/gfx/.../{m.replace(' ', '_')}/{m.replace(' ', '_')}.pnml")


def build_en(rows, detail_src) -> str:
    L = []
    L.append("# Placeholder Aircraft TODO")
    L.append("")
    L.append(
        "This mod currently has **71 aircraft using \"placeholder graphics\"** — their model logic, "
        "real parameters, and livery switching are all fully wired and compiled into the `.grf`, but the "
        "**aircraft pixel sprites temporarily borrow the placeholder image of a similar model** "
        "(each model needs hand-drawn pixel sprites for 5 flight states × 8 frames, which is art asset work)."
    )
    L.append("")
    L.append(
        "This document records the real parameters of these 71 models, their current placeholder graphic "
        "source, and the specific task of replacing them with real pixel art."
    )
    L.append("")
    L.append(
        "> Note: This repository is an independent continuation of the upstream "
        "`RvP93/WorldAirlinersSet`. These placeholder models are additions made in this continuation; "
        "the upstream does not include them, so \"replacing the real graphics\" is future art work for this project."
    )
    L.append("")
    L.append("## How the placeholder mechanism works")
    L.append("")
    L.append(
        "In each placeholder model's `.pnml`, the `#define IMAGEFILE` points to a **donor model's PNG "
        "directory** (not its own). NML compiles by reading the donor's real sprite sheet directly, so it "
        "compiles and displays in-game fine — only the fuselage shape is the donor's."
    )
    L.append("")
    L.append("To replace with real graphics, simply:")
    L.append("")
    L.append("1. Draw the real sprite PNGs for this model in its own directory (keeping the **same sprite layout coordinates** as the donor);")
    L.append("2. Change all `#define IMAGEFILE \"src/gfx/<donor>/.../*.png\"` in the `.pnml` to point to this model's directory;")
    L.append("3. Recompile `bin/AeroLinersSet.grf` — zero logic changes.")
    L.append("")
    L.append("## TODO list (71 models)")
    L.append("")
    L.append("| # | Model | Intro yr* | Seats | Range | Speed (km/h) | Cost | Current placeholder source | Priority |")
    L.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for r in rows:
        L.append(
            f"| {r['num']} | {r['model']} | {r['year']} | {r['seats']} | {r['range']} | {r['speed']} | {r['cost']} | `{r['donor']}` | {r['emoji']} {r['level']} |"
        )
    L.append("")
    L.append("> \\* Intro year is the actual purchasable year after `get_plane_year(year) = year - 2`.")
    L.append(">")
    L.append("> Models #13–71 were **added / corrected** in this continuation (13–22 added early Aug 2026, 23–48 supplemented 2026-08-07, 49–54 Cessna added 2026-08-09, **55–71 filled from the upstream WAS full model list on 2026-08-09** — excluding renamed/merged items such as ARJ21→C909). Among these, **#49–71 have their parameters OVERRIDDEN with real specs** (seats / range / speed / cost shown are real values); the other placeholders show the donor's effective values (see \"Current placeholder source\"), not the model's true parameters.")
    L.append("> When drawing real graphics, the performance parameters should also be replaced with the model's real data.")
    L.append("")
    L.append("## Details & replacement steps")
    L.append("")
    for r in rows:
        src = src_for(r, detail_src)
        L.append(f"### {r['num']}. {r['model']}")
        L.append(f"- Source file: `{src}`")
        L.append(f"- Placeholder donor: `{r['donor']}`")
        L.append(f"- Priority: {r['emoji']} {r['level']}")
        L.append(f"- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for {r['model']} into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.")
        L.append("")
    L.append("## How to contribute real graphics")
    L.append("")
    L.append("1. Draw the sprite sheet PNGs in the model's directory, keeping the same sprite layout as the donor (use the donor's PNG as coordinate reference).")
    L.append("2. Change the `#define IMAGEFILE` in that `.pnml` to point to the model's own directory.")
    L.append("3. Recompile locally (see [Building from Source](/guide/building)) and confirm correct in-game display.")
    L.append("4. Commit / push to this repository and update the replacement status of the corresponding row in this document.")
    L.append("")
    L.append("## Automation scripts")
    L.append("")
    L.append("- `tools/add_aircraft.py`: clones a donor model to generate placeholder `.pnml` (models #1–12).")
    L.append("- `tools/gen_placeholder_aircraft.py`: the generator used for #13–54 — clones donor sprite-layout macros + model parameters, only swapping identifier / name / intro year, wiring the donor's first liveries, with zero new livery strings.")
    L.append("- `tools/gen_aircraft_docs.py`: extracts all models from `WAS.pnml` and generates the [Fleet Gallery](/aircraft/) plus livery preview images.")
    L.append("")
    return "\n".join(L)


def main() -> None:
    text = ZH.read_text(encoding="utf-8")
    rows, detail_src = parse(text)
    print(f"解析到 {len(rows)} 款占位机")
    en = build_en(rows, detail_src)
    EN.write_text(en, encoding="utf-8")
    print(f"已生成 {EN}")


if __name__ == "__main__":
    main()
