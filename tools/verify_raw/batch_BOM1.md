# 批次BOM1（Bombardier CRJ 系列）

> 说明：游戏内 `cost_factor` 为相对价格系数（游戏不存美元价）。下表「价格」填现实目录价 USD 作参考，并注明年份；偏差栏注明游戏用相对系数。
> 单位换算：nm×1.852=km；kt×1.852=km/h；巡航 Mach≈Mach×1062 km/h。
> 来源主用 aerocorner（slug 用连字符，如 bombardier-crj-1000），交叉用英文维基与 Jane's（airplanes24 镜像）。每字段均标实际读取 URL。
> ER=延程(Extended Range)、LR=长程(Long Range)、EL=EuroLite（减重型，欧洲噪声/重量限制，航程反而更短）。

---

### Bombardier CRJ1000 (Bombardier_CRJ1000)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $24.8 million（2018 折让价；名录约 $25m） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （2018 折让 $24.8M）；https://aerocorner.com/aircraft/bombardier-crj-1000/ （$25M 2018） | (游戏 cost_factor=44) | 现实目录价仅参考 |
| 航程 | 典型 2,698 km（1,457 nmi）；最大约 3,056 km（1,650 nmi） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （base 1,457 nmi / 2,698 km）；https://aerocorner.com/aircraft/bombardier-crj-1000/ （3,004 km 典型）；https://pdf.aeroexpo.online/pdf/bombardier/crj1000/169445-15819.html （max 1,650 nmi / 3,056 km） | range_km_est 2612 km | 接近典型航程；与最大差约 15% |
| 座级 | 最大 104（单舱）/ 两舱约 97–100 | https://aerocorner.com/aircraft/bombardier-crj-1000/ （104 economy · 100 business）；https://pdf.aeroexpo.online/pdf/bombardier/crj1000/169445-15819.html （双舱 97 / 单舱 100 / 最大 104） | passenger 100 人 | 与两舱典型值一致 |
| 巡航 | 829 km/h（Mach 0.78 正常）；最大 871 km/h（Mach 0.82） | https://aerocorner.com/aircraft/bombardier-crj-1000/ （cruise 829 km/h）；https://pdf.aeroexpo.online/pdf/bombardier/crj1000/169445-15819.html （max 0.82M / 871 km/h） | speed_kmh 850 km/h | 略高于正常巡航，接近最大巡航 |

---

### Bombardier CRJ1000EL (Bombardier_CRJ1000EL)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 同 CRJ1000，约 $24.8M（2018 折让） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （CRJ1000 折让价；EL 无单独报价） | (游戏 cost_factor=45) | 现实目录价仅参考；EL 为减重型 |
| 航程 | 1,910 km（1,030 nmi）EuroLite，减重 MTOW 80,969 lb | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （CRJ1000EL 1,030 nmi / 1,910 km） | range_km_est 1788 km | 接近（EL 航程最短，比 base 短约 30%） |
| 座级 | 最大 104（单舱） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （CRJ1000EL 104） | passenger 100 人 | 座级同基础型 |
| 巡航 | 829 km/h（同基础型，EL 不改速度） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （未列 EL 单独速度） | speed_kmh 850 km/h | 沿用 CRJ1000 巡航 |

注：CRJ1000EL = EuroLite，为符合欧洲机场减重/噪声限制而降 MTOW，航程反而比标准型更短（约 1,910 km vs 2,698 km）。游戏 EL 航程(1788)明显短于 base(2612)，方向正确。

---

### Bombardier CRJ-100ER (Bombardier_CRJ100ER)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $18.3M（1994 单机成本）；上限约 $39.7M（2006） | https://a.osmarks.net/content/wikipedia_en_all_maxi_2020-08/A/CRJ100 （Unit cost US$18.3M 1994）；https://www.airports-worldwide.com/articles/article0892.php （US$24–39.7m as of 2006） | (游戏 cost_factor=22) | 现实目录价仅参考 |
| 航程 | 约 3,000 km（1,620 nmi）ER | https://www.airplanes24.net/airplanes/10-bombardier-crj200 （CRJ100 ER: 3,000 km / 1,620 nmi，源 Jane's 2006） | range_km_est 2970 km | 几乎一致（维基规格表另列 ER 2,417 km，见下方备注） |
| 座级 | 50 典型 / 最大 52 | https://en.wikipedia.org/wiki/Bombardier_CRJ100 （典型 50，最大 52） | passenger 50 人 | 完全一致 |
| 巡航 | 786 km/h（Mach 0.74 正常）；最大 860 km/h（Mach 0.81） | https://en.wikipedia.org/wiki/Bombardier_CRJ100 （Mach .74 / 786 km/h 正常；Mach .81 / 860 km/h 高速） | speed_kmh 814 km/h | 介于正常与高速巡航之间 |

