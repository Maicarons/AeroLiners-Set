# 批次S2（BAC / BAe / Britten-Norman / COMAC / Convair）

> 核对说明：aerocorner 主源对 BAC_1-11 / Concorde / BAe_146 / Britten-Norman / COMAC_ARJ21(C909) / COMAC_C929 / Convair_990 均返回 404（页面不存在），故这些机型以英文维基百科为实际读取来源并交叉核对；C919 与 Convair_880 的 aerocorner 页面存在（已读取，但其 USD 目录价为占位/错误值，价格仍采用维基）。价格若无公开 USD 目录价则标注「未找到可靠来源（无公开目录价）」。汇率换算仅为近似参考，括号内注明来源币种与年份。

### BAC 1-11 200 (BAC_1_11_200)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（无单独200系列目录价；500系列单位成本 US$5.2M, 1972） | https://en.wikipedia.org/wiki/BAC_One-Eleven | (游戏 cost_factor=24) | 200系列无单独公开目录价 |
| 航程 | 1,340 km（830 mi / 720 nmi，典型载荷+2h备用） | https://en.wikipedia.org/wiki/BAC_One-Eleven | range_km_est 1292 km | 接近（游戏略低） |
| 座级 | 89 人（单级最大；无两舱数据） | https://en.wikipedia.org/wiki/BAC_One-Eleven | passenger 75 人 | 游戏低于真实最大座级 |
| 巡航 | 882 km/h（476 kn，最大巡航） | https://en.wikipedia.org/wiki/BAC_One-Eleven | speed_kmh 878 km/h | 接近 |

### BAC 1-11 300 (BAC_1_11_300)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（300/400无单独目录价；500系列 US$5.2M, 1972） | https://en.wikipedia.org/wiki/BAC_One-Eleven | (游戏 cost_factor=24) | — |
| 航程 | 2,040 km（1,270 mi / 1,100 nmi，典型载荷） | https://en.wikipedia.org/wiki/BAC_One-Eleven | range_km_est 1292 km | 偏差大：游戏显著低估（200/300共用同一航程值） |
| 座级 | 89 人（单级最大） | https://en.wikipedia.org/wiki/BAC_One-Eleven | passenger 75 人 | 游戏低于真实最大 |
| 巡航 | 882 km/h（476 kn） | https://en.wikipedia.org/wiki/BAC_One-Eleven | speed_kmh 878 km/h | 接近 |

### BAC 1-11 400 (BAC_1_11_400)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（400系列无单独目录价；500系列 US$5.2M, 1972） | https://en.wikipedia.org/wiki/BAC_One-Eleven | (游戏 cost_factor=37) | 400=300的美式仪表型，价格相近 |
| 航程 | 2,040 km（1,100 nmi，典型载荷） | https://en.wikipedia.org/wiki/BAC_One-Eleven | range_km_est 3492 km | 偏差大：游戏高估（实为300/400与200不同，但与500航程也差距明显） |
| 座级 | 89 人（单级最大） | https://en.wikipedia.org/wiki/BAC_One-Eleven | passenger 89 人 | 一致 |
| 巡航 | 882 km/h（476 kn） | https://en.wikipedia.org/wiki/BAC_One-Eleven | speed_kmh 870 km/h | 接近 |

### BAC 1-11 500 (BAC_1_11_500)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$5.2M（1972，500系列单位成本） | https://en.wikipedia.org/wiki/BAC_One-Eleven | (游戏 cost_factor=37) | 真实USD目录价参考 |
| 航程 | 2,744 km（1,705 mi / 1,482 nmi，典型载荷） | https://en.wikipedia.org/wiki/BAC_One-Eleven | range_km_est 3492 km | 偏差：游戏高估约750 km |
| 座级 | 119 人（单级最大） | https://en.wikipedia.org/wiki/BAC_One-Eleven | passenger 115 人 | 接近（游戏略低） |
| 巡航 | 871 km/h（470 kn） | https://en.wikipedia.org/wiki/BAC_One-Eleven | speed_kmh 870 km/h | 一致 |

