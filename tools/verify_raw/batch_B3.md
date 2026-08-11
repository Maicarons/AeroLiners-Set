# 批次B3（Boeing 3/4）

核对日期：2026-08-10
方法：主源 aerocorner.com，交叉 en.wikipedia.org 型号/家族专页，缺失用 WebSearch 补充（barrieaircraft、liquisearch、airliners.net、deagel、sprinkle、baike/newton 镜像等）。
说明：
- 价格均注明年份；"未找到可靠来源"者多为客改货/客货混装/特定子型（无独立公布目录价）。
- 航程：nmi×1.852=km；标注"最大/典型"或"满载/典型两级"。
- 座级：标注"两级/三级/单级"。货机为 0 客，列业载。
- 巡航：kt×1.852≈km/h；Mach×1062≈km/h。游戏 speed_kmh 普遍偏高（接近最大速度而非典型巡航）。
- 游戏内 range_km_est = base_range×5.5；下表"游戏内当前值"列直接引用该估算值对比。

---

### Boeing 747-300 (Boeing_747_300)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$83 million (1982) | https://aerocorner.com/aircraft/boeing-747-300/ | (游戏 cost_factor=274) | 合理 |
| 航程 | 11,720 km (6,330 nmi) | https://aerocorner.com/aircraft/boeing-747-300/ （barrieaircraft: 11,675 km/6,300 nmi；liquisearch 最高 12,400 km/6,700 nmi） | range_km_est 12,292 km | 真实 11,720 vs 游戏 12,292，接近 |
| 座级 | 412 人(三级典型) / 496 人(两级) / 最高 524 人(单级) | https://www.liquisearch.com/boeing_747/specifications （aerocorner 列 496） | passenger 412 人 | 三级 412 与游戏吻合 |
| 巡航 | ~905 km/h (Mach 0.85, ~490 kt) | https://en.wikipedia.org/wiki/Boeing_747 （barrieaircraft 经济巡航 907 km/h） | speed_kmh 999 km/h | 游戏偏高，接近最大速度(~939 km/h) |

### Boeing 747-300M (Boeing_747_300M)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（客货混装型无独立目录价；参照 747-300 约 US$50–83M） | https://accaviation.com/aviation-consultancy/sell-buy-boeing-747-200b-300-lcf-dreamlifter | (游戏 cost_factor=274) | 混装型无单独目录价 |
| 航程 | 12,400 km (6,700 nmi) | https://baike.baidu.com/item/%E6%B3%A2%E9%9F%B3747-300Combi | range_km_est 11,908 km | 真实 12,400 vs 游戏 11,908，接近 |
| 座级 | 全客典型 366 人(三级)；混装态约 245–266 人 + 主舱货盘 | https://baike.baidu.com/item/%E6%B3%A2%E9%9F%B3747-300Combi （airliners.net combi 约 266 人） | passenger 245 人 | 混装座级 245 与真实混装态一致 |
| 巡航 | Mach 0.85 (~905 km/h, ~490 kt) | https://baike.baidu.com/item/%E6%B3%A2%E9%9F%B3747-300Combi | speed_kmh 999 km/h | 游戏偏高 |

### Boeing 747-400 (Boeing_747_400)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$266.5 million (2007) | https://aerocorner.com/aircraft/boeing-747-400/ | (游戏 cost_factor=297) | 合理 |
| 航程 | 13,450 km (7,260 nmi) | https://en.wikipedia.org/wiki/Boeing_747-400 （planefyi / liquisearch 同值） | range_km_est 13,310 km | 高度吻合 |
| 座级 | 416 人(三级典型) / 524 人(两级最高) | https://en.wikipedia.org/wiki/Boeing_747-400 （stands.aero 同值） | passenger 416 人 | 吻合 |
| 巡航 | 910 km/h (Mach 0.855, 491 kt) | https://en.wikipedia.org/wiki/Boeing_747-400 | speed_kmh 991 km/h | 游戏偏高（接近最大速度） |

### Boeing 747-400BCF (Boeing_747_400BCF)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（客改货，无独立目录价） | https://en.wikipedia.org/wiki/Boeing_747-400 （BCF 为客改货，无单独公布价） | (游戏 cost_factor=187) | 改装货机无目录价 |
| 航程 | ≈8,250 km (4,455 nmi)（近似 747-400F；BCF 无独立公布值） | https://en.wikipedia.org/wiki/Boeing_747-400 （取 747-400F 值） | range_km_est 7,508 km | 游戏航程偏短（真实约 8,250 km）；BCF 仅侧货门、无鼻门，航程略短于新造 F |
| 座级 | 0 人(全货)；主货舱约 30 货板 | https://en.wikipedia.org/wiki/Boeing_747-400 | passenger 0 人 | 吻合 |
| 巡航 | 910 km/h (Mach 0.855, 491 kt) | https://en.wikipedia.org/wiki/Boeing_747-400 | speed_kmh 991 km/h | 游戏偏高 |

