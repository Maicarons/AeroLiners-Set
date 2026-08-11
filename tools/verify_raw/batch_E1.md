# 批次E1（Embraer 1/2）

> 主源 aerocorner；交叉源英文维基百科；E2 主源 aerocorner 对应 slug 均 404，改用英文维基百科为主源并以 airplaneupdate / aeroflap / airlineplanes 交叉。
> 换算：nm×1.852=km；kt×1.852=km/h；Mach×1062≈km/h。游戏 range_km_est = base_range×5.5。

---

### Embraer E175-E2 (EMBRAER_E175_E2)

| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$46.8 million（2013 目录价）；现行目录约 US$56.4M | https://en.wikipedia.org/wiki/Embraer_E-Jet_E2 （交叉：https://www.airplaneupdate.com/2019/02/embraer-e175-e2.html US$46.8M；https://www.aeroflap.com.br/en/saiba-quanto-custa-um-aviao-e-jet-da-embraer/ 现行 US$56.4M） | cost_factor=26 | 游戏系数 26，未对应真实目录价；真实 2013 目录 US$46.8M |
| 航程 | 3,700 km（2,000 nmi，满载；维基）；AR 型 3,735 km（2,017 nmi）；手册另列高速巡航 5,280 km（2,850 nmi） | https://en.wikipedia.org/wiki/Embraer_E-Jet_E2 （交叉：wikiwand 2,017 nmi/3,735 km） | range_km_est=3702 km | 几乎完全吻合（3702 vs 3700） |
| 座级 | 两舱 80 人（8J+72Y，wikiwand）/ 三舱 80（12J+12W+56Y）；最大 90（单舱） | https://en.wikipedia.org/wiki/Embraer_E-Jet_E2 （交叉：https://extension.wikiwand.com/zh/articles/ 两舱80/最大90） | passenger=88 | 88 介于两舱80与最大90之间，合理 |
| 巡航 | 833 km/h（Mach 0.78，@35,000 ft）；最大 Mach 0.82（876 km/h） | https://en.wikipedia.org/wiki/Embraer_E-Jet_E2 | speed_kmh=886 | 游戏 886 接近最大 876，高于典型巡航 833 |

---

### Embraer E190-E2 (EMBRAER_E190_E2)

| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$53.6 million（2013 目录价）；2018 报价约 US$60.8M；现行目录约 US$64.6M；airlineplanes 列价 US$59.1M | https://en.wikipedia.org/wiki/Embraer_E-Jet_E2 （交叉：https://aviatorinsider.com/airplane-brands/embraer-190/ US$60.8M 2018；https://www.aeroflap.com.br/en/saiba-quanto-custa-um-aviao-e-jet-da-embraer/ US$64.6M；https://airlineplanes.com/aircraft/embraer-e190-e2 US$59.1M） | cost_factor=65 | 游戏系数 65，接近真实目录量级 |
| 航程 | 5,460 km（2,950 nmi，满载）；手册高速巡航 5,280 km（2,850 nmi） | https://en.wikipedia.org/wiki/Embraer_E-Jet_E2 （交叉：airlineplanes 5,330 km） | range_km_est=5296 km | 接近（5296 vs 5460，差 ~3%） |
| 座级 | 三舱 97（9J+20W+68Y）；最大 114（单舱） | https://en.wikipedia.org/wiki/Embraer_E-Jet_E2 | passenger=97 | 97 正好等于三舱座级，吻合 |
| 巡航 | 833 km/h（Mach 0.78）；最大 876 km/h（Mach 0.82） | https://en.wikipedia.org/wiki/Embraer_E-Jet_E2 | speed_kmh=886 | 游戏 886 接近最大 876 |

---

### Embraer ERJ-135 (EMBRAER_ERJ135)

| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$16.5 million（年份未在页面标注）；维基无独立 ERJ-135 目录价（同族 1989–1996 年估计 US$11–15M） | https://aerocorner.com/aircraft/embraer-erj-135/ （交叉：https://en.wikipedia.org/wiki/Embraer_ERJ_family 无独立 135 价） | cost_factor=14 | 游戏系数 14，量级合理；真实价年份不明 |
| 航程 | 3,240 km（1,750 nmi，ERJ-135LR）；约 3,241 km | https://en.wikipedia.org/wiki/Embraer_ERJ_family （交叉：aerocorner 文 "near 1,750 nmi / 3,241 km"） | range_km_est=3250 km | 几乎吻合（3250 vs 3240） |
| 座级 | 37 人（最大） | https://aerocorner.com/aircraft/embraer-erj-135/ （交叉：维基 37） | passenger=37 | 完全吻合 |
| 巡航 | 831 km/h（Mach 0.78，最大巡航）；aerocorner 实时均值约 704 km/h（380 kt） | https://en.wikipedia.org/wiki/Embraer_ERJ_family （交叉：aerocorner 最大巡航 Mach 0.78） | speed_kmh=834 | 几乎吻合（834 vs 831） |

---

### Embraer ERJ-140 (EMBRAER_ERJ140)

| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$15.2 million（2000） | https://aerocorner.com/aircraft/embraer-erj-140/ （交叉：https://en.wikipedia.org/wiki/Embraer_ERJ_family "launch cost ≈ US$15.2M"） | cost_factor=14 | 两源一致 US$15.2M；游戏系数 14 合理 |
| 航程 | 3,060 km（1,650 nmi，ERJ-140LR） | https://en.wikipedia.org/wiki/Embraer_ERJ_family （交叉：aerocorner 同族） | range_km_est=3052 km | 几乎吻合（3052 vs 3060） |
| 座级 | 44 人（最大） | https://aerocorner.com/aircraft/embraer-erj-140/ （交叉：维基 44） | passenger=44 | 完全吻合 |
| 巡航 | 831 km/h（Mach 0.78，最大巡航） | https://en.wikipedia.org/wiki/Embraer_ERJ_family | speed_kmh=834 | 几乎吻合（834 vs 831） |

