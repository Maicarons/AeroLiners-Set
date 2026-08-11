# 批次E2（Embraer 2/2）

> 数据核对日期：2026-08-10
> 主源 aerocorner，交叉源 英文维基百科、Embraer 官方。
> 单位换算：nm×1.852=km；kt×1.852=km/h；Mach×1062≈km/h。
> 注：E190/E195 的 STD/LR/AR 为同机身子型号（STD 基准、LR 长程、AR 超程，AR 航程最长）。

---

### Embraer 190 STD (<id>Embraer_E190STD</id>)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $51 million（目录参考价，aerocorner 未注年份） | https://aerocorner.com/aircraft/embraer-190/ | (游戏 cost_factor=65) | cost_factor 为相对系数；真实目录价约 $51M 作参考 |
| 航程 | ~2,400 nmi（约 4,448 km，E190 基准型）；子型号 STD<LR<AR | https://www.embraer.com/e-jets/e190/en/ + https://en.wikipedia.org/wiki/Embraer_E-Jet | range_km_est 3300 km | 游戏 STD 3300 km 偏低于基准 4,448 km；子型号排序 STD<LR<AR 正确 |
| 座级 | 100 人（单级@32"）/ 96 人（双级 8J+88Y）/ 最大 114 人 | https://www.embraer.com/e-jets/e190/en/ | passenger 106 人 | 游戏 106 介于单级典型与最大之间，合理 |
| 巡航 | Mach 0.78（829 km/h，典型）；最大 0.82 Mach（约 871 km/h） | https://en.wikipedia.org/wiki/Embraer_E-Jet + https://www.embraer.com/e-jets/e190/en/ | speed_kmh 886 km/h | 游戏 886 km/h 略高于最大巡航 871 km/h，基本合理 |

### Embraer 190 LR (<id>Embraer_E190LR</id>)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $51 million（目录参考价） | https://aerocorner.com/aircraft/embraer-190/ | (游戏 cost_factor=60) | 同机身型号，真实目录价一致；cost_factor 为相对系数 |
| 航程 | LR 长程型，高于 STD；E190 家族基准 2,450 nmi（4,537 km），AR 较 LR 增 50 nmi（93 km） | https://en.wikipedia.org/wiki/Embraer_E-Jet | range_km_est 4208 km | 游戏 LR 4208 km，接近基准上限，排序正确 |
| 座级 | 100 人（单级@32"）/ 最大 114 人 | https://www.embraer.com/e-jets/e190/en/ | passenger 106 人 | 合理 |
| 巡航 | Mach 0.78（829 km/h，典型）；最大 0.82 Mach（约 871 km/h） | https://en.wikipedia.org/wiki/Embraer_E-Jet | speed_kmh 886 km/h | 略高于最大巡航 |

### Embraer 190 AR (<id>Embraer_E190AR</id>)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $51 million（目录参考价） | https://aerocorner.com/aircraft/embraer-190/ | (游戏 cost_factor=59) | 同机身型号；cost_factor 为相对系数 |
| 航程 | AR 超程型（最长），较 LR 增 50 nmi（93 km）；基准型 2,450 nmi（4,537 km） | https://en.wikipedia.org/wiki/Embraer_E-Jet + https://www.embraer.com/e-jets/e190/en/ | range_km_est 4400 km | 游戏 AR 4400 km，与基准 4,537 km 很接近；为家族最长，排序正确 |
| 座级 | 100 人（单级@32"）/ 最大 114 人 | https://www.embraer.com/e-jets/e190/en/ | passenger 106 人 | 合理 |
| 巡航 | Mach 0.78（829 km/h，典型）；最大 0.82 Mach（约 871 km/h） | https://en.wikipedia.org/wiki/Embraer_E-Jet | speed_kmh 886 km/h | 略高于最大巡航 |

### Embraer 195 STD (<id>Embraer_E195STD</id>)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $53.5 million（2019，目录参考价） | https://aerocorner.com/aircraft/embraer-195/ | (游戏 cost_factor=37) | cost_factor 为相对系数；真实目录价约 $53.5M |
| 航程 | 2,594 km（STD 标准型，aerocorner Performance） | https://aerocorner.com/aircraft/embraer-195/ | range_km_est 2558 km | 游戏 2558 km 与真实 STD 2,594 km 几乎一致 ✔ |
| 座级 | 100 人（双级 12J+88Y）/ 最大 124 人 | https://en.wikipedia.org/wiki/Embraer_E-Jet + https://aerocorner.com/aircraft/embraer-195/ | passenger 118 人 | 游戏 118 介于双级与最大之间，合理 |
| 巡航 | Mach 0.78（829 km/h） | https://en.wikipedia.org/wiki/Embraer_E-Jet | speed_kmh 886 km/h | 游戏 886 略高于典型巡航 829 km/h |

### Embraer 195 LR (<id>Embraer_E195LR</id>)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $53.5 million（2019，目录参考价） | https://aerocorner.com/aircraft/embraer-195/ | (游戏 cost_factor=37) | 同机身；cost_factor 为相对系数 |
| 航程 | 3,334 km（LR 长程型） | https://aerocorner.com/aircraft/embraer-195/ | range_km_est 3300 km | 游戏 3300 km 与真实 LR 3,334 km 几乎一致 ✔ |
| 座级 | 100 人（双级 12J+88Y）/ 最大 124 人 | https://en.wikipedia.org/wiki/Embraer_E-Jet | passenger 118 人 | 合理 |
| 巡航 | Mach 0.78（829 km/h） | https://en.wikipedia.org/wiki/Embraer_E-Jet | speed_kmh 886 km/h | 略高于典型巡航 |