### BAC Concorde (BAC_CONCORDE)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$46M（1977，£23M） | https://aerospaceweb.org/aircraft/jetliner/concorde ; https://en.wikipedia.org/wiki/Concorde | (游戏 cost_factor=160) | 真实USD目录价参考 |
| 航程 | 6,580 km（3,560 nmi，最大燃油）；另有来源列最大航程 7,250 km | https://aerospaceweb.org/aircraft/jetliner/concorde ; https://en.wikipedia.org/wiki/Concorde | range_km_est 6765 km | 接近（取6,580~7,250区间） |
| 座级 | 100–128 人（典型），最大 144 | https://aerospaceweb.org/aircraft/jetliner/concorde ; https://en.wikipedia.org/wiki/Concorde | passenger 100 人 | 游戏取典型下限，一致 |
| 巡航 | 2,154 km/h（Mach 2.02；约 Mach×1062） | https://en.wikipedia.org/wiki/Concorde | speed_kmh 2337 km/h | 偏差：游戏约按 Mach 2.2（2,337 km/h）折算，高于常规巡航 Mach 2.02 |

### BAe 146-100 (BAe_146_100)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（无-100单独USD目录价；-200为£11M, 1981） | https://en.wikipedia.org/wiki/British_Aerospace_146 | (游戏 cost_factor=20) | — |
| 航程 | 3,870 km（82 pax） | https://en.wikipedia.org/wiki/British_Aerospace_146 | range_km_est 3052 km | 偏差：游戏低估约820 km |
| 座级 | 70–82 人（典型），最大约 82–94 | https://en.wikipedia.org/wiki/British_Aerospace_146 | passenger 92 人 | 游戏取高密/上限，偏高 |
| 巡航 | 789 km/h（426 kn，最大巡航；标准747 km/h） | https://en.wikipedia.org/wiki/British_Aerospace_146 | speed_kmh 781 km/h | 接近 |

### BAe 146-200 (BAe_146_200)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | £11M（1981，约 US$20M 1981汇率）= -200单位成本 | https://en.wikipedia.org/wiki/British_Aerospace_146 | (游戏 cost_factor=22) | 来源币种为英镑，USD为近似 |
| 航程 | 3,650 km（100 pax） | https://en.wikipedia.org/wiki/British_Aerospace_146 | range_km_est 2888 km | 偏差：游戏低估约760 km |
| 座级 | 85–100 人（典型），最大 112 | https://en.wikipedia.org/wiki/British_Aerospace_146 | passenger 112 人 | 一致（取最大） |
| 巡航 | 789 km/h（426 kn） | https://en.wikipedia.org/wiki/British_Aerospace_146 | speed_kmh 781 km/h | 接近 |

### BAe 146-300 (BAe_146_300)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（无-300单独USD目录价） | https://en.wikipedia.org/wiki/British_Aerospace_146 | (游戏 cost_factor=24) | — |
| 航程 | 3,340 km（100 pax） | https://en.wikipedia.org/wiki/British_Aerospace_146 | range_km_est 2722 km | 偏差：游戏低估约620 km |
| 座级 | 97–112 人（典型）；高密 RJ115 提案达 128（未投产） | https://en.wikipedia.org/wiki/British_Aerospace_146 | passenger 128 人 | 游戏取高密提案上限，偏高 |
| 巡航 | 789 km/h（426 kn） | https://en.wikipedia.org/wiki/British_Aerospace_146 | speed_kmh 781 km/h | 接近 |