注：维基规格表 CRJ100 行将 ER/LR 列标为 2,417 km / 3,056 km（即 1,305 / 1,650 nmi），与 Jane's(airplanes24) 的 ER 3,000 km / LR 3,710 km 不一致；游戏 ER/LR 值(2970 / 3685) 与 Jane's 吻合，故采用 Jane's 作为 ER/LR 航程依据。

---

### Bombardier CRJ-100LR (Bombardier_CRJ100LR)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 同 CRJ100 家族，约 $18.3M（1994） | https://a.osmarks.net/content/wikipedia_en_all_maxi_2020-08/A/CRJ100 （家族单机成本） | (游戏 cost_factor=25) | 现实目录价仅参考 |
| 航程 | 约 3,710 km（2,003 nmi）LR | https://www.airplanes24.net/airplanes/10-bombardier-crj200 （CRJ100 LR: 3,710 km / 2,003 nmi，源 Jane's 2006） | range_km_est 3685 km | 几乎一致 |
| 座级 | 50 典型 / 最大 52 | https://en.wikipedia.org/wiki/Bombardier_CRJ100 （50 典型，最大 52） | passenger 50 人 | 完全一致 |
| 巡航 | 786 km/h（Mach 0.74）；最大 860 km/h（Mach 0.81） | https://en.wikipedia.org/wiki/Bombardier_CRJ100 | speed_kmh 814 km/h | 介于正常与高速巡航之间 |

---

### Bombardier CRJ-200ER (Bombardier_CRJ200ER)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 约 $24.4M（新机名录均值） / 区间 $18–40M | https://www.sunairlines.net/bombardier-crj200/price （list ~$24.375M）；https://www.airports-worldwide.com/articles/article0892.php （US$24–39.7m 2006） | (游戏 cost_factor=26) | 现实目录价仅参考 |
| 航程 | 约 3,045 km（1,644 nmi）ER | https://www.airplanes24.net/airplanes/10-bombardier-crj200 （CRJ200 ER: 3,045 km / 1,644 nmi，源 Jane's 2006） | range_km_est 3025 km | 几乎一致 |
| 座级 | 50 典型 / 最大 52 | https://en.wikipedia.org/wiki/Bombardier_CRJ100 （CRJ200 同 50） | passenger 50 人 | 完全一致 |
| 巡航 | 786 km/h（Mach 0.74）；最大 860 km/h（Mach 0.81） | https://en.wikipedia.org/wiki/Bombardier_CRJ100 （CRJ200 同 CRJ100 速度） | speed_kmh 814 km/h | 介于正常与高速巡航之间 |

---

### Bombardier CRJ-200LR (Bombardier_CRJ200LR)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 约 $24.4M（新机名录均值） / 区间 $18–40M | https://www.sunairlines.net/bombardier-crj200/price ；https://www.airports-worldwide.com/articles/article0892.php | (游戏 cost_factor=28) | 现实目录价仅参考 |
| 航程 | 约 3,713 km（2,004 nmi）LR | https://www.airplanes24.net/airplanes/10-bombardier-crj200 （CRJ200 LR: 3,713 km / 2,004 nmi，源 Jane's 2006） | range_km_est 3685 km | 几乎一致 |
| 座级 | 50 典型 / 最大 52 | https://en.wikipedia.org/wiki/Bombardier_CRJ100 | passenger 50 人 | 完全一致 |
| 巡航 | 786 km/h（Mach 0.74）；最大 860 km/h（Mach 0.81） | https://en.wikipedia.org/wiki/Bombardier_CRJ100 | speed_kmh 814 km/h | 介于正常与高速巡航之间 |

---

### Bombardier CRJ-700 (Bombardier_CRJ700)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $24–25 million（1999 名录） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （listed at $24–25 million 1999）；https://aerocorner.com/aircraft/bombardier-crj-700/ （$24.4M） | (游戏 cost_factor=22) | 现实目录价仅参考 |
| 航程 | 3,152 km（1,702 nmi）base（68 座） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （CRJ700 1,702 nmi / 3,152 km） | range_km_est 2228 km | 游戏偏低约 29% |
| 座级 | 最大 78（702 型）/ 典型 70（701 型） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （68/70/78 因型号而异） | passenger 70 人 | 与典型 70 座一致 |
| 巡航 | 876 km/h（Mach 0.825 最大）；正常巡航约 829 km/h | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （对比表 Mach .825 = 876 km/h） | speed_kmh 830 km/h | 接近正常巡航 |

---

