# 批次S1（ATR / AVIC / Antonov）

> 字段说明：价格(USD,注年份)｜航程(km;nm×1.852；注明最大/典型)｜座级(两舱/最大)｜巡航(km/h;kt×1.852；马赫≈Mach×1062)
> 来源：主源 aerocorner.com，交叉 en.wikipedia.org，缺失 WebSearch（同花顺/百度/民航局/各航空资料站）。每条标注实际读取 URL。

---

### ATR 42-300 (ATR_42_300)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 约 US$9.2M（ATR 42-200 单价，1991）／全系估值 US$18–19.5M；**无 -300 单独目录价** | https://baike.baidu.com/item/ATR42%E9%A3%9E%E6%9C%BA （1991 单价）；https://www.deagel.com/Civil%20Aviation/ATR%204272/a000090 （ATR 42 组 US$18M）；https://www.newton.com.tw/wiki/ATR42%E9%A3%9E%E6%9C%BA （单机造价 US$19.5M/2012） | (cost_factor=11) | 合理区间，无精确 -300 价 |
| 航程 | 1,470 km（48 座最大商载，794 nmi）；最大燃油 4,481 km | https://en.wikipedia.org/wiki/ATR_42 ；https://www.caac.gov.cn/PHONE/GYMH/MHBK/HKQJS/201509/t20150923_1832.html | range_km_est 908 km | 游戏偏低约 38%（取最大商载值） |
| 座级 | 48 人（30" 间距） | https://en.wikipedia.org/wiki/ATR_42 | passenger 48 人 | 一致 |
| 巡航 | 484 km/h（261 kt，最大巡航）；495 km/h（CAAC 最大巡航） | https://en.wikipedia.org/wiki/ATR_42 ；https://www.caac.gov.cn/PHONE/GYMH/MHBK/HKQJS/201509/t20150923_1832.html | speed_kmh 491 km/h | 一致 |

### ATR 42-300F (ATR_42_300F)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 由客机改装，无单独目录价；约 US$9–19.5M 估算 | https://baike.baidu.com/item/ATR42%E9%A3%9E%E6%9C%BA ；https://www.newton.com.tw/wiki/ATR42%E9%A3%9E%E6%9C%BA | (cost_factor=12) | 货机换算系数略高，合理 |
| 航程 | 约 2,316 km（载 3,800 kg 货或 42 客，ATR 42-F） | https://baike.baidu.com/item/ATR42%E9%A3%9E%E6%9C%BA （ATR42-F） | range_km_est 908 km | 游戏严重偏低（货机实际航程更高） |
| 座级 | 0（全货运） | https://en.wikipedia.org/wiki/ATR_42 | passenger 0 人 | 一致 |
| 巡航 | 约 484–495 km/h | https://en.wikipedia.org/wiki/ATR_42 | speed_kmh 491 km/h | 一致 |

### ATR 42-500 (ATR_42_500)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$12.1 million | https://aerocorner.com/aircraft/atr-42-500/ | (cost_factor=14) | 合理 |
| 航程 | 1,345 km（48 座，726 nmi） | https://en.wikipedia.org/wiki/ATR_42 | range_km_est 1540 km | 游戏偏高约 14% |
| 座级 | 48 人（30" 间距） | https://aerocorner.com/aircraft/atr-42-500/ ；https://en.wikipedia.org/wiki/ATR_42 | passenger 48 人 | 一致 |
| 巡航 | 556 km/h（300 kt，最大巡航） | https://en.wikipedia.org/wiki/ATR_42 | speed_kmh 564 km/h | 基本一致（差 1.4%） |

