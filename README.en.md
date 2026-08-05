# AeroLiners Set（寰宇飞机）

> `Maicarons/AeroLiners-Set` is an **independent continuation (fork)** of the OpenTTD NewGRF project **World Airliner Set (WAS)**. It keeps the upstream aircraft and graphics, but adopts a new Chinese brand "寰宇飞机", an English brand "AeroLiners Set", a new GRFID (`AERO`), and a fully bilingual (Chinese + English) documentation site with i18n. Code and graphics originate from upstream; this repo maintains and extends them going forward.

[![GitHub Release](https://img.shields.io/github/v/release/Maicarons/AeroLiners-Set?label=Release)](https://github.com/Maicarons/AeroLiners-Set/releases)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](docs/license.txt)

---

## What is this?

**AeroLiners Set（寰宇飞机）** is a **NewGRF** (new graphics resource pack) for [OpenTTD](https://www.openttd.org/).
It collects real-world airliners and freighters — both recent and historical — and lets every aircraft **refit** into the **real liveries** of the corresponding airlines.

- Most original aircraft sprites were created by **PikkaBird** and originally shipped in the AV8 set; WAS added real liveries on top, and some models were drawn by the WAS team.
- Thanks to OpenTTD's NewGRF engine pool, the set can contain up to **65535** aircraft instead of the old limit of 48.
- It currently ships **157** aircraft models, **1957** liveries, spanning **15** manufacturers, with **15** interface language files.
- It can be loaded alongside other aircraft NewGRFs without conflict.
- The project is released under the **GNU General Public License v3.0**.

> ℹ️ **About branding & compatibility**: This continuation replaces the upstream `WAS2` with a brand-new GRFID `AERO`, and uses the new Chinese name "寰宇飞机" and English name "AeroLiners Set". This means **old saves made with the WAS set will treat this as a different NewGRF** (aircraft in those saves will not map onto this set) — an inherent cost of changing the GRFID.

## Documentation

The full guides — installation, parameters, building, liveries, translating, and contributing — live on the bilingual documentation site:

👉 **[AeroLiners Set Docs](https://maicarons.github.io/AeroLiners-Set/)** (VitePress sources in `docs/`; preview locally with `npm run docs:dev`; switch between 简体中文 / English, with hooks reserved for more languages)

| What you want to do | Go here |
| --- | --- |
| Learn the project background & goals | [Introduction](docs/en/guide/introduction.md) |
| Install the set and play | [Installation & Usage](docs/en/guide/installation.md) |
| Understand the adjustable NewGRF parameters | [NewGRF Parameters](docs/en/guide/parameters.md) |
| Figure out what's in the directory | [Project Structure](docs/en/guide/project-structure.md) |
| Compile the `.grf` from source | [Building from Source](docs/en/guide/building.md) |
| Add liveries / draw sprites | [Liveries & Graphics](docs/en/guide/liveries.md) |
| Help translate the interface | [Translating](docs/en/guide/translating.md) |
| Submit code or report issues | [Contributing](docs/en/guide/contributing.md) |

---

## Download & Install

### Option 1: Download the Release (recommended)

Download `AeroLinersSet.grf` from the [GitHub Releases](https://github.com/Maicarons/AeroLiners-Set/releases) page, drop it into OpenTTD's `newgrf` directory (usually `Documents/OpenTTD/newgrf` on Windows), then open the in-game "NewGRF" window, click "Add", and enable it.

> The Chinese name only appears after you select **Simplified Chinese** or **Traditional Chinese** in OpenTTD's language settings.

### Option 2: Download from BaNaNaS (stable only, English UI, upstream original)

Search for *World Airliner Set* in OpenTTD's in-game "Content Download" list and click "Download". This channel serves the **upstream English original** (still GRFID `WAS2`), not this continuation "AeroLiners Set". For the Chinese branding and the latest content of this continuation, use Option 1.

### Enable & Play

1. Open OpenTTD → "NewGRF" settings window → "Add", and select **AeroLiners Set（寰宇飞机）**.
2. Click "Apply Changes" and start a new game.
3. After building any aircraft, click the **Refit** button. You'll see a cargo list; each cargo is annotated with the corresponding airline livery. Pick the livery you want and click "Refit vehicle".

---

## NewGRF Parameters

After selecting the set in the "NewGRF" window, you can configure these parameters (entry: select it, then click "Parameters" or "Settings"):

| Parameter | Description |
| --- | --- |
| **Enable default aircraft** | Whether to also enable OpenTTD's built-in default aircraft. |
| **Enable range setting** | Whether to limit an aircraft's "maximum flight distance". When off, all aircraft have unlimited range. |
| **Range limitation** | Active when "Enable range setting" is on: `Normal range` / `Extended range` / `No range`. |
| **Purchase cost factor** | Adjusts purchase price: `0` = 1/16×, default `4` = unchanged, `8` = 16×. |
| **Running cost factor** | Adjusts running cost: `0` = 1/16×, default `4` = unchanged, `8` = 16×. |

---

## Building from Source (advanced)

> You usually **don't** need to build it yourself — just download the Release. Build only when you want the latest changes or to modify the set.

The pipeline is: `.pnml` → (C preprocessor) → `.nml` → (nmlc) → `.grf`. Tools required:

- **C preprocessor** (GCC / clang, to expand `#include` and macros in `.pnml`)
- **nmlc** (NewGRF compiler, `pip install nml`)
- Build environment: make / cmake etc. (CMake already defines `NML`, `GRF`, `Bundles` targets)

Brief steps (verified manual pipeline in this repo):

```bash
# 1. Compute REPO_REVISION (days since 2000-01-01), preprocess to .nml
gcc -D REPO_REVISION=$(python3 -c "import datetime;print((datetime.datetime.now(datetime.timezone.utc)-datetime.datetime(2000,1,1,tzinfo=datetime.timezone.utc)).days)") \
    -D NEWGRF_VERSION=1.0 -C -E -nostdinc -x c-header \
    -o bin/AeroLinersSet.nml WAS.pnml

# 2. Compile to .grf
nmlc --grf=bin/AeroLinersSet.grf -c bin/AeroLinersSet.nml
```

Full instructions: [Building from Source](docs/en/guide/building.md).

> Note: language files (`.lng`) are not `#include`d by `.pnml`; nmlc picks them up automatically from the `lang/` directory. So **after editing translations you must re-run nmlc** for the new text to be baked into the `.grf`.

---

## Translations

This repo ships **15** interface language files (including Simplified Chinese, Traditional Chinese, and several European languages).

- `lang/chinese_simplified.lng` — Simplified Chinese (`##grflangid 0x56`)
- `lang/chinese_traditional.lng` — Traditional Chinese (`##grflangid 0x62`, Taiwan glyphs, generated via OpenCC `s2tw` + Taiwan airline naming rules)

Translation principle: airline and aircraft names follow the **official / common Chinese name**; when one country has multiple airlines (e.g. Spain, Venezuela, Portugal), they are distinguished by transliteration or full names to avoid confusion in the livery list. Aircraft codes (ATR/BAC/Boeing/Airbus etc.) keep their Latin original per aviation convention.

To help translate or correct text, see [Translating](docs/en/guide/translating.md).

---

## License & Copyright

- **Code & graphics**: GNU General Public License v3.0 — see [docs/license.txt](docs/license.txt).
- **Original graphics attribution**: most aircraft sprites originate from **PikkaBird**'s AV8 set; please credit him when used.
- This continuation's Chinese branding, documentation, and maintenance work: also released under GPL-3.0.

---

## Credits & Links

- Upstream dev home: <https://dev.openttdcoop.org/projects/worldairlineset>
- Upstream forum: <http://worldairlinerset.forumotion.com/>
- TT-Forums thread: <http://www.tt-forums.net/viewtopic.php?t=39227>
- Upstream code repo: <https://github.com/RvP93/WorldAirlinersSet>
- AeroLiners Set docs: <https://maicarons.github.io/AeroLiners-Set/>

**World Airliner Set team** (upstream): Beardie, DJNekkid, Frank, Yorick, Faddypainter, RvP93, Aras, Audigex (development); EXTSpotter, Dimme, Simozzz, Trainboy2004, Firzafp, et al. (art).

**Special thanks**: PikkaBird (original graphics), ludde (created OpenTTD), Petern (added the NewGRF engine pool that made mass aircraft possible), Chris Sawyer (created Transport Tycoon), and all translators and issue reporters.

---

*This README is maintained by the AeroLiners Set continuation. Where it differs from the upstream `readme.txt`, this file takes precedence.*
