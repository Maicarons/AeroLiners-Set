# 批次B2（Boeing 2/4）

> 核对说明：真实值统一换算为 km / km/h；价格填现实目录价 USD 作参考（游戏 cost_factor 为相对系数，非绝对值）。
> 主源 aerocorner.com，交叉源英文维基百科家族页、SimpleFlying、knaviation 2019 目录价表、airliners.net 论坛（货机改装费）。每条均标注实际读取 URL。
> 说明：aerocorner 个别页面数据混乱（如 737-800 页误写"526 seats"），已以维基/官方目录价交叉校正；737-300F、737-900 无标准整机目录价，已注明。

---

### Boeing 737-300F (Boeing_737_300F)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 无官方整机目录价（客改货）。客改货改装费 ≈US$2.5M（IBA/ISTAT）；含购机+改装整机约 US$8–9M | https://www.airliners.net/forum/viewtopic.php?f=3&t=1453721 ；https://www.aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Freight/2013/ISSUE86_FRT.pdf | (游戏 cost_factor=45) | 货机，以 737-300 为基型；无整机目录价 |
| 航程 | ≈4,176 km (2,255 nmi) [126 客位，典型] | https://en.wikipedia.org/wiki/Boeing_737_Classic | range_km_est 4648 km | 较接近（游戏略高） |
| 座级 | 0（全货机） | —（货机定义） | passenger 0 人 | 一致 |
| 巡航 | ≈828 km/h (Mach 0.78) | https://simpleflying.com/tag/boeing-737/classic/ | speed_kmh 910 km/h | 游戏偏高（910 vs 真实 ~828） |

### Boeing 737-400 (Boeing_737_400)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$35.0M (1988 目录价) | https://simpleflying.com/tag/boeing-737/classic/ | (游戏 cost_factor=49) | 历史目录价 |
| 航程 | ≈3,820 km (2,060 nmi) [147 客位] | https://en.wikipedia.org/wiki/Boeing_737_Classic | range_km_est 4152 km | 游戏略高 |
| 座级 | 188 人（最大）；典型 147–168 | https://en.wikipedia.org/wiki/Boeing_737_Classic ；https://simpleflying.com/tag/boeing-737/classic/ | passenger 146 人 | 游戏取典型低端 |
| 巡航 | ≈828 km/h (Mach 0.78) | https://simpleflying.com/tag/boeing-737/classic/ | speed_kmh 918 km/h | 游戏偏高 |

### Boeing 737-500 (Boeing_737_500)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$29.5M (1990 目录价)；aerocorner 列 $31M (2020) | https://simpleflying.com/tag/boeing-737/classic/ ；https://aerocorner.com/aircraft/boeing-737-500/ | (游戏 cost_factor=53) | 两源一致量级 |
| 航程 | ≈4,398 km (2,375 nmi) [110 客位] | https://en.wikipedia.org/wiki/Boeing_737_Classic | range_km_est 4400 km | 几乎一致 |
| 座级 | 132 人（最大）；典型 110–140 | https://en.wikipedia.org/wiki/Boeing_737_Classic | passenger 108 人 | 游戏偏低 |
| 巡航 | ≈828 km/h (Mach 0.78) | https://simpleflying.com/tag/boeing-737/classic/ | speed_kmh 910 km/h | 游戏偏高 |

### Boeing 737-600 (Boeing_737_600)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$58.5M (2010) | https://aerocorner.com/aircraft/boeing-737-600/ | (游戏 cost_factor=53) | aerocorner 列价 |
| 航程 | ≈5,991 km (3,235 nmi) [110 客位] | https://en.wikipedia.org/wiki/Boeing_737_Next_Generation | range_km_est 5582 km | 游戏略低 |
| 座级 | 130 人（最大）；110 两舱 | https://en.wikipedia.org/wiki/Boeing_737_Next_Generation | passenger 108 人 | 游戏偏低 |
| 巡航 | ≈834 km/h (Mach 0.785；-800 极速 Mach 0.82) | https://en.wikipedia.org/wiki/Boeing_737_Next_Generation | speed_kmh 959 km/h | 游戏明显偏高 |

### Boeing 737-700 (Boeing_737_700)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$89.1M (2019 目录价) | https://www.knaviation.net/737-vs-a320/ | (游戏 cost_factor=64) | 2019 波音目录价 |
| 航程 | ≈5,570 km (3,010 nmi) [126 客位] | https://en.wikipedia.org/wiki/Boeing_737_Next_Generation | range_km_est 6160 km | 游戏略高 |
| 座级 | 149 人（最大）；126 两舱 | https://en.wikipedia.org/wiki/Boeing_737_Next_Generation | passenger 128 人 | 游戏取两舱附近 |
| 巡航 | ≈834 km/h (Mach 0.785；极速 Mach 0.82) | https://en.wikipedia.org/wiki/Boeing_737_Next_Generation | speed_kmh 975 km/h | 游戏偏高 |

