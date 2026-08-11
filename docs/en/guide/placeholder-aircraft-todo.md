# Placeholder Aircraft TODO

This mod currently has **71 aircraft using "placeholder graphics"** — their model logic, real parameters, and livery switching are all fully wired and compiled into the `.grf`, but the **aircraft pixel sprites temporarily borrow the placeholder image of a similar model** (each model needs hand-drawn pixel sprites for 5 flight states × 8 frames, which is art asset work).

This document records the real parameters of these 71 models, their current placeholder graphic source, and the specific task of replacing them with real pixel art.

> Note: This repository is an independent continuation of the upstream `RvP93/WorldAirlinersSet`. These placeholder models are additions made in this continuation; the upstream does not include them, so "replacing the real graphics" is future art work for this project.

## How the placeholder mechanism works

In each placeholder model's `.pnml`, the `#define IMAGEFILE` points to a **donor model's PNG directory** (not its own). NML compiles by reading the donor's real sprite sheet directly, so it compiles and displays in-game fine — only the fuselage shape is the donor's.

To replace with real graphics, simply:

1. Draw the real sprite PNGs for this model in its own directory (keeping the **same sprite layout coordinates** as the donor);
2. Change all `#define IMAGEFILE "src/gfx/<donor>/.../*.png"` in the `.pnml` to point to this model's directory;
3. Recompile `bin/AeroLinersSet.grf` — zero logic changes.

## TODO list (71 models)