### Embraer 195 AR (<id>Embraer_E195AR</id>)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $53.5 million（2019，目录参考价） | https://aerocorner.com/aircraft/embraer-195/ | (游戏 cost_factor=37) | 同机身；cost_factor 为相对系数 |
| 航程 | 4,077 km（AR 超程型，最长） | https://aerocorner.com/aircraft/embraer-195/ | range_km_est 4042 km | 游戏 4042 km 与真实 AR 4,077 km 几乎一致 ✔ |
| 座级 | 100 人（双级 12J+88Y）/ 最大 124 人 | https://en.wikipedia.org/wiki/Embraer_E-Jet | passenger 118 人 | 合理 |
| 巡航 | Mach 0.78（829 km/h） | https://en.wikipedia.org/wiki/Embraer_E-Jet | speed_kmh 886 km/h | 略高于典型巡航 |

### Embraer E195-E2 (<id>Embraer_E195_E2</id>)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $60.4 million（2013 单位成本） | https://en.wikipedia.org/wiki/Embraer_E-Jet_E2 | (游戏 cost_factor=44) | cost_factor 为相对系数；aerocorner 对应页面 404 未找到，改用维基 |
| 航程 | 3,000 nmi（5,600 km，brochure 满客航程，2024 升级后） | https://en.wikipedia.org/wiki/Embraer_E-Jet_E2 | range_km_est 4802 km | 游戏 4802 km 低于真实 5,600 km，偏差约 -14% |
| 座级 | 120 人（三级 12J+24W+84Y）/ 最大 146 人 | https://en.wikipedia.org/wiki/Embraer_E-Jet_E2 | passenger 132 人 | 游戏 132 介于三级与最大之间，合理 |
| 巡航 | Mach 0.78（833 km/h，@35,000 ft）；最大 0.82 Mach（876 km/h） | https://en.wikipedia.org/wiki/Embraer_E-Jet_E2 | speed_kmh 890 km/h | 游戏 890 高于最大巡航 876 km/h，略偏高 |

### Embraer 145 (ERJ-145) (<id>Embraer_ERJ145</id>)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $21 million（aerocorner 当前参考）；历史 ~$14.5M（1995）/$15M（1996） | https://aerocorner.com/aircraft/embraer-erj-145/ + https://en.wikipedia.org/wiki/Embraer_ERJ_family | (游戏 cost_factor=14) | 游戏 intro_year=1994，历史价约 $14.5–15M 更贴合；cost_factor 为相对系数 |
| 航程 | 2,000 nmi（3,700 km，家族上限；145XR 同值） | https://aerocorner.com/aircraft/embraer-erj-145/ + https://en.wikipedia.org/wiki/Embraer_ERJ_family | range_km_est 2832 km | 游戏 2832 km 低于真实 3,700 km，偏差约 -23% |
| 座级 | 50 人（典型）/ 最大 60 人 | https://aerocorner.com/aircraft/embraer-erj-145/ + https://en.wikipedia.org/wiki/Embraer_ERJ_family | passenger 50 人 | 与真实典型座级完全一致 ✔ |
| 巡航 | Mach 0.78（829 km/h，基准）；最大 0.80 Mach（852 km/h，XR） | https://en.wikipedia.org/wiki/Embraer_ERJ_family + https://aerocorner.com/aircraft/embraer-erj-145/ | speed_kmh 829 km/h | 游戏 829 km/h 与真实典型巡航 829 km/h 完全一致 ✔ |

---

## 来源清单（实际读取）
- https://aerocorner.com/aircraft/embraer-190/ （E190 价格/座级/巡航；Performance 子型号区间未列出）
- https://aerocorner.com/aircraft/embraer-195/ （E195 价格$53.5M2019、座级、STD/LR/AR 航程 2594/3334/4077 km）
- https://aerocorner.com/aircraft/embraer-erj-145/ （ERJ-145 价格$21M、座级50、航程3704km、最大速度833km/h）
- https://www.embraer.com/e-jets/e190/en/ （E190 官方：0.82 Mach、114座、2,450nm/4537km、典型96双级/100单级）
- https://en.wikipedia.org/wiki/Embraer_E-Jet （E190/E195 巡航 Mach0.78=829km/h、双级/最大座级、子型号 AR 增程说明）
- https://en.wikipedia.org/wiki/Embraer_E-Jet_E2 （E195-E2：$60.4M2013、满客航程5600km、120三级/146最大、巡航833km/h）
- https://en.wikipedia.org/wiki/Embraer_ERJ_family （ERJ-145：50/60座、3700km、Mach0.78/0.80、历史价$14.5–15M）
- 未找到可靠来源（404）：aerocorner 的 embraer-e190 / embraer-e195-e2 / embraer-195-e2 页面（E2 改用维基百科 E-Jet E2 页）

## 小结
- E195 三个子型号（STD/LR/AR）游戏航程与真实值几乎一致（误差<2%）。✔
- ERJ-145 座级(50)与巡航(829km/h)与真实完全一致；航程偏低约 23%。
- E190 子型号排序正确，游戏航程略低于官方基准(4537km)。
- E195-E2 航程(4802km)低于真实满客航程(5600km)约14%；巡航(890)略高于最大巡航(876)。
- 巡航速度整体游戏值偏高 3–7%（更接近最大巡航/马赫上限）。
