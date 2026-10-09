# Adding a Livery

> Real liveries are what makes AeroLiners Set what it is, and every single one of them came from a community contribution.
> **This page assumes you have never drawn a NewGRF sprite and do not know NML.** Follow it end to end and you will have added a real airline livery to the set.

## Pick what fits you

| Your situation | What to contribute | Difficulty |
| --- | --- | --- |
| You can draw, want something visible fast | Add a new airline to a type that already has liveries | ⭐ Lowest — one PNG |
| You can draw, want something substantial | Draw real airframes for the "borrowed graphics" types | ⭐⭐⭐ Full 5 states × 8 frames |
| You are unsure of your pixel art | Start with a type that has only 1–2 liveries (see [Appendix B](#appendix-btypes-with-the-fewest-liveries-best-for-a-first-contribution)) | ⭐ |
| You would rather not draw at all | [Translate the airline names](/guide/translating) | ⭐ |

---

## Step 1: Pick an aircraft and open its greyscale base image

Every aircraft folder contains a `(0)Greyscale.png` — **this is the base image provided for you**. The fuselage, wings and engines are already drawn as pixels; it simply has no colour scheme.

Your job is to paint colours onto that base image.

```text
src/gfx/Airbus/A320/A318/
├── (0)Greyscale.png        ← open this one
├── AirFrance.png           ← finished liveries, for reference
├── BA.png
├── TAROM.png
└── A318.pnml
```

If you are adding a new airline to a type that **already has liveries**, just follow the steps below.
If you want to draw the **real airframe for one of the 73 types that still borrow their graphics**, see [Appendix A](#appendix-atypes-with-no-artwork-of-their-own-73) — more work, but far more valuable.

---

## Step 2: Set up GIMP and the OpenTTD palette

NewGRF sprites **cannot use arbitrary colours** — only colours from the official OpenTTD palette, otherwise the build errors out or the colours come out wrong. So the first thing to do is load that palette into GIMP.

1. Install [GIMP](https://www.gimp.org/) (free, open source; this walkthrough was verified on GIMP 2.10).
2. Download the **OpenTTD palette file `ttd-newgrf-win.gpl`** — see the [TT-Forums thread](https://www.tt-forums.net/viewtopic.php?t=91568).
3. Open GIMP → menu **Windows (W) → Dockable Dialogs (D)**, and find the palette area in the panel on the right.
4. Drag `ttd-newgrf-win.gpl` into the palette panel.
5. Double-click `ttd-newgrf-win.gpl`; the official palette now appears on the right.

What each swatch means (white / dark blue / green / silver / red …) is documented at [TT-Wiki: Palettes And Coordinates](https://newgrf-specs.tt-wiki.net/wiki/PalettesAndCoordinates).

This set enables `PALETTE_CC_FIRST`, so the **first group of colours is the airline-custom (company colour) range** — take your tail and fuselage stripe colours from that group.

---

## Step 3: Paint your livery

Open the target aircraft's `(0)Greyscale.png` in GIMP and paint away with the pencil tool.

### How the spritesheet is laid out (important)

This image is **not** a normal picture of a plane. It is a **spritesheet**: 8 columns across, 5 rows down.

| Row | Flight state | Description |
| --- | --- | --- |
| 1 | `Flight` | Cruise |
| 2 | `Grounded` | Parked / taxiing |
| 3 | `Climbing` | Climbing after take-off |
| 4 | `Touchdown` | Just touched down (gear compressed) |
| 5 | `Landing` | Landing, gear down |

The 8 columns of each row are the 8 animation frames. For A318 the exact coordinates live in `A318.pnml`:

```c
spriteset (name##_Flight, IMAGEFILE)
{
  [  5, 5, 45, 19, -23, -10, ANIM]   // x, y, width, height, offset x, offset y, animation
  [ 55, 5, 40, 21, -20, -11, ANIM]
  [100, 5, 44, 23, -22, -12, ANIM]
  ...                                // 8 frames in total
}
spriteset (name##_Grounded, IMAGEFILE)   { /* y = 47 */ }
spriteset (name##_Climbing, IMAGEFILE)   { /* y = 99 */ }
spriteset (name##_Touchdown, IMAGEFILE)  { /* y = 146 */ }
spriteset (name##_Landing,  IMAGEFILE)   { /* y = 190 */ }
```

### Four hard rules

1. **The PNG must be exactly the same dimensions as the original** (the A318 greyscale is `452 × 223` pixels). Change the size and every sprite will be sampled from the wrong place.
2. **Do not move any pixels.** Each frame's position is fixed by `x, y, xrel, yrel`. Change colours only.
3. **Convert to Indexed colour before exporting.** GIMP menu **Image (I) → Mode (M) → Indexed (I)**, confirm Indexed is selected, then export the PNG. Saving as RGB is the single most common failure.
4. **Use only colours from the palette.** Set **Dither** to None when quantising, so no stray speckles appear in your pixel art.

Export as PNG. Name it after the airline, e.g. `Emirates.png`.

---

## Step 4: Wire the PNG into the game

There are four code edits, all in that aircraft's `.pnml`. Using `A318.pnml` as the example:

### ① Declare the spritesets

Copy an existing `#define IMAGEFILE` block and point it at your new file:

```c
#define IMAGEFILE  "src/gfx/Airbus/A320/A318/Emirates.png"
Airbus_A318_sprite_layout_template(Airbus_A318_Emirates)
#undef IMAGEFILE
```

### ② Switch by flight state

Copy an existing `flight_state()` switch:

```c
switch (FEAT_AIRCRAFT, SELF, Airbus_A318_Emirates, flight_state())
{
  15: Airbus_A318_Emirates_Climbing;
  18: Airbus_A318_Emirates_Flight;
  21: Airbus_A318_Emirates_Landing;
  22: Airbus_A318_Emirates_Touchdown;
      Airbus_A318_Emirates_Grounded;
}
```

### ③ Allocate a livery number

Add a line to the `cargo_subtype` switch. The number must not collide with an existing one (`7` below):

```c
switch (FEAT_AIRCRAFT, SELF, Airbus_A318_sprites, cargo_subtype)
{
  1: Airbus_A318_AirFrance;
  ...
  6: Airbus_A318_TAROM;
  7: Airbus_A318_Emirates;      // ← new
     Airbus_A318_Greyscale;      // default greyscale, must stay last
}
```

And add the display name in `cargo_subtype_text`:

```c
switch (FEAT_AIRCRAFT, SELF, Airbus_A318_cargo_subtype_text, cargo_subtype)
{
  ...
  7: string(STR_VLIV_EMIRATES);
     return CB_RESULT_NO_TEXT;
}
```

For freighters, also add the capacity in `cargo_subtype_capacity`.

### ④ Add the name string

Livery names are defined in **`lang/*.lng`**, not `cargotable.pnml`. At minimum add it to `lang/english.lng`:

```text
STR_VLIV_EMIRATES                                              : Emirates
```

Other languages can follow later; a missing entry falls back to English. Follow the existing naming convention: upper case with underscores, and a suffix when one airline has multiple liveries (e.g. `STR_VLIV_AIR_CANADA_OLD` / `STR_VLIV_AIR_CANADA_NEW`).

---

## Step 5: Build and verify

```bash
nmlc --grf=bin/AeroLinersSet.grf -c bin/AeroLinersSet.nml
```

The full preprocess + compile pipeline is in [Building from Source](/guide/building).

Install it into OpenTTD, start a new game, buy the aircraft, then click **Refit** — your livery should appear in the cargo list. If it does not, the `STR_` name in step ④ is probably misspelled, or the number collides with an existing livery.

> ⚠️ Language files are not expanded by `.pnml` `#include`; nmlc picks them up from `lang/` at compile time. **After editing translations you must re-run nmlc** for the new text to be baked into the `.grf`.

---

## Step 6: Submit

1. Put the PNG in the right aircraft folder.
2. Commit and open a pull request.
3. In the PR description state the **airline, aircraft type and livery era**, and link a reference image (an official livery photo from an aviation site, for example).
4. A maintainer will build it and merge.

One tip: note your credit in the PR description (e.g. `Livery by @yourhandle`) and we will add graphic contributors to the [credits page](/guide/credits).

---

## Common pitfalls

| Symptom | Cause | Fix |
| --- | --- | --- |
| Build fails: file not found | Wrong PNG path or filename case | The path must match the repo exactly; Linux is case-sensitive |
| Livery missing from the refit list | Duplicate `cargo_subtype` number, or the `STR_` name does not exist | Check number uniqueness and `lang/english.lng` |
| Aircraft misaligned or missing chunks in game | PNG dimensions differ from the original | Keep the original size exactly |
| Colours scrambled / odd colour blocks | Exported as RGB, or used off-palette colours | Convert to Indexed, then export |
| Name change has no effect | Forgot to re-run nmlc | Language files are picked up by nmlc |

---

## Appendix A: types with no artwork of their own (73)

These **73** aircraft are fully wired up — logic, real parameters and livery switching all compile into the `.grf` — but their **airframe pixel art is borrowed from a similar type** (the *donor* column below). That is why the C919 looks like an A320 and the ATR 42-600 looks like an ATR 42-500 in game.

Of these:

- **71** are "placeholder" types: their `IMAGEFILE` points into the donor's folder. To swap in real artwork, **just repoint `IMAGEFILE` at the aircraft's own folder — no logic changes at all**.
- **2** (Dash 8-200 and Il-76) have only a greyscale base image and **no liveries at all**; their refit list is empty.

When drawing these, keep the **same sprite layout coordinates as the donor** so the swap is seamless. Per-type parameters and step-by-step replacement instructions are in [Placeholder Aircraft TODO](/guide/placeholder-aircraft-todo).

| Aircraft | Folder | Current placeholder artwork (donor) |
| --- | --- | --- |
| Cessna 208 Caravan | `Cessna/208/208` | `ATR/ATR72/72-500` |
| Cessna 208B Grand Caravan | `Cessna/208B/208B` | `ATR/ATR72/72-500` |
| Cessna 402 | `Cessna/402/402` | `ATR/ATR42/42-500` |
| Cessna 404 Titan | `Cessna/404/404` | `ATR/ATR42/42-500` |
| Cessna 408 SkyCourier | `Cessna/408/408` | `ATR/ATR72/72-500` |
| Cessna 414 Chancellor | `Cessna/414/414` | `ATR/ATR42/42-500` |
| Cessna 421 Golden Eagle | `Cessna/421/421` | `ATR/ATR42/42-500` |
| Airbus A220-100 | `Airbus/A220/A220-100` | `Airbus/A320/A320neo` |
| Airbus A220 300 | `Airbus/A220/A220-300` | `Airbus/A320/A320neo` |
| Airbus A319neo | `Airbus/A320/A319neo` | `Airbus/A320/A320neo` |
| Airbus A321LR | `Airbus/A321/A321LR` | `Airbus/A320/A321-200` |
| Airbus A321XLR | `Airbus/A321/A321XLR` | `Airbus/A320/A320-200` |
| Airbus A321neo | `Airbus/A321/A321neo` | `Airbus/A320/A320neo` |
| Airbus A330-800neo | `Airbus/A330/A330-800neo` | `Airbus/A330/A330-300` |
| Airbus A330 900neo | `Airbus/A330/A330-900neo` | `Airbus/A330/A330-300` |
| Airbus A350 1000 | `Airbus/A350/A350-1000` | `Airbus/A350/A350-900` |
| Antonov An-140 | `Antonov/An140` | `ATR/ATR42/42-500` |
| Antonov An-148 | `Antonov/An148` | `Embraer/E190/E190STD` |
| Antonov An-158 | `Antonov/An158` | `Embraer/E190/E190STD` |
| ATR 42-600 | `ATR/ATR42/42-600` | `ATR/ATR42/42-500` |
| ATR 72-600 | `ATR/ATR72/72-600` | `ATR/ATR72/72-500` |
| AVIC MA-60 | `AVIC/MA60` | `ATR/ATR42/42-500` |
| AVIC MA-600 | `AVIC/MA600` | `ATR/ATR72/72-500` |
| AVIC Y-7-200 | `AVIC/Y7-200` | `ATR/ATR42/42-500` |
| Boeing 737 MAX 7 | `Boeing/B737/B737MAX7` | `Boeing/B737/B737MAX8` |
| Boeing 737 MAX10 | `Boeing/B737/B737MAX10` | `Boeing/B737/B737MAX8` |
| Boeing 737 MAX9 | `Boeing/B737/B737MAX9` | `Boeing/B737/B737MAX8` |
| Boeing 747SP | `Boeing/B747/B747SP` | `Boeing/B747/B747-200` |
| Boeing 757-300 | `Boeing/B757/B757-300` | `Boeing/B757/B757-200` |
| Boeing 777-8 | `Boeing/B777/B777-8` | `Boeing/B777/B777-300` |
| Boeing 777X | `Boeing/B777/B777X` | `Boeing/B777/B777-300ER` |
| Boeing 787 10 | `Boeing/B787/B787-10` | `Boeing/B787/B787-9` |
| Britten-Norman BN-2B Islander | `Britten-Norman/BN-2B` | `ATR/ATR42/42-500` |
| Britten-Norman BN-2T Turbine Islander | `Britten-Norman/BN-2T` | `ATR/ATR42/42-500` |
| COMAC C929 | `COMAC/C929` | `Airbus/A350/A350-900` |
| COMAC-C909 | `COMAC/C909` | `Embraer/E190/E190STD` |
| COMAC-C919 | `COMAC/C919` | `Airbus/A320/A320-200` |
| Convair 880 | `Convair/880` | `Boeing/B737/B737-300` |
| Convair 990 | `Convair/990` | `Boeing/B737/B737-300` |
| Bombardier-Dash8-200 | `Bombardier/Dash_8/Dash_8-200` | `Bombardier/Dash_8/Dash_8-200` |
| de Havilland Comet | `de Havilland/Comet` | `BAC/1-11/1-11-500` |
| de Havilland DHC-6-400 Twin Otter | `de Havilland/DHC6-400` | `Bombardier/Dash_8/Dash_8-400Q` |
| Embraer E175-E2 | `Embraer/E175/E175-E2` | `Embraer/E175/E175STD` |
| Embraer E190-E2 | `Embraer/E190/E190-E2` | `Embraer/E190/E190STD` |
| Embraer E195 E2 | `Embraer/E195/E195_E2` | `Embraer/E195/E195LR` |
| Embraer ERJ-135 | `Embraer/ERJ135/ERJ135` | `Embraer/E145/ERJ145` |
| Embraer ERJ-140 | `Embraer/ERJ140/ERJ140` | `Embraer/E145/ERJ145` |
| Fokker F27 | `Fokker/F27` | `ATR/ATR42/42-500` |
| Fokker F28 | `Fokker/F28` | `Fokker/F100` |
| General Atomics DO 228 | `General Atomics/DO228` | `ATR/ATR42/42-500` |
| Hawker Siddeley Trident | `Hawker_Siddeley/Trident` | `Boeing/B727/B727-200` |
| Ilyushin Il-114 | `Ilyushin/Il114` | `ATR/ATR42/42-500` |
| Ilyushin Il-18 | `Ilyushin/Il18` | `ATR/ATR72/72-500` |
| Ilyushin Il-96 | `Ilyushin/Il96` | `Airbus/A330/A330-300` |
| Ilyushin-76 | `Ilyushin/Il76` | `Ilyushin/Il76` |
| Irkut MC-21 | `Irkut/MC21` | `Airbus/A320/A320-200` |
| LET L-410 | `LET/L410` | `ATR/ATR42/42-500` |
| Lockheed L-1011 TriStar | `Lockheed/L1011` | `McDonnell_Douglas/DC10/DC10-30` |
| Lockheed L-188 Electra | `Lockheed/L188` | `ATR/ATR72/72-500` |
| Douglas DC-3 | `McDonnell_Douglas/DC3` | `ATR/ATR42/42-500` |
| Douglas DC-6 | `McDonnell_Douglas/DC6` | `Lockheed/Constellation/L049 Constellation` |
| Douglas DC-7 | `McDonnell_Douglas/DC7` | `Lockheed/Constellation/L049 Constellation` |
| Pilatus PC-12 | `Pilatus/PC12` | `ATR/ATR42/42-500` |
| Pilatus PC-24 | `Pilatus/PC24` | `Fokker/F100` |
| PZL/Antonov AN-28 Skytruck | `PZL/AN28` | `ATR/ATR42/42-500` |
| Raytheon Beech 1900D Airliner | `Raytheon/Beech1900D` | `ATR/ATR42/42-500` |
| Sukhoi Superjet 100 | `Sukhoi/SSJ100` | `Embraer/E190/E190STD` |
| Tupolev Tu-204 | `Tupolev/Tu204` | `Boeing/B757/B757-200` |
| Tupolev Tu-214 | `Tupolev/Tu214` | `Boeing/B757/B757-200` |
| Vickers VC10 | `Vickers/VC10` | `Ilyushin/Il62` |
| Vickers Viscount | `Vickers/Viscount` | `ATR/ATR42/42-500` |
| Yakovlev Yak-40 | `Yakovlev/Yak40` | `Boeing/B727/B727-200` |
| Yakovlev Yak-42 | `Yakovlev/Yak42` | `Boeing/B727/B727-200` |

---

## Appendix B: types with the fewest liveries (best for a first contribution)

These types **already have their own pixel art**, so all you do is paint colours onto the existing greyscale base — the easiest possible first contribution.

| Aircraft | Folder | Existing liveries |
| --- | --- | --- |
| BAC 1-11-300 | `BAC/1-11/1-11-300` | 1 |
| Antonov An-124 | `Antonov/An124` | 1 |
| Antonov An-225 | `Antonov/An225` | 1 |
| BAe 146-300QT | `BAe/146-300QT` | 1 |
| Boeing 737-200C | `Boeing/B737/B737-200C` | 1 |
| Boeing 747-400ER | `Boeing/B747/B747-400ER` | 1 |
| Boeing 757-200F | `Boeing/B757/B757-200F` | 1 |
| Bombardier CRJ1000EL | `Bombardier/CRJ/CRJ1000EL` | 1 |
| Bombardier Dash 8-100 | `Bombardier/Dash_8/Dash_8-100` | 1 |
| Bombardier Dash 8-200Q | `Bombardier/Dash_8/Dash_8-200Q` | 1 |
| Embraer E195STD | `Embraer/E195/E195STD` | 1 |
| McDonnell Douglas DC10-40 | `McDonnell_Douglas/DC10/DC10-40` | 1 |
| Airbus A310-200F | `Airbus/A300/A310-200F` | 2 |
| BAC 1-11-200 | `BAC/1-11/1-11-200` | 3 |
| Airbus A310-300F | `Airbus/A300/A310-300F` | 3 |
| Airbus A330-200F | `Airbus/A330/A330-200F` | 3 |
| ATR 72-200F | `ATR/ATR72/72-200F` | 3 |
| Boeing 727-200F | `Boeing/B727/B727-200F` | 3 |
| Boeing 747-300 / -300M | `Boeing/B747/B747-300`, `B747-300M` | 3 |
| Boeing 747-8F / -8I | `Boeing/B747/B747-8F`, `B747-8I` | 3 |
| Bombardier CRJ700 / -900 / -100LR / -1000 | `Bombardier/CRJ/…` | 3 |
| Bombardier Dash 8-300 | `Bombardier/Dash_8/Dash_8-300` | 3 |
| Embraer ERJ145 / E170STD / E170LR / E175STD / E175LR / E195AR | `Embraer/…` | 3 |
| McDonnell Douglas DC8-10 / -40 / DC9-20 / -40 | `McDonnell_Douglas/…` | 3 |

(For the full picture, read the `cargo_subtype_text` switch in each aircraft's `.pnml`.)

---

## Related pages

Back to [Liveries & Graphics](/guide/liveries) ｜ [Project Structure](/guide/project-structure) ｜ [Building from Source](/guide/building) ｜ [Translating](/guide/translating) ｜ [Contributing](/guide/contributing) ｜ [Credits](/guide/credits)