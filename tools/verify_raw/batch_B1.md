# 批次B1（Boeing 1/4）

> 说明：游戏内 `cost_factor` 为相对价格系数（游戏不存美元价）。下表「价格」填现实目录价 USD 作参考，并注明年份；偏差栏注明游戏用相对系数。
> 单位换算：nm×1.852=km；kt×1.852=km/h；巡航高度 Mach≈Mach×1062 km/h。
> 来源主用 aerocorner / 英文维基，交叉用 simpleflying / 247wallst 等。每字段均标实际读取 URL。

---

### Boeing 737 MAX 7 (BOEING_737MAX7)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $99.7 million（2019） | https://aerocorner.com/aircraft/boeing-737-max-7/ （simpleflying 亦列 $99.7m 2022） | (游戏 cost_factor=101) | 现实目录价仅参考；游戏用相对系数 |
| 航程 | 3,800 nmi（约 7,000 km）最大 | https://en.wikipedia.org/wiki/Boeing_737_MAX （对比表 3,800 nmi / 7,000 km） | range_km_est 7002 km | 几乎一致；simpleflying 列 3,850 nmi |
| 座级 | 153（两舱典型 8J+145Y）/ 最大 172（单舱） | https://en.wikipedia.org/wiki/Boeing_737_MAX （典型 153）；https://aerocorner.com/aircraft/boeing-737-max-7/ （172 单舱） | passenger 150 人 | 接近两舱典型值 |
| 巡航 | Mach 0.79（约 839 km/h，453 kn） | https://simpleflying.com/tag/boeing-737/max （MAX 7 巡航 Mach 0.79 ~839 km/h） | speed_kmh 975 km/h | 游戏值偏高（约 Mach 0.92 量级） |

注：737 MAX 7 于 2026 年才获 FAA 认证，尚未交付；座级/航程为厂商目标值。

---

### Boeing 747SP (BOEING_747SP)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $24 million（1972） | https://aerocorner.com/aircraft/boeing-747sp/ | (游戏 cost_factor=265) | 现实目录价仅参考 |
| 航程 | 6,650 nmi（约 12,315 km）最大 | https://aerocorner.com/aircraft/boeing-747sp/ （航程 6,650 nmi） | range_km_est 12298 km | 几乎一致（≈6,650 nmi）；维基列 5,830 nmi（10,800 km，276 人三舱载重） |
| 座级 | 331（两舱）/ 最大 400（单舱） | https://en.wikipedia.org/wiki/Boeing_747SP （230 三舱、331 两舱、最大 400） | passenger 320 人 | 接近两舱值 |
| 巡航 | 540 kt（约 1,000 km/h） | https://aerocorner.com/aircraft/boeing-747sp/ （cruise 540 kn） | speed_kmh 967 km/h | 维基列最大 Mach 0.92；典型巡航约 Mach 0.85（~905 km/h） |

注：aerocorner 概览页 "Seats 276" 为三舱典型载重，非最大布局。

---

### Boeing 757-300 (BOEING_757_300)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $75 million（2004） | https://simpleflying.com/tag/boeing-757/-300/ （List Price $75m 2004；另 aviationstrategy 1999 列 $73.5–81.0m） | (游戏 cost_factor=79) | 现实目录价仅参考 |
| 航程 | 3,395 nmi（约 6,288 km）最大 | https://en.wikipedia.org/wiki/Boeing_757 （757-300 最大航程 3,395 nmi / 6,288 km） | range_km_est 7002 km | 游戏偏高约 11% |
| 座级 | 243（两舱典型）/ 最大 295 | https://en.wikipedia.org/wiki/Boeing_757 （典型 243；最大认证 295） | passenger 243 人 | 完全一致 |
| 巡航 | Mach 0.80（约 858 km/h） | https://en.wikipedia.org/wiki/Boeing_757 （全系列巡航 Mach 0.8 / 858 km/h） | speed_kmh 934 km/h | 游戏偏高 |

---