### Bombardier CRJ-700ER (Bombardier_CRJ700ER)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 同 CRJ700 家族，约 $24–25M（1999） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 | (游戏 cost_factor=24) | 现实目录价仅参考 |
| 航程 | 3,763 km（2,032 nmi）ER（68 座） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （CRJ700ER 2,032 nmi / 3,763 km） | range_km_est 2750 km | 游戏偏低约 27% |
| 座级 | 最大 68–78 | https://en.wikipedia.org/wiki/Bombardier_CRJ700 | passenger 70 人 | 与典型 70 座一致 |
| 巡航 | 876 km/h（Mach 0.825 最大） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 | speed_kmh 830 km/h | 接近正常巡航 |

---

### Bombardier CRJ-900 (Bombardier_CRJ900)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | $28–29M（1999 初始）/ 名录 $48M（2018，市场约 $24M） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （1999 $28–29M；2018 list $48M）；https://aerocorner.com/aircraft/bombardier-crj-900/ （$46.5M） | (游戏 cost_factor=27) | 现实目录价仅参考 |
| 航程 | 2,500 km（1,350 nmi）base（MTOW 80,500 lb） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （CRJ900 1,350 nmi / 2,500 km） | range_km_est 1925 km | 游戏偏低约 23% |
| 座级 | 最大 90 | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （CRJ900 up to 90） | passenger 88 人 | 接近最大座级 |
| 巡航 | 829 km/h（巡航）/ 871 km/h（Mach 0.82 最大） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （cruise 829 km/h, Mach 0.82 / 871 km/h） | speed_kmh 846 km/h | 介于巡航与最大之间 |

---

### Bombardier CRJ-900ER (Bombardier_CRJ900ER)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 同 CRJ900 家族，约 $28–48M | https://en.wikipedia.org/wiki/Bombardier_CRJ700 | (游戏 cost_factor=28) | 现实目录价仅参考 |
| 航程 | 2,950 km（1,593 nmi）ER（MTOW 82,500 lb） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （CRJ900ER 1,593 nmi / 2,950 km） | range_km_est 2365 km | 游戏偏低约 20% |
| 座级 | 最大 90 | https://en.wikipedia.org/wiki/Bombardier_CRJ700 | passenger 88 人 | 接近最大座级 |
| 巡航 | 829 km/h（巡航）/ 871 km/h（最大） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 | speed_kmh 846 km/h | 介于巡航与最大之间 |

---

### Bombardier CRJ-900LR (Bombardier_CRJ900LR)
| 字段 | 真实值 | 来源 URL | 游戏内当前值 | 偏差/备注 |
|---|---|---|---|---|
| 价格 | 同 CRJ900 家族，约 $28–48M | https://en.wikipedia.org/wiki/Bombardier_CRJ700 | (游戏 cost_factor=29) | 现实目录价仅参考 |
| 航程 | 3,385 km（1,828 nmi）LR（MTOW 84,500 lb） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 （CRJ900LR 1,828 nmi / 3,385 km） | range_km_est 2778 km | 游戏偏低约 18% |
| 座级 | 最大 90 | https://en.wikipedia.org/wiki/Bombardier_CRJ700 | passenger 90 人 | 完全一致 |
| 巡航 | 829 km/h（巡航）/ 871 km/h（最大） | https://en.wikipedia.org/wiki/Bombardier_CRJ700 | speed_kmh 846 km/h | 介于巡航与最大之间 |

---

## 批次小结
- 座级：CRJ100/200 全系 50（与游戏一致）；CRJ700 典型 70（游戏 70 一致）；CRJ900 最大 90（游戏 88/90 接近）；CRJ1000 两舱约 100（游戏 100 一致）。整体匹配良好。
- 航程：CRJ100/200 的 ER/LR 游戏值(2970/3685) 与 Jane's 数据(3000/3710)几乎一致；CRJ700/900/1000 游戏航程普遍比维基低 18–29%，呈系统性偏低。
- 巡航：CRJ700/900/1000 游戏值(830–850)落在真实巡航(829)与最大(871–876)之间，合理；CRJ100/200 游戏 814 介于正常(786)与高速(860)之间。
- 价格：游戏 `cost_factor` 仅为相对系数，已附现实目录价（USD，注年份）作参考，无法直接对应。
- 来源覆盖：aerocorner（CRJ700/900/1000/200 概览，含价格/航程/座级/巡航）、英文维基（CRJ700 系对比表含各 ER/LR 航程与价格，CRJ100 系含座级/巡航）、airplanes24（Jane's 2006，CRJ100/200 ER/LR 航程）、sunairlines（CRJ200 名录价）。CRJ100 专属 aerocorner slug 404（已用维基/airplanes24 替代）；airliners.net slug 亦 404。