### Boeing 737-800 (Boeing_737_800)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$106.1M (2019 目录价) | https://www.knaviation.net/737-vs-a320/ | (游戏 cost_factor=74) | 2019 波音目录价（aerocorner 误列 $89.2M） |
| 航程 | ≈5,436 km (2,935 nmi) [162 客位] | https://en.wikipedia.org/wiki/Boeing_737_Next_Generation | range_km_est 5610 km | 游戏略高 |
| 座级 | 189 人（最大）；162 两舱 | https://en.wikipedia.org/wiki/Boeing_737_Next_Generation | passenger 160 人 | 游戏取两舱 |
| 巡航 | ≈837 km/h (Mach 0.82 max；典型 0.785) | https://en.wikipedia.org/wiki/Boeing_737_Next_Generation | speed_kmh 975 km/h | 游戏偏高 |

### Boeing 737-900 (Boeing_737_900)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 无单独 2019 目录（仅 -900ER 入列）；参考 737-900ER US$112.6M (2019)，基础型略低 | https://www.knaviation.net/737-vs-a320/ ；https://aerocorner.com/aircraft/boeing-737-900er/ | (游戏 cost_factor=77) | 基础型产量少、无独立目录价 |
| 航程 | ≈5,500 km (2,975 nmi) | https://www.aviation-center.com.au/contents/en-us/d146.html | range_km_est 3768 km | 游戏明显偏低 |
| 座级 | 189 人（两舱典型）；最高 ~215–220 | https://www.aviation-center.com.au/contents/en-us/d146.html ；https://baike.baidu.com/view/327480.html | passenger 180 人 | 游戏取两舱 |
| 巡航 | ≈828 km/h (Mach 0.785) | https://www.aviation-center.com.au/contents/en-us/d146.html | speed_kmh 975 km/h | 游戏偏高 |

### Boeing 737-900ER (Boeing_737_900ER)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$112.6M (2019) | https://aerocorner.com/aircraft/boeing-737-900er/ ；https://www.knaviation.net/737-vs-a320/ | (游戏 cost_factor=80) | 两源一致 |
| 航程 | ≈5,925 km (3,200 nmi) | https://baike.com/wikiid/8425867783035115666 （737-900ER 段） | range_km_est 4950 km | 游戏偏低 |
| 座级 | 220 人（最大）；177–180 两舱 | https://en.wikipedia.org/wiki/Boeing_737_Next_Generation ；https://aerocorner.com/aircraft/boeing-737-900er/ | passenger 180 人 | 游戏取两舱 |
| 巡航 | ≈840 km/h (Mach 0.785) | https://en.wikipedia.org/wiki/Boeing_737_Next_Generation | speed_kmh 975 km/h | 游戏偏高 |

### Boeing 737 MAX 8 (Boeing_737_MAX8)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$121.6M (2019) | https://aerocorner.com/aircraft/boeing-737-max-8/ ；https://www.knaviation.net/737-vs-a320/ | (游戏 cost_factor=101) | 两源一致 |
| 航程 | ≈6,500 km (3,500 nmi) [典型] | https://en.wikipedia.org/wiki/Boeing_737_MAX | range_km_est 6628 km | 接近 |
| 座级 | 189 人（最大）；178 两舱 | https://en.wikipedia.org/wiki/Boeing_737_MAX | passenger 162 人 | 游戏偏低（取两舱偏低端） |
| 巡航 | ≈842 km/h (Mach 0.79) | https://aerocorner.com/aircraft/boeing-737-max-8/ （家族 Mach 0.79） | speed_kmh 975 km/h | 游戏偏高 |

### Boeing 737 MAX 9 (Boeing_737_MAX9)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$128.9M (2019) | https://aerocorner.com/aircraft/boeing-737-max-9/ ；https://www.knaviation.net/737-vs-a320/ | (游戏 cost_factor=106) | 两源一致 |
| 航程 | ≈6,100 km (3,300 nmi) [典型] | https://en.wikipedia.org/wiki/Boeing_737_MAX | range_km_est 6518 km | 接近 |
| 座级 | 220 人（最大）；193 两舱 | https://en.wikipedia.org/wiki/Boeing_737_MAX | passenger 178 人 | 游戏偏低 |
| 巡航 | ≈842 km/h (Mach 0.79) | https://aerocorner.com/aircraft/boeing-737-max-9/ （家族 Mach 0.79） | speed_kmh 975 km/h | 游戏偏高 |