### Boeing 777-8 (BOEING_777_8)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $394.9 million（2018） | https://247wallst.com/military/2018/01/19/boeing-raises-2018-commercial-jet-prices-by-4-1/ （2018 价目 777-8 $394.9m；simpleflying 列 $442.2m 2022） | (游戏 cost_factor=262) | 尚未交付；目录价仅参考 |
| 航程 | 9,500 nmi（约 17,590 km）最大 / 8,745 nmi 典型 | https://en.wikipedia.org/wiki/Boeing_777X （最大 9,500 nmi；典型 8,745 nmi） | range_km_est 16698 km | 接近最大航程 |
| 座级 | 350–425（两舱）/ 典型 395 | https://en.wikipedia.org/wiki/Boeing_777X （两舱 350–425；典型 395） | passenger 365 人 | 接近两舱下限 |
| 巡航 | Mach 0.84（约 905 km/h） | https://flightq.app/aircraft/boeing-777-8 （Mach 0.84 / 905 km/h）；https://simpleflying.com/tag/boeing-777/-x/ | speed_kmh 951 km/h | 接近 |

---

### Boeing 707-320 (Boeing_707_320)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $5.5 million（1960） | https://simpleflying.com/tag/boeing-707/-320/ （List Price $5.5m 1960） | (游戏 cost_factor=38) | 现实目录价仅参考 |
| 航程 | 3,750 nmi（约 6,940 km，141 人两舱载重） | https://en.wikipedia.org/wiki/Boeing_707 （对比表 3,750 nmi / 6,940 km） | range_km_est 11275 km | 游戏明显偏高（约 6,090 nmi） |
| 座级 | 约 189 典型 / 对比表列 194 / 最大 202 | https://en.wikipedia.org/wiki/Boeing_707 （载客 194）；https://simpleflying.com/tag/boeing-707/-320/ （最大 202） | passenger 189 人 | 一致 |
| 巡航 | 478–525 kn（约 885–972 km/h） | https://en.wikipedia.org/wiki/Boeing_707 （对比表巡航 478–525 kn） | speed_kmh 999 km/h | 游戏接近上限（约 540 kn） |

注：simpleflying 707-320 页列航程 3,915 nmi（7,250 km），与维基 3,750 nmi 略有出入；turbojet 型航程受载重影响大。

---

### Boeing 707-420 (Boeing_707_420)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $6.0 million（1960） | https://simpleflying.com/tag/boeing-707/-420/ （List Price $6.0m 1960） | (游戏 cost_factor=41) | 比 -320 略高（换装 Conway 涡扇） |
| 航程 | 4,830 nmi（约 8,950 km） | https://simpleflying.com/tag/boeing-707/-420/ （Range 4,830 nmi / 8,950 km） | range_km_est 12155 km | 游戏偏高；维基称与 -320 同 3,750 nmi |
| 座级 | 约 189 典型 / 对比表列 194 / 最大 202 | https://en.wikipedia.org/wiki/Boeing_707 （载客 194）；https://simpleflying.com/tag/boeing-707/-420/ （最大 202） | passenger 189 人 | 一致 |
| 巡航 | 478–525 kn（约 885–972 km/h；simpleflying 列 Mach 0.8 / 933 km/h） | https://en.wikipedia.org/wiki/Boeing_707 （对比表 478–525 kn）；https://simpleflying.com/tag/boeing-707/-420/ | speed_kmh 991 km/h | 游戏接近上限 |

---

### Boeing 717-200 (Boeing_717_200)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $33.08 million（1999） | https://www.flyradius.com/boeing-717/200-price （1999 目录价 $33.08m；aviationstrategy 1999 列 $31.5–35.5m） | (游戏 cost_factor=34) | 现实目录价仅参考 |
| 航程 | 2,060 nmi（约 3,820 km）设计航程 | https://en.wikipedia.org/wiki/Boeing_717 （设计航程 2,060 nmi；基本型 1,430 nmi） | range_km_est 4785 km | 游戏偏高约 25% |
| 座级 | 106（两舱）/ 117（单舱）/ 最大 134 | https://en.wikipedia.org/wiki/Boeing_717 （106 两舱 / 117 单舱 / 最大 134） | passenger 117 人 | 等于单舱值 |
| 巡航 | 504 mph（约 811 km/h，438 kn） | https://en.wikipedia.org/wiki/Boeing_717 （巡航 504 mph / 811 km/h） | speed_kmh 918 km/h | 游戏偏高 |

