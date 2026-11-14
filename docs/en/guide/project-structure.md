# Project Structure

AeroLiners Set is a CMake-driven NewGRF project. The source is written in **NML** and organized into thousands of source files via the C preprocessor (`#include` and `#define` in `.pnml` files). Release metadata lives in the root `bundle.json`, and packaging is implemented once in `scripts/bundle.py`. The following breaks down the whole repository by directory.

```
AeroLinersSet/
├── CMakeLists.txt          # Top-level build definitions (NML / GRF / Bundles targets)
├── CMakePresets.json       # CMake presets (Ninja / Make / VS generators)
├── bundle.json             # ★ Single source of truth for release metadata (GRFID / version / docs / archive names)
├── Makefile                # CMake-generated build entry (make / make clean)
├── WAS.pnml                # Main entry: #include all aircraft source files
├── custom_tags.txt         # Build-time generated version / identity info
├── bin/                    # Build output: .grf / .nml / release tarballs (git-ignored)
├── build/                  # CMake intermediate directory
├── docs/                   # VitePress docs site (incl. bundled readme.txt / license.txt / changelog.txt)
├── lang/                   # 15 language files (*.lng)
├── scripts/                # Build and packaging scripts
│   ├── Compile.cmake           # Calls nmlc to compile .grf
│   ├── GenerateCustomTags.cmake # Generates custom_tags.txt
│   └── bundle.py               # ★ Shared build/verify/info packaging script
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
- Currently about **216** model `.pnml` files and about **1743** livery PNGs (2264 logical liveries).

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
- `.lng` files **must keep CRLF line endings** (NewGRF spec); after editing translations you must re-run nmlc for the changes to reach the `.grf`.

## Build and packaging scripts (`scripts/`)

| Script | Role |
| --- | --- |
| `Compile.cmake` | Calls `nmlc` to compile `.nml` into the final `.grf` |
| `GenerateCustomTags.cmake` | Generates `custom_tags.txt` (version, GRF filename, date, etc.) |
| `bundle.py` | Reads `bundle.json`, substitutes doc placeholders (${GRF_REVISION}` / ${GRF_MD5}`), builds the BaNaNa-format tar / tar.gz, and self-verifies layout, GRF ID and MD5 |

## Release metadata (`bundle.json`)

`bundle.json` is the **single source of truth** for the version, GRFID, project name, GRF filename, bundled doc list and archive naming. Both `CMakeLists.txt` and `.github/workflows/release.yml` consume it through `scripts/bundle.py` instead of each carrying their own copy of the GRFID / version / doc list. To release, bump `version` here and push a `v<version>` tag.

Back: [NewGRF Parameters →](/guide/parameters) ｜ Next: [Building from Source →](/guide/building)