### Boeing 747-400D (Boeing_747_400D)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（日本国内型，无独立目录价；参照 747-400 ~US$266.5M） | https://aerocorner.com/aircraft/boeing-747-400/ | (游戏 cost_factor=274) | 国内型无单独目录价 |
| 航程 | 10,000 km (5,556 nmi) | https://baike.baidu.com/view/327402.htm （newton 镜像同值） | range_km_est 3,300 km | ⚠ 游戏 3,300 km 严重不足（真实 10,000 km；D 为短程国内型但远超此值） |
| 座级 | 568 人(高密度两级) | https://en.wikipedia.org/wiki/Boeing_747-400 （baike 同值） | passenger 560 人 | 吻合 |
| 巡航 | 957 km/h (Mach 0.85, 487 kt) | https://baike.baidu.com/view/327402.htm | speed_kmh 991 km/h | 游戏偏高 |

### Boeing 747-400ER (Boeing_747_400ER)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源 | https://en.wikipedia.org/wiki/Boeing_747-400 | (游戏 cost_factor=298) | 无单独目录价来源 |
| 航程 | 14,045 km (7,585 nmi) | https://en.wikipedia.org/wiki/Boeing_747-400 | range_km_est 14,052 km | 极吻合 |
| 座级 | 416 人(三级) / 524 人(两级) | https://en.wikipedia.org/wiki/Boeing_747-400 | passenger 524 人 | 两级 524 与游戏吻合 |
| 巡航 | 899 km/h (Mach 0.845, 485 kt) | https://en.wikipedia.org/wiki/Boeing_747-400 | speed_kmh 991 km/h | 游戏偏高 |

### Boeing 747-400ERF (Boeing_747_400ERF)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源 | https://en.wikipedia.org/wiki/Boeing_747-400 | (游戏 cost_factor=311) | 无单独目录价来源 |
| 航程 | 9,230 km (4,985 nmi) | https://en.wikipedia.org/wiki/Boeing_747-400 | range_km_est 9,102 km | 吻合 |
| 座级 | 0 人(全货)；最大业载 248,600 lb (112,760 kg) | https://en.wikipedia.org/wiki/Boeing_747-400 | passenger 0 人 | 吻合 |
| 巡航 | 899 km/h (Mach 0.845, 485 kt) | https://en.wikipedia.org/wiki/Boeing_747-400 | speed_kmh 991 km/h | 游戏偏高 |

### Boeing 747-400M (Boeing_747_400M)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源 | https://en.wikipedia.org/wiki/Boeing_747-400 | (游戏 cost_factor=293) | 客货混装无单独目录价 |
| 航程 | 13,450 km (7,260 nmi) | https://baike.baidu.com/view/327425.htm （747-400M 同值） | range_km_est 13,200 km | 吻合 |
| 座级 | 混装典型 266 人(三级) + 主舱 6–7 货盘（全客 413 人） | https://www.airliners.net/info/stats.main?id=100 （baidu 同值） | passenger 266 人 | 吻合 |
| 巡航 | 957 km/h (Mach 0.85, 487 kt) | https://baike.baidu.com/view/327425.htm | speed_kmh 991 km/h | 游戏偏高 |

### Boeing 747-400SCD (Boeing_747_400SCD)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（客改组合货 deck，无独立目录价） | https://sprinkle.com/aircraft/PH-BFW （747 406 SCD） | (游戏 cost_factor=291) | 改装组合货 deck 无目录价 |
| 航程 | 13,440 km (7,260 nmi) | https://sprinkle.com/aircraft/PH-BFW （747 406 SCD） | range_km_est 8,140 km | ⚠ 游戏 8,140 km 偏短（真实约 13,440 km） |
| 座级 | 组合货 deck 型，可载客（典型约 266–450 人）或全货；游戏记 0 客(纯货配置) | https://sprinkle.com/aircraft/PH-BFW （Seats 450） | passenger 0 人 | SCD 为可载货/客的组合 deck；游戏按纯货记 0 |
| 巡航 | 911 km/h (492 kt, Mach ~0.85) | https://sprinkle.com/aircraft/PH-BFW | speed_kmh 991 km/h | 游戏偏高 |