| # | Model | Intro yr* | Seats | Range | Speed (km/h) | Cost | Current placeholder source | Priority |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | COMAC C909 | 2015 | 90 | 600 | 850 | 65 | `Embraer/E190/E190STD` | 🔴 High |
| 2 | COMAC C919 | 2023 | 158 | 1020 | 839 | 73 | `Airbus/A320/A320-200` | 🔴 High |
| 3 | Airbus A220-300 | 2016 | 145 | 1090 | 870 | 92 | `Airbus/A320/A320neo` | 🔴 High |
| 4 | Airbus A319neo | 2017 | 160 | 1200 | 839 | 95 | `Airbus/A320/A320neo` | 🟡 Medium |
| 5 | Airbus A321neo | 2016 | 220 | 1400 | 839 | 108 | `Airbus/A320/A320neo` | 🟡 Medium |
| 6 | Boeing 737 MAX 9 | 2018 | 178 | 1250 | 839 | 106 | `Boeing/B737/B737MAX8` | 🟢 Low |
| 7 | Boeing 737 MAX 10 | 2021 | 230 | 1300 | 839 | 112 | `Boeing/B737/B737MAX9` | 🟢 Low |
| 8 | Boeing 787-10 | 2018 | 330 | 2400 | 902 | 230 | `Boeing/B787/B787-9` | 🟢 Low |
| 9 | Airbus A330-900neo | 2018 | 300 | 2600 | 871 | 190 | `Airbus/A330/A330-300` | 🟢 Low |
| 10 | Airbus A350-1000 | 2018 | 366 | 2950 | 905 | 235 | `Airbus/A350/A350-900` | 🟢 Low |
| 11 | Boeing 777X | 2020 | 426 | 3400 | 896 | 305 | `Boeing/B777/B777-300ER` | 🟡 Medium |
| 12 | Embraer E195-E2 | 2019 | 146 | 1050 | 890 | 44 | `Embraer/E195/E195LR` | 🟡 Medium |
| 13 | Airbus A321XLR | 2024 | 150 | 1020 | 902 | 73 | `Airbus/A320/A320-200` | 🟢 Low |
| 14 | Embraer E190-E2 | 2018 | 106 | 600 | 886 | 65 | `Embraer/E190/E190STD` | 🟡 Medium |
| 15 | Airbus A220-100 | 2016 | 165 | 1165 | 833 | 101 | `Airbus/A320/A320neo` | 🔴 High |
| 16 | ATR 72-600 | 2010 | 74 | 295 | 515 | 18 | `ATR/ATR72/72-500` | 🟢 Low |
| 17 | ATR 42-600 | 2012 | 48 | 280 | 564 | 14 | `ATR/ATR42/42-500` | 🟢 Low |
| 18 | Boeing 737 MAX 7 | 2024 | 162 | 1205 | 975 | 101 | `Boeing/B737/B737MAX8` | 🟢 Low |
| 19 | Airbus A330-800neo | 2018 | 295 | 1950 | 926 | 187 | `Airbus/A330/A330-300` | 🟢 Low |
| 20 | Sukhoi Superjet 100 | 2011 | 106 | 600 | 886 | 65 | `Embraer/E190/E190STD` | 🟡 Medium |
| 21 | Irkut MC-21 | 2024 | 150 | 1020 | 902 | 73 | `Airbus/A320/A320-200` | 🟡 Medium |
| 22 | COMAC C929 | 2030 | 315 | 2700 | 945 | 220 | `Airbus/A350/A350-900` | 🟢 Low |
| 23 | Embraer E175-E2 | 2027 | 86 | 600 | 886 | 26 | `Embraer/E175/E175STD` | 🟢 Low |
| 24 | Boeing 757-300 | 1999 | 200 | 1365 | 934 | 79 | `Boeing/B757/B757-200` | 🟢 Low |
| 25 | Boeing 777-8 | 2027 | 451 | 2000 | 951 | 262 | `Boeing/B777/B777-300` | 🟢 Low |
| 26 | Antonov An-148 | 2009 | 106 | 600 | 886 | 65 | `Embraer/E190/E190STD` | 🟢 Low |
| 27 | Antonov An-158 | 2010 | 106 | 600 | 886 | 65 | `Embraer/E190/E190STD` | 🟢 Low |
| 28 | Tupolev Tu-204 | 1992 | 200 | 1365 | 934 | 79 | `Boeing/B757/B757-200` | 🟢 Low |
| 29 | Tupolev Tu-214 | 1996 | 200 | 1365 | 934 | 79 | `Boeing/B757/B757-200` | 🟢 Low |
| 30 | Ilyushin Il-96 | 1992 | 295 | 1950 | 926 | 187 | `Airbus/A330/A330-300` | 🟢 Low |
| 31 | Ilyushin Il-114 | 1997 | 48 | 280 | 564 | 14 | `ATR/ATR42/42-500` | 🟢 Low |
| 32 | Yakovlev Yak-40 | 1968 | 147 | 1155 | 999 | 37 | `Boeing/B727/B727-200` | 🟢 Low |
| 33 | Yakovlev Yak-42 | 1980 | 147 | 1155 | 999 | 37 | `Boeing/B727/B727-200` | 🟢 Low |
| 34 | Douglas DC-3 | 1936 | 48 | 280 | 564 | 14 | `ATR/ATR42/42-500` | 🟢 Low |
| 35 | Douglas DC-6 | 1946 | 81 | 1330 | 504 | 35 | `Lockheed/Constellation/L049 Constellation` | 🟢 Low |
| 36 | Douglas DC-7 | 1953 | 81 | 1330 | 504 | 35 | `Lockheed/Constellation/L049 Constellation` | 🟢 Low |
| 37 | Lockheed L-188 Electra | 1959 | 74 | 295 | 515 | 18 | `ATR/ATR72/72-500` | 🟢 Low |
| 38 | Lockheed L-1011 TriStar | 1972 | 255 | 1910 | 983 | 155 | `McDonnell_Douglas/DC10/DC10-30` | 🟢 Low |
| 39 | de Havilland Comet | 1952 | 115 | 635 | 870 | 37 | `BAC/1-11/1-11-500` | 🟢 Low |
| 40 | Vickers Viscount | 1953 | 48 | 280 | 564 | 14 | `ATR/ATR42/42-500` | 🟢 Low |
| 41 | Vickers VC10 | 1962 | 168 | 1800 | 822 | 169 | `Ilyushin/Il62` | 🟢 Low |
| 42 | Fokker F27 | 1958 | 48 | 280 | 564 | 14 | `ATR/ATR42/42-500` | 🟢 Low |
| 43 | Fokker F28 | 1969 | 107 | 570 | 846 | 27 | `Fokker/F100` | 🟢 Low |
| 44 | Convair 880 | 1960 | 128 | 755 | 910 | 29 | `Boeing/B737/B737-300` | 🟢 Low |
| 45 | Convair 990 | 1961 | 128 | 755 | 910 | 29 | `Boeing/B737/B737-300` | 🟢 Low |
| 46 | Hawker Siddeley Trident | 1964 | 147 | 1155 | 999 | 37 | `Boeing/B727/B727-200` | 🟢 Low |
| 47 | Boeing 747SP | 1976 | 366 | 2000 | 967 | 265 | `Boeing/B747/B747-200` | 🟢 Low |
| 48 | Ilyushin Il-18 | 1957 | 74 | 295 | 515 | 18 | `ATR/ATR72/72-500` | 🟢 Low |
| 49 | Cessna 208 Caravan | 1984 | 13 | 360 | 344 | 18 | `ATR/ATR72/72-500` | 🟢 Low |
| 50 | Cessna 208B Grand Caravan | 1986 | 14 | 360 | 344 | 19 | `ATR/ATR72/72-500` | 🟢 Low |
| 51 | Cessna 402 | 1966 | 8 | 236 | 380 | 12 | `ATR/ATR42/42-500` | 🟢 Low |
| 52 | Cessna 404 Titan | 1976 | 9 | 436 | 330 | 13 | `ATR/ATR42/42-500` | 🟢 Low |
| 53 | Cessna 414 Chancellor | 1969 | 7 | 447 | 360 | 12 | `ATR/ATR42/42-500` | 🟢 Low |
| 54 | Cessna 421 Golden Eagle | 1967 | 8 | 501 | 420 | 14 | `ATR/ATR42/42-500` | 🟢 Low |
| 55 | Airbus A321LR | 2018 | 206 | 1345 | 830 | 84 | `Airbus/A320/A321-200` | 🟢 Low |
| 56 | Antonov An-140 | 2002 | 52 | 382 | 575 | 14 | `ATR/ATR42/42-600` | 🟢 Low |
| 57 | AVIC MA-60 | 2000 | 60 | 249 | 430 | 14 | `ATR/ATR42/42-600` | 🟢 Low |
| 58 | AVIC MA-600 | 2010 | 60 | 251 | 430 | 18 | `ATR/ATR72/72-600` | 🟢 Low |
| 59 | AVIC Y-7-200 | 1984 | 52 | 282 | 420 | 14 | `Fokker/F27` | 🟢 Low |
| 60 | Britten-Norman BN-2B Islander | 1967 | 9 | 195 | 257 | 14 | `ATR/ATR42/42-600` | 🟢 Low |
| 61 | Britten-Norman BN-2T Turbine Islander | 1978 | 9 | 244 | 326 | 14 | `ATR/ATR42/42-600` | 🟢 Low |
| 62 | Cessna 408 SkyCourier | 2022 | 19 | 304 | 388 | 18 | `ATR/ATR72/72-600` | 🟢 Low |
| 63 | de Havilland DHC-6-400 Twin Otter | 1986 | 19 | 236 | 337 | 22 | `Bombardier/Dash_8/Dash_8-400Q` | 🟢 Low |
| 64 | Embraer ERJ-135 | 1999 | 37 | 591 | 834 | 14 | `Embraer/E145/ERJ145` | 🟢 Low |
| 65 | Embraer ERJ-140 | 2001 | 44 | 555 | 834 | 14 | `Embraer/E145/ERJ145` | 🟢 Low |
| 66 | General Atomics DO 228 | 1983 | 19 | 187 | 432 | 14 | `ATR/ATR42/42-600` | 🟢 Low |
| 67 | LET L-410 | 1971 | 19 | 251 | 405 | 14 | `ATR/ATR42/42-600` | 🟢 Low |
| 68 | Pilatus PC-12 | 1994 | 9 | 544 | 528 | 14 | `ATR/ATR42/42-600` | 🟢 Low |
| 69 | Pilatus PC-24 | 2018 | 12 | 673 | 787 | 27 | `Fokker/F100` | 🟢 Low |
| 70 | PZL/Antonov AN-28 Skytruck | 1975 | 19 | 264 | 335 | 14 | `Fokker/F27` | 🟢 Low |
| 71 | Raytheon Beech 1900D Airliner | 1990 | 19 | 327 | 518 | 14 | `ATR/ATR42/42-600` | 🟢 Low |