### BAe 146-300QT (BAe_146_300QT)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（货机无客舱目录价） | https://en.wikipedia.org/wiki/British_Aerospace_146 | (游戏 cost_factor=24) | 货机（Quiet Trader），0客座 |
| 航程 | 约 3,340 km（货机，与-300同机体） | https://en.wikipedia.org/wiki/British_Aerospace_146 | range_km_est 2722 km | 同-300，游戏低估 |
| 座级 | 0 人（货机） | https://en.wikipedia.org/wiki/British_Aerospace_146 | passenger 0 人 | 一致 |
| 巡航 | 789 km/h（426 kn） | https://en.wikipedia.org/wiki/British_Aerospace_146 | speed_kmh 781 km/h | 接近 |

### Britten-Norman BN-2B Islander (BRITTEN_NORMAN_BN2B)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（无公开USD目录价） | https://en.wikipedia.org/wiki/Britten-Norman_Islander | (游戏 cost_factor=14) | — |
| 航程 | 1,398 km（869 mi / 755 nmi，标准燃油，130 kn） | https://en.wikipedia.org/wiki/Britten-Norman_Islander | range_km_est 1072 km | 偏差：游戏低估约330 km |
| 座级 | 9 人（最大，1机组+9客） | https://en.wikipedia.org/wiki/Britten-Norman_Islander | passenger 9 人 | 一致 |
| 巡航 | 240 km/h（150 mph / 130 kn，59%功率） | https://en.wikipedia.org/wiki/Britten-Norman_Islander | speed_kmh 257 km/h | 接近（游戏略高） |

### Britten-Norman BN-2T Turbine Islander (BRITTEN_NORMAN_BN2T)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（无公开USD目录价） | https://en.wikipedia.org/wiki/Britten-Norman_Islander | (游戏 cost_factor=14) | — |
| 航程 | 未找到可靠来源（维基未单列BN-2T航程；涡桨型通常略长于BN-2B） | https://en.wikipedia.org/wiki/Britten-Norman_Islander | range_km_est 1342 km | 真实BN-2T专项航程未列 |
| 座级 | 最多 9 人 | https://en.wikipedia.org/wiki/Britten-Norman_Islander | passenger 9 人 | 一致 |
| 巡航 | 未找到可靠来源（维基未单列BN-2T巡航；涡桨型估约260–300 km/h） | https://en.wikipedia.org/wiki/Britten-Norman_Islander | speed_kmh 326 km/h | BN-2T专项巡航未列，游戏取涡桨较高值 |

### COMAC C909 (ARJ21) (COMAC_C909)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（无公开USD目录价） | https://en.wikipedia.org/wiki/Comac_ARJ21 | (游戏 cost_factor=65) | 2024年11月由ARJ21更名C909 |
| 航程 | STD 2,200 km（1,200 nmi）/ ER 3,700 km（2,000 nmi），满载 | https://en.wikipedia.org/wiki/Comac_ARJ21 | range_km_est 3702 km | 一致（取ER 3,700 km） |
| 座级 | 78 人（两舱）/ 90 人（单级最大） | https://en.wikipedia.org/wiki/Comac_ARJ21 | passenger 90 人 | 一致（取单级最大） |
| 巡航 | 828 km/h（Mach 0.78）；最大Mach 0.82=870 km/h | https://en.wikipedia.org/wiki/Comac_ARJ21 | speed_kmh 886 km/h | 偏差：游戏接近最大巡航870，高于常规828 |

### COMAC C919 (COMAC_C919)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$101M（2022年5月，653百万元人民币） | https://en.wikipedia.org/wiki/Comac_C919 | (游戏 cost_factor=73) | 真实USD目录价；aerocorner列"$1M(2012)"为占位错误值，未采用 |
| 航程 | STD 4,075 km / ER 5,555 km（2,999 nmi） | https://en.wikipedia.org/wiki/Comac_C919 | range_km_est 5610 km | 接近（取ER 5,555 km） |
| 座级 | 158 人（两舱 8J+150Y）/ 最大 192 | https://en.wikipedia.org/wiki/Comac_C919 | passenger 158 人 | 一致（取两舱） |
| 巡航 | 835 km/h（Mach 0.785） | https://en.wikipedia.org/wiki/Comac_C919 | speed_kmh 902 km/h | 偏差：游戏约高67 km/h |

