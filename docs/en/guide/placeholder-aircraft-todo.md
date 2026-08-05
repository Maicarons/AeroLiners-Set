# Placeholder Aircraft TODO

This mod currently has **12 aircraft using "placeholder graphics"** — their model logic, real parameters, and livery switching are all fully wired and compiled into the `.grf`, but the **aircraft pixel sprites temporarily borrow the placeholder image of a similar model** (each model needs hand-drawn pixel sprites for 5 flight states × 8 frames, which is art asset work).

This document records the real parameters of these 12 models, their current placeholder graphic source, and the specific task of replacing them with real pixel art.

> Note: This repository is an independent continuation of the upstream `RvP93/WorldAirlinersSet`. These placeholder models are additions made in this continuation; the upstream does not include them, so "replacing the real graphics" is future art work for this project.

## How the placeholder mechanism works

In each placeholder model's `.pnml`, the `#define IMAGEFILE` points to a **donor model's PNG directory** (not its own). NML compiles by reading the donor's real sprite sheet directly, so it compiles and displays in-game fine — only the fuselage shape is the donor's.

To replace with real graphics, simply:

1. Draw the real sprite PNGs for this model in its own directory (keeping the **same sprite layout coordinates** as the donor);
2. Change all `#define IMAGEFILE "src/gfx/<donor>/.../*.png"` in the `.pnml` to point to this model's directory;
3. Recompile `bin/AeroLinersSet.grf` — zero logic changes.

## TODO list (12 models)

| # | Model | Intro yr* | Seats | Range | Speed (km/h) | Cost | Current placeholder source | Priority |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | COMAC C909 | 2015 | 90 | 600 | 850 | 65 | `Embraer/E190/E190STD` | 🔴 High (big shape difference) |
| 2 | COMAC C919 | 2023 | 158 | 1020 | 839 | 73 | `Airbus/A320/A320-200` | 🔴 High (domestic flagship) |
| 3 | Airbus A220-300 | 2016 | 145 | 1090 | 870 | 92 | `Airbus/A320/A320neo` | 🔴 High (real CSeries, least similar) |
| 4 | Airbus A319neo | 2017 | 160 | 1200 | 839 | 95 | `Airbus/A320/A320neo` | 🟡 Medium |
| 5 | Airbus A321neo | 2016 | 220 | 1400 | 839 | 108 | `Airbus/A320/A320neo` | 🟡 Medium |
| 6 | Boeing 737 MAX 9 | 2018 | 178 | 1250 | 839 | 106 | `Boeing/B737/B737MAX8` | 🟢 Low (close to MAX 8) |
| 7 | Boeing 737 MAX 10 | 2021 | 230 | 1300 | 839 | 112 | `Boeing/B737/B737MAX9` | 🟢 Low |
| 8 | Boeing 787-10 | 2018 | 330 | 2400 | 902 | 230 | `Boeing/B787/B787-9` | 🟢 Low |
| 9 | Airbus A330-900neo | 2018 | 300 | 2600 | 871 | 190 | `Airbus/A330/A330-300` | 🟢 Low |
| 10 | Airbus A350-1000 | 2018 | 366 | 2950 | 905 | 235 | `Airbus/A350/A350-900` | 🟢 Low |
| 11 | Boeing 777X | 2020 | 426 | 3400 | 896 | 305 | `Boeing/B777/B777-300ER` | 🟡 Medium (folding wingtips distinctive) |
| 12 | Embraer E195-E2 | 2019 | 146 | 1050 | 890 | 44 | `Embraer/E195/E195LR` | 🟡 Medium (E2 has new swept winglets) |

> \* Intro year is the actually-purchasable year after `get_plane_year(year) = year - 2`.

## Details and replacement steps per model

### 1. COMAC C909 (formerly ARJ21)
- Source: `src/gfx/COMAC/C909/C909.pnml`
- Placeholder source: `src/gfx/Embraer/E190/E190STD/*.png` (regional jet shape, close in size to C909 but different engines/tail)
- Suggested liveries: Air China, China Eastern, China Southern, Hainan, Xiamen (already wired)
- Replacement task: draw the real C909 side-view pixel art (5 states × 8 frames) into `src/gfx/COMAC/C909/`, repoint `IMAGEFILE`.

### 2. COMAC C919
- Source: `src/gfx/COMAC/C919/C919.pnml`
- Placeholder source: `src/gfx/Airbus/A320/A320-200/*.png` (narrow-body shape, C919 overall outline similar but different nose/wing)
- Suggested liveries: Air China, China Eastern, China Southern, Hainan, Xiamen (already wired)
- Replacement task: draw the real C919 pixel art into `src/gfx/COMAC/C919/`.

### 3. Airbus A220-300
- Source: `src/gfx/Airbus/A220/A220-300/A220-300.pnml`
- Placeholder source: `src/gfx/Airbus/A320/A320neo/*.png` (**biggest shape difference** — A220 is the CSeries, shorter/stubbier fuselage, distinctive winglets)
- Highest replacement priority — replace graphics first.

### 4–12. Remaining models
- Sourced from the corresponding donor directories (see the "Current placeholder source" column above).
- These models and their donors are mostly same-series stretches/derivatives (e.g. MAX 10 ← MAX 9, 787-10 ← 787-9), with similar shapes and lower priority; among them **Boeing 777X** (folding wingtips) and **Embraer E195-E2** (new swept winglets) are suggested to take priority over the same-series stretches.

## How to contribute real graphics

1. Draw the sprite-sheet PNG in the model's directory, keeping the same sprite layout as the donor (use the donor's PNG as a coordinate reference).
2. Change the model's `.pnml` `#define IMAGEFILE` to point to its own directory.
3. Recompile locally (see [Building from Source](/guide/building)) and confirm correct in-game display.
4. Submit a PR / push to this repository and update the replacement status of the corresponding row in this document.

## Automation scripts

- `tools/add_aircraft.py`: clones a donor model to generate a placeholder model `.pnml` (e.g. the last 10 of the 12 above).
- `tools/gen_aircraft_md.py`: extracts all models from `WAS.pnml` to generate the [Fleet Gallery](/aircraft/) and livery preview images.