> \* Intro year is the actual purchasable year after `get_plane_year(year) = year - 2`.
>
> Models #13–71 were **added / corrected** in this continuation (13–22 added early Aug 2026, 23–48 supplemented 2026-08-07, 49–54 Cessna added 2026-08-09, **55–71 filled from the upstream WAS full model list on 2026-08-09** — excluding renamed/merged items such as ARJ21→C909). Among these, **#49–71 have their parameters OVERRIDDEN with real specs** (seats / range / speed / cost shown are real values); the other placeholders show the donor's effective values (see "Current placeholder source"), not the model's true parameters.
> When drawing real graphics, the performance parameters should also be replaced with the model's real data.

## Details & replacement steps

### 1. COMAC C909
- Source file: `src/gfx/COMAC/C909/C909.pnml`
- Placeholder donor: `Embraer/E190/E190STD`
- Priority: 🔴 High
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for COMAC C909 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 2. COMAC C919
- Source file: `src/gfx/COMAC/C919/C919.pnml`
- Placeholder donor: `Airbus/A320/A320-200`
- Priority: 🔴 High
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for COMAC C919 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 3. Airbus A220-300
- Source file: `src/gfx/Airbus/A220/A220-300/A220-300.pnml`
- Placeholder donor: `Airbus/A320/A320neo`
- Priority: 🔴 High
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Airbus A220-300 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 4. Airbus A319neo
- Source file: `src/gfx/Airbus/A320/A319neo/A319neo.pnml`
- Placeholder donor: `Airbus/A320/A320neo`
- Priority: 🟡 Medium
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Airbus A319neo into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 5. Airbus A321neo
- Source file: `src/gfx/Airbus/A320/A321neo/A321neo.pnml`
- Placeholder donor: `Airbus/A320/A320neo`
- Priority: 🟡 Medium
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Airbus A321neo into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 6. Boeing 737 MAX 9
- Source file: `src/gfx/Boeing/B737/B737MAX9/B737MAX9.pnml`
- Placeholder donor: `Boeing/B737/B737MAX8`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Boeing 737 MAX 9 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 7. Boeing 737 MAX 10
- Source file: `src/gfx/Boeing/B737/B737MAX10/B737MAX10.pnml`
- Placeholder donor: `Boeing/B737/B737MAX9`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Boeing 737 MAX 10 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 8. Boeing 787-10
- Source file: `src/gfx/Boeing/B787/B787-10/B787-10.pnml`
- Placeholder donor: `Boeing/B787/B787-9`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Boeing 787-10 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 9. Airbus A330-900neo
- Source file: `src/gfx/Airbus/A330/A330-900neo/A330-900neo.pnml`
- Placeholder donor: `Airbus/A330/A330-300`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Airbus A330-900neo into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 10. Airbus A350-1000
- Source file: `src/gfx/Airbus/A350/A350-1000/A350-1000.pnml`
- Placeholder donor: `Airbus/A350/A350-900`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Airbus A350-1000 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 11. Boeing 777X
- Source file: `src/gfx/Boeing/B777/B777X/B777X.pnml`
- Placeholder donor: `Boeing/B777/B777-300ER`
- Priority: 🟡 Medium
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Boeing 777X into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 12. Embraer E195-E2
- Source file: `src/gfx/Embraer/E195/E195-E2/E195-E2.pnml`
- Placeholder donor: `Embraer/E195/E195LR`
- Priority: 🟡 Medium
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Embraer E195-E2 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 13. Airbus A321XLR
- Source file: `src/gfx/Airbus/A321/A321XLR/A321XLR.pnml`
- Placeholder donor: `Airbus/A320/A320-200`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Airbus A321XLR into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 14. Embraer E190-E2
- Source file: `src/gfx/Embraer/E190/E190-E2/E190-E2.pnml`
- Placeholder donor: `Embraer/E190/E190STD`
- Priority: 🟡 Medium
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Embraer E190-E2 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 15. Airbus A220-100
- Source file: `src/gfx/Airbus/A220/A220-100/A220-100.pnml`
- Placeholder donor: `Airbus/A320/A320neo`
- Priority: 🔴 High
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Airbus A220-100 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 16. ATR 72-600
- Source file: `src/gfx/ATR/ATR72/72-600/72-600.pnml`
- Placeholder donor: `ATR/ATR72/72-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for ATR 72-600 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 17. ATR 42-600
- Source file: `src/gfx/ATR/ATR42/42-600/42-600.pnml`
- Placeholder donor: `ATR/ATR42/42-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for ATR 42-600 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 18. Boeing 737 MAX 7
- Source file: `src/gfx/Boeing/B737/B737MAX7/B737MAX7.pnml`
- Placeholder donor: `Boeing/B737/B737MAX8`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Boeing 737 MAX 7 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 19. Airbus A330-800neo
- Source file: `src/gfx/Airbus/A330/A330-800neo/A330-800neo.pnml`
- Placeholder donor: `Airbus/A330/A330-300`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Airbus A330-800neo into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 20. Sukhoi Superjet 100
- Source file: `src/gfx/Sukhoi/SSJ100/SSJ100.pnml`
- Placeholder donor: `Embraer/E190/E190STD`
- Priority: 🟡 Medium
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Sukhoi Superjet 100 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 21. Irkut MC-21
- Source file: `src/gfx/Irkut/MC21/MC21.pnml`
- Placeholder donor: `Airbus/A320/A320-200`
- Priority: 🟡 Medium
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Irkut MC-21 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 22. COMAC C929
- Source file: `src/gfx/COMAC/C929/C929.pnml`
- Placeholder donor: `Airbus/A350/A350-900`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for COMAC C929 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 23. Embraer E175-E2
- Source file: `src/gfx/Embraer/E175/E175-E2/E175-E2.pnml`
- Placeholder donor: `Embraer/E175/E175STD`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Embraer E175-E2 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 24. Boeing 757-300
- Source file: `src/gfx/Boeing/B757/B757-300/B757-300.pnml`
- Placeholder donor: `Boeing/B757/B757-200`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Boeing 757-300 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 25. Boeing 777-8
- Source file: `src/gfx/Boeing/B777/B777-8/B777-8.pnml`
- Placeholder donor: `Boeing/B777/B777-300`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Boeing 777-8 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 26. Antonov An-148
- Source file: `src/gfx/Antonov/An148/An148.pnml`
- Placeholder donor: `Embraer/E190/E190STD`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Antonov An-148 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 27. Antonov An-158
- Source file: `src/gfx/Antonov/An158/An158.pnml`
- Placeholder donor: `Embraer/E190/E190STD`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Antonov An-158 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 28. Tupolev Tu-204
- Source file: `src/gfx/Tupolev/Tu204/Tu204.pnml`
- Placeholder donor: `Boeing/B757/B757-200`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Tupolev Tu-204 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 29. Tupolev Tu-214
- Source file: `src/gfx/Tupolev/Tu214/Tu214.pnml`
- Placeholder donor: `Boeing/B757/B757-200`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Tupolev Tu-214 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 30. Ilyushin Il-96
- Source file: `src/gfx/Ilyushin/Il96/Il96.pnml`
- Placeholder donor: `Airbus/A330/A330-300`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Ilyushin Il-96 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 31. Ilyushin Il-114
- Source file: `src/gfx/Ilyushin/Il114/Il114.pnml`
- Placeholder donor: `ATR/ATR42/42-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Ilyushin Il-114 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 32. Yakovlev Yak-40
- Source file: `src/gfx/Yakovlev/Yak40/Yak40.pnml`
- Placeholder donor: `Boeing/B727/B727-200`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Yakovlev Yak-40 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 33. Yakovlev Yak-42
- Source file: `src/gfx/Yakovlev/Yak42/Yak42.pnml`
- Placeholder donor: `Boeing/B727/B727-200`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Yakovlev Yak-42 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 34. Douglas DC-3
- Source file: `src/gfx/McDonnell_Douglas/DC3/DC3.pnml`
- Placeholder donor: `ATR/ATR42/42-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Douglas DC-3 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 35. Douglas DC-6
- Source file: `src/gfx/McDonnell_Douglas/DC6/DC6.pnml`
- Placeholder donor: `Lockheed/Constellation/L049 Constellation`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Douglas DC-6 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 36. Douglas DC-7
- Source file: `src/gfx/McDonnell_Douglas/DC7/DC7.pnml`
- Placeholder donor: `Lockheed/Constellation/L049 Constellation`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Douglas DC-7 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 37. Lockheed L-188 Electra
- Source file: `src/gfx/Lockheed/L188/L188.pnml`
- Placeholder donor: `ATR/ATR72/72-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Lockheed L-188 Electra into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 38. Lockheed L-1011 TriStar
- Source file: `src/gfx/Lockheed/L1011/L1011.pnml`
- Placeholder donor: `McDonnell_Douglas/DC10/DC10-30`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Lockheed L-1011 TriStar into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 39. de Havilland Comet
- Source file: `src/gfx/de Havilland/Comet/Comet.pnml`
- Placeholder donor: `BAC/1-11/1-11-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for de Havilland Comet into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 40. Vickers Viscount
- Source file: `src/gfx/Vickers/Viscount/Viscount.pnml`
- Placeholder donor: `ATR/ATR42/42-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Vickers Viscount into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 41. Vickers VC10
- Source file: `src/gfx/Vickers/VC10/VC10.pnml`
- Placeholder donor: `Ilyushin/Il62`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Vickers VC10 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 42. Fokker F27
- Source file: `src/gfx/Fokker/F27/F27.pnml`
- Placeholder donor: `ATR/ATR42/42-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Fokker F27 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 43. Fokker F28
- Source file: `src/gfx/Fokker/F28/F28.pnml`
- Placeholder donor: `Fokker/F100`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Fokker F28 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 44. Convair 880
- Source file: `src/gfx/Convair/880/880.pnml`
- Placeholder donor: `Boeing/B737/B737-300`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Convair 880 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 45. Convair 990
- Source file: `src/gfx/Convair/990/990.pnml`
- Placeholder donor: `Boeing/B737/B737-300`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Convair 990 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 46. Hawker Siddeley Trident
- Source file: `src/gfx/Hawker_Siddeley/Trident/Trident.pnml`
- Placeholder donor: `Boeing/B727/B727-200`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Hawker Siddeley Trident into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 47. Boeing 747SP
- Source file: `src/gfx/Boeing/B747/B747SP/B747SP.pnml`
- Placeholder donor: `Boeing/B747/B747-200`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Boeing 747SP into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 48. Ilyushin Il-18
- Source file: `src/gfx/Ilyushin/Il18/Il18.pnml`
- Placeholder donor: `ATR/ATR72/72-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Ilyushin Il-18 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 49. Cessna 208 Caravan
- Source file: `src/gfx/Cessna/208/208/208.pnml`
- Placeholder donor: `ATR/ATR72/72-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Cessna 208 Caravan into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 50. Cessna 208B Grand Caravan
- Source file: `src/gfx/Cessna/208B/208B/208B.pnml`
- Placeholder donor: `ATR/ATR72/72-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Cessna 208B Grand Caravan into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 51. Cessna 402
- Source file: `src/gfx/Cessna/402/402/402.pnml`
- Placeholder donor: `ATR/ATR42/42-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Cessna 402 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 52. Cessna 404 Titan
- Source file: `src/gfx/Cessna/404/404/404.pnml`
- Placeholder donor: `ATR/ATR42/42-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Cessna 404 Titan into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 53. Cessna 414 Chancellor
- Source file: `src/gfx/Cessna/414/414/414.pnml`
- Placeholder donor: `ATR/ATR42/42-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Cessna 414 Chancellor into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 54. Cessna 421 Golden Eagle
- Source file: `src/gfx/Cessna/421/421/421.pnml`
- Placeholder donor: `ATR/ATR42/42-500`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Cessna 421 Golden Eagle into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 55. Airbus A321LR
- Source file: `src/gfx/Airbus/A321/A321LR/A321LR.pnml`
- Placeholder donor: `Airbus/A320/A321-200`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Airbus A321LR into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 56. Antonov An-140
- Source file: `src/gfx/Antonov/An140/An140.pnml`
- Placeholder donor: `ATR/ATR42/42-600`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Antonov An-140 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 57. AVIC MA-60
- Source file: `src/gfx/AVIC/MA60/MA60.pnml`
- Placeholder donor: `ATR/ATR42/42-600`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for AVIC MA-60 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 58. AVIC MA-600
- Source file: `src/gfx/AVIC/MA600/MA600.pnml`
- Placeholder donor: `ATR/ATR72/72-600`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for AVIC MA-600 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 59. AVIC Y-7-200
- Source file: `src/gfx/AVIC/Y7-200/Y7-200.pnml`
- Placeholder donor: `Fokker/F27`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for AVIC Y-7-200 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 60. Britten-Norman BN-2B Islander
- Source file: `src/gfx/Britten-Norman/BN-2B/BN-2B.pnml`
- Placeholder donor: `ATR/ATR42/42-600`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Britten-Norman BN-2B Islander into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 61. Britten-Norman BN-2T Turbine Islander
- Source file: `src/gfx/Britten-Norman/BN-2T/BN-2T.pnml`
- Placeholder donor: `ATR/ATR42/42-600`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Britten-Norman BN-2T Turbine Islander into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 62. Cessna 408 SkyCourier
- Source file: `src/gfx/Cessna/408/408/408.pnml`
- Placeholder donor: `ATR/ATR72/72-600`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Cessna 408 SkyCourier into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 63. de Havilland DHC-6-400 Twin Otter
- Source file: `src/gfx/de Havilland/DHC6-400/DHC6-400.pnml`
- Placeholder donor: `Bombardier/Dash_8/Dash_8-400Q`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for de Havilland DHC-6-400 Twin Otter into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 64. Embraer ERJ-135
- Source file: `src/gfx/Embraer/ERJ135/ERJ135/ERJ135.pnml`
- Placeholder donor: `Embraer/E145/ERJ145`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Embraer ERJ-135 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 65. Embraer ERJ-140
- Source file: `src/gfx/Embraer/ERJ140/ERJ140/ERJ140.pnml`
- Placeholder donor: `Embraer/E145/ERJ145`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Embraer ERJ-140 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 66. General Atomics DO 228
- Source file: `src/gfx/General Atomics/DO228/DO228.pnml`
- Placeholder donor: `ATR/ATR42/42-600`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for General Atomics DO 228 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 67. LET L-410
- Source file: `src/gfx/LET/L410/L410.pnml`
- Placeholder donor: `ATR/ATR42/42-600`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for LET L-410 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 68. Pilatus PC-12
- Source file: `src/gfx/Pilatus/PC12/PC12.pnml`
- Placeholder donor: `ATR/ATR42/42-600`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Pilatus PC-12 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 69. Pilatus PC-24
- Source file: `src/gfx/Pilatus/PC24/PC24.pnml`
- Placeholder donor: `Fokker/F100`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Pilatus PC-24 into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 70. PZL/Antonov AN-28 Skytruck
- Source file: `src/gfx/PZL/AN28/AN28.pnml`
- Placeholder donor: `Fokker/F27`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for PZL/Antonov AN-28 Skytruck into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