### Boeing 737 MAX 10 (Boeing_737_MAX10)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$134.9M (2019) | https://aerocorner.com/aircraft/boeing-737-max-10/ ；https://www.knaviation.net/737-vs-a320/ | (游戏 cost_factor=112) | 两源一致 |
| 航程 | ≈5,700 km (3,100 nmi) [典型] | https://en.wikipedia.org/wiki/Boeing_737_MAX | range_km_est 5742 km | 接近 |
| 座级 | 230 人（最大）；204 两舱 | https://en.wikipedia.org/wiki/Boeing_737_MAX | passenger 195 人 | 游戏取两舱 |
| 巡航 | ≈842 km/h (Mach 0.79) | https://aerocorner.com/aircraft/boeing-737-max-10/ （家族 Mach 0.79） | speed_kmh 975 km/h | 游戏偏高 |

### Boeing 747-100 (Boeing_747_100)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$146.7M (2019 目录价)；历史 US$24M (1972) | https://aerocorner.com/aircraft/boeing-747-100/ ；https://en.wikipedia.org/wiki/Boeing_747 | (游戏 cost_factor=276) | 2019 目录价 vs 历史出厂价 |
| 航程 | ≈9,800 km (5,300 nmi) [设计典型] | https://en.wikipedia.org/wiki/Boeing_747 | range_km_est 9158 km | 游戏略低 |
| 座级 | 366 人（三舱典型） | https://en.wikipedia.org/wiki/Boeing_747 | passenger 366 人 | 一致 |
| 巡航 | ≈900 km/h (Mach 0.85) | https://en.wikipedia.org/wiki/Boeing_747 | speed_kmh 967 km/h | 游戏略高 |

### Boeing 747-200 (Boeing_747_200)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$39M (1976) | https://aerocorner.com/aircraft/boeing-747-200/ ；https://en.wikipedia.org/wiki/Boeing_747 | (游戏 cost_factor=265) | 两源一致 |
| 航程 | ≈12,150 km (6,560 nmi) [最大；-200B 典型 ~11,000 km] | https://en.wikipedia.org/wiki/Boeing_747 | range_km_est 11000 km | 游戏取 -200B 典型量级 |
| 座级 | 366 人（三舱典型） | https://en.wikipedia.org/wiki/Boeing_747 | passenger 366 人 | 一致 |
| 巡航 | ≈900 km/h (Mach 0.85) | https://en.wikipedia.org/wiki/Boeing_747 | speed_kmh 967 km/h | 游戏略高 |

### Boeing 747-200M (Boeing_747_200M)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | ≈US$39M (1976，与 -200 共用基价；combi 无单独目录价) | https://aerocorner.com/aircraft/boeing-747-200/ | (游戏 cost_factor=265) | aerocorner 无独立 -200M 页 |
| 航程 | ≈12,150 km (6,560 nmi) [最大，同 -200] | https://en.wikipedia.org/wiki/Boeing_747 | range_km_est 11000 km | 游戏取典型量级 |
| 座级 | up to 238 人（三舱）+ 主货舱 | https://en.wikipedia.org/wiki/Boeing_747 | passenger 258 人 | 游戏偏高（取混合载客布局） |
| 巡航 | ≈900 km/h (Mach 0.85) | https://en.wikipedia.org/wiki/Boeing_747 | speed_kmh 967 km/h | 游戏略高 |

---

## 汇总观察
- **价格**：737 Classic 用历史目录价（300/400/500 约 US$29.5–35M），NG/MAX 用 2019 波音目录价（knaviation/aerocorner 一致）；747 用 1976/2019 目录价。游戏 cost_factor 为相对系数，量级顺序大致合理。
- **航程**：NG/MAX/747 批次游戏值与实际接近；**737-900 / 737-900ER 游戏航程明显偏低**（约 3,800–4,950 km vs 真实 5,500–5,925 km）。
- **座级**：游戏多取"两舱典型"偏低端，与真实两舱值基本吻合；747-200M 游戏 258 高于维基所述 238（combi 混合布局差异）。
- **巡航**：游戏 speed_kmh 系统性偏高（737 系列多在 910–975 km/h，而真实典型巡航约 828–842 km/h，极速 Mach 0.82≈880 km/h）。建议后续校准。
- **缺失/说明**：737-300F、737-900 无标准整机目录价，已注明；aerocorner 737-800 页"526 seats"为明显错误，已弃用。