### Boeing 747-8F (Boeing_747_8F)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$419.2 million (2019) | https://en.wikipedia.org/wiki/Boeing_747-8 | (游戏 cost_factor=322) | 合理 |
| 航程 | 8,130 km (4,390 nmi, 最大业载) | https://en.wikipedia.org/wiki/Boeing_747-8 | range_km_est 8,195 km | 吻合 |
| 座级 | 0 人(全货)；业载 308,000 lb (140 t) | https://en.wikipedia.org/wiki/Boeing_747-8 | passenger 0 人 | 吻合 |
| 巡航 | 898 km/h (Mach 0.845, 485 kt) | https://en.wikipedia.org/wiki/Boeing_747-8 | speed_kmh 1007 km/h | 游戏偏高 |

### Boeing 747-8I (Boeing_747_8I)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$418.4 million (2019) | https://en.wikipedia.org/wiki/Boeing_747-8 | (游戏 cost_factor=321) | 合理 |
| 航程 | 15,000 km (8,000 nmi, 三级 467 人) | https://en.wikipedia.org/wiki/Boeing_747-8 | range_km_est 14,658 km | 接近（真实 15,000 km） |
| 座级 | 467 人(三级典型) | https://en.wikipedia.org/wiki/Boeing_747-8 | passenger 467 人 | 吻合 |
| 巡航 | 908 km/h (Mach 0.855, 490 kt) | https://en.wikipedia.org/wiki/Boeing_747-8 | speed_kmh 1007 km/h | 游戏偏高（接近最大速度 Mach 0.9） |

### Boeing 757-200 (Boeing_757_200)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$65 million (2002) | https://aerocorner.com/aircraft/boeing-757-200/ | (游戏 cost_factor=79) | 合理 |
| 航程 | 7,130 km (3,850 nmi, 满载) / 7,250 km (3,915 nmi, 两级典型) | https://en.wikipedia.org/wiki/Boeing_757 | range_km_est 7,508 km | 接近 |
| 座级 | 200 人(两级典型) / 最高 239 人 | https://en.wikipedia.org/wiki/Boeing_757 | passenger 200 人 | 吻合 |
| 巡航 | 858 km/h (Mach 0.8, ~463 kt) | https://en.wikipedia.org/wiki/Boeing_757 | speed_kmh 934 km/h | 游戏偏高 |

### Boeing 757-200F (Boeing_757_200F)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$60 million | https://www.deagel.com/Airliners/Boeing-757-200F_a000203002.aspx （Unitary Cost） | (游戏 cost_factor=82) | 二级市场来源，合理量级 |
| 航程 | 5,830 km (3,150 nmi, 满载) | https://en.wikipedia.org/wiki/Boeing_757 | range_km_est 5,775 km | 极吻合 |
| 座级 | 0 人(全货)；最大业载 39,800 kg | https://en.wikipedia.org/wiki/Boeing_757 | passenger 0 人 | 吻合 |
| 巡航 | 858 km/h (Mach 0.8, ~463 kt) | https://en.wikipedia.org/wiki/Boeing_757 | speed_kmh 934 km/h | 游戏偏高 |

### Boeing 767-200 (Boeing_767_200)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$160.2 million | https://aerocorner.com/aircraft/boeing-767-200/ （未标注年份；Wikipedia 仅列 767-200ER 同价 US$160.2M，基型原始目录价约 US$45M/1982） | (游戏 cost_factor=127) | aerocorner 列价偏高（疑似等效/ER 价）；基型原始约 US$45M |
| 航程 | 7,200 km (3,900 nmi, 典型) / 7,130 km (3,850 nmi, 设计) | https://en.wikipedia.org/wiki/Boeing_767 | range_km_est 7,068 km | 吻合 |
| 座级 | 216 人(两级典型) / 最高 255–290 人 | https://en.wikipedia.org/wiki/Boeing_767 | passenger 181 人 | ⚠ 游戏 181 偏低（真实典型 216） |
| 巡航 | 858 km/h (Mach 0.8, ~463 kt) | https://en.wikipedia.org/wiki/Boeing_767 | speed_kmh 910 km/h | 游戏偏高（接近最大速度 ~893 km/h） |

---

## 汇总备注
- 座级（passenger）：747-400/400ER/400M/8I/757-200/757-200F 与游戏高度吻合；747-400D(560)与 747-300M(245)/400M(266) 混装/国内型也合理。
- 航程（range_km_est）：多数吻合或接近；⚠ 747-400D（游戏 3,300 vs 真实 10,000 km）与 747-400SCD（游戏 8,140 vs 真实 13,440 km）明显偏短，建议校正。747-400BCF 真实约 8,250 km 亦高于游戏 7,508 km。
- 巡航（speed_kmh）：全部机型游戏值均高于真实典型巡航约 8–12%（多为接近最大速度取值），属系统性偏差，非单架问题。
- 价格字段：客改货（BCF/SCD）、客货混装（300M/400M）、国内型（400D）及 400ER/ERF 无独立可靠目录价来源，已标"未找到可靠来源"。