### 71. Raytheon Beech 1900D Airliner
- Source file: `src/gfx/Raytheon/Beech1900D/Beech1900D.pnml`
- Placeholder donor: `ATR/ATR42/42-600`
- Priority: 🟢 Low
- Replacement task: draw the 5-state × 8-frame real side-view pixel sprites for Raytheon Beech 1900D Airliner into its own directory, then change `IMAGEFILE` to point there. Recompile to verify.

## How to contribute real graphics

1. Draw the sprite sheet PNGs in the model's directory, keeping the same sprite layout as the donor (use the donor's PNG as coordinate reference).
2. Change the `#define IMAGEFILE` in that `.pnml` to point to the model's own directory.
3. Recompile locally (see [Building from Source](/guide/building)) and confirm correct in-game display.
4. Commit / push to this repository and update the replacement status of the corresponding row in this document.

## Automation scripts

- `tools/add_aircraft.py`: clones a donor model to generate placeholder `.pnml` (models #1–12).
- `tools/gen_placeholder_aircraft.py`: the generator used for #13–54 — clones donor sprite-layout macros + model parameters, only swapping identifier / name / intro year, wiring the donor's first liveries, with zero new livery strings.
- `tools/gen_aircraft_docs.py`: extracts all models from `WAS.pnml` and generates the [Fleet Gallery](/aircraft/) plus livery preview images.
