# Introduction

## What is AeroLiners Set?

**AeroLiners Set (寰宇飞机)** is a **NewGRF** (New Graphics Resource File) developed for [OpenTTD](https://www.openttd.org/). Its core goal is:

> Bring real-world airliners and freighters — both recent and historic — into OpenTTD, and let every aircraft be refit into the livery of a real airline.

What sets AeroLiners Set apart from a plain "aircraft replacement set" is that it does not merely swap aircraft shapes — it offers **authentic liveries** as refit options (cargo subtypes). After purchasing an aircraft, click the **Refit** button and you will see a list of livery names among the cargo entries; pick one and the aircraft dons that airline's appearance.

## History and origins

- Most of the original aircraft sprites were drawn by **PikkaBird** and originally released with the **AV8** set.
- The AeroLiners Set team added authentic liveries on top of AV8 and drew some models themselves.
- When using this set, please credit **PikkaBird**.

AeroLiners Set is an independent continuation of the upstream **World Airliner Set (WAS)** by `RvP93/WorldAirlinersSet`, carrying forward its aircraft and liveries under a new identity (GRFID `AERO`).

## Technical capabilities

| Capability | Description |
| --- | --- |
| Aircraft count | Up to **65535** (supported since OpenTTD added the NewGRF engine pool; requires OpenTTD > 0.7.0) |
| Authentic liveries | Each aircraft has a set of real-airline liveries, switched via refit |
| Compatibility | Loadable alongside other aircraft NewGRFs; **TTDPatch is not supported** |
| Languages | 15 built-in languages (including Simplified Chinese); UI text follows the game language |
| Sound | Built-in turboprop / jet takeoff & landing sounds (`.wav`) |

## Known issues

Some issues are already known to the development team and usually need not be reported again. For a more complete list, see this project's GitHub Issues:
<https://github.com/Maicarons/AeroLiners-Set/issues>

## Planned features

The following are planned for later beta versions:

- **ECS/FIRS compatibility** (integration with new economy / industry replacement sets)
- **Random livery selection at purchase**
- **Skylift 150 advertising livery**
- **Clearer images in the purchase list**

## Contact and community

- Development homepage (GitHub): <https://github.com/Maicarons/AeroLiners-Set>
- Official forum: <http://worldairlinerset.forumotion.com/>
- tt-forums thread: <http://www.tt-forums.net/viewtopic.php?t=39227>

## Upstream and this project

- Upstream repository: `RvP93/WorldAirlinersSet` (<https://github.com/RvP93/WorldAirlinersSet>)
- This project (independent continuation): `Maicarons/AeroLiners-Set` (<https://github.com/Maicarons/AeroLiners-Set>)

Next: [Installation & Usage →](/guide/installation)
