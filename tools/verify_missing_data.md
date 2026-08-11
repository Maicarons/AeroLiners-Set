# 未获取到真实数据的机型清单（游戏内当前为估计/占位值，暂不修改）

> 依据 `tools/all_aircraft_realdata_verify.md` 核对报告，以下字段被研究代理显式标注「未找到可靠来源」——即联网核对时**拿不到可靠真实出处**，游戏内当前数值为估计/占位值。本表仅列出，未做任何修改。

**合计：42 款机型 / 44 处字段缺失真实来源。**

缺失高度集中在两类：**老飞机/货机/客货混装/研发中机型的「价格」字段**（无公开 USD 目录价），以及个别机型（BN-2T、de Havilland Comet）的航程/巡航。航程/座级/巡航在绝大多数机型上已有可靠来源。

## AVIC（2 款）

| 机型           | ID          | 缺失字段    | 游戏内当前值（估计）     |
| ------------ | ----------- | ------- | -------------- |
| AVIC MA-600  | AVIC_MA600  | 价格(USD) | cost_factor=18 |
| AVIC Y-7-200 | AVIC_Y7_200 | 价格(USD) | cost_factor=14 |

## BAC（3 款）

| 机型           | ID           | 缺失字段    | 游戏内当前值（估计）     |
| ------------ | ------------ | ------- | -------------- |
| BAC 1-11-200 | BAC_1_11_200 | 价格(USD) | cost_factor=24 |
| BAC 1-11-300 | BAC_1_11_300 | 价格(USD) | cost_factor=24 |
| BAC 1-11-400 | BAC_1_11_400 | 价格(USD) | cost_factor=37 |

## BAe（3 款）

| 机型                          | ID            | 缺失字段    | 游戏内当前值（估计）     |
| --------------------------- | ------------- | ------- | -------------- |
| British Aerospace 146-100   | BAe_146_100   | 价格(USD) | cost_factor=20 |
| British Aerospace 146-300   | BAe_146_300   | 价格(USD) | cost_factor=24 |
| British Aerospace 146-300QT | BAe_146_300QT | 价格(USD) | cost_factor=24 |

## Boeing（9 款）

| 机型                  | ID                | 缺失字段    | 游戏内当前值（估计）      |
| ------------------- | ----------------- | ------- | --------------- |
| Boeing 727-200F     | Boeing_727_200F   | 价格(USD) | cost_factor=29  |
| Boeing 737-200C     | Boeing_737_200C   | 价格(USD) | cost_factor=37  |
| Boeing 747-300M     | Boeing_747_300M   | 价格(USD) | cost_factor=274 |
| Boeing 747-400F BCF | Boeing_747_400BCF | 价格(USD) | cost_factor=187 |
| Boeing 747-400D     | Boeing_747_400D   | 价格(USD) | cost_factor=274 |
| Boeing 747-400ER    | Boeing_747_400ER  | 价格(USD) | cost_factor=298 |
| Boeing 747-400F ERF | Boeing_747_400ERF | 价格(USD) | cost_factor=311 |
| Boeing 747-400M     | Boeing_747_400M   | 价格(USD) | cost_factor=293 |
| Boeing 747-400F SCD | Boeing_747_400SCD | 价格(USD) | cost_factor=291 |

## Britten-Norman（2 款）

| 机型                                    | ID                  | 缺失字段                    | 游戏内当前值（估计）                         |
| ------------------------------------- | ------------------- | ----------------------- | ---------------------------------- |
| Britten-Norman BN-2B Islander         | BRITTEN_NORMAN_BN2B | 价格(USD)                 | cost_factor=14                     |
| Britten-Norman BN-2T Turbine Islander | BRITTEN_NORMAN_BN2T | 价格(USD)、航程(km)、巡航(km/h) | cost_factor=14, ≈1342 km, 326 km/h |

## COMAC（2 款）

| 机型         | ID         | 缺失字段    | 游戏内当前值（估计）      |
| ---------- | ---------- | ------- | --------------- |
| COMAC C909 | COMAC_C909 | 价格(USD) | cost_factor=65  |
| COMAC C929 | COMAC_C929 | 价格(USD) | cost_factor=220 |