### COMAC C929 (COMAC_C929)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（研发中，无最终目录价） | https://en.wikipedia.org/wiki/Comac_C929 | (游戏 cost_factor=220) | 中俄联合(CR929)后由中国独立研制，仍在详细设计阶段 |
| 航程 | 约 12,000 km（C929-600，2024年目标） | https://en.wikipedia.org/wiki/Comac_C929 | range_km_est 12001 km | 一致（取-600目标值） |
| 座级 | 280 人（三舱，-600）；目标 280–400 | https://en.wikipedia.org/wiki/Comac_C929 | passenger 280 人 | 一致（取-600三舱） |
| 巡航 | 约 908 km/h（Mach 0.85） | https://en.wikipedia.org/wiki/Comac_C929 | speed_kmh 945 km/h | 偏差：游戏略高约37 km/h；规格未冻结 |

### Convair 880 (CONVAIR_880)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（无公开USD目录价；通用动力项目亏损，无单机价） | https://en.wikipedia.org/wiki/Convair_880 ; https://aerocorner.com/aircraft/convair-880/ | (游戏 cost_factor=35) | — |
| 航程 | 4,578 km（2,472 nmi，22型）/ 4,636 km（22M） | https://en.wikipedia.org/wiki/Convair_880 ; https://aerocorner.com/aircraft/convair-880/ | range_km_est 5599 km | 偏差：游戏高估约1,000 km |
| 座级 | 110 人（最大） | https://en.wikipedia.org/wiki/Convair_880 ; https://aerocorner.com/aircraft/convair-880/ | passenger 100 人 | 游戏略低 |
| 巡航 | 990 km/h（534.5 kn，最大巡航）；经济巡航 Mach 0.82 | https://en.wikipedia.org/wiki/Convair_880 ; https://aerocorner.com/aircraft/convair-880/ | speed_kmh 910 km/h | 偏差：游戏取经济巡航附近，低于最大990 |

### Convair 990 (CONVAIR_990)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 未找到可靠来源（无公开USD目录价） | https://en.wikipedia.org/wiki/Convair_990 | (游戏 cost_factor=39) | — |
| 航程 | 6,115 km（3,302 nmi，990A） | https://en.wikipedia.org/wiki/Convair_990 | range_km_est 6116 km | 一致（几乎完全相同） |
| 座级 | 最多 149 人（990A） | https://en.wikipedia.org/wiki/Convair_990 | passenger 120 人 | 偏差：游戏低于真实最大 |
| 巡航 | 896 km/h（484 kn，Mach 0.84） | https://en.wikipedia.org/wiki/Convair_990 | speed_kmh 896 km/h | 一致 |

---
### 备注汇总
- aerocorner 主源 404 机型（无页面）：BAC_1_11_200/300/400/500、BAC_CONCORDE、BAe_146_100/200/300/300QT、BRITTEN_NORMAN_BN2B/BN2T、COMAC_C909、COMAC_C929、CONVAIR_990。以上实际读取来源为英文维基百科（及 Concorde 交叉 aerospaceweb）。
- aerocorner 可用机型：COMAC_C919、CONVAIR_880（但其 USD 价格字段为占位/错误，价格仍采维基）。
- 价格普遍缺失：多数老旧/在研机型无公开 USD 目录价，已如实标注「未找到可靠来源」。
- 大偏差提示：BAC_1_11_300/400 航程游戏值明显偏离真实（200/300/400 共用同一低估/高估值）；Convair_880 航程游戏高估约1,000 km；BAe 146 全系航程游戏偏低约600–820 km；Concorde 巡航游戏按 Mach 2.2 而非常规 Mach 2.02。
