# Liveries & Graphics

The signature feature of AeroLiners Set is "authentic liveries". This page explains how aircraft graphics and liveries are organized, rendered, and switched.

## Core concepts

- Each aircraft (one `.pnml` file) defines several **spritesets**, corresponding to different flight states:
  `Flight`, `Grounded`, `Climbing`, `Touchdown`, `Landing`.
- Each **livery** corresponds to an independent spriteset (e.g. `ATR_42_300_AerLingusRegional_Flight`), referencing its own independent PNG file.
- Livery switching is implemented via **cargo_subtype**: the "cargo item" you choose when refitting is actually the livery number, and each livery's name comes from the `STR_VLIV_*` string defined in `cargotable.pnml`.

## File makeup of a model

Using `src/gfx/ATR/ATR42/42-300/` as an example:

```text
42-300/
├── (0)Greyscale.png        # Greyscale base (cargo_subtype 0)
├── AerLingusRegional.png   # Livery 1
├── AirSouthwest.png        # Livery 2
├── AurignyAirServices.png  # Livery 3
├── ...                     # More airline liveries
└── 42-300.pnml             # Aircraft logic
```

## How it works in `.pnml` (excerpt)

`42-300.pnml` defines the sprite pickup positions for 8 frames per state with a macro:

```c
#define ATR_42_300_sprite_layout_template(name)        \
spriteset (name##_Flight, IMAGEFILE)                   \
{                                                      \
  [  1, 1, 46, 22, -23, -11, ANIM]                     \
  [ 52, 1, 38, 19, -19, -10, ANIM]                     \
  ...                                                  \
}                                                      \
spriteset (name##_Grounded, IMAGEFILE) { ... }         \
spriteset (name##_Climbing, IMAGEFILE) { ... }         \
spriteset (name##_Touchdown, IMAGEFILE) { ... }        \
spriteset (name##_Landing,  IMAGEFILE) { ... }
```

Then, for each livery, switch the `IMAGEFILE` macro and instantiate the template:

```c
#define IMAGEFILE "src/gfx/ATR/ATR42/42-300/(0)Greyscale.png"
purchase_sprite(ATR_42_300, 285, 1, 46, 23, -23, -12)
ATR_42_300_sprite_layout_template(ATR_42_300_Greyscale)
#undef IMAGEFILE

#define IMAGEFILE "src/gfx/ATR/ATR42/42-300/AerLingusRegional.png"
ATR_42_300_sprite_layout_template(ATR_42_300_AerLingusRegional)
#undef IMAGEFILE
```

State switching is driven by the `flight_state()` macro (reading vehicle variable `0xE2`):

```c
switch (FEAT_AIRCRAFT, SELF, ATR_42_300_Greyscale, flight_state())
{
  15: ATR_42_300_Greyscale_Climbing;
  18: ATR_42_300_Greyscale_Flight;
  21: ATR_42_300_Greyscale_Landing;
  22: ATR_42_300_Greyscale_Touchdown;
      ATR_42_300_Greyscale_Grounded;
}
```

And "which livery is selected" is decided by `cargo_subtype`:

```c
switch (FEAT_AIRCRAFT, SELF, ATR_42_300_sprites, cargo_subtype)
{
  1: ATR_42_300_AerLingusRegional;
  2: ATR_42_300_AirSouthwest;
  ...
     ATR_42_300_Greyscale;   // default greyscale
}
```

## How to add a livery

1. Drop a PNG into the model's directory (same dimensions as existing liveries, usually a horizontally-tiled multi-frame sprite sheet).
2. In the `.pnml`, add a new `IMAGEFILE` + template instantiation (follow an existing livery).
3. In `cargotable.pnml`, define a `STR_VLIV_*` string for the new livery.
4. In the model's `.pnml` `cargo_subtype` switch, assign a number to the new livery, and add the corresponding display text and (for freighters) capacity in `cargo_subtype_text` / `cargo_subtype_capacity`.
5. In `lang/*.lng`, provide translations for the new string in every language.

## Greyscale

The `greyscales/` directory holds each model's greyscale PNG as a base appearance with no airline markings (`(0)Greyscale.png`). It is `cargo_subtype 0` for every model and a common base image when drawing new liveries.

Back: [Building from Source →](/guide/building) ｜ Next: [Translating →](/guide/translating)