## Cessna（4 款）

| 机型                      | ID         | 缺失字段    | 游戏内当前值（估计）     |
| ----------------------- | ---------- | ------- | -------------- |
| Cessna 402              | CESSNA_402 | 价格(USD) | cost_factor=12 |
| Cessna 404 Titan        | CESSNA_404 | 价格(USD) | cost_factor=13 |
| Cessna 414 Chancellor   | CESSNA_414 | 价格(USD) | cost_factor=12 |
| Cessna 421 Golden Eagle | CESSNA_421 | 价格(USD) | cost_factor=14 |

## Convair（2 款）

| 机型          | ID          | 缺失字段    | 游戏内当前值（估计）     |
| ----------- | ----------- | ------- | -------------- |
| Convair 880 | CONVAIR_880 | 价格(USD) | cost_factor=35 |
| Convair 990 | CONVAIR_990 | 价格(USD) | cost_factor=42 |

## Fokker（3 款）

| 机型         | ID          | 缺失字段    | 游戏内当前值（估计）     |
| ---------- | ----------- | ------- | -------------- |
| Fokker F28 | FOKKER_F28  | 价格(USD) | cost_factor=27 |
| Fokker 100 | Fokker_F100 | 价格(USD) | cost_factor=27 |
| Fokker 70  | Fokker_F70  | 价格(USD) | cost_factor=18 |

## Ilyushin（2 款）

| 机型             | ID            | 缺失字段    | 游戏内当前值（估计）      |
| -------------- | ------------- | ------- | --------------- |
| Ilyushin Il-18 | ILYUSHIN_IL18 | 价格(USD) | cost_factor=25  |
| Ilyushin Il-62 | Ilyushin_62   | 价格(USD) | cost_factor=169 |

## LET（1 款）

| 机型        | ID       | 缺失字段    | 游戏内当前值（估计）     |
| --------- | -------- | ------- | -------------- |
| LET L-410 | LET_L410 | 价格(USD) | cost_factor=14 |

## Lockheed（1 款）

| 机型                     | ID            | 缺失字段    | 游戏内当前值（估计）     |
| ---------------------- | ------------- | ------- | -------------- |
| Lockheed L-188 Electra | LOCKHEED_L188 | 价格(USD) | cost_factor=18 |

## McDonnell_Douglas（4 款）

| 机型              | ID             | 缺失字段    | 游戏内当前值（估计）     |
| --------------- | -------------- | ------- | -------------- |
| Douglas DC-6    | DOUGLAS_DC6    | 价格(USD) | cost_factor=35 |
| Douglas DC-9-10 | Douglas_DC9_10 | 价格(USD) | cost_factor=38 |
| Douglas DC-9-20 | Douglas_DC9_20 | 价格(USD) | cost_factor=38 |
| Douglas DC-9-30 | Douglas_DC9_30 | 价格(USD) | cost_factor=42 |

## PZL（1 款）

| 机型                         | ID       | 缺失字段    | 游戏内当前值（估计）     |
| -------------------------- | -------- | ------- | -------------- |
| PZL/Antonov AN-28 Skytruck | PZL_AN28 | 价格(USD) | cost_factor=14 |

## Tupolev（1 款）

| 机型             | ID            | 缺失字段    | 游戏内当前值（估计）     |
| -------------- | ------------- | ------- | -------------- |
| Tupolev Tu-134 | Tupolev_Tu134 | 价格(USD) | cost_factor=32 |

## Vickers（1 款）

| 机型           | ID           | 缺失字段    | 游戏内当前值（估计）      |
| ------------ | ------------ | ------- | --------------- |
| Vickers VC10 | VICKERS_VC10 | 价格(USD) | cost_factor=169 |

## de Havilland（1 款）

| 机型                 | ID                | 缺失字段   | 游戏内当前值（估计） |
| ------------------ | ----------------- | ------ | ---------- |
| de Havilland Comet | DEHAVILLAND_COMET | 航程(km) | ≈7398 km   |
