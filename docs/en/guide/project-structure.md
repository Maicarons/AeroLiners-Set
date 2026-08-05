# Project Structure

AeroLiners Set is a CMake-driven NewGRF project. The source is written in **NML** and organized into thousands of source files via the C preprocessor (`#include` and `#define` in `.pnml` files). The following breaks down the whole repository by directory.

```
AeroLinersSet/
├── CMakeLists.txt          # Top-level build definitions (NML / GRF / Bundles targets)
├── CMakePresets.json       # CMake presets (Ninja / Make / VS generators)
├── Makefile                # CMake-generated build entry (make / make clean)
├── WAS.pnml                # Main entry: #include all aircraft source files
├── custom_tags.txt         # Build-time generated version / identity info
├── bin/                    # Build output: generated .grf and .nml
├── build/                  # CMake intermediate directory
├── docs/                   # This VitePress documentation (incl. readme.txt / license.txt / changelog.txt)
├── documentation/          # Misc docs, xlsx tracking sheets, logo, etc.
├── greyscales/             # Greyscale (base) livery PNGs per model, grouped by manufacturer
├── lang/                   # 15 language files (*.lng)
├── scripts/                # 3 CMake scripts driving NML/GRF/doc processing
├── sprites/                # Historical / auxiliary sprite assets (pcx / nfo / png / examplenfo)
└── src/                    # Core source
    ├── *.pnml              # Top-level definitions (header / check / basecost / cargotable ...)
    ├── gfx/                # All aircraft, in manufacturer / series / model three-level dirs
    └── sound/              # Takeoff & landing sounds (.wav)
```

## Core source (`src/`)

| File | Role |
| --- | --- |
| `header.pnml` | GRF header: `grfid` (`AERO`), `name`, `url`, version, and the 4 adjustable parameters |
| `check.pnml` | Compiler / environment check macros |
| `basecost.pnml` | Base cost related definitions |
| `cargotable.pnml` | Cargo table definition, corresponding to refit options |
| `definition.pnml` | Common macros: `get_model_life`, `get_retire_early`, `plane_speed_kmh`, `plane_RC`, `flight_state`, etc. |
| `graph_templates.pnml` | Graphics templates (spriteset template macros) |
| `disable_origin.pnml` | Switches to disable original aircraft, etc. |
| `sort_order.pnml` | Sort order definitions for the purchase list |
| `gfx/` | One directory per model, containing a `.pnml` (aircraft logic) and several `.png` (livery sprites) |
| `sound/` | Takeoff & landing sound files (`av_turbogo.wav`, `av_landturbo.wav`) |

## Aircraft source files (`src/gfx/`)

- Three-level directory structure: `manufacturer / series / specific model`.
  For example `Boeing / B737 / B737-800 /`.
- Each model directory contains:
  - One **`model.pnml`**: defines the aircraft's spriteset, state switches, properties, and graphics.
  - Several **`.png` livery files**: each PNG corresponds to one airline livery (including a `(0)Greyscale.png` as the greyscale base).
- Currently about **157** model `.pnml` files and about **1743** livery PNGs.

```text
src/gfx/Boeing/B737/B737-800/
├── (0)Greyscale.png      # Greyscale base livery
├── B737-800.pnml         # Aircraft logic + sprite references
├── AerLingus.png         # Airline liveries
├── Lufthansa.png
└── ...
```

## Language files (`lang/`)

- 15 `.lng` files, covering catalan, chinese_simplified, chinese_traditional, croatian, czech, dutch, english, finnish, german, indonesian, italian, korean, polish, russian, spanish.
- Declared via `##grflangid`, providing localization for all `STR_*` strings (GRF name, parameter descriptions, model names, livery names, etc.).

## Build scripts (`scripts/`)

| Script | Role |
| --- | --- |
| `Compile.cmake` | Calls `nmlc` to compile `.nml` into the final `.grf` |
| `GenerateCustomTags.cmake` | Generates `custom_tags.txt` (version, GRF filename, date, etc.) |
| `ProcessDocs.cmake` | Calls `grfid` to compute MD5 and configure the three text files into the release bundle |

## Resource directory notes

- `greyscales/`: PNG backups/sources of each model's greyscale livery, grouped by manufacturer (129 `.png`).
- `sprites/`: historical and auxiliary assets, including `pcx/`, `png/`, `nfo/`, `examplenfo/`. `nfo/` keeps the old NFO flow's string/sprite definitions; `examplenfo/` holds callback examples (`callback36.txt`, `xx.nfo`).
- `documentation/`: development tracking sheets (xlsx), logo sources, old English lng, and other references.

Back: [NewGRF Parameters →](/guide/parameters) ｜ Next: [Building from Source →](/guide/building)