### ATR 42-600 (ATR_42_600)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$19.5 million | https://aerocorner.com/aircraft/atr-42-600/ | (cost_factor=14) | 合理 |
| 航程 | 1,345 km（48 座，726 nmi）；满客最大速度航程 716 nmi≈1,326 km | https://en.wikipedia.org/wiki/ATR_42 ；https://aerocorner.com/aircraft/atr-42-600/ | range_km_est 1348 km | 高度一致 |
| 座级 | 48 人（40–50 典型） | https://aerocorner.com/aircraft/atr-42-600/ ；https://en.wikipedia.org/wiki/ATR_42 | passenger 48 人 | 一致 |
| 巡航 | 535 km/h（289 kt）；aerocorner 最大 556 km/h | https://en.wikipedia.org/wiki/ATR_42 | speed_kmh 564 km/h | 游戏偏高约 5% |

### ATR 72-200 (ATR_72_200)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 约 US$21 million（ATR 72 组估值；无 -200 单独价） | https://www.deagel.com/Civil%20Aviation/ATR%204272/a000090 | (cost_factor=16) | 合理 |
| 航程 | 1,596 km（最大客载，862 nmi） | https://en.wikipedia.org/wiki/ATR_72 | range_km_est 1595 km | 几乎一致 |
| 座级 | 66@31" / 72@29"，最大 78 | https://en.wikipedia.org/wiki/ATR_72 | passenger 74 人 | 在范围内 |
| 巡航 | 515 km/h（278 kt） | https://en.wikipedia.org/wiki/ATR_72 | speed_kmh 515 km/h | 完全一致 |

### ATR 72-200F (ATR_72_200F)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 由客机改装，无单独目录价；约 US$21M 估算 | https://www.deagel.com/Civil%20Aviation/ATR%204272/a000090 | (cost_factor=19) | 货机系数略高，合理 |
| 航程 | 约 1,596 km（同 -200 客机基准，货载不同） | https://en.wikipedia.org/wiki/ATR_72 | range_km_est 1595 km | 一致 |
| 座级 | 0（全货运） | https://en.wikipedia.org/wiki/ATR_72 | passenger 0 人 | 一致 |
| 巡航 | 约 515–517 km/h | https://en.wikipedia.org/wiki/ATR_72 | speed_kmh 523 km/h | 基本一致 |

### ATR 72-500 (ATR_72_500)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$14.4 million（aerocorner；Wikipedia 仅列 -600 价） | https://aerocorner.com/aircraft/atr-72-500/ | (cost_factor=18) | 合理 |
| 航程 | 1,430 km（最大客载，772 nmi） | https://en.wikipedia.org/wiki/ATR_72 | range_km_est 1622 km | 游戏偏高约 13% |
| 座级 | 74（典型），最大 78 | https://aerocorner.com/aircraft/atr-72-500/ ；https://en.wikipedia.org/wiki/ATR_72 | passenger 74 人 | 一致 |
| 巡航 | 510 km/h（275 kt） | https://en.wikipedia.org/wiki/ATR_72 | speed_kmh 515 km/h | 基本一致 |

### ATR 72-600 (ATR_72_600)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$26 million（2017）；目录价 US$26.8M、折后约 US$20.1M（2018） | https://aerocorner.com/aircraft/atr-72-600/ ；https://en.wikipedia.org/wiki/ATR_72 | (cost_factor=18) | 合理 |
| 航程 | 1,404 km（最大客载，758 nmi）；aerocorner 列 "最大航程 2,065 mi≈3,323 km"（疑似最大燃油） | https://en.wikipedia.org/wiki/ATR_72 ；https://aerocorner.com/aircraft/atr-72-600/ | range_km_est 1370 km | 接近（取最大客载值） |
| 座级 | 72（29" 间距），最大 78 | https://aerocorner.com/aircraft/atr-72-600/ ；https://en.wikipedia.org/wiki/ATR_72 | passenger 72 人 | 一致 |
| 巡航 | 510 km/h（275 kt） | https://en.wikipedia.org/wiki/ATR_72 | speed_kmh 515 km/h | 基本一致 |

