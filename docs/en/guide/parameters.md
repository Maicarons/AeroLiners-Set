# NewGRF Parameters

AeroLiners Set defines several adjustable parameters (GRF parameters) in the `.grf`, configurable in the NewGRF settings window, to change the behaviour of the whole fleet — range, purchase cost, and operating cost.

Parameter definitions live in [`src/header.pnml`](https://github.com/Maicarons/AeroLiners-Set/blob/main/src/header.pnml).

## Parameter overview

| Bit | Name | Type | Range | Default | Description |
| --- | --- | --- | --- | --- | --- |
| `param 0` | `enable_standard_planes` | bool | 0 / 1 | `0` (off) | Whether to enable all standard planes |
| `param 1` | `BCosts` (base cost factor) | int | 0 – 8 | `4` | Scales **purchase cost** (0 = 1/16, 4 = unchanged, 8 = ×16) |
| `param 2` | `RCosts` (base running-cost factor) | int | 0 – 8 | `4` | Scales **operating cost** (0 = 1/16, 4 = unchanged, 8 = ×16) |
| `param 3` | `Ranges` (flight range) | int | 0 – 2 | `1` | Enable / disable flight range for all aircraft (see table below) |

## Flight range (Ranges) values

| Value | Meaning | Effect |
| --- | --- | --- |
| `0` | Ranges Off | Disable range limits (all aircraft `range: 0`) |
| `1` | Normal Ranges (default) | Enable normal flight range |
| `2` | Long Ranges | Enable "long-range" flight range (about 1.5× normal) |

> Example: the ATR 42-300 has `range: 165` under normal ranges, scaled to `range: 245` in long-range mode, and `0` when disabled.

## Cost / operating-cost factors (BCosts / RCosts)

These two parameters scale the whole fleet's **price** and **daily operating cost**:

- `0` → 1/16 (cheapest)
- `4` → unchanged (baseline, default)
- `8` → ×16 (most expensive)

They are applied globally when NewGRF computes each aircraft's `cost_factor` / `purchase_running_cost_factor`, making it easy to balance the game economy.

## How to adjust

In OpenTTD's **NewGRF Settings** window, select AeroLiners Set and click **Parameters** to modify each item and see its description text live (these descriptions come from [`lang/*.lng`](https://github.com/Maicarons/AeroLiners-Set/tree/main/lang)).

Back: [Introduction →](/guide/introduction) ｜ Next: [Project Structure →](/guide/project-structure)