---

### Boeing 727-100 (Boeing_727_100)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 约 $4.25 million（1960 年代中期） | https://skyindustrynews.com/delta-retires-last-us-passenger-boeing-727-as-trijet-era-ends （727 初始目录价约 $4.25m 中期-60s） | (游戏 cost_factor=35) | 现实目录价仅参考 |
| 航程 | 2,250 nmi（约 4,170 km）两舱 | https://en.wikipedia.org/wiki/Boeing_727 （2,250 nmi / 4,170 km，两舱） | range_km_est 5225 km | 游戏偏高约 25% |
| 座级 | 106（两舱）/ 125（单舱） | https://en.wikipedia.org/wiki/Boeing_727 （106 两舱 / 125 单舱） | passenger 131 人 | 游戏略高于单舱最大值 |
| 巡航 | 600 mph（约 960 km/h）/ 495–518 kn（917–959 km/h） | https://en.wikipedia.org/wiki/Boeing_727 （巡航 600 mph；对比表 495–518 kn） | speed_kmh 999 km/h | 游戏接近上限 |

---

### Boeing 727-200 (Boeing_727_200)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $6.5 million（1967） | https://simpleflying.com/tag/boeing-727/-200/ （List Price $6.5m 1967） | (游戏 cost_factor=37) | 现实目录价仅参考（Advanced 型后期更高） |
| 航程 | 2,550 nmi（约 4,720 km）Advanced | https://en.wikipedia.org/wiki/Boeing_727 （-200 Advanced 2,550 nmi；基型 1,900 nmi） | range_km_est 6352 km | 游戏偏高约 35% |
| 座级 | 134（两舱）/ 155（单舱） | https://en.wikipedia.org/wiki/Boeing_727 （134 两舱 / 155 单舱） | passenger 147 人 | 介于两舱与单舱间 |
| 巡航 | 467–515 kn（约 865–954 km/h） | https://en.wikipedia.org/wiki/Boeing_727 （对比表 467–515 kn） | speed_kmh 999 km/h | 游戏接近上限（约 540 kn） |

---

### Boeing 727-200F (Boeing_727_200F)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠单独来源（货机 1981 年推出；参考 727-200 $6.5m 1967 同机体价，F 型应更高） | https://simpleflying.com/tag/boeing-727/-200/ （仅 727-200 价）；尝试维基/WebSearch 均无 727-200F 专属目录价 | (游戏 cost_factor=29) | 货机价无可靠公开来源 |
| 航程 | 2,550 nmi（约 4,720 km）Advanced | https://en.wikipedia.org/wiki/Boeing_727 （继承 -200 Advanced 航程） | range_km_est 4978 km | 接近 Advanced 航程 |
| 座级 | 0（货机，无客座） | https://en.wikipedia.org/wiki/Boeing_727 （windowless cabin 货机） | passenger 0 人 | 一致 |
| 巡航 | 467–515 kn（约 865–954 km/h） | https://en.wikipedia.org/wiki/Boeing_727 （同 727-200） | speed_kmh 905 km/h | 游戏接近上限 |

---

### Boeing 737-100 (Boeing_737_100)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $3.6 million（1968） | https://en.wikipedia.org/wiki/Boeing_737 （unit cost US$3,600,000 / 1968） | (游戏 cost_factor=29) | 现实目录价仅参考 |
| 航程 | 1,540 nmi（约 2,850 km） | https://en.wikipedia.org/wiki/Boeing_737 （对比表 1,540 nmi / 2,850 km） | range_km_est 4702 km | 游戏偏高约 65% |
| 座级 | 118 | https://en.wikipedia.org/wiki/Boeing_737 （对比表载客 118） | passenger 85 人 | 游戏偏低 |
| 巡航 | Mach 0.745（约 796 km/h） | https://simpleflying.com/how-fast-does-a-boeing-737-fly （Original/Classic 巡航 Mach 0.745 / 796 km/h） | speed_kmh 878 km/h | 游戏偏高 |