### AVIC MA-60 (AVIC_MA60)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 目录价 US$14.5 million（2011，9 架合同） | https://m.10jqka.com.cn/20110929/c61758076.shtml | (cost_factor=14) | 高度一致 |
| 航程 | 1,600 km（860 nmi） | https://en.wikipedia.org/wiki/Xi%27an_MA60 | range_km_est 1370 km | 游戏偏低约 14% |
| 座级 | 60（典型）/ 最大 62 | https://en.wikipedia.org/wiki/Xi%27an_MA60 | passenger 60 人 | 一致 |
| 巡航 | 430 km/h（230 kt） | https://en.wikipedia.org/wiki/Xi%27an_MA60 | speed_kmh 430 km/h | 完全一致 |

### AVIC MA-600 (AVIC_MA600)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | **未找到可靠单独目录价**；参考 MA60 约 US$14.5M | https://en.wikipedia.org/wiki/Xi%27an_MA600 （无价） | (cost_factor=18) | 系数偏高，建议复核 |
| 航程 | 1,430 km（770 nmi，56 客+储备） | https://en.wikipedia.org/wiki/Xi%27an_MA600 | range_km_est 1380 km | 接近 |
| 座级 | 60（最大） | https://en.wikipedia.org/wiki/Xi%27an_MA600 | passenger 60 人 | 一致 |
| 巡航 | 430 km/h（230 kt） | https://en.wikipedia.org/wiki/Xi%27an_MA600 | speed_kmh 430 km/h | 完全一致 |

### AVIC Y-7-200 (AVIC_Y7_200)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | **未找到可靠目录价**（Y-7 系列无公开价） | https://en.wikipedia.org/wiki/Xian_Y-7 （无价） | (cost_factor=14) | 无法核对 |
| 航程 | Y-7-200 无独立数据；参考 Y-7-100：最大商载 910 km，最大燃油 1,982 km | https://en.wikipedia.org/wiki/Xian_Y-7 | range_km_est 1551 km | 取最大燃油值接近；Y-7-200 实测缺失 |
| 座级 | Y-7-100：52（最大）；Y-7-200 无独立数据 | https://en.wikipedia.org/wiki/Xian_Y-7 | passenger 52 人 | 与 Y-7-100 一致 |
| 巡航 | 423 km/h（228 kt，Y-7-100） | https://en.wikipedia.org/wiki/Xian_Y-7 | speed_kmh 420 km/h | 基本一致 |

### Antonov An-140 (ANTONOV_AN140)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$9 million | https://aerocorner.com/aircraft/antonov-an-140/ | (cost_factor=14) | 合理（系数偏高些） |
| 航程 | 2,100 km（52 客）；最大商载 900 km；33 客 3,700 km | https://en.wikipedia.org/wiki/Antonov_An-140 | range_km_est 2101 km | 高度一致 |
| 座级 | 52（最大） | https://aerocorner.com/aircraft/antonov-an-140/ ；https://en.wikipedia.org/wiki/Antonov_An-140 | passenger 52 人 | 一致 |
| 巡航 | 575 km/h（310 kt，最大）；经济 520 km/h | https://en.wikipedia.org/wiki/Antonov_An-140 | speed_kmh 575 km/h | 完全一致 |

### Antonov An-148 (ANTONOV_AN148)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$22M（aerocorner）/ US$24–30M（2009 目录价） | https://aerocorner.com/aircraft/antonov-an-148/ ；https://en.wikipedia.org/wiki/Antonov_An-148 | (cost_factor=50) | 合理 |
| 航程 | 2,100–4,400 km（典型 2,100；-100E 最大 4,400 km） | https://en.wikipedia.org/wiki/Antonov_An-148 | range_km_est 3102 km | 在范围内（取中值） |
| 座级 | 68（两舱）/ 最大 85 | https://aerocorner.com/aircraft/antonov-an-148/ ；https://en.wikipedia.org/wiki/Antonov_An-148 | passenger 80 人 | 在范围内 |
| 巡航 | 800–870 km/h（Mach 0.80≈850 km/h） | https://en.wikipedia.org/wiki/Antonov_An-148 ；https://aerocorner.com/aircraft/antonov-an-148/ | speed_kmh 830 km/h | 在范围内 |