---

### Embraer 170 LR (Embraer_E170LR)

| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$41 million（2016） | https://aerocorner.com/aircraft/embraer-170/ （维基未列 E170 独立价） | cost_factor=25 | 游戏系数 25，量级合理 |
| 航程 | 基础 E170：3,982 km（2,150 nmi）；LR 为同型高 MTOW 远程型，航程更高（aerocorner 估约 3,889 km/2,100 nmi） | https://en.wikipedia.org/wiki/Embraer_E-Jet （交叉：aerocorner embraer-170 "near 2,100 nmi / 3,889 km"） | range_km_est=3850 km | 接近（3850 vs 3982 基础值） |
| 座级 | 两舱 66（6J+60Y）；最大 78 | https://en.wikipedia.org/wiki/Embraer_E-Jet （交叉：aerocorner 78） | passenger=78 | 78 = 最大座级，吻合 |
| 巡航 | 829 km/h（Mach 0.78）；最大 871 km/h（Mach 0.82）；aerocorner 称"接近 Mach 0.80" | https://en.wikipedia.org/wiki/Embraer_E-Jet （交叉：aerocorner embraer-170） | speed_kmh=886 | 游戏 886 接近最大 871，高于典型 829 |

---

### Embraer 170 STD (Embraer_E170STD)

| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$41 million（2016，无 STD 独立价，同 E170 系列） | https://aerocorner.com/aircraft/embraer-170/ | cost_factor=24 | 游戏系数 24，略低于 LR |
| 航程 | 基础 E170：3,982 km（2,150 nmi）；STD 即标准型，航程同基础值 | https://en.wikipedia.org/wiki/Embraer_E-Jet | range_km_est=3300 km | 游戏 3300 低于真实基础 3982（STD/LR 游戏差值 550 km，真实 STD 与 LR 差距很小） |
| 座级 | 两舱 66；最大 78 | https://en.wikipedia.org/wiki/Embraer_E-Jet | passenger=78 | = 最大座级 |
| 巡航 | 829 km/h（Mach 0.78）；最大 871 km/h | https://en.wikipedia.org/wiki/Embraer_E-Jet | speed_kmh=886 | 同 E170LR |

---

### Embraer 175 LR (Embraer_E175LR)

| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$45.7 million（2016）；维基记 2018 二手价约 US$27M（非目录） | https://aerocorner.com/aircraft/embraer-175/ （交叉：https://en.wikipedia.org/wiki/Embraer_E-Jet 2018 价值 US$27M） | cost_factor=27 | 游戏系数 27 接近真实目录量级 |
| 航程 | 基础 E175：4,074 km（2,200 nmi）；LR 为高 MTOW 远程型（更高）；airlineplanes 列 3,700 km | https://en.wikipedia.org/wiki/Embraer_E-Jet （交叉：https://airlineplanes.com/aircraft/embraer-e175 3,700 km） | range_km_est=3850 km | 接近（3850 vs 4074 基础值） |
| 座级 | 两舱 76（12J+64Y）；最大 88 | https://en.wikipedia.org/wiki/Embraer_E-Jet （交叉：aerocorner 86–88） | passenger=86 | 86 接近最大 88，合理 |
| 巡航 | 829 km/h（Mach 0.78）；最大 871 km/h | https://en.wikipedia.org/wiki/Embraer_E-Jet | speed_kmh=886 | 游戏 886 接近最大 871 |

---

### Embraer 175 STD (Embraer_E175STD)

| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | US$45.7 million（2016，无 STD 独立价） | https://aerocorner.com/aircraft/embraer-175/ | cost_factor=26 | 游戏系数 26 |
| 航程 | 基础 E175：4,074 km（2,200 nmi）；STD 即标准型 | https://en.wikipedia.org/wiki/Embraer_E-Jet | range_km_est=3300 km | 游戏 3300 明显低于真实 4074（STD/LR 差值游戏设 550 km，真实差距很小） |
| 座级 | 两舱 76；最大 88 | https://en.wikipedia.org/wiki/Embraer_E-Jet | passenger=86 | 接近最大 88 |
| 巡航 | 829 km/h（Mach 0.78）；最大 871 km/h | https://en.wikipedia.org/wiki/Embraer_E-Jet | speed_kmh=886 | 同 E175LR |

---

## 汇总备注

- **ERJ-135 / ERJ-140**：游戏四字段与真实值高度吻合（座级、航程、巡航几乎一致），仅价格系数无年份标注来源。
- **E175-E2 / E190-E2**：aerocorner 对应页面 404，主源改用英文维基；座级与航程吻合良好，游戏 speed_kmh(886) 取的是接近最大速度(Mach 0.82≈876) 而非典型巡航(833)。
- **E170 / E175（STD 与 LR）**：游戏对 STD/LR 的 range 差值(550 km)放大了真实差距——真实 STD 与 LR 航程差距很小（同基础机体、仅 MTOW 不同）；座级取最大布局合理；speed_kmh(886) 同样偏高。
- 价格字段：游戏 cost_factor 为相对系数，已在备注对照真实目录价（USD），非 1:1 换算。