---

### Boeing 737-200 (Boeing_737_200)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $4.0 million（1968） | https://en.wikipedia.org/wiki/Boeing_737 （unit cost US$4.0M 1968；另 $5.2M 1972） | (游戏 cost_factor=29) | 现实目录价仅参考 |
| 航程 | 2,600 nmi（约 4,800 km） | https://en.wikipedia.org/wiki/Boeing_737 （对比表 2,600 nmi / 4,800 km） | range_km_est 5198 km | 接近 |
| 座级 | 130 | https://en.wikipedia.org/wiki/Boeing_737 （对比表载客 130） | passenger 97 人 | 游戏偏低 |
| 巡航 | Mach 0.745（约 796 km/h） | https://simpleflying.com/how-fast-does-a-boeing-737-fly （Original/Classic 巡航 Mach 0.745） | speed_kmh 878 km/h | 游戏偏高 |

---

### Boeing 737-200C (Boeing_737_200C)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到单独来源；与 737-200 同机体，参考 $4.0 million（1968） | https://en.wikipedia.org/wiki/Boeing_737 （737-200 价；Combi 无独立目录价） | (游戏 cost_factor=37) | 货客混装（Combi），无专门目录价 |
| 航程 | 约 2,600 nmi（约 4,800 km，同 737-200） | https://en.wikipedia.org/wiki/Boeing_737 （737-200 航程） | range_km_est 4648 km | 接近 |
| 座级 | 0（客货混装 Combi，客座可变；游戏记 0） | https://en.wikipedia.org/wiki/Boeing_737 （200C 为客货转换型） | passenger 0 人 | 一致（纯货配置） |
| 巡航 | Mach 0.745（约 796 km/h） | https://simpleflying.com/how-fast-does-a-boeing-737-fly （Original/Classic 巡航 Mach 0.745） | speed_kmh 878 km/h | 游戏偏高 |

---

### Boeing 737-300 (Boeing_737_300)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $32.0 million（1984） | https://simpleflying.com/tag/boeing-737/classic/ （737-300 List Price $32.0m 1984） | (游戏 cost_factor=29) | 现实目录价仅参考 |
| 航程 | 2,255 nmi（约 4,175 km） | https://simpleflying.com/tag/boeing-737/classic/ （737-300 Range 2,255 nmi / 4,175 km） | range_km_est 4152 km | 几乎一致 |
| 座级 | 149 | https://en.wikipedia.org/wiki/Boeing_737 （载客 149）；https://simpleflying.com/tag/boeing-737/classic/ | passenger 128 人 | 游戏偏低约 14% |
| 巡航 | Mach 0.78（约 828 km/h） | https://simpleflying.com/tag/boeing-737/classic/ （737-300 巡航 Mach 0.78 / 828 km/h；MMO 0.82） | speed_kmh 910 km/h | 游戏偏高 |

---

## 汇总：缺来源字段
- Boeing 727-200F 价格：无可靠单独来源（货机 1981 年推出，公开目录价缺失）。
- Boeing 737-200C 价格：无单独来源（Combi 客货混装，参考 737-200 $4.0m 1968）。
共 2 个字段缺可靠专属来源（其余 54 字段均有实际读取 URL）。

## 总体观察
- 航程：737-300、747SP、737 MAX 7、737-200、737-200C 与真实值高度吻合；但 707 系列、727 系列、737-100/200 及 717-200 游戏值普遍偏高 25–65%（老机型游戏里程被放大）。
- 座级：757-300（243）完全一致；多数老机型游戏座级偏低（如 737-100=85 vs 118、737-200=97 vs 130、737-300=128 vs 149）。
- 巡航：游戏 `speed_kmh` 普遍高于真实巡航（多取接近上限/Mmo 量级的数值）。