### Antonov An-158 (ANTONOV_AN158)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 约 US$25–30M（2011 基价 US$25M；目录约 US$30M） | https://aviamuseum.com.ua/en/news/museum-news/1456-april-28-is-the-15th-anniversary-of-the-an-158-regional-airliner ；https://www.beyondtheordinary.co.uk/features/antonov-an-158-cubas-unique-passenger-jet | (cost_factor=65) | 合理 |
| 航程 | 2,500 km（75 客）；实用 2,600 km | https://en.wikipedia.org/wiki/Antonov_An-148 ；https://aviamuseum.com.ua/en/news/museum-news/1456-april-28-is-the-15th-anniversary-of-the-an-158-regional-airliner | range_km_est 2800 km | 游戏偏高约 12% |
| 座级 | 86–99（最大 99） | https://en.wikipedia.org/wiki/Antonov_An-148 | passenger 90 人 | 在范围内 |
| 巡航 | 870 km/h（An-158 实用）；家族 800–870 km/h | https://aviamuseum.com.ua/en/news/museum-news/1456-april-28-is-the-15th-anniversary-of-the-an-158-regional-airliner ；https://en.wikipedia.org/wiki/Antonov_An-148 | speed_kmh 886 km/h | 游戏略高（约 1.8%） |

### Antonov An-124 (Antonov_124)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$70–100 million（历史；商用估计 US$50–90M） | https://www.wikiwand.com/sl/articles/An-124 ；https://www.aircharterservice.co.kr/aircraft-guide/cargo/antonov-ukraine/antonov-an-124 | (cost_factor=274) | 重型机，系数合理 |
| 航程 | 最大商载(120t) 3,700 km；80t 8,400 km；转场 14,000 km | https://en.wikipedia.org/wiki/Antonov_An-124 | range_km_est 5912 km | 介于部分商载与转场之间（取 80t 级更接近） |
| 座级 | 0（货运）；上舱 88 客 / 货舱可载 350 人（应急） | https://en.wikipedia.org/wiki/Antonov_An-124 | passenger 0 人 | 一致（货机） |
| 巡航 | 865 km/h（最大）；典型 800–850 km/h | https://en.wikipedia.org/wiki/Antonov_An-124 | speed_kmh 862 km/h | 一致 |

### Antonov An-225 (Antonov_225)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 估算 US$250–300M（2005 估 US$300M；独特机，2022 被毁，无售价） | https://simpleflying.com/5-facts-about-antonov-an-225-mriya-largest-aircraft-built ；https://www.aircharterchina.cn/aircraft/antonovan-225/ | (cost_factor=274) | 重型机，系数与 An-124 持平，合理 |
| 航程 | 15,400 km（最大燃油）；200t 商载 4,000 km | https://en.wikipedia.org/wiki/Antonov_An-225 | range_km_est 15235 km | 高度一致（取最大燃油） |
| 座级 | 0（货运，最大载重 250 t） | https://en.wikipedia.org/wiki/Antonov_An-225 | passenger 0 人 | 一致（货机） |
| 巡航 | 800 km/h（430 kt） | https://en.wikipedia.org/wiki/Antonov_An-225 | speed_kmh 846 km/h | 游戏略高（约 5.8%） |

---

## 批次汇总（偏差提示）
- **航程**：ATR 42-300 / ATR 42-300F 游戏值明显偏低（客机约 −38%，货机差更大，因货机实际满油航程高于客机基准）；其余机型基本在 ±15% 内。建议复核 ATR 42-300 系列 base_range。
- **座级**：全部一致或在真实范围内。
- **巡航**：全部在 ±6% 内，基本一致。
- **价格**：多为历史/估算区间，无单一官方目录价时以系列估值或同期同型参考；MA600、Y-7-200 缺可靠目录价，已在单元格标注。
- **货机(300F/200F)**：座级 0 正确；价格按改装估算，航程建议采用对应满油/货载值而非客机最大商载值。
