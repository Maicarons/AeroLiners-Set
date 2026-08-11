# AeroLiners Set 全机队真实数据联网核对报告

> 生成日期：2026-08-10  ｜  核对对象：游戏内 **全部 216 款** 机型（新旧皆含）>   
> 核对字段：价格（美元目录价）、航程（km）、座级（乘客）、巡航速度（km/h）>   
> 每个真实数据均标注**实际读取的来源 URL**；游戏内当前值一并列出以供对比。

## 一、方法与来源说明

- **数据来源优先级**：
  1. [aerocorner.com](https://aerocorner.com/aircraft/) —— 结构化给出 Price、Seats，Range/Cruise 在正文（主源）；
  2. 英文维基百科对应机型条目 —— 信息框/正文含 Range、Capacity、Cruise speed，有时含 Unit cost（交叉核对主用）；
  3. [airliners.net/aircraft-data](https://www.airliners.net/aircraft-data) 及 WebSearch 补充 —— 主源 404 或字段缺失时定位可靠页面。
- **单位折算**：航程统一为 km（海里 nm ×1.852）；巡航统一为 km/h（节 kt ×1.852；马赫按约 Mach×1062 @巡航高度折算并注明）。
- **游戏内值含义**：`passenger`=座级、`speed_kmh`=巡航、`range_km_est`=游戏内航程估算（由内部值×5.5 反推）、`cost_factor`=相对价格系数（游戏不直接存绝对美元价，故真实价仅作参考，备注注明「游戏用相对系数」）。
- **诚信原则**：每条真实数据均来自实际抓取的页面 URL；未能获取可靠来源的字段如实标注「未找到可靠来源」，绝不编造。

## 二、覆盖率校验

- 权威机型总数（源码抽取）：**216**
- 已核对并写入文档的机型：**216**
- 缺失（未在任一研究批次找到）：**0** （无）
- 研究批次中出现但不在权威列表的冗余 ID：**0** （无）
- 全文「未找到可靠来源」字段标注次数（粗略）：**41**

## 三、厂商分组索引

- **ATR (ATR)** [8/8] —— [ATR\_42\_300](#atr_42_300), [ATR\_42\_300F](#atr_42_300f), [ATR\_42\_500](#atr_42_500), [ATR\_42\_600](#atr_42_600), [ATR\_72\_200](#atr_72_200), [ATR\_72\_200F](#atr_72_200f), [ATR\_72\_500](#atr_72_500), [ATR\_72\_600](#atr_72_600)
- **中航工业 (AVIC)** [3/3] —— [AVIC\_MA60](#avic_ma60), [AVIC\_MA600](#avic_ma600), [AVIC\_Y7\_200](#avic_y7_200)
- **空中客车 (Airbus)** [30/30] —— [AIRBUS\_A220\_100](#airbus_a220_100), [AIRBUS\_A321LR](#airbus_a321lr), [AIRBUS\_A321XLR](#airbus_a321xlr), [AIRBUS\_A330\_800NEO](#airbus_a330_800neo), [Airbus\_A220\_300](#airbus_a220_300), [Airbus\_A300\_600F](#airbus_a300_600f), [Airbus\_A300\_600R](#airbus_a300_600r), [Airbus\_A310\_200](#airbus_a310_200), [Airbus\_A310\_200F](#airbus_a310_200f), [Airbus\_A310\_300](#airbus_a310_300), [Airbus\_A310\_300F](#airbus_a310_300f), [Airbus\_A318](#airbus_a318), [Airbus\_A319](#airbus_a319), [Airbus\_A319neo](#airbus_a319neo), [Airbus\_A320\_100](#airbus_a320_100), [Airbus\_A320\_200](#airbus_a320_200), [Airbus\_A320neo](#airbus_a320neo), [Airbus\_A321\_100](#airbus_a321_100), [Airbus\_A321\_200](#airbus_a321_200), [Airbus\_A321neo](#airbus_a321neo), [Airbus\_A330\_200](#airbus_a330_200), [Airbus\_A330\_200F](#airbus_a330_200f), [Airbus\_A330\_300](#airbus_a330_300), [Airbus\_A330\_900neo](#airbus_a330_900neo), [Airbus\_A340\_300](#airbus_a340_300), [Airbus\_A340\_500](#airbus_a340_500), [Airbus\_A340\_600](#airbus_a340_600), [Airbus\_A350\_1000](#airbus_a350_1000), [Airbus\_A350\_900](#airbus_a350_900), [Airbus\_A380\_800](#airbus_a380_800)
- **安东诺夫 (Antonov)** [5/5] —— [ANTONOV\_AN140](#antonov_an140), [ANTONOV\_AN148](#antonov_an148), [ANTONOV\_AN158](#antonov_an158), [Antonov\_124](#antonov_124), [Antonov\_225](#antonov_225)
- **英国飞机公司 (BAC)** [5/5] —— [BAC\_1\_11\_200](#bac_1_11_200), [BAC\_1\_11\_300](#bac_1_11_300), [BAC\_1\_11\_400](#bac_1_11_400), [BAC\_1\_11\_500](#bac_1_11_500), [BAC\_CONCORDE](#bac_concorde)
- **英宇航 (BAe)** [4/4] —— [BAe\_146\_100](#bae_146_100), [BAe\_146\_200](#bae_146_200), [BAe\_146\_300](#bae_146_300), [BAe\_146\_300QT](#bae_146_300qt)
- **波音 (Boeing)** [57/57] —— [BOEING\_737MAX7](#boeing_737max7), [BOEING\_747SP](#boeing_747sp), [BOEING\_757\_300](#boeing_757_300), [BOEING\_777\_8](#boeing_777_8), [Boeing\_707\_320](#boeing_707_320), [Boeing\_707\_420](#boeing_707_420), [Boeing\_717\_200](#boeing_717_200), [Boeing\_727\_100](#boeing_727_100), [Boeing\_727\_200](#boeing_727_200), [Boeing\_727\_200F](#boeing_727_200f), [Boeing\_737\_100](#boeing_737_100), [Boeing\_737\_200](#boeing_737_200), [Boeing\_737\_200C](#boeing_737_200c), [Boeing\_737\_300](#boeing_737_300), [Boeing\_737\_300F](#boeing_737_300f), [Boeing\_737\_400](#boeing_737_400), [Boeing\_737\_500](#boeing_737_500), [Boeing\_737\_600](#boeing_737_600), [Boeing\_737\_700](#boeing_737_700), [Boeing\_737\_800](#boeing_737_800), [Boeing\_737\_900](#boeing_737_900), [Boeing\_737\_900ER](#boeing_737_900er), [Boeing\_737\_MAX10](#boeing_737_max10), [Boeing\_737\_MAX8](#boeing_737_max8), [Boeing\_737\_MAX9](#boeing_737_max9), [Boeing\_747\_100](#boeing_747_100), [Boeing\_747\_200](#boeing_747_200), [Boeing\_747\_200M](#boeing_747_200m), [Boeing\_747\_300](#boeing_747_300), [Boeing\_747\_300M](#boeing_747_300m), [Boeing\_747\_400](#boeing_747_400), [Boeing\_747\_400BCF](#boeing_747_400bcf), [Boeing\_747\_400D](#boeing_747_400d), [Boeing\_747\_400ER](#boeing_747_400er), [Boeing\_747\_400ERF](#boeing_747_400erf), [Boeing\_747\_400M](#boeing_747_400m), [Boeing\_747\_400SCD](#boeing_747_400scd), [Boeing\_747\_8F](#boeing_747_8f), [Boeing\_747\_8I](#boeing_747_8i), [Boeing\_757\_200](#boeing_757_200), [Boeing\_757\_200F](#boeing_757_200f), [Boeing\_767\_200](#boeing_767_200), [Boeing\_767\_200ER](#boeing_767_200er), [Boeing\_767\_300](#boeing_767_300), [Boeing\_767\_300ER](#boeing_767_300er), [Boeing\_767\_300F](#boeing_767_300f), [Boeing\_767\_400ER](#boeing_767_400er), [Boeing\_777X](#boeing_777x), [Boeing\_777\_200](#boeing_777_200), [Boeing\_777\_200ER](#boeing_777_200er), [Boeing\_777\_200F](#boeing_777_200f), [Boeing\_777\_200LR](#boeing_777_200lr), [Boeing\_777\_300](#boeing_777_300), [Boeing\_777\_300ER](#boeing_777_300er), [Boeing\_787\_10](#boeing_787_10), [Boeing\_787\_8](#boeing_787_8), [Boeing\_787\_9](#boeing_787_9)
- **庞巴迪 (Bombardier)** [17/17] —— [Bombardier\_CRJ1000](#bombardier_crj1000), [Bombardier\_CRJ1000EL](#bombardier_crj1000el), [Bombardier\_CRJ100ER](#bombardier_crj100er), [Bombardier\_CRJ100LR](#bombardier_crj100lr), [Bombardier\_CRJ200ER](#bombardier_crj200er), [Bombardier\_CRJ200LR](#bombardier_crj200lr), [Bombardier\_CRJ700](#bombardier_crj700), [Bombardier\_CRJ700ER](#bombardier_crj700er), [Bombardier\_CRJ900](#bombardier_crj900), [Bombardier\_CRJ900ER](#bombardier_crj900er), [Bombardier\_CRJ900LR](#bombardier_crj900lr), [Bombardier\_Dash\_8\_100](#bombardier_dash_8_100), [Bombardier\_Dash\_8\_200](#bombardier_dash_8_200), [Bombardier\_Dash\_8\_200Q](#bombardier_dash_8_200q), [Bombardier\_Dash\_8\_300](#bombardier_dash_8_300), [Bombardier\_Dash\_8\_300Q](#bombardier_dash_8_300q), [Bombardier\_Dash\_8\_400Q](#bombardier_dash_8_400q)
- **布里顿-诺曼 (Britten-Norman)** [2/2] —— [BRITTEN\_NORMAN\_BN2B](#britten_norman_bn2b), [BRITTEN\_NORMAN\_BN2T](#britten_norman_bn2t)
- **中国商飞 (COMAC)** [3/3] —— [COMAC\_C909](#comac_c909), [COMAC\_C919](#comac_c919), [COMAC\_C929](#comac_c929)
- **塞斯纳 (Cessna)** [7/7] —— [CESSNA\_208](#cessna_208), [CESSNA\_208B](#cessna_208b), [CESSNA\_402](#cessna_402), [CESSNA\_404](#cessna_404), [CESSNA\_408](#cessna_408), [CESSNA\_414](#cessna_414), [CESSNA\_421](#cessna_421)
- **康维尔 (Convair)** [2/2] —— [CONVAIR\_880](#convair_880), [CONVAIR\_990](#convair_990)
- **巴航工 (Embraer)** [16/16] —— [EMBRAER\_E175\_E2](#embraer_e175_e2), [EMBRAER\_E190\_E2](#embraer_e190_e2), [EMBRAER\_ERJ135](#embraer_erj135), [EMBRAER\_ERJ140](#embraer_erj140), [Embraer\_E170LR](#embraer_e170lr), [Embraer\_E170STD](#embraer_e170std), [Embraer\_E175LR](#embraer_e175lr), [Embraer\_E175STD](#embraer_e175std), [Embraer\_E190AR](#embraer_e190ar), [Embraer\_E190LR](#embraer_e190lr), [Embraer\_E190STD](#embraer_e190std), [Embraer\_E195AR](#embraer_e195ar), [Embraer\_E195LR](#embraer_e195lr), [Embraer\_E195STD](#embraer_e195std), [Embraer\_E195\_E2](#embraer_e195_e2), [Embraer\_ERJ145](#embraer_erj145)
- **福克 (Fokker)** [4/4] —— [FOKKER\_F27](#fokker_f27), [FOKKER\_F28](#fokker_f28), [Fokker\_F100](#fokker_f100), [Fokker\_F70](#fokker_f70)
- **通用原子 (General Atomics)** [1/1] —— [GENERAL\_ATOMICS\_DO228](#general_atomics_do228)
- **霍克·西德利 (Hawker_Siddeley)** [1/1] —— [HS\_TRIDENT](#hs_trident)
- **伊尔 (Ilyushin)** [5/5] —— [ILYUSHIN\_IL114](#ilyushin_il114), [ILYUSHIN\_IL18](#ilyushin_il18), [ILYUSHIN\_IL96](#ilyushin_il96), [Ilyushin\_62](#ilyushin_62), [Ilyushin\_76](#ilyushin_76)
- **伊尔库特 (Irkut)** [1/1] —— [IRKUT\_MC21](#irkut_mc21)
- **LET (LET)** [1/1] —— [LET\_L410](#let_l410)
- **洛克希德 (Lockheed)** [3/3] —— [LOCKHEED\_L1011](#lockheed_l1011), [LOCKHEED\_L188](#lockheed_l188), [Lockheed\_L049\_Constellation](#lockheed_l049_constellation)
- **麦道 (McDonnell_Douglas)** [24/24] —— [DOUGLAS\_DC3](#douglas_dc3), [DOUGLAS\_DC6](#douglas_dc6), [DOUGLAS\_DC7](#douglas_dc7), [Douglas\_DC10\_10](#douglas_dc10_10), [Douglas\_DC10\_30](#douglas_dc10_30), [Douglas\_DC10\_40](#douglas_dc10_40), [Douglas\_DC8\_10](#douglas_dc8_10), [Douglas\_DC8\_20](#douglas_dc8_20), [Douglas\_DC8\_30](#douglas_dc8_30), [Douglas\_DC8\_40](#douglas_dc8_40), [Douglas\_DC8\_50](#douglas_dc8_50), [Douglas\_DC9\_10](#douglas_dc9_10), [Douglas\_DC9\_20](#douglas_dc9_20), [Douglas\_DC9\_30](#douglas_dc9_30), [Douglas\_DC9\_40](#douglas_dc9_40), [Douglas\_DC9\_50](#douglas_dc9_50), [McDonnell\_Douglas\_MD11](#mcdonnell_douglas_md11), [McDonnell\_Douglas\_MD11F](#mcdonnell_douglas_md11f), [McDonnell\_Douglas\_MD81](#mcdonnell_douglas_md81), [McDonnell\_Douglas\_MD82](#mcdonnell_douglas_md82), [McDonnell\_Douglas\_MD83](#mcdonnell_douglas_md83), [McDonnell\_Douglas\_MD87](#mcdonnell_douglas_md87), [McDonnell\_Douglas\_MD88](#mcdonnell_douglas_md88), [McDonnell\_Douglas\_MD90](#mcdonnell_douglas_md90)
- **PZL (PZL)** [1/1] —— [PZL\_AN28](#pzl_an28)
- **皮拉图斯 (Pilatus)** [2/2] —— [PILATUS\_PC12](#pilatus_pc12), [PILATUS\_PC24](#pilatus_pc24)
- **雷神 (Raytheon)** [1/1] —— [RAYTHEON\_BEECH1900D](#raytheon_beech1900d)
- **南方飞机 (SUD)** [1/1] —— [SUD\_CARAVELLE\_III](#sud_caravelle_iii)
- **苏霍伊 (Sukhoi)** [1/1] —— [SUKHOI\_SSJ100](#sukhoi_ssj100)
- **图波列夫 (Tupolev)** [5/5] —— [TUPOLEV\_TU204](#tupolev_tu204), [TUPOLEV\_TU214](#tupolev_tu214), [Tupolev\_Tu134](#tupolev_tu134), [Tupolev\_Tu154B](#tupolev_tu154b), [Tupolev\_Tu154M](#tupolev_tu154m)
- **维克斯 (Vickers)** [2/2] —— [VICKERS\_VC10](#vickers_vc10), [VICKERS\_VISCOUNT](#vickers_viscount)
- **雅克福列夫 (Yakovlev)** [2/2] —— [YAKOVLEV\_YAK40](#yakovlev_yak40), [YAKOVLEV\_YAK42](#yakovlev_yak42)
- **德哈维兰 (de Havilland)** [2/2] —— [DEHAVILLAND\_COMET](#dehavilland_comet), [DEHAVILLAND\_DHC6\_400](#dehavilland_dhc6_400)

## 四、逐机核对明细（按厂商分组）

### ATR · ATR

<a id="atr_42_300"></a>

### ATR 42-300 (ATR_42_300)

| 字段 | 真实值                                                             | 来源 URL                                                                                                                                                                                                                      | 游戏内当前值              | 偏差/备注             |
| -- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------- |
| 价格 | 约 US$9.2M（ATR 42-200 单价，1991）／全系估值 US$18–19.5M；**无 -300 单独目录价** | <https://baike.baidu.com/item/ATR42%E9%A3%9E%E6%9C%BA> （1991 单价）；<https://www.deagel.com/Civil%20Aviation/ATR%204272/a000090> （ATR 42 组 US$18M）；https://www.newton.com.tw/wiki/ATR42%E9%A3%9E%E6%9C%BA （单机造价 US$19.5M/2012） | (cost_factor=11)    | 合理区间，无精确 -300 价   |
| 航程 | 1,470 km（48 座最大商载，794 nmi）；最大燃油 4,481 km                        | <https://en.wikipedia.org/wiki/ATR_42> ；<https://www.caac.gov.cn/PHONE/GYMH/MHBK/HKQJS/201509/t20150923_1832.html>                                                                                                          | range_km_est 908 km | 游戏偏低约 38%（取最大商载值） |
| 座级 | 48 人（30" 间距）                                                    | <https://en.wikipedia.org/wiki/ATR_42>                                                                                                                                                                                      | passenger 48 人      | 一致                |
| 巡航 | 484 km/h（261 kt，最大巡航）；495 km/h（CAAC 最大巡航）                       | <https://en.wikipedia.org/wiki/ATR_42> ；<https://www.caac.gov.cn/PHONE/GYMH/MHBK/HKQJS/201509/t20150923_1832.html>                                                                                                          | speed_kmh 491 km/h  | 一致                |

<a id="atr_42_300f"></a>

### ATR 42-300F (ATR_42_300F)

| 字段 | 真实值                                     | 来源 URL                                                                                                           | 游戏内当前值              | 偏差/备注            |
| -- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------- | ---------------- |
| 价格 | 由客机改装，无单独目录价；约 US$9–19.5M 估算            | <https://baike.baidu.com/item/ATR42%E9%A3%9E%E6%9C%BA> ；<https://www.newton.com.tw/wiki/ATR42%E9%A3%9E%E6%9C%BA> | (cost_factor=12)    | 货机换算系数略高，合理      |
| 航程 | 约 2,316 km（载 3,800 kg 货或 42 客，ATR 42-F） | <https://baike.baidu.com/item/ATR42%E9%A3%9E%E6%9C%BA> （ATR42-F）                                                 | range_km_est 908 km | 游戏严重偏低（货机实际航程更高） |
| 座级 | 0（全货运）                                  | <https://en.wikipedia.org/wiki/ATR_42>                                                                           | passenger 0 人       | 一致               |
| 巡航 | 约 484–495 km/h                          | <https://en.wikipedia.org/wiki/ATR_42>                                                                           | speed_kmh 491 km/h  | 一致               |

<a id="atr_42_500"></a>

### ATR 42-500 (ATR_42_500)

| 字段 | 真实值                    | 来源 URL                                                                                | 游戏内当前值               | 偏差/备注        |
| -- | ---------------------- | ------------------------------------------------------------------------------------- | -------------------- | ------------ |
| 价格 | US$12.1 million        | <https://aerocorner.com/aircraft/atr-42-500/>                                         | (cost_factor=14)     | 合理           |
| 航程 | 1,345 km（48 座，726 nmi） | <https://en.wikipedia.org/wiki/ATR_42>                                                | range_km_est 1540 km | 游戏偏高约 14%    |
| 座级 | 48 人（30" 间距）           | <https://aerocorner.com/aircraft/atr-42-500/> ；<https://en.wikipedia.org/wiki/ATR_42> | passenger 48 人       | 一致           |
| 巡航 | 556 km/h（300 kt，最大巡航）  | <https://en.wikipedia.org/wiki/ATR_42>                                                | speed_kmh 564 km/h   | 基本一致（差 1.4%） |

<a id="atr_42_600"></a>

### ATR 42-600 (ATR_42_600)

| 字段 | 真实值                                              | 来源 URL                                                                                | 游戏内当前值               | 偏差/备注    |
| -- | ------------------------------------------------ | ------------------------------------------------------------------------------------- | -------------------- | -------- |
| 价格 | US$19.5 million                                  | <https://aerocorner.com/aircraft/atr-42-600/>                                         | (cost_factor=14)     | 合理       |
| 航程 | 1,345 km（48 座，726 nmi）；满客最大速度航程 716 nmi≈1,326 km | <https://en.wikipedia.org/wiki/ATR_42> ；<https://aerocorner.com/aircraft/atr-42-600/> | range_km_est 1348 km | 高度一致     |
| 座级 | 48 人（40–50 典型）                                   | <https://aerocorner.com/aircraft/atr-42-600/> ；<https://en.wikipedia.org/wiki/ATR_42> | passenger 48 人       | 一致       |
| 巡航 | 535 km/h（289 kt）；aerocorner 最大 556 km/h          | <https://en.wikipedia.org/wiki/ATR_42>                                                | speed_kmh 564 km/h   | 游戏偏高约 5% |

<a id="atr_72_200"></a>

### ATR 72-200 (ATR_72_200)

| 字段 | 真实值                                    | 来源 URL                                                       | 游戏内当前值               | 偏差/备注 |
| -- | -------------------------------------- | ------------------------------------------------------------ | -------------------- | ----- |
| 价格 | 约 US$21 million（ATR 72 组估值；无 -200 单独价） | <https://www.deagel.com/Civil%20Aviation/ATR%204272/a000090> | (cost_factor=16)     | 合理    |
| 航程 | 1,596 km（最大客载，862 nmi）                 | <https://en.wikipedia.org/wiki/ATR_72>                       | range_km_est 1595 km | 几乎一致  |
| 座级 | 66@31" / 72@29"，最大 78                  | <https://en.wikipedia.org/wiki/ATR_72>                       | passenger 74 人       | 在范围内  |
| 巡航 | 515 km/h（278 kt）                       | <https://en.wikipedia.org/wiki/ATR_72>                       | speed_kmh 515 km/h   | 完全一致  |

<a id="atr_72_200f"></a>

### ATR 72-200F (ATR_72_200F)

| 字段 | 真实值                          | 来源 URL                                                       | 游戏内当前值               | 偏差/备注     |
| -- | ---------------------------- | ------------------------------------------------------------ | -------------------- | --------- |
| 价格 | 由客机改装，无单独目录价；约 US$21M 估算     | <https://www.deagel.com/Civil%20Aviation/ATR%204272/a000090> | (cost_factor=19)     | 货机系数略高，合理 |
| 航程 | 约 1,596 km（同 -200 客机基准，货载不同） | <https://en.wikipedia.org/wiki/ATR_72>                       | range_km_est 1595 km | 一致        |
| 座级 | 0（全货运）                       | <https://en.wikipedia.org/wiki/ATR_72>                       | passenger 0 人        | 一致        |
| 巡航 | 约 515–517 km/h               | <https://en.wikipedia.org/wiki/ATR_72>                       | speed_kmh 523 km/h   | 基本一致      |

<a id="atr_72_500"></a>

### ATR 72-500 (ATR_72_500)

| 字段 | 真实值                                             | 来源 URL                                                                                | 游戏内当前值               | 偏差/备注     |
| -- | ----------------------------------------------- | ------------------------------------------------------------------------------------- | -------------------- | --------- |
| 价格 | US$14.4 million（aerocorner；Wikipedia 仅列 -600 价） | <https://aerocorner.com/aircraft/atr-72-500/>                                         | (cost_factor=18)     | 合理        |
| 航程 | 1,430 km（最大客载，772 nmi）                          | <https://en.wikipedia.org/wiki/ATR_72>                                                | range_km_est 1622 km | 游戏偏高约 13% |
| 座级 | 74（典型），最大 78                                    | <https://aerocorner.com/aircraft/atr-72-500/> ；<https://en.wikipedia.org/wiki/ATR_72> | passenger 74 人       | 一致        |
| 巡航 | 510 km/h（275 kt）                                | <https://en.wikipedia.org/wiki/ATR_72>                                                | speed_kmh 515 km/h   | 基本一致      |

<a id="atr_72_600"></a>

### ATR 72-600 (ATR_72_600)

| 字段 | 真实值                                                                  | 来源 URL                                                                                | 游戏内当前值               | 偏差/备注      |
| -- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------------- | ---------- |
| 价格 | US$26 million（2017）；目录价 US$26.8M、折后约 US$20.1M（2018）                  | <https://aerocorner.com/aircraft/atr-72-600/> ；<https://en.wikipedia.org/wiki/ATR_72> | (cost_factor=18)     | 合理         |
| 航程 | 1,404 km（最大客载，758 nmi）；aerocorner 列 "最大航程 2,065 mi≈3,323 km"（疑似最大燃油） | <https://en.wikipedia.org/wiki/ATR_72> ；<https://aerocorner.com/aircraft/atr-72-600/> | range_km_est 1370 km | 接近（取最大客载值） |
| 座级 | 72（29" 间距），最大 78                                                     | <https://aerocorner.com/aircraft/atr-72-600/> ；<https://en.wikipedia.org/wiki/ATR_72> | passenger 72 人       | 一致         |
| 巡航 | 510 km/h（275 kt）                                                     | <https://en.wikipedia.org/wiki/ATR_72>                                                | speed_kmh 515 km/h   | 基本一致       |

### 中航工业 · AVIC

<a id="avic_ma60"></a>

### AVIC MA-60 (AVIC_MA60)

| 字段 | 真实值                             | 来源 URL                                             | 游戏内当前值               | 偏差/备注     |
| -- | ------------------------------- | -------------------------------------------------- | -------------------- | --------- |
| 价格 | 目录价 US$14.5 million（2011，9 架合同） | <https://m.10jqka.com.cn/20110929/c61758076.shtml> | (cost_factor=14)     | 高度一致      |
| 航程 | 1,600 km（860 nmi）               | <https://en.wikipedia.org/wiki/Xi%27an_MA60>       | range_km_est 1370 km | 游戏偏低约 14% |
| 座级 | 60（典型）/ 最大 62                   | <https://en.wikipedia.org/wiki/Xi%27an_MA60>       | passenger 60 人       | 一致        |
| 巡航 | 430 km/h（230 kt）                | <https://en.wikipedia.org/wiki/Xi%27an_MA60>       | speed_kmh 430 km/h   | 完全一致      |

<a id="avic_ma600"></a>

### AVIC MA-600 (AVIC_MA600)

| 字段 | 真实值                               | 来源 URL                                             | 游戏内当前值               | 偏差/备注     |
| -- | --------------------------------- | -------------------------------------------------- | -------------------- | --------- |
| 价格 | **未找到可靠单独目录价**；参考 MA60 约 US$14.5M | <https://en.wikipedia.org/wiki/Xi%27an_MA600> （无价） | (cost_factor=18)     | 系数偏高，建议复核 |
| 航程 | 1,430 km（770 nmi，56 客+储备）         | <https://en.wikipedia.org/wiki/Xi%27an_MA600>      | range_km_est 1380 km | 接近        |
| 座级 | 60（最大）                            | <https://en.wikipedia.org/wiki/Xi%27an_MA600>      | passenger 60 人       | 一致        |
| 巡航 | 430 km/h（230 kt）                  | <https://en.wikipedia.org/wiki/Xi%27an_MA600>      | speed_kmh 430 km/h   | 完全一致      |

<a id="avic_y7_200"></a>

### AVIC Y-7-200 (AVIC_Y7_200)

| 字段 | 真实值                                                | 来源 URL                                        | 游戏内当前值               | 偏差/备注                 |
| -- | -------------------------------------------------- | --------------------------------------------- | -------------------- | --------------------- |
| 价格 | **未找到可靠目录价**（Y-7 系列无公开价）                           | <https://en.wikipedia.org/wiki/Xian_Y-7> （无价） | (cost_factor=14)     | 无法核对                  |
| 航程 | Y-7-200 无独立数据；参考 Y-7-100：最大商载 910 km，最大燃油 1,982 km | <https://en.wikipedia.org/wiki/Xian_Y-7>      | range_km_est 1551 km | 取最大燃油值接近；Y-7-200 实测缺失 |
| 座级 | Y-7-100：52（最大）；Y-7-200 无独立数据                       | <https://en.wikipedia.org/wiki/Xian_Y-7>      | passenger 52 人       | 与 Y-7-100 一致          |
| 巡航 | 423 km/h（228 kt，Y-7-100）                           | <https://en.wikipedia.org/wiki/Xian_Y-7>      | speed_kmh 420 km/h   | 基本一致                  |

### 空中客车 · Airbus

<a id="airbus_a220_100"></a>

### Airbus A220-100 (AIRBUS_A220_100)

| 字段 | 真实值                                    | 来源 URL                                                                                           | 游戏内当前值               | 偏差/备注                   |
| -- | -------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------- | ----------------------- |
| 价格 | US$81 million（无年份，目录价参考）               | <https://aerocorner.com/aircraft/airbus-a220-100/>                                               | (游戏 cost_factor=80)  | 量级一致                    |
| 航程 | 3,400 nmi（6,300 km）认证航程（2019 MTOW 提升后） | <https://en.wikipedia.org/wiki/Airbus_A220>                                                      | range_km_est=6298 km | 基本一致（6,300 vs 6,298）    |
| 座级 | 两舱约 116 座；典型 108–133 座                 | <https://aerocorner.com/aircraft/airbus-a220-100/> + <https://en.wikipedia.org/wiki/Airbus_A220> | passenger=120 人      | 合理（游戏取中值）               |
| 巡航 | 约 470 kt（870 km/h）                     | <https://aerocorner.com/aircraft/airbus-a220-100/>                                               | speed_kmh=829 km/h   | 略偏低；真实约 M0.78（≈829–870） |

<a id="airbus_a321lr"></a>

### Airbus A321LR (AIRBUS_A321LR)

| 字段 | 真实值                               | 来源 URL                                                                                         | 游戏内当前值               | 偏差/备注              |
| -- | --------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------- | ------------------ |
| 价格 | 无单独目录价；参考 A321neo US$129.5M（2018） | <https://www.airbus.com/sites/g/files/jlcbta136/files/2021-07/new-airbus-list-prices-2018.pdf> | (游戏 cost_factor=84)  | 参考价偏高，游戏值偏低        |
| 航程 | 4,000 nmi（7,410 km）载 206 客        | <https://en.wikipedia.org/wiki/Airbus_A321> + <https://en.wikipedia.org/wiki/Airbus_A321XLR>   | range_km_est=7398 km | 一致（7,410 vs 7,398） |
| 座级 | 两舱 206（16J+190Y）；单舱最大 244         | <https://en.wikipedia.org/wiki/Airbus_A321>                                                    | passenger=206 人      | 一致                 |
| 巡航 | Mach 0.78（833 km/h）               | <https://en.wikipedia.org/wiki/Airbus_A321>                                                    | speed_kmh=830 km/h   | 一致                 |

<a id="airbus_a321xlr"></a>

### Airbus A321XLR (AIRBUS_A321XLR)

| 字段 | 真实值                  | 来源 URL                                         | 游戏内当前值               | 偏差/备注                  |
| -- | -------------------- | ---------------------------------------------- | -------------------- | ---------------------- |
| 价格 | US$142 million（2019） | <https://en.wikipedia.org/wiki/Airbus_A321XLR> | (游戏 cost_factor=73)  | 游戏值明显偏低                |
| 航程 | 4,700 nmi（8,700 km）  | <https://en.wikipedia.org/wiki/Airbus_A321XLR> | range_km_est=8701 km | 一致（8,700 vs 8,701）     |
| 座级 | 两舱 206；单舱最大 244      | <https://en.wikipedia.org/wiki/Airbus_A321XLR> | passenger=210 人      | 接近（取两舱值）               |
| 巡航 | Mach 0.78（833 km/h）  | <https://en.wikipedia.org/wiki/Airbus_A321XLR> | speed_kmh=902 km/h   | 游戏偏高（902≈M0.85，接近 Mmo） |

<a id="airbus_a330_800neo"></a>

### Airbus A330-800neo (AIRBUS_A330_800NEO)

| 字段 | 真实值                                      | 来源 URL                                                                                               | 游戏内当前值                | 偏差/备注                |
| -- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------- | -------------------- |
| 价格 | US$259.9 million（2018，unit cost）         | <https://www.airbus.com/sites/g/files/jlcbta136/files/2021-07/new-airbus-list-prices-2018.pdf>       | (游戏 cost_factor=187)  | 游戏偏低                 |
| 航程 | 8,100 nmi（15,000 km）载 257 客；最大 15,090 km | <https://en.wikipedia.org/wiki/Airbus_A330neo> + <https://flightq.app/aircraft/airbus-a330-800neo>   | range_km_est=14998 km | 一致（15,000 vs 14,998） |
| 座级 | 三舱 220–260（典型 257）；最大 406                | <https://en.wikipedia.org/wiki/Airbus_A330neo>                                                       | passenger=264 人       | 合理（取典型值）             |
| 巡航 | Mach 0.82（约 871 km/h）                    | <https://simpleflying.com/tag/airbus-a330/-800/> + <https://flightq.app/aircraft/airbus-a330-800neo> | speed_kmh=926 km/h    | 游戏偏高（926≈Mmo 0.86）   |

<a id="airbus_a220_300"></a>

### Airbus A220-300 (Airbus_A220_300)

| 字段 | 真实值                             | 来源 URL                                                                                           | 游戏内当前值               | 偏差/备注                    |
| -- | ------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------- | ------------------------ |
| 价格 | US$91.5 million                 | <https://aerocorner.com/aircraft/airbus-a220-300/>                                               | (游戏 cost_factor=92)  | 一致                       |
| 航程 | 3,350–3,550 nmi（6,200–6,570 km） | <https://en.wikipedia.org/wiki/Airbus_A220>                                                      | range_km_est=6298 km | 略偏低（真实上限 6,570 vs 6,298） |
| 座级 | 两舱约 141；典型 130–160              | <https://aerocorner.com/aircraft/airbus-a220-300/> + <https://en.wikipedia.org/wiki/Airbus_A220> | passenger=145 人      | 合理                       |
| 巡航 | 约 470 kt（870 km/h）              | <https://aerocorner.com/aircraft/airbus-a220-100/（同系列）>                                          | speed_kmh=840 km/h   | 合理（游戏取 ~M0.79）           |

<a id="airbus_a300_600f"></a>

### Airbus A300-600F (Airbus_A300_600F)

| 字段 | 真实值                                     | 来源 URL                                                     | 游戏内当前值                | 偏差/备注            |
| -- | --------------------------------------- | ---------------------------------------------------------- | --------------------- | ---------------- |
| 价格 | 无单独目录价；参考 A300-600 US$109.9M（2001）      | <https://www.janes.migavia.com/inter/airbus/a300-600.html> | (游戏 cost_factor=122)  | 参考价偏高，游戏偏低       |
| 航程 | 7,500 km（4,050 nmi）最大业载；最大航程约 12,200 km | <https://en.wikipedia.org/wiki/Airbus_A300>                | range_km_est=14108 km | 游戏值接近"最大航程"上限，偏高 |
| 座级 | 0（全货机，主货舱 43 AYY/9 LD7）                 | <https://en.wikipedia.org/wiki/Airbus_A300>                | passenger=0 人         | 一致               |
| 巡航 | Mach 0.78（833 km/h）                     | <https://en.wikipedia.org/wiki/Airbus_A300>                | speed_kmh=870 km/h    | 略偏高              |

<a id="airbus_a300_600r"></a>

### Airbus A300-600R (Airbus_A300_600R)

| 字段 | 真实值                        | 来源 URL                                                     | 游戏内当前值                | 偏差/备注                 |
| -- | -------------------------- | ---------------------------------------------------------- | --------------------- | --------------------- |
| 价格 | US$109.9 million（2001，参考价） | <https://www.janes.migavia.com/inter/airbus/a300-600.html> | (游戏 cost_factor=122)  | 参考价偏高，游戏偏低            |
| 航程 | 7,500 km（4,050 nmi）        | <https://en.wikipedia.org/wiki/Airbus_A300>                | range_km_est=12265 km | 游戏偏高（可能混入货机/ Ferry 值） |
| 座级 | 两舱 247（46F+201Y）；最大 345    | <https://en.wikipedia.org/wiki/Airbus_A300>                | passenger=220 人       | 偏低（真实两舱 247）          |
| 巡航 | Mach 0.78（833 km/h）        | <https://en.wikipedia.org/wiki/Airbus_A300>                | speed_kmh=870 km/h    | 略偏高                   |

<a id="airbus_a310_200"></a>

### Airbus A310-200 (Airbus_A310_200)

| 字段 | 真实值                 | 来源 URL                                             | 游戏内当前值               | 偏差/备注           |
| -- | ------------------- | -------------------------------------------------- | -------------------- | --------------- |
| 价格 | US$88 million（2004） | <https://aerocorner.com/aircraft/airbus-a310-200/> | (游戏 cost_factor=134) | 游戏偏高            |
| 航程 | 3,500 nmi（6,500 km） | <https://en.wikipedia.org/wiki/Airbus_A310>        | range_km_est=5500 km | 游戏偏低            |
| 座级 | 两舱 195；最大 245       | <https://en.wikipedia.org/wiki/Airbus_A310>        | passenger=218 人      | 合理（取两舱偏上）       |
| 巡航 | 约 470 kt（870 km/h）  | <https://aerocorner.com/aircraft/airbus-a310-200/> | speed_kmh=902 km/h   | 游戏偏高（902≈M0.85） |

<a id="airbus_a310_200f"></a>

### Airbus A310-200F (Airbus_A310_200F)

| 字段 | 真实值                         | 来源 URL                                           | 游戏内当前值               | 偏差/备注                |
| -- | --------------------------- | ------------------------------------------------ | -------------------- | -------------------- |
| 价格 | US$80.0 million（1980，转换型）   | <https://simpleflying.com/tag/airbus-a310/-200/> | (游戏 cost_factor=134) | 游戏偏高                 |
| 航程 | 3,214 nmi（5,950 km）载 39 t 货 | <https://simpleflying.com/tag/airbus-a310/-200/> | range_km_est=5500 km | 基本一致（5,950 vs 5,500） |
| 座级 | 0（货机）                       | <https://simpleflying.com/tag/airbus-a310/-200/> | passenger=0 人        | 一致                   |
| 巡航 | Mach 0.82（约 871 km/h）       | <https://simpleflying.com/tag/airbus-a310/-200/> | speed_kmh=902 km/h   | 游戏偏高                 |

<a id="airbus_a310_300"></a>

### Airbus A310-300 (Airbus_A310_300)

| 字段 | 真实值                 | 来源 URL                                             | 游戏内当前值                | 偏差/备注 |
| -- | ------------------- | -------------------------------------------------- | --------------------- | ----- |
| 价格 | US$72 million（1998） | <https://aerocorner.com/aircraft/airbus-a310-300/> | (游戏 cost_factor=137)  | 游戏偏高  |
| 航程 | 5,150 nmi（9,540 km） | <https://en.wikipedia.org/wiki/Airbus_A310>        | range_km_est=10808 km | 游戏偏高  |
| 座级 | 两舱 220；最大 240       | <https://en.wikipedia.org/wiki/Airbus_A310>        | passenger=218 人       | 一致    |
| 巡航 | 约 470 kt（870 km/h）  | <https://aerocorner.com/aircraft/airbus-a310-300/> | speed_kmh=902 km/h    | 游戏偏高  |

<a id="airbus_a310_300f"></a>

### Airbus A310-300F (Airbus_A310_300F)

| 字段 | 真实值                                                                | 来源 URL                                           | 游戏内当前值               | 偏差/备注                  |
| -- | ------------------------------------------------------------------ | ------------------------------------------------ | -------------------- | ---------------------- |
| 价格 | US$85.0 million（1993，转换型）                                          | <https://simpleflying.com/tag/airbus-a310/-300/> | (游戏 cost_factor=142) | 游戏偏高                   |
| 航程 | 4,350 nmi（8,060 km）【来源差异：procharter 最大航程 7,250 km，Ferry 10,860 km】 | <https://simpleflying.com/tag/airbus-a310/-300/> | range_km_est=7260 km | 落于来源区间（8,060 vs 7,260） |
| 座级 | 0（货机）                                                              | <https://simpleflying.com/tag/airbus-a310/-300/> | passenger=0 人        | 一致                     |
| 巡航 | Mach 0.82（约 871 km/h）                                              | <https://simpleflying.com/tag/airbus-a310/-300/> | speed_kmh=902 km/h   | 游戏偏高                   |

<a id="airbus_a318"></a>

### Airbus A318 (Airbus_A318)

| 字段 | 真实值                 | 来源 URL                                      | 游戏内当前值               | 偏差/备注   |
| -- | ------------------- | ------------------------------------------- | -------------------- | ------- |
| 价格 | US$56–62 million    | <https://en.wikipedia.org/wiki/Airbus_A318> | (游戏 cost_factor=57)  | 一致（取下限） |
| 航程 | 3,100 nmi（5,740 km） | <https://en.wikipedia.org/wiki/Airbus_A318> | range_km_est=3658 km | 游戏偏低    |
| 座级 | 两舱 107；最大 132       | <https://en.wikipedia.org/wiki/Airbus_A318> | passenger=107 人      | 一致      |
| 巡航 | Mach 0.78（829 km/h） | <https://en.wikipedia.org/wiki/Airbus_A318> | speed_kmh=854 km/h   | 略偏高     |

<a id="airbus_a319"></a>

### Airbus A319 (Airbus_A319)

| 字段 | 真实值                        | 来源 URL                                                                                         | 游戏内当前值               | 偏差/备注              |
| -- | -------------------------- | ---------------------------------------------------------------------------------------------- | -------------------- | ------------------ |
| 价格 | US$92.3 million（2018）      | <https://www.airbus.com/sites/g/files/jlcbta136/files/2021-07/new-airbus-list-prices-2018.pdf> | (游戏 cost_factor=57)  | 游戏明显偏低             |
| 航程 | 3,750 nmi（6,940 km）最大（带鲨翼） | <https://en.wikipedia.org/wiki/Airbus_A319>                                                    | range_km_est=6765 km | 一致（6,940 vs 6,765） |
| 座级 | 两舱 124（8F+116Y）；最大 156     | <https://en.wikipedia.org/wiki/Airbus_A319>                                                    | passenger=124 人      | 一致                 |
| 巡航 | Mach 0.78（829 km/h）        | <https://en.wikipedia.org/wiki/Airbus_A319>                                                    | speed_kmh=869 km/h   | 略偏高                |

<a id="airbus_a319neo"></a>

### Airbus A319neo (Airbus_A319neo)

| 字段 | 真实值                    | 来源 URL                                                                                                                  | 游戏内当前值               | 偏差/备注              |
| -- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------ |
| 价格 | US$101.5 million（2018） | <https://www.airbus.com/sites/g/files/jlcbta136/files/2021-07/new-airbus-list-prices-2018.pdf>                          | (游戏 cost_factor=95)  | 游戏略偏低              |
| 航程 | 3,700 nmi（6,850 km）    | <https://aircraft.airbus.com/en/aircraft/a320-family/a319neo> + <https://simpleflying.com/tag/airbus-a320neo/-a319neo/> | range_km_est=6952 km | 一致（6,850 vs 6,952） |
| 座级 | 最大 160；两舱 120–150      | <https://aircraft.airbus.com/en/aircraft/a320-family/a319neo>                                                           | passenger=160 人      | 一致（取最大）            |
| 巡航 | Mach 0.78（约 833 km/h）  | <https://aerocorner.com/aircraft/airbus-a319neo>                                                                        | speed_kmh=833 km/h   | 一致                 |

<a id="airbus_a320_100"></a>

### Airbus A320-100 (Airbus_A320_100)

| 字段 | 真实值                                     | 来源 URL                                                                                         | 游戏内当前值               | 偏差/备注                    |
| -- | --------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------- | ------------------------ |
| 价格 | US$30.0 million（1988）                   | <https://simpleflying.com/tag/airbus-a320/-a320/>                                              | (游戏 cost_factor=71)  | 游戏偏高（早期型便宜）              |
| 航程 | 2,600 nmi（4,813 km）（-100 燃油少，航程短于 -200） | <https://simpleflying.com/tag/airbus-a320/-a320/>                                              | range_km_est=5390 km | 游戏偏高（接近 -200 的 5,700 km） |
| 座级 | 最大 150（两舱典型 150）                        | <https://simpleflying.com/tag/airbus-a320/-a320/>                                              | passenger=150 人      | 一致                       |
| 巡航 | Mach 0.78（约 828 km/h）                   | <https://simpleflying.com/tag/airbus-a320/-a320/> + <https://flightq.app/aircraft/airbus-a320> | speed_kmh=902 km/h   | 游戏偏高（902≈M0.85）          |

<a id="airbus_a320_200"></a>

### Airbus A320-200 (Airbus_A320_200)

| 字段 | 真实值                          | 来源 URL                                                              | 游戏内当前值               | 偏差/备注                      |
| -- | ---------------------------- | ------------------------------------------------------------------- | -------------------- | -------------------------- |
| 价格 | US$101.0M（2018 目录价）          | <https://en.wikipedia.org/wiki/Airbus_A320_family>                  | (游戏 cost_factor=73)  | 游戏为相对系数，非 USD              |
| 航程 | 6,100 km（3,300 nmi，典型/150 座） | <https://en.wikipedia.org/wiki/Airbus_A320_family>                  | range_km_est 5610 km | 接近（游戏略低 ~8%）               |
| 座级 | 150 人（两舱）/ 186 人（最大）         | <https://en.wikipedia.org/wiki/Airbus_A320_family>                  | passenger 150 人      | 一致                         |
| 巡航 | 828 km/h（Mach 0.78）          | <https://www.easycharter.co/charter-aircraft-types/airbus-a320-200> | speed_kmh 902 km/h   | 游戏偏高 ~74 km/h（约 Mach 0.85） |

<a id="airbus_a320neo"></a>

### Airbus A320neo (Airbus_A320neo)

| 字段 | 真实值                    | 来源 URL                                                                  | 游戏内当前值               | 偏差/备注     |
| -- | ---------------------- | ----------------------------------------------------------------------- | -------------------- | --------- |
| 价格 | US$110.6M（2018 目录价）    | <https://aerocorner.com/aircraft/airbus-a320neo/>                       | (游戏 cost_factor=101) | —         |
| 航程 | 6,300 km（3,400 nmi，典型） | <https://aerocorner.com/aircraft/airbus-a320neo/>                       | range_km_est 6408 km | 接近        |
| 座级 | 150 人（两舱）/ 194 人（最大）   | <https://accaviation.com/aviation-consultancy/aircraft/airbus-a320neo/> | passenger 165 人      | 游戏取中间值，合理 |
| 巡航 | 828 km/h（Mach 0.78）    | <https://simpleflying.com/how-fast-airbus-a321xlr-fly>                  | speed_kmh 833 km/h   | 基本一致      |

<a id="airbus_a321_100"></a>

### Airbus A321-100 (Airbus_A321_100)

| 字段 | 真实值                             | 来源 URL                                           | 游戏内当前值               | 偏差/备注         |
| -- | ------------------------------- | ------------------------------------------------ | -------------------- | ------------- |
| 价格 | US$50.0M（1994 目录价）              | <https://simpleflying.com/tag/airbus-a320/-a321> | (游戏 cost_factor=84)  | 早期目录价，偏低      |
| 航程 | 4,150 km（2,238 nmi，典型；较 A320 短） | <https://simpleflying.com/tag/airbus-a320/-a321> | range_km_est 4318 km | 接近            |
| 座级 | 185 人（两舱）/ 220 人（最大）            | <https://simpleflying.com/tag/airbus-a320/-a321> | passenger 185 人      | 一致            |
| 巡航 | 828 km/h（Mach 0.78）             | <https://simpleflying.com/tag/airbus-a320/-a321> | speed_kmh 902 km/h   | 游戏偏高 ~74 km/h |

<a id="airbus_a321_200"></a>

### Airbus A321-200 (Airbus_A321_200)

| 字段 | 真实值                           | 来源 URL                                                              | 游戏内当前值               | 偏差/备注         |
| -- | ----------------------------- | ------------------------------------------------------------------- | -------------------- | ------------- |
| 价格 | US$118.3M（2018 目录价）           | <https://en.wikipedia.org/wiki/Airbus_A320_family>                  | (游戏 cost_factor=84)  | —             |
| 航程 | 5,930 km（3,200 nmi，典型）        | <https://demo.aerobook.com/aircraft/a321>                           | range_km_est 4868 km | 游戏偏低 ~18%     |
| 座级 | 185 人（两舱）/ 220 人（最大，单舱可达 236） | <https://planefyi.com/pt/aircraft/airbus-a321-200/>                 | passenger 185 人      | 一致            |
| 巡航 | 828 km/h（Mach 0.78）           | <https://www.easycharter.co/charter-aircraft-types/airbus-a321-200> | speed_kmh 902 km/h   | 游戏偏高 ~74 km/h |

<a id="airbus_a321neo"></a>

### Airbus A321neo (Airbus_A321neo)

| 字段 | 真实值                    | 来源 URL                                                                      | 游戏内当前值               | 偏差/备注 |
| -- | ---------------------- | --------------------------------------------------------------------------- | -------------------- | ----- |
| 价格 | US$129.5M（2023 目录价）    | <https://businessmirror.com.ph/2023/03/02/cebu-pacific-to-lease-more-jets/> | (游戏 cost_factor=108) | —     |
| 航程 | 7,400 km（4,000 nmi，典型） | <https://ukaviation.aero/cebu-pacific-orders-70-airbus-a321neos>            | range_km_est 7398 km | 几乎一致  |
| 座级 | 206 人（两舱）/ 244 人（最大）   | <https://ukaviation.aero/cebu-pacific-orders-70-airbus-a321neos>            | passenger 220 人      | 合理区间  |
| 巡航 | 833 km/h（Mach 0.78）    | <https://simpleflying.com/how-fast-airbus-a321xlr-fly>                      | speed_kmh 833 km/h   | 一致    |

<a id="airbus_a330_200"></a>

### Airbus A330-200 (Airbus_A330_200)

| 字段 | 真实值                     | 来源 URL                                         | 游戏内当前值                | 偏差/备注 |
| -- | ----------------------- | ---------------------------------------------- | --------------------- | ----- |
| 价格 | US$238.5M（2018 目录价）     | <https://en.wikipedia.org/wiki/Airbus_A330>    | (游戏 cost_factor=169)  | —     |
| 航程 | 13,450 km（7,250 nmi，典型） | <https://flightq.app/aircraft/airbus-a330-200> | range_km_est 13282 km | 接近    |
| 座级 | 253 人（三舱典型）/ 406 人（最大）  | <https://en.wikipedia.org/wiki/Airbus_A330>    | passenger 253 人       | 一致    |
| 巡航 | 871 km/h（Mach 0.82）     | <https://aerocompare.org/?p=106>               | speed_kmh 878 km/h    | 接近    |

<a id="airbus_a330_200f"></a>

### Airbus A330-200F (Airbus_A330_200F)

| 字段 | 真实值                         | 来源 URL                                                              | 游戏内当前值               | 偏差/备注  |
| -- | --------------------------- | ------------------------------------------------------------------- | -------------------- | ------ |
| 价格 | US$241.7M（2018 目录价）         | <https://en.wikipedia.org/wiki/Airbus_A330>                         | (游戏 cost_factor=171) | —      |
| 航程 | 7,400 km（4,000 nmi，65 t 载荷） | <https://en.wikipedia.org/wiki/Airbus_A330>                         | range_km_est 7342 km | 几乎一致   |
| 座级 | 0 人（货机，货舱约 70 t）            | <https://en.wikipedia.org/wiki/Airbus_A330>                         | passenger 0 人        | 一致（货机） |
| 巡航 | 871 km/h（Mach 0.82，家族值）     | <https://www.easycharter.co/charter-aircraft-types/airbus-a330-200> | speed_kmh 878 km/h   | 接近     |

<a id="airbus_a330_300"></a>

### Airbus A330-300 (Airbus_A330_300)

| 字段 | 真实值                           | 来源 URL                                      | 游戏内当前值                | 偏差/备注             |
| -- | ----------------------------- | ------------------------------------------- | --------------------- | ----------------- |
| 价格 | US$264.2M（2018 目录价）           | <https://en.wikipedia.org/wiki/Airbus_A330> | (游戏 cost_factor=187)  | —                 |
| 航程 | 11,750 km（6,340 nmi，典型/277 座） | <https://en.wikipedia.org/wiki/Airbus_A330> | range_km_est 10725 km | 游戏偏低 ~9%          |
| 座级 | 277 人（典型）/ 440 人（最大）          | <https://en.wikipedia.org/wiki/Airbus_A330> | passenger 295 人       | 合理区间              |
| 巡航 | 871 km/h（Mach 0.82）           | <https://aerobook.com/aircraft/a330-200>    | speed_kmh 926 km/h    | 游戏偏高（约 Mach 0.87） |

<a id="airbus_a330_900neo"></a>

### Airbus A330-900neo (Airbus_A330_900neo)

| 字段 | 真实值                          | 来源 URL                                                                                                            | 游戏内当前值                | 偏差/备注 |
| -- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------- | ----- |
| 价格 | US$296.4M（2018 目录价）          | <https://skyindustrynews.com/airbus-promotes-cost-effective-alternative-with-competitive-pricing-on-new-aircraft> | (游戏 cost_factor=190)  | —     |
| 航程 | 13,610 km（7,350 nmi，287 座标准） | <https://en.wikipedia.org/wiki/Airbus_A330>                                                                       | range_km_est 13348 km | 接近    |
| 座级 | 287 人（标准配置）                  | <https://en.wikipedia.org/wiki/Airbus_A330>                                                                       | passenger 300 人       | 合理区间  |
| 巡航 | 871 km/h（Mach 0.82）          | <https://aerobook.com/aircraft/a330-200>                                                                          | speed_kmh 926 km/h    | 游戏偏高  |

<a id="airbus_a340_300"></a>

### Airbus A340-300 (Airbus_A340_300)

| 字段 | 真实值                          | 来源 URL                                      | 游戏内当前值                | 偏差/备注         |
| -- | ---------------------------- | ------------------------------------------- | --------------------- | ------------- |
| 价格 | US$110M（1992）/ US$238M（2011） | <https://en.wikipedia.org/wiki/Airbus_A340> | (游戏 cost_factor=200)  | 取较新 2011 价更可比 |
| 航程 | 12,400 km（6,700 nmi，三舱典型）    | <https://en.wikipedia.org/wiki/Airbus_A340> | range_km_est 13558 km | 游戏偏高 ~9%      |
| 座级 | 295 人（三舱典型）                  | <https://en.wikipedia.org/wiki/Airbus_A340> | passenger 295 人       | 一致            |
| 巡航 | 871 km/h（Mach 0.82）          | <https://www.aerobook.com/aircraft/a340>    | speed_kmh 902 km/h    | 游戏略偏高         |

<a id="airbus_a340_500"></a>

### Airbus A340-500 (Airbus_A340_500)

| 字段 | 真实值                          | 来源 URL                                        | 游戏内当前值                | 偏差/备注 |
| -- | ---------------------------- | --------------------------------------------- | --------------------- | ----- |
| 价格 | US$261.8M（2011）              | <https://en.wikipedia.org/wiki/Airbus_A340>   | (游戏 cost_factor=200)  | —     |
| 航程 | 16,670 km（9,000 nmi，超远程 ULR） | <https://en.wikipedia.org/wiki/Airbus_A340>   | range_km_est 16500 km | 几乎一致  |
| 座级 | 313 人（三舱典型）                  | <https://en.wikipedia.org/wiki/Airbus_A340>   | passenger 313 人       | 一致    |
| 巡航 | 871 km/h（Mach 0.82）          | <https://demo.aerobook.com/aircraft/a340-500> | speed_kmh 902 km/h    | 游戏略偏高 |

<a id="airbus_a340_600"></a>

### Airbus A340-600 (Airbus_A340_600)

| 字段 | 真实值                       | 来源 URL                                      | 游戏内当前值                | 偏差/备注    |
| -- | ------------------------- | ------------------------------------------- | --------------------- | -------- |
| 价格 | US$275.4M（2011）           | <https://en.wikipedia.org/wiki/Airbus_A340> | (游戏 cost_factor=231)  | —        |
| 航程 | 13,900 km（7,500 nmi，三舱典型） | <https://en.wikipedia.org/wiki/Airbus_A340> | range_km_est 14492 km | 游戏偏高 ~4% |
| 座级 | 379 人（三舱典型）               | <https://en.wikipedia.org/wiki/Airbus_A340> | passenger 380 人       | 一致       |
| 巡航 | 871 km/h（Mach 0.82）       | <https://www.aerobook.com/aircraft/a340>    | speed_kmh 902 km/h    | 游戏略偏高    |

<a id="airbus_a350_1000"></a>

### Airbus A350-1000 (Airbus_A350_1000)

| 字段 | 真实值                      | 来源 URL                                      | 游戏内当前值                | 偏差/备注         |
| -- | ------------------------ | ------------------------------------------- | --------------------- | ------------- |
| 价格 | US$366.5M（2018 目录价）      | <https://en.wikipedia.org/wiki/Airbus_A350> | (游戏 cost_factor=235)  | —             |
| 航程 | 16,700 km（9,000 nmi，最大）  | <https://en.wikipedia.org/wiki/Airbus_A350> | range_km_est 16225 km | 接近（游戏略低 ~3%）  |
| 座级 | 350–410 人（典型）/ 最大 475    | <https://en.wikipedia.org/wiki/Airbus_A350> | passenger 366 人       | 合理区间          |
| 巡航 | 912 km/h（Mach 0.854，试飞值） | <https://en.wikipedia.org/wiki/Airbus_A350> | speed_kmh 945 km/h    | 游戏偏高 ~33 km/h |

<a id="airbus_a350_900"></a>

### Airbus A350-900 (Airbus_A350_900)

| 字段 | 真实值                     | 来源 URL                                           | 游戏内当前值                | 偏差/备注         |
| -- | ----------------------- | ------------------------------------------------ | --------------------- | ------------- |
| 价格 | US$317.4M（2018 目录价）     | <https://en.wikipedia.org/wiki/Airbus_A350>      | (游戏 cost_factor=220)  | —             |
| 航程 | 15,750 km（8,500 nmi，典型） | <https://en.wikipedia.org/wiki/Airbus_A350>      | range_km_est 14850 km | 游戏偏低 ~6%      |
| 座级 | 325 人（典型）/ 最大 440       | <https://en.wikipedia.org/wiki/Airbus_A350>      | passenger 315 人       | 合理区间          |
| 巡航 | 903 km/h（Mach 0.85）     | <https://simpleflying.com/tag/airbus-a350/-900/> | speed_kmh 945 km/h    | 游戏偏高 ~42 km/h |

<a id="airbus_a380_800"></a>

### Airbus A380-800 (Airbus_A380_800)

| 字段 | 真实值                              | 来源 URL                                      | 游戏内当前值                | 偏差/备注                      |
| -- | -------------------------------- | ------------------------------------------- | --------------------- | -------------------------- |
| 价格 | US$445.6M（2018 目录价）              | <https://en.wikipedia.org/wiki/Airbus_A380> | (游戏 cost_factor=347)  | 本批次最贵，与游戏最高系数一致            |
| 航程 | 15,700 km（8,500 nmi，设计/三舱 525 座） | <https://en.wikipedia.org/wiki/Airbus_A380> | range_km_est 15042 km | 接近                         |
| 座级 | 525 人（三舱典型）/ 853 人（最大全经济）        | <https://en.wikipedia.org/wiki/Airbus_A380> | passenger 652 人       | 游戏取中间值                     |
| 巡航 | 903 km/h（Mach 0.85）              | <https://flightq.app/aircraft/airbus-a380>  | speed_kmh 1023 km/h   | 游戏明显偏高（约 Mach 0.96，接近最大速度） |

---

## 汇总备注

- 价格：游戏 `cost_factor` 为相对系数，已另列真实目录价 USD（年份见上）。A320/A321neo 价取 2018/2023 年 Airbus 目录价；A340 系列取 2011 单位成本更可比。
- 座级：游戏值多取典型/中间布局，与真实两舱/最大区间基本相符；A330-200F 为货机（0 客座）已标注。
- 巡航：真实窄体（A320/A321 全系）约 Mach 0.78（~828–833 km/h）；宽体（A330/A340）约 Mach 0.82（~871 km/h）；A350 约 Mach 0.85（~903–912 km/h）；A380 约 Mach 0.85（~903 km/h）。游戏 `speed_kmh` 对多数机型偏高于真实巡航（更接近最大/高速值），A380 偏差最大。
- 航程：游戏 `range_km_est`（=base_range×5.5）与真实值整体吻合，A321-200 偏低约 18%、A330-300 偏低约 9% 为较明显偏差。

### 安东诺夫 · Antonov

<a id="antonov_an140"></a>

### Antonov An-140 (ANTONOV_AN140)

| 字段 | 真实值                                      | 来源 URL                                                                                            | 游戏内当前值               | 偏差/备注     |
| -- | ---------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------- | --------- |
| 价格 | US$9 million                             | <https://aerocorner.com/aircraft/antonov-an-140/>                                                 | (cost_factor=14)     | 合理（系数偏高些） |
| 航程 | 2,100 km（52 客）；最大商载 900 km；33 客 3,700 km | <https://en.wikipedia.org/wiki/Antonov_An-140>                                                    | range_km_est 2101 km | 高度一致      |
| 座级 | 52（最大）                                   | <https://aerocorner.com/aircraft/antonov-an-140/> ；<https://en.wikipedia.org/wiki/Antonov_An-140> | passenger 52 人       | 一致        |
| 巡航 | 575 km/h（310 kt，最大）；经济 520 km/h          | <https://en.wikipedia.org/wiki/Antonov_An-140>                                                    | speed_kmh 575 km/h   | 完全一致      |

<a id="antonov_an148"></a>

### Antonov An-148 (ANTONOV_AN148)

| 字段 | 真实值                                        | 来源 URL                                                                                            | 游戏内当前值               | 偏差/备注     |
| -- | ------------------------------------------ | ------------------------------------------------------------------------------------------------- | -------------------- | --------- |
| 价格 | US$22M（aerocorner）/ US$24–30M（2009 目录价）    | <https://aerocorner.com/aircraft/antonov-an-148/> ；<https://en.wikipedia.org/wiki/Antonov_An-148> | (cost_factor=50)     | 合理        |
| 航程 | 2,100–4,400 km（典型 2,100；-100E 最大 4,400 km） | <https://en.wikipedia.org/wiki/Antonov_An-148>                                                    | range_km_est 3102 km | 在范围内（取中值） |
| 座级 | 68（两舱）/ 最大 85                              | <https://aerocorner.com/aircraft/antonov-an-148/> ；<https://en.wikipedia.org/wiki/Antonov_An-148> | passenger 80 人       | 在范围内      |
| 巡航 | 800–870 km/h（Mach 0.80≈850 km/h）           | <https://en.wikipedia.org/wiki/Antonov_An-148> ；<https://aerocorner.com/aircraft/antonov-an-148/> | speed_kmh 830 km/h   | 在范围内      |

<a id="antonov_an158"></a>

### Antonov An-158 (ANTONOV_AN158)

| 字段 | 真实值                                    | 来源 URL                                                                                                                                                                                                          | 游戏内当前值               | 偏差/备注        |
| -- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------ |
| 价格 | 约 US$25–30M（2011 基价 US$25M；目录约 US$30M） | <https://aviamuseum.com.ua/en/news/museum-news/1456-april-28-is-the-15th-anniversary-of-the-an-158-regional-airliner> ；<https://www.beyondtheordinary.co.uk/features/antonov-an-158-cubas-unique-passenger-jet> | (cost_factor=65)     | 合理           |
| 航程 | 2,500 km（75 客）；实用 2,600 km             | <https://en.wikipedia.org/wiki/Antonov_An-148> ；<https://aviamuseum.com.ua/en/news/museum-news/1456-april-28-is-the-15th-anniversary-of-the-an-158-regional-airliner>                                           | range_km_est 2800 km | 游戏偏高约 12%    |
| 座级 | 86–99（最大 99）                           | <https://en.wikipedia.org/wiki/Antonov_An-148>                                                                                                                                                                  | passenger 90 人       | 在范围内         |
| 巡航 | 870 km/h（An-158 实用）；家族 800–870 km/h    | <https://aviamuseum.com.ua/en/news/museum-news/1456-april-28-is-the-15th-anniversary-of-the-an-158-regional-airliner> ；<https://en.wikipedia.org/wiki/Antonov_An-148>                                           | speed_kmh 886 km/h   | 游戏略高（约 1.8%） |

<a id="antonov_124"></a>

### Antonov An-124 (Antonov_124)

| 字段 | 真实值                                           | 来源 URL                                                                                                                                   | 游戏内当前值               | 偏差/备注                   |
| -- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------- |
| 价格 | US$70–100 million（历史；商用估计 US$50–90M）          | <https://www.wikiwand.com/sl/articles/An-124> ；<https://www.aircharterservice.co.kr/aircraft-guide/cargo/antonov-ukraine/antonov-an-124> | (cost_factor=274)    | 重型机，系数合理                |
| 航程 | 最大商载(120t) 3,700 km；80t 8,400 km；转场 14,000 km | <https://en.wikipedia.org/wiki/Antonov_An-124>                                                                                           | range_km_est 5912 km | 介于部分商载与转场之间（取 80t 级更接近） |
| 座级 | 0（货运）；上舱 88 客 / 货舱可载 350 人（应急）                | <https://en.wikipedia.org/wiki/Antonov_An-124>                                                                                           | passenger 0 人        | 一致（货机）                  |
| 巡航 | 865 km/h（最大）；典型 800–850 km/h                  | <https://en.wikipedia.org/wiki/Antonov_An-124>                                                                                           | speed_kmh 862 km/h   | 一致                      |

<a id="antonov_225"></a>

### Antonov An-225 (Antonov_225)

| 字段 | 真实值                                            | 来源 URL                                                                                                                                         | 游戏内当前值                | 偏差/备注                |
| -- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | -------------------- |
| 价格 | 估算 US$250–300M（2005 估 US$300M；独特机，2022 被毁，无售价） | <https://simpleflying.com/5-facts-about-antonov-an-225-mriya-largest-aircraft-built> ；<https://www.aircharterchina.cn/aircraft/antonovan-225/> | (cost_factor=274)     | 重型机，系数与 An-124 持平，合理 |
| 航程 | 15,400 km（最大燃油）；200t 商载 4,000 km               | <https://en.wikipedia.org/wiki/Antonov_An-225>                                                                                                 | range_km_est 15235 km | 高度一致（取最大燃油）          |
| 座级 | 0（货运，最大载重 250 t）                               | <https://en.wikipedia.org/wiki/Antonov_An-225>                                                                                                 | passenger 0 人         | 一致（货机）               |
| 巡航 | 800 km/h（430 kt）                               | <https://en.wikipedia.org/wiki/Antonov_An-225>                                                                                                 | speed_kmh 846 km/h    | 游戏略高（约 5.8%）         |

---

## 批次汇总（偏差提示）

- **航程**：ATR 42-300 / ATR 42-300F 游戏值明显偏低（客机约 −38%，货机差更大，因货机实际满油航程高于客机基准）；其余机型基本在 ±15% 内。建议复核 ATR 42-300 系列 base_range。
- **座级**：全部一致或在真实范围内。
- **巡航**：全部在 ±6% 内，基本一致。
- **价格**：多为历史/估算区间，无单一官方目录价时以系列估值或同期同型参考；MA600、Y-7-200 缺可靠目录价，已在单元格标注。
- **货机(300F/200F)**：座级 0 正确；价格按改装估算，航程建议采用对应满油/货载值而非客机最大商载值。

### 英国飞机公司 · BAC

<a id="bac_1_11_200"></a>

### BAC 1-11 200 (BAC_1_11_200)

| 字段 | 真实值                                          | 来源 URL                                         | 游戏内当前值               | 偏差/备注         |
| -- | -------------------------------------------- | ---------------------------------------------- | -------------------- | ------------- |
| 价格 | 未找到可靠来源（无单独200系列目录价；500系列单位成本 US$5.2M, 1972） | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | (游戏 cost_factor=24)  | 200系列无单独公开目录价 |
| 航程 | 1,340 km（830 mi / 720 nmi，典型载荷+2h备用）         | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | range_km_est 1292 km | 接近（游戏略低）      |
| 座级 | 89 人（单级最大；无两舱数据）                             | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | passenger 75 人       | 游戏低于真实最大座级    |
| 巡航 | 882 km/h（476 kn，最大巡航）                        | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | speed_kmh 878 km/h   | 接近            |
|    |                                              |                                                |                      |               |

<a id="bac_1_11_300"></a>

### BAC 1-11 300 (BAC_1_11_300)

| 字段 | 真实值                                        | 来源 URL                                         | 游戏内当前值               | 偏差/备注                      |
| -- | ------------------------------------------ | ---------------------------------------------- | -------------------- | -------------------------- |
| 价格 | 未找到可靠来源（300/400无单独目录价；500系列 US$5.2M, 1972） | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | (游戏 cost_factor=24)  | —                          |
| 航程 | 2,040 km（1,270 mi / 1,100 nmi，典型载荷）        | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | range_km_est 1292 km | 偏差大：游戏显著低估（200/300共用同一航程值） |
| 座级 | 89 人（单级最大）                                 | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | passenger 75 人       | 游戏低于真实最大                   |
| 巡航 | 882 km/h（476 kn）                           | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | speed_kmh 878 km/h   | 接近                         |

<a id="bac_1_11_400"></a>

### BAC 1-11 400 (BAC_1_11_400)

| 字段 | 真实值                                      | 来源 URL                                         | 游戏内当前值               | 偏差/备注                                  |
| -- | ---------------------------------------- | ---------------------------------------------- | -------------------- | -------------------------------------- |
| 价格 | 未找到可靠来源（400系列无单独目录价；500系列 US$5.2M, 1972） | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | (游戏 cost_factor=37)  | 400=300的美式仪表型，价格相近                     |
| 航程 | 2,040 km（1,100 nmi，典型载荷）                 | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | range_km_est 3492 km | 偏差大：游戏高估（实为300/400与200不同，但与500航程也差距明显） |
| 座级 | 89 人（单级最大）                               | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | passenger 89 人       | 一致                                     |
| 巡航 | 882 km/h（476 kn）                         | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | speed_kmh 870 km/h   | 接近                                     |

<a id="bac_1_11_500"></a>

### BAC 1-11 500 (BAC_1_11_500)

| 字段 | 真实值                                 | 来源 URL                                         | 游戏内当前值               | 偏差/备注          |
| -- | ----------------------------------- | ---------------------------------------------- | -------------------- | -------------- |
| 价格 | US$5.2M（1972，500系列单位成本）             | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | (游戏 cost_factor=37)  | 真实USD目录价参考     |
| 航程 | 2,744 km（1,705 mi / 1,482 nmi，典型载荷） | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | range_km_est 3492 km | 偏差：游戏高估约750 km |
| 座级 | 119 人（单级最大）                         | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | passenger 115 人      | 接近（游戏略低）       |
| 巡航 | 871 km/h（470 kn）                    | <https://en.wikipedia.org/wiki/BAC_One-Eleven> | speed_kmh 870 km/h   | 一致             |

<a id="bac_concorde"></a>

### BAC Concorde (BAC_CONCORDE)

| 字段 | 真实值                                         | 来源 URL                                                                                           | 游戏内当前值               | 偏差/备注                                           |
| -- | ------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------- | ----------------------------------------------- |
| 价格 | US$46M（1977，£23M）                           | <https://aerospaceweb.org/aircraft/jetliner/concorde> ; <https://en.wikipedia.org/wiki/Concorde> | (游戏 cost_factor=160) | 真实USD目录价参考                                      |
| 航程 | 6,580 km（3,560 nmi，最大燃油）；另有来源列最大航程 7,250 km | <https://aerospaceweb.org/aircraft/jetliner/concorde> ; <https://en.wikipedia.org/wiki/Concorde> | range_km_est 6765 km | 接近（取6,580~7,250区间）                              |
| 座级 | 100–128 人（典型），最大 144                        | <https://aerospaceweb.org/aircraft/jetliner/concorde> ; <https://en.wikipedia.org/wiki/Concorde> | passenger 100 人      | 游戏取典型下限，一致                                      |
| 巡航 | 2,154 km/h（Mach 2.02；约 Mach×1062）           | <https://en.wikipedia.org/wiki/Concorde>                                                         | speed_kmh 2337 km/h  | 偏差：游戏约按 Mach 2.2（2,337 km/h）折算，高于常规巡航 Mach 2.02 |

### 英宇航 · BAe

<a id="bae_146_100"></a>

### BAe 146-100 (BAe_146_100)

| 字段 | 真实值                                    | 来源 URL                                                | 游戏内当前值               | 偏差/备注          |
| -- | -------------------------------------- | ----------------------------------------------------- | -------------------- | -------------- |
| 价格 | 未找到可靠来源（无-100单独USD目录价；-200为£11M, 1981） | <https://en.wikipedia.org/wiki/British_Aerospace_146> | (游戏 cost_factor=20)  | —              |
| 航程 | 3,870 km（82 pax）                       | <https://en.wikipedia.org/wiki/British_Aerospace_146> | range_km_est 3052 km | 偏差：游戏低估约820 km |
| 座级 | 70–82 人（典型），最大约 82–94                  | <https://en.wikipedia.org/wiki/British_Aerospace_146> | passenger 92 人       | 游戏取高密/上限，偏高    |
| 巡航 | 789 km/h（426 kn，最大巡航；标准747 km/h）       | <https://en.wikipedia.org/wiki/British_Aerospace_146> | speed_kmh 781 km/h   | 接近             |

<a id="bae_146_200"></a>

### BAe 146-200 (BAe_146_200)

| 字段 | 真实值                                  | 来源 URL                                                | 游戏内当前值               | 偏差/备注          |
| -- | ------------------------------------ | ----------------------------------------------------- | -------------------- | -------------- |
| 价格 | £11M（1981，约 US$20M 1981汇率）= -200单位成本 | <https://en.wikipedia.org/wiki/British_Aerospace_146> | (游戏 cost_factor=22)  | 来源币种为英镑，USD为近似 |
| 航程 | 3,650 km（100 pax）                    | <https://en.wikipedia.org/wiki/British_Aerospace_146> | range_km_est 2888 km | 偏差：游戏低估约760 km |
| 座级 | 85–100 人（典型），最大 112                  | <https://en.wikipedia.org/wiki/British_Aerospace_146> | passenger 112 人      | 一致（取最大）        |
| 巡航 | 789 km/h（426 kn）                     | <https://en.wikipedia.org/wiki/British_Aerospace_146> | speed_kmh 781 km/h   | 接近             |

<a id="bae_146_300"></a>

### BAe 146-300 (BAe_146_300)

| 字段 | 真实值                                | 来源 URL                                                | 游戏内当前值               | 偏差/备注          |
| -- | ---------------------------------- | ----------------------------------------------------- | -------------------- | -------------- |
| 价格 | 未找到可靠来源（无-300单独USD目录价）             | <https://en.wikipedia.org/wiki/British_Aerospace_146> | (游戏 cost_factor=24)  | —              |
| 航程 | 3,340 km（100 pax）                  | <https://en.wikipedia.org/wiki/British_Aerospace_146> | range_km_est 2722 km | 偏差：游戏低估约620 km |
| 座级 | 97–112 人（典型）；高密 RJ115 提案达 128（未投产） | <https://en.wikipedia.org/wiki/British_Aerospace_146> | passenger 128 人      | 游戏取高密提案上限，偏高   |
| 巡航 | 789 km/h（426 kn）                   | <https://en.wikipedia.org/wiki/British_Aerospace_146> | speed_kmh 781 km/h   | 接近             |

<a id="bae_146_300qt"></a>

### BAe 146-300QT (BAe_146_300QT)

| 字段 | 真实值                     | 来源 URL                                                | 游戏内当前值               | 偏差/备注                |
| -- | ----------------------- | ----------------------------------------------------- | -------------------- | -------------------- |
| 价格 | 未找到可靠来源（货机无客舱目录价）       | <https://en.wikipedia.org/wiki/British_Aerospace_146> | (游戏 cost_factor=24)  | 货机（Quiet Trader），0客座 |
| 航程 | 约 3,340 km（货机，与-300同机体） | <https://en.wikipedia.org/wiki/British_Aerospace_146> | range_km_est 2722 km | 同-300，游戏低估           |
| 座级 | 0 人（货机）                 | <https://en.wikipedia.org/wiki/British_Aerospace_146> | passenger 0 人        | 一致                   |
| 巡航 | 789 km/h（426 kn）        | <https://en.wikipedia.org/wiki/British_Aerospace_146> | speed_kmh 781 km/h   | 接近                   |

### 波音 · Boeing

<a id="boeing_737max7"></a>

### Boeing 737 MAX 7 (BOEING_737MAX7)

| 字段 | 真实值                           | 来源 URL                                                                                                               | 游戏内当前值               | 偏差/备注                         |
| -- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------- |
| 价格 | $99.7 million（2019）           | <https://aerocorner.com/aircraft/boeing-737-max-7/> （simpleflying 亦列 $99.7m 2022）                                    | (游戏 cost_factor=101) | 现实目录价仅参考；游戏用相对系数              |
| 航程 | 3,800 nmi（约 7,000 km）最大       | <https://en.wikipedia.org/wiki/Boeing_737_MAX> （对比表 3,800 nmi / 7,000 km）                                            | range_km_est 7002 km | 几乎一致；simpleflying 列 3,850 nmi |
| 座级 | 153（两舱典型 8J+145Y）/ 最大 172（单舱） | <https://en.wikipedia.org/wiki/Boeing_737_MAX> （典型 153）；<https://aerocorner.com/aircraft/boeing-737-max-7/> （172 单舱） | passenger 150 人      | 接近两舱典型值                       |
| 巡航 | Mach 0.79（约 839 km/h，453 kn）  | <https://simpleflying.com/tag/boeing-737/max> （MAX 7 巡航 Mach 0.79 ~839 km/h）                                         | speed_kmh 975 km/h   | 游戏值偏高（约 Mach 0.92 量级）         |

注：737 MAX 7 于 2026 年才获 FAA 认证，尚未交付；座级/航程为厂商目标值。

---

<a id="boeing_747sp"></a>

### Boeing 747SP (BOEING_747SP)

| 字段 | 真实值                      | 来源 URL                                                              | 游戏内当前值                | 偏差/备注                                               |
| -- | ------------------------ | ------------------------------------------------------------------- | --------------------- | --------------------------------------------------- |
| 价格 | $24 million（1972）        | <https://aerocorner.com/aircraft/boeing-747sp/>                     | (游戏 cost_factor=265)  | 现实目录价仅参考                                            |
| 航程 | 6,650 nmi（约 12,315 km）最大 | <https://aerocorner.com/aircraft/boeing-747sp/> （航程 6,650 nmi）      | range_km_est 12298 km | 几乎一致（≈6,650 nmi）；维基列 5,830 nmi（10,800 km，276 人三舱载重） |
| 座级 | 331（两舱）/ 最大 400（单舱）      | <https://en.wikipedia.org/wiki/Boeing_747SP> （230 三舱、331 两舱、最大 400） | passenger 320 人       | 接近两舱值                                               |
| 巡航 | 540 kt（约 1,000 km/h）     | <https://aerocorner.com/aircraft/boeing-747sp/> （cruise 540 kn）     | speed_kmh 967 km/h    | 维基列最大 Mach 0.92；典型巡航约 Mach 0.85（~905 km/h）          |

注：aerocorner 概览页 "Seats 276" 为三舱典型载重，非最大布局。

---

<a id="boeing_757_300"></a>

### Boeing 757-300 (BOEING_757_300)

| 字段 | 真实值                     | 来源 URL                                                                                                       | 游戏内当前值               | 偏差/备注     |
| -- | ----------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------- | --------- |
| 价格 | $75 million（2004）       | <https://simpleflying.com/tag/boeing-757/-300/> （List Price $75m 2004；另 aviationstrategy 1999 列 $73.5–81.0m） | (游戏 cost_factor=79)  | 现实目录价仅参考  |
| 航程 | 3,395 nmi（约 6,288 km）最大 | <https://en.wikipedia.org/wiki/Boeing_757> （757-300 最大航程 3,395 nmi / 6,288 km）                               | range_km_est 7002 km | 游戏偏高约 11% |
| 座级 | 243（两舱典型）/ 最大 295       | <https://en.wikipedia.org/wiki/Boeing_757> （典型 243；最大认证 295）                                                 | passenger 243 人      | 完全一致      |
| 巡航 | Mach 0.80（约 858 km/h）   | <https://en.wikipedia.org/wiki/Boeing_757> （全系列巡航 Mach 0.8 / 858 km/h）                                       | speed_kmh 934 km/h   | 游戏偏高      |

---

<a id="boeing_777_8"></a>

### Boeing 777-8 (BOEING_777_8)

| 字段 | 真实值                                     | 来源 URL                                                                                                                                           | 游戏内当前值                | 偏差/备注       |
| -- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- | ----------- |
| 价格 | $394.9 million（2018）                    | <https://247wallst.com/military/2018/01/19/boeing-raises-2018-commercial-jet-prices-by-4-1/> （2018 价目 777-8 $394.9m；simpleflying 列 $442.2m 2022） | (游戏 cost_factor=262)  | 尚未交付；目录价仅参考 |
| 航程 | 9,500 nmi（约 17,590 km）最大 / 8,745 nmi 典型 | <https://en.wikipedia.org/wiki/Boeing_777X> （最大 9,500 nmi；典型 8,745 nmi）                                                                          | range_km_est 16698 km | 接近最大航程      |
| 座级 | 350–425（两舱）/ 典型 395                     | <https://en.wikipedia.org/wiki/Boeing_777X> （两舱 350–425；典型 395）                                                                                  | passenger 365 人       | 接近两舱下限      |
| 巡航 | Mach 0.84（约 905 km/h）                   | <https://flightq.app/aircraft/boeing-777-8> （Mach 0.84 / 905 km/h）；<https://simpleflying.com/tag/boeing-777/-x/>                                 | speed_kmh 951 km/h    | 接近          |

---

<a id="boeing_707_320"></a>

### Boeing 707-320 (Boeing_707_320)

| 字段 | 真实值                             | 来源 URL                                                                                                       | 游戏内当前值                | 偏差/备注               |
| -- | ------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------- | ------------------- |
| 价格 | $5.5 million（1960）              | <https://simpleflying.com/tag/boeing-707/-320/> （List Price $5.5m 1960）                                      | (游戏 cost_factor=38)   | 现实目录价仅参考            |
| 航程 | 3,750 nmi（约 6,940 km，141 人两舱载重） | <https://en.wikipedia.org/wiki/Boeing_707> （对比表 3,750 nmi / 6,940 km）                                        | range_km_est 11275 km | 游戏明显偏高（约 6,090 nmi） |
| 座级 | 约 189 典型 / 对比表列 194 / 最大 202    | <https://en.wikipedia.org/wiki/Boeing_707> （载客 194）；<https://simpleflying.com/tag/boeing-707/-320/> （最大 202） | passenger 189 人       | 一致                  |
| 巡航 | 478–525 kn（约 885–972 km/h）      | <https://en.wikipedia.org/wiki/Boeing_707> （对比表巡航 478–525 kn）                                                | speed_kmh 999 km/h    | 游戏接近上限（约 540 kn）    |

注：simpleflying 707-320 页列航程 3,915 nmi（7,250 km），与维基 3,750 nmi 略有出入；turbojet 型航程受载重影响大。

---

<a id="boeing_707_420"></a>

### Boeing 707-420 (Boeing_707_420)

| 字段 | 真实值                                                           | 来源 URL                                                                                                       | 游戏内当前值                | 偏差/备注                      |
| -- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------- | -------------------------- |
| 价格 | $6.0 million（1960）                                            | <https://simpleflying.com/tag/boeing-707/-420/> （List Price $6.0m 1960）                                      | (游戏 cost_factor=41)   | 比 -320 略高（换装 Conway 涡扇）    |
| 航程 | 4,830 nmi（约 8,950 km）                                         | <https://simpleflying.com/tag/boeing-707/-420/> （Range 4,830 nmi / 8,950 km）                                 | range_km_est 12155 km | 游戏偏高；维基称与 -320 同 3,750 nmi |
| 座级 | 约 189 典型 / 对比表列 194 / 最大 202                                  | <https://en.wikipedia.org/wiki/Boeing_707> （载客 194）；<https://simpleflying.com/tag/boeing-707/-420/> （最大 202） | passenger 189 人       | 一致                         |
| 巡航 | 478–525 kn（约 885–972 km/h；simpleflying 列 Mach 0.8 / 933 km/h） | <https://en.wikipedia.org/wiki/Boeing_707> （对比表 478–525 kn）；<https://simpleflying.com/tag/boeing-707/-420/>  | speed_kmh 991 km/h    | 游戏接近上限                     |

---

<a id="boeing_717_200"></a>

### Boeing 717-200 (Boeing_717_200)

| 字段 | 真实值                        | 来源 URL                                                                                                  | 游戏内当前值               | 偏差/备注     |
| -- | -------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------- | --------- |
| 价格 | $33.08 million（1999）       | <https://www.flyradius.com/boeing-717/200-price> （1999 目录价 $33.08m；aviationstrategy 1999 列 $31.5–35.5m） | (游戏 cost_factor=34)  | 现实目录价仅参考  |
| 航程 | 2,060 nmi（约 3,820 km）设计航程  | <https://en.wikipedia.org/wiki/Boeing_717> （设计航程 2,060 nmi；基本型 1,430 nmi）                               | range_km_est 4785 km | 游戏偏高约 25% |
| 座级 | 106（两舱）/ 117（单舱）/ 最大 134   | <https://en.wikipedia.org/wiki/Boeing_717> （106 两舱 / 117 单舱 / 最大 134）                                   | passenger 117 人      | 等于单舱值     |
| 巡航 | 504 mph（约 811 km/h，438 kn） | <https://en.wikipedia.org/wiki/Boeing_717> （巡航 504 mph / 811 km/h）                                      | speed_kmh 918 km/h   | 游戏偏高      |

---

<a id="boeing_727_100"></a>

### Boeing 727-100 (Boeing_727_100)

| 字段 | 真实值                                           | 来源 URL                                                                                                                 | 游戏内当前值               | 偏差/备注      |
| -- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------- | ---------- |
| 价格 | 约 $4.25 million（1960 年代中期）                    | <https://skyindustrynews.com/delta-retires-last-us-passenger-boeing-727-as-trijet-era-ends> （727 初始目录价约 $4.25m 中期-60s） | (游戏 cost_factor=35)  | 现实目录价仅参考   |
| 航程 | 2,250 nmi（约 4,170 km）两舱                       | <https://en.wikipedia.org/wiki/Boeing_727> （2,250 nmi / 4,170 km，两舱）                                                   | range_km_est 5225 km | 游戏偏高约 25%  |
| 座级 | 106（两舱）/ 125（单舱）                              | <https://en.wikipedia.org/wiki/Boeing_727> （106 两舱 / 125 单舱）                                                           | passenger 131 人      | 游戏略高于单舱最大值 |
| 巡航 | 600 mph（约 960 km/h）/ 495–518 kn（917–959 km/h） | <https://en.wikipedia.org/wiki/Boeing_727> （巡航 600 mph；对比表 495–518 kn）                                                 | speed_kmh 999 km/h   | 游戏接近上限     |

---

<a id="boeing_727_200"></a>

### Boeing 727-200 (Boeing_727_200)

| 字段 | 真实值                           | 来源 URL                                                                            | 游戏内当前值               | 偏差/备注                    |
| -- | ----------------------------- | --------------------------------------------------------------------------------- | -------------------- | ------------------------ |
| 价格 | $6.5 million（1967）            | <https://simpleflying.com/tag/boeing-727/-200/> （List Price $6.5m 1967）           | (游戏 cost_factor=37)  | 现实目录价仅参考（Advanced 型后期更高） |
| 航程 | 2,550 nmi（约 4,720 km）Advanced | <https://en.wikipedia.org/wiki/Boeing_727> （-200 Advanced 2,550 nmi；基型 1,900 nmi） | range_km_est 6352 km | 游戏偏高约 35%                |
| 座级 | 134（两舱）/ 155（单舱）              | <https://en.wikipedia.org/wiki/Boeing_727> （134 两舱 / 155 单舱）                      | passenger 147 人      | 介于两舱与单舱间                 |
| 巡航 | 467–515 kn（约 865–954 km/h）    | <https://en.wikipedia.org/wiki/Boeing_727> （对比表 467–515 kn）                       | speed_kmh 999 km/h   | 游戏接近上限（约 540 kn）         |

---

<a id="boeing_727_200f"></a>

### Boeing 727-200F (Boeing_727_200F)

| 字段 | 真实值                                                      | 来源 URL                                                                                         | 游戏内当前值               | 偏差/备注          |
| -- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------- | -------------- |
| 价格 | 未找到可靠单独来源（货机 1981 年推出；参考 727-200 $6.5m 1967 同机体价，F 型应更高） | <https://simpleflying.com/tag/boeing-727/-200/> （仅 727-200 价）；尝试维基/WebSearch 均无 727-200F 专属目录价 | (游戏 cost_factor=29)  | 货机价无可靠公开来源     |
| 航程 | 2,550 nmi（约 4,720 km）Advanced                            | <https://en.wikipedia.org/wiki/Boeing_727> （继承 -200 Advanced 航程）                               | range_km_est 4978 km | 接近 Advanced 航程 |
| 座级 | 0（货机，无客座）                                                | <https://en.wikipedia.org/wiki/Boeing_727> （windowless cabin 货机）                               | passenger 0 人        | 一致             |
| 巡航 | 467–515 kn（约 865–954 km/h）                               | <https://en.wikipedia.org/wiki/Boeing_727> （同 727-200）                                         | speed_kmh 905 km/h   | 游戏接近上限         |

---

<a id="boeing_737_100"></a>

### Boeing 737-100 (Boeing_737_100)

| 字段 | 真实值                    | 来源 URL                                                                                                | 游戏内当前值               | 偏差/备注     |
| -- | ---------------------- | ----------------------------------------------------------------------------------------------------- | -------------------- | --------- |
| 价格 | $3.6 million（1968）     | <https://en.wikipedia.org/wiki/Boeing_737> （unit cost US$3,600,000 / 1968）                            | (游戏 cost_factor=29)  | 现实目录价仅参考  |
| 航程 | 1,540 nmi（约 2,850 km）  | <https://en.wikipedia.org/wiki/Boeing_737> （对比表 1,540 nmi / 2,850 km）                                 | range_km_est 4702 km | 游戏偏高约 65% |
| 座级 | 118                    | <https://en.wikipedia.org/wiki/Boeing_737> （对比表载客 118）                                                | passenger 85 人       | 游戏偏低      |
| 巡航 | Mach 0.745（约 796 km/h） | <https://simpleflying.com/how-fast-does-a-boeing-737-fly> （Original/Classic 巡航 Mach 0.745 / 796 km/h） | speed_kmh 878 km/h   | 游戏偏高      |

---

<a id="boeing_737_200"></a>

### Boeing 737-200 (Boeing_737_200)

| 字段 | 真实值                    | 来源 URL                                                                                     | 游戏内当前值               | 偏差/备注    |
| -- | ---------------------- | ------------------------------------------------------------------------------------------ | -------------------- | -------- |
| 价格 | $4.0 million（1968）     | <https://en.wikipedia.org/wiki/Boeing_737> （unit cost US$4.0M 1968；另 $5.2M 1972）           | (游戏 cost_factor=29)  | 现实目录价仅参考 |
| 航程 | 2,600 nmi（约 4,800 km）  | <https://en.wikipedia.org/wiki/Boeing_737> （对比表 2,600 nmi / 4,800 km）                      | range_km_est 5198 km | 接近       |
| 座级 | 130                    | <https://en.wikipedia.org/wiki/Boeing_737> （对比表载客 130）                                     | passenger 97 人       | 游戏偏低     |
| 巡航 | Mach 0.745（约 796 km/h） | <https://simpleflying.com/how-fast-does-a-boeing-737-fly> （Original/Classic 巡航 Mach 0.745） | speed_kmh 878 km/h   | 游戏偏高     |

---

<a id="boeing_737_200c"></a>

### Boeing 737-200C (Boeing_737_200C)

| 字段 | 真实值                                         | 来源 URL                                                                                     | 游戏内当前值               | 偏差/备注              |
| -- | ------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------- | ------------------ |
| 价格 | 未找到单独来源；与 737-200 同机体，参考 $4.0 million（1968） | <https://en.wikipedia.org/wiki/Boeing_737> （737-200 价；Combi 无独立目录价）                        | (游戏 cost_factor=37)  | 货客混装（Combi），无专门目录价 |
| 航程 | 约 2,600 nmi（约 4,800 km，同 737-200）           | <https://en.wikipedia.org/wiki/Boeing_737> （737-200 航程）                                    | range_km_est 4648 km | 接近                 |
| 座级 | 0（客货混装 Combi，客座可变；游戏记 0）                    | <https://en.wikipedia.org/wiki/Boeing_737> （200C 为客货转换型）                                   | passenger 0 人        | 一致（纯货配置）           |
| 巡航 | Mach 0.745（约 796 km/h）                      | <https://simpleflying.com/how-fast-does-a-boeing-737-fly> （Original/Classic 巡航 Mach 0.745） | speed_kmh 878 km/h   | 游戏偏高               |

---

<a id="boeing_737_300"></a>

### Boeing 737-300 (Boeing_737_300)

| 字段 | 真实值                   | 来源 URL                                                                                                 | 游戏内当前值               | 偏差/备注     |
| -- | --------------------- | ------------------------------------------------------------------------------------------------------ | -------------------- | --------- |
| 价格 | $32.0 million（1984）   | <https://simpleflying.com/tag/boeing-737/classic/> （737-300 List Price $32.0m 1984）                    | (游戏 cost_factor=29)  | 现实目录价仅参考  |
| 航程 | 2,255 nmi（约 4,175 km） | <https://simpleflying.com/tag/boeing-737/classic/> （737-300 Range 2,255 nmi / 4,175 km）                | range_km_est 4152 km | 几乎一致      |
| 座级 | 149                   | <https://en.wikipedia.org/wiki/Boeing_737> （载客 149）；<https://simpleflying.com/tag/boeing-737/classic/> | passenger 128 人      | 游戏偏低约 14% |
| 巡航 | Mach 0.78（约 828 km/h） | <https://simpleflying.com/tag/boeing-737/classic/> （737-300 巡航 Mach 0.78 / 828 km/h；MMO 0.82）          | speed_kmh 910 km/h   | 游戏偏高      |

---

## 汇总：缺来源字段

- Boeing 727-200F 价格：无可靠单独来源（货机 1981 年推出，公开目录价缺失）。
- Boeing 737-200C 价格：无单独来源（Combi 客货混装，参考 737-200 $4.0m 1968）。    
  共 2 个字段缺可靠专属来源（其余 54 字段均有实际读取 URL）。

## 总体观察

- 航程：737-300、747SP、737 MAX 7、737-200、737-200C 与真实值高度吻合；但 707 系列、727 系列、737-100/200 及 717-200 游戏值普遍偏高 25–65%（老机型游戏里程被放大）。
- 座级：757-300（243）完全一致；多数老机型游戏座级偏低（如 737-100=85 vs 118、737-200=97 vs 130、737-300=128 vs 149）。
- 巡航：游戏 `speed_kmh` 普遍高于真实巡航（多取接近上限/Mmo 量级的数值）。

<a id="boeing_737_300f"></a>

### Boeing 737-300F (Boeing_737_300F)

| 字段 | 真实值                                                        | 来源 URL                                                                                                                                                                     | 游戏内当前值               | 偏差/备注                   |
| -- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------- |
| 价格 | 无官方整机目录价（客改货）。客改货改装费 ≈US$2.5M（IBA/ISTAT）；含购机+改装整机约 US$8–9M | <https://www.airliners.net/forum/viewtopic.php?f=3\&t=1453721> ；<https://www.aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Freight/2013/ISSUE86_FRT.pdf> | (游戏 cost_factor=45)  | 货机，以 737-300 为基型；无整机目录价 |
| 航程 | ≈4,176 km (2,255 nmi) [126 客位，典型]                          | <https://en.wikipedia.org/wiki/Boeing_737_Classic>                                                                                                                         | range_km_est 4648 km | 较接近（游戏略高）               |
| 座级 | 0（全货机）                                                     | —（货机定义）                                                                                                                                                                    | passenger 0 人        | 一致                      |
| 巡航 | ≈828 km/h (Mach 0.78)                                      | <https://simpleflying.com/tag/boeing-737/classic/>                                                                                                                         | speed_kmh 910 km/h   | 游戏偏高（910 vs 真实 ~828）    |

<a id="boeing_737_400"></a>

### Boeing 737-400 (Boeing_737_400)

| 字段 | 真实值                            | 来源 URL                                                                                                 | 游戏内当前值               | 偏差/备注   |
| -- | ------------------------------ | ------------------------------------------------------------------------------------------------------ | -------------------- | ------- |
| 价格 | US$35.0M (1988 目录价)            | <https://simpleflying.com/tag/boeing-737/classic/>                                                     | (游戏 cost_factor=49)  | 历史目录价   |
| 航程 | ≈3,820 km (2,060 nmi) [147 客位] | <https://en.wikipedia.org/wiki/Boeing_737_Classic>                                                     | range_km_est 4152 km | 游戏略高    |
| 座级 | 188 人（最大）；典型 147–168           | <https://en.wikipedia.org/wiki/Boeing_737_Classic> ；<https://simpleflying.com/tag/boeing-737/classic/> | passenger 146 人      | 游戏取典型低端 |
| 巡航 | ≈828 km/h (Mach 0.78)          | <https://simpleflying.com/tag/boeing-737/classic/>                                                     | speed_kmh 918 km/h   | 游戏偏高    |

<a id="boeing_737_500"></a>

### Boeing 737-500 (Boeing_737_500)

| 字段 | 真实值                                          | 来源 URL                                                                                                | 游戏内当前值               | 偏差/备注  |
| -- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------- | ------ |
| 价格 | US$29.5M (1990 目录价)；aerocorner 列 $31M (2020) | <https://simpleflying.com/tag/boeing-737/classic/> ；<https://aerocorner.com/aircraft/boeing-737-500/> | (游戏 cost_factor=53)  | 两源一致量级 |
| 航程 | ≈4,398 km (2,375 nmi) [110 客位]               | <https://en.wikipedia.org/wiki/Boeing_737_Classic>                                                    | range_km_est 4400 km | 几乎一致   |
| 座级 | 132 人（最大）；典型 110–140                         | <https://en.wikipedia.org/wiki/Boeing_737_Classic>                                                    | passenger 108 人      | 游戏偏低   |
| 巡航 | ≈828 km/h (Mach 0.78)                        | <https://simpleflying.com/tag/boeing-737/classic/>                                                    | speed_kmh 910 km/h   | 游戏偏高   |

<a id="boeing_737_600"></a>

### Boeing 737-600 (Boeing_737_600)

| 字段 | 真实值                                      | 来源 URL                                                     | 游戏内当前值               | 偏差/备注         |
| -- | ---------------------------------------- | ---------------------------------------------------------- | -------------------- | ------------- |
| 价格 | US$58.5M (2010)                          | <https://aerocorner.com/aircraft/boeing-737-600/>          | (游戏 cost_factor=53)  | aerocorner 列价 |
| 航程 | ≈5,991 km (3,235 nmi) [110 客位]           | <https://en.wikipedia.org/wiki/Boeing_737_Next_Generation> | range_km_est 5582 km | 游戏略低          |
| 座级 | 130 人（最大）；110 两舱                         | <https://en.wikipedia.org/wiki/Boeing_737_Next_Generation> | passenger 108 人      | 游戏偏低          |
| 巡航 | ≈834 km/h (Mach 0.785；-800 极速 Mach 0.82) | <https://en.wikipedia.org/wiki/Boeing_737_Next_Generation> | speed_kmh 959 km/h   | 游戏明显偏高        |

<a id="boeing_737_700"></a>

### Boeing 737-700 (Boeing_737_700)

| 字段 | 真实值                                 | 来源 URL                                                     | 游戏内当前值               | 偏差/备注      |
| -- | ----------------------------------- | ---------------------------------------------------------- | -------------------- | ---------- |
| 价格 | US$89.1M (2019 目录价)                 | <https://www.knaviation.net/737-vs-a320/>                  | (游戏 cost_factor=64)  | 2019 波音目录价 |
| 航程 | ≈5,570 km (3,010 nmi) [126 客位]      | <https://en.wikipedia.org/wiki/Boeing_737_Next_Generation> | range_km_est 6160 km | 游戏略高       |
| 座级 | 149 人（最大）；126 两舱                    | <https://en.wikipedia.org/wiki/Boeing_737_Next_Generation> | passenger 128 人      | 游戏取两舱附近    |
| 巡航 | ≈834 km/h (Mach 0.785；极速 Mach 0.82) | <https://en.wikipedia.org/wiki/Boeing_737_Next_Generation> | speed_kmh 975 km/h   | 游戏偏高       |

<a id="boeing_737_800"></a>

### Boeing 737-800 (Boeing_737_800)

| 字段 | 真实值                                | 来源 URL                                                     | 游戏内当前值               | 偏差/备注                            |
| -- | ---------------------------------- | ---------------------------------------------------------- | -------------------- | -------------------------------- |
| 价格 | US$106.1M (2019 目录价)               | <https://www.knaviation.net/737-vs-a320/>                  | (游戏 cost_factor=74)  | 2019 波音目录价（aerocorner 误列 $89.2M） |
| 航程 | ≈5,436 km (2,935 nmi) [162 客位]     | <https://en.wikipedia.org/wiki/Boeing_737_Next_Generation> | range_km_est 5610 km | 游戏略高                             |
| 座级 | 189 人（最大）；162 两舱                   | <https://en.wikipedia.org/wiki/Boeing_737_Next_Generation> | passenger 160 人      | 游戏取两舱                            |
| 巡航 | ≈837 km/h (Mach 0.82 max；典型 0.785) | <https://en.wikipedia.org/wiki/Boeing_737_Next_Generation> | speed_kmh 975 km/h   | 游戏偏高                             |

<a id="boeing_737_900"></a>

### Boeing 737-900 (Boeing_737_900)

| 字段 | 真实值                                                          | 来源 URL                                                                                                    | 游戏内当前值               | 偏差/备注         |
| -- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- | -------------------- | ------------- |
| 价格 | 无单独 2019 目录（仅 -900ER 入列）；参考 737-900ER US$112.6M (2019)，基础型略低 | <https://www.knaviation.net/737-vs-a320/> ；<https://aerocorner.com/aircraft/boeing-737-900er/>            | (游戏 cost_factor=77)  | 基础型产量少、无独立目录价 |
| 航程 | ≈5,500 km (2,975 nmi)                                        | <https://www.aviation-center.com.au/contents/en-us/d146.html>                                             | range_km_est 3768 km | 游戏明显偏低        |
| 座级 | 189 人（两舱典型）；最高 ~215–220                                      | <https://www.aviation-center.com.au/contents/en-us/d146.html> ；<https://baike.baidu.com/view/327480.html> | passenger 180 人      | 游戏取两舱         |
| 巡航 | ≈828 km/h (Mach 0.785)                                       | <https://www.aviation-center.com.au/contents/en-us/d146.html>                                             | speed_kmh 975 km/h   | 游戏偏高          |

<a id="boeing_737_900er"></a>

### Boeing 737-900ER (Boeing_737_900ER)

| 字段 | 真实值                    | 来源 URL                                                                                                          | 游戏内当前值               | 偏差/备注 |
| -- | ---------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------- | ----- |
| 价格 | US$112.6M (2019)       | <https://aerocorner.com/aircraft/boeing-737-900er/> ；<https://www.knaviation.net/737-vs-a320/>                  | (游戏 cost_factor=80)  | 两源一致  |
| 航程 | ≈5,925 km (3,200 nmi)  | <https://baike.com/wikiid/8425867783035115666> （737-900ER 段）                                                    | range_km_est 4950 km | 游戏偏低  |
| 座级 | 220 人（最大）；177–180 两舱   | <https://en.wikipedia.org/wiki/Boeing_737_Next_Generation> ；<https://aerocorner.com/aircraft/boeing-737-900er/> | passenger 180 人      | 游戏取两舱 |
| 巡航 | ≈840 km/h (Mach 0.785) | <https://en.wikipedia.org/wiki/Boeing_737_Next_Generation>                                                      | speed_kmh 975 km/h   | 游戏偏高  |

<a id="boeing_737_max10"></a>

### Boeing 737 MAX 10 (Boeing_737_MAX10)

| 字段 | 真实值                        | 来源 URL                                                                                          | 游戏内当前值               | 偏差/备注 |
| -- | -------------------------- | ----------------------------------------------------------------------------------------------- | -------------------- | ----- |
| 价格 | US$134.9M (2019)           | <https://aerocorner.com/aircraft/boeing-737-max-10/> ；<https://www.knaviation.net/737-vs-a320/> | (游戏 cost_factor=112) | 两源一致  |
| 航程 | ≈5,700 km (3,100 nmi) [典型] | <https://en.wikipedia.org/wiki/Boeing_737_MAX>                                                  | range_km_est 5742 km | 接近    |
| 座级 | 230 人（最大）；204 两舱           | <https://en.wikipedia.org/wiki/Boeing_737_MAX>                                                  | passenger 195 人      | 游戏取两舱 |
| 巡航 | ≈842 km/h (Mach 0.79)      | <https://aerocorner.com/aircraft/boeing-737-max-10/> （家族 Mach 0.79）                             | speed_kmh 975 km/h   | 游戏偏高  |

<a id="boeing_737_max8"></a>

### Boeing 737 MAX 8 (Boeing_737_MAX8)

| 字段 | 真实值                        | 来源 URL                                                                                         | 游戏内当前值               | 偏差/备注        |
| -- | -------------------------- | ---------------------------------------------------------------------------------------------- | -------------------- | ------------ |
| 价格 | US$121.6M (2019)           | <https://aerocorner.com/aircraft/boeing-737-max-8/> ；<https://www.knaviation.net/737-vs-a320/> | (游戏 cost_factor=101) | 两源一致         |
| 航程 | ≈6,500 km (3,500 nmi) [典型] | <https://en.wikipedia.org/wiki/Boeing_737_MAX>                                                 | range_km_est 6628 km | 接近           |
| 座级 | 189 人（最大）；178 两舱           | <https://en.wikipedia.org/wiki/Boeing_737_MAX>                                                 | passenger 162 人      | 游戏偏低（取两舱偏低端） |
| 巡航 | ≈842 km/h (Mach 0.79)      | <https://aerocorner.com/aircraft/boeing-737-max-8/> （家族 Mach 0.79）                             | speed_kmh 975 km/h   | 游戏偏高         |

<a id="boeing_737_max9"></a>

### Boeing 737 MAX 9 (Boeing_737_MAX9)

| 字段 | 真实值                        | 来源 URL                                                                                         | 游戏内当前值               | 偏差/备注 |
| -- | -------------------------- | ---------------------------------------------------------------------------------------------- | -------------------- | ----- |
| 价格 | US$128.9M (2019)           | <https://aerocorner.com/aircraft/boeing-737-max-9/> ；<https://www.knaviation.net/737-vs-a320/> | (游戏 cost_factor=106) | 两源一致  |
| 航程 | ≈6,100 km (3,300 nmi) [典型] | <https://en.wikipedia.org/wiki/Boeing_737_MAX>                                                 | range_km_est 6518 km | 接近    |
| 座级 | 220 人（最大）；193 两舱           | <https://en.wikipedia.org/wiki/Boeing_737_MAX>                                                 | passenger 178 人      | 游戏偏低  |
| 巡航 | ≈842 km/h (Mach 0.79)      | <https://aerocorner.com/aircraft/boeing-737-max-9/> （家族 Mach 0.79）                             | speed_kmh 975 km/h   | 游戏偏高  |

<a id="boeing_747_100"></a>

### Boeing 747-100 (Boeing_747_100)

| 字段 | 真实值                                   | 来源 URL                                                                                        | 游戏内当前值               | 偏差/备注             |
| -- | ------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------- | ----------------- |
| 价格 | US$146.7M (2019 目录价)；历史 US$24M (1972) | <https://aerocorner.com/aircraft/boeing-747-100/> ；<https://en.wikipedia.org/wiki/Boeing_747> | (游戏 cost_factor=276) | 2019 目录价 vs 历史出厂价 |
| 航程 | ≈9,800 km (5,300 nmi) [设计典型]          | <https://en.wikipedia.org/wiki/Boeing_747>                                                    | range_km_est 9158 km | 游戏略低              |
| 座级 | 366 人（三舱典型）                           | <https://en.wikipedia.org/wiki/Boeing_747>                                                    | passenger 366 人      | 一致                |
| 巡航 | ≈900 km/h (Mach 0.85)                 | <https://en.wikipedia.org/wiki/Boeing_747>                                                    | speed_kmh 967 km/h   | 游戏略高              |

<a id="boeing_747_200"></a>

### Boeing 747-200 (Boeing_747_200)

| 字段 | 真实值                                             | 来源 URL                                                                                        | 游戏内当前值                | 偏差/备注          |
| -- | ----------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------- | -------------- |
| 价格 | US$39M (1976)                                   | <https://aerocorner.com/aircraft/boeing-747-200/> ；<https://en.wikipedia.org/wiki/Boeing_747> | (游戏 cost_factor=265)  | 两源一致           |
| 航程 | ≈12,150 km (6,560 nmi) [最大；-200B 典型 ~11,000 km] | <https://en.wikipedia.org/wiki/Boeing_747>                                                    | range_km_est 11000 km | 游戏取 -200B 典型量级 |
| 座级 | 366 人（三舱典型）                                     | <https://en.wikipedia.org/wiki/Boeing_747>                                                    | passenger 366 人       | 一致             |
| 巡航 | ≈900 km/h (Mach 0.85)                           | <https://en.wikipedia.org/wiki/Boeing_747>                                                    | speed_kmh 967 km/h    | 游戏略高           |

<a id="boeing_747_200m"></a>

### Boeing 747-200M (Boeing_747_200M)

| 字段 | 真实值                                     | 来源 URL                                            | 游戏内当前值                | 偏差/备注                  |
| -- | --------------------------------------- | ------------------------------------------------- | --------------------- | ---------------------- |
| 价格 | ≈US$39M (1976，与 -200 共用基价；combi 无单独目录价) | <https://aerocorner.com/aircraft/boeing-747-200/> | (游戏 cost_factor=265)  | aerocorner 无独立 -200M 页 |
| 航程 | ≈12,150 km (6,560 nmi) [最大，同 -200]      | <https://en.wikipedia.org/wiki/Boeing_747>        | range_km_est 11000 km | 游戏取典型量级                |
| 座级 | up to 238 人（三舱）+ 主货舱                    | <https://en.wikipedia.org/wiki/Boeing_747>        | passenger 258 人       | 游戏偏高（取混合载客布局）          |
| 巡航 | ≈900 km/h (Mach 0.85)                   | <https://en.wikipedia.org/wiki/Boeing_747>        | speed_kmh 967 km/h    | 游戏略高                   |

---

## 汇总观察

- **价格**：737 Classic 用历史目录价（300/400/500 约 US$29.5–35M），NG/MAX 用 2019 波音目录价（knaviation/aerocorner 一致）；747 用 1976/2019 目录价。游戏 cost_factor 为相对系数，量级顺序大致合理。
- **航程**：NG/MAX/747 批次游戏值与实际接近；**737-900 / 737-900ER 游戏航程明显偏低**（约 3,800–4,950 km vs 真实 5,500–5,925 km）。
- **座级**：游戏多取"两舱典型"偏低端，与真实两舱值基本吻合；747-200M 游戏 258 高于维基所述 238（combi 混合布局差异）。
- **巡航**：游戏 speed_kmh 系统性偏高（737 系列多在 910–975 km/h，而真实典型巡航约 828–842 km/h，极速 Mach 0.82≈880 km/h）。建议后续校准。
- **缺失/说明**：737-300F、737-900 无标准整机目录价，已注明；aerocorner 737-800 页"526 seats"为明显错误，已弃用。

<a id="boeing_747_300"></a>

### Boeing 747-300 (Boeing_747_300)

| 字段 | 真实值                                    | 来源 URL                                                                                                                     | 游戏内当前值                 | 偏差/备注                     |
| -- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------- |
| 价格 | US$83 million (1982)                   | <https://aerocorner.com/aircraft/boeing-747-300/>                                                                          | (游戏 cost_factor=274)   | 合理                        |
| 航程 | 11,720 km (6,330 nmi)                  | <https://aerocorner.com/aircraft/boeing-747-300/> （barrieaircraft: 11,675 km/6,300 nmi；liquisearch 最高 12,400 km/6,700 nmi） | range_km_est 12,292 km | 真实 11,720 vs 游戏 12,292，接近 |
| 座级 | 412 人(三级典型) / 496 人(两级) / 最高 524 人(单级) | <https://www.liquisearch.com/boeing_747/specifications> （aerocorner 列 496）                                                 | passenger 412 人        | 三级 412 与游戏吻合              |
| 巡航 | ~905 km/h (Mach 0.85, ~490 kt)         | <https://en.wikipedia.org/wiki/Boeing_747> （barrieaircraft 经济巡航 907 km/h）                                                  | speed_kmh 999 km/h     | 游戏偏高，接近最大速度(~939 km/h)    |

<a id="boeing_747_300m"></a>

### Boeing 747-300M (Boeing_747_300M)

| 字段 | 真实值                                         | 来源 URL                                                                                      | 游戏内当前值                 | 偏差/备注                     |
| -- | ------------------------------------------- | ------------------------------------------------------------------------------------------- | ---------------------- | ------------------------- |
| 价格 | 未找到可靠来源（客货混装型无独立目录价；参照 747-300 约 US$50–83M） | <https://accaviation.com/aviation-consultancy/sell-buy-boeing-747-200b-300-lcf-dreamlifter> | (游戏 cost_factor=274)   | 混装型无单独目录价                 |
| 航程 | 12,400 km (6,700 nmi)                       | <https://baike.baidu.com/item/%E6%B3%A2%E9%9F%B3747-300Combi>                               | range_km_est 11,908 km | 真实 12,400 vs 游戏 11,908，接近 |
| 座级 | 全客典型 366 人(三级)；混装态约 245–266 人 + 主舱货盘        | <https://baike.baidu.com/item/%E6%B3%A2%E9%9F%B3747-300Combi> （airliners.net combi 约 266 人） | passenger 245 人        | 混装座级 245 与真实混装态一致         |
| 巡航 | Mach 0.85 (~905 km/h, ~490 kt)              | <https://baike.baidu.com/item/%E6%B3%A2%E9%9F%B3747-300Combi>                               | speed_kmh 999 km/h     | 游戏偏高                      |

<a id="boeing_747_400"></a>

### Boeing 747-400 (Boeing_747_400)

| 字段 | 真实值                           | 来源 URL                                                                     | 游戏内当前值                 | 偏差/备注        |
| -- | ----------------------------- | -------------------------------------------------------------------------- | ---------------------- | ------------ |
| 价格 | US$266.5 million (2007)       | <https://aerocorner.com/aircraft/boeing-747-400/>                          | (游戏 cost_factor=297)   | 合理           |
| 航程 | 13,450 km (7,260 nmi)         | <https://en.wikipedia.org/wiki/Boeing_747-400> （planefyi / liquisearch 同值） | range_km_est 13,310 km | 高度吻合         |
| 座级 | 416 人(三级典型) / 524 人(两级最高)     | <https://en.wikipedia.org/wiki/Boeing_747-400> （stands.aero 同值）            | passenger 416 人        | 吻合           |
| 巡航 | 910 km/h (Mach 0.855, 491 kt) | <https://en.wikipedia.org/wiki/Boeing_747-400>                             | speed_kmh 991 km/h     | 游戏偏高（接近最大速度） |

<a id="boeing_747_400bcf"></a>

### Boeing 747-400BCF (Boeing_747_400BCF)

| 字段 | 真实值                                           | 来源 URL                                                           | 游戏内当前值                | 偏差/备注                                       |
| -- | --------------------------------------------- | ---------------------------------------------------------------- | --------------------- | ------------------------------------------- |
| 价格 | 未找到可靠来源（客改货，无独立目录价）                           | <https://en.wikipedia.org/wiki/Boeing_747-400> （BCF 为客改货，无单独公布价） | (游戏 cost_factor=187)  | 改装货机无目录价                                    |
| 航程 | ≈8,250 km (4,455 nmi)（近似 747-400F；BCF 无独立公布值） | <https://en.wikipedia.org/wiki/Boeing_747-400> （取 747-400F 值）    | range_km_est 7,508 km | 游戏航程偏短（真实约 8,250 km）；BCF 仅侧货门、无鼻门，航程略短于新造 F |
| 座级 | 0 人(全货)；主货舱约 30 货板                            | <https://en.wikipedia.org/wiki/Boeing_747-400>                   | passenger 0 人         | 吻合                                          |
| 巡航 | 910 km/h (Mach 0.855, 491 kt)                 | <https://en.wikipedia.org/wiki/Boeing_747-400>                   | speed_kmh 991 km/h    | 游戏偏高                                        |

<a id="boeing_747_400d"></a>

### Boeing 747-400D (Boeing_747_400D)

| 字段 | 真实值                                         | 来源 URL                                                    | 游戏内当前值                | 偏差/备注                                          |
| -- | ------------------------------------------- | --------------------------------------------------------- | --------------------- | ---------------------------------------------- |
| 价格 | 未找到可靠来源（日本国内型，无独立目录价；参照 747-400 ~US$266.5M） | <https://aerocorner.com/aircraft/boeing-747-400/>         | (游戏 cost_factor=274)  | 国内型无单独目录价                                      |
| 航程 | 10,000 km (5,556 nmi)                       | <https://baike.baidu.com/view/327402.htm> （newton 镜像同值）   | range_km_est 3,300 km | ⚠ 游戏 3,300 km 严重不足（真实 10,000 km；D 为短程国内型但远超此值） |
| 座级 | 568 人(高密度两级)                                | <https://en.wikipedia.org/wiki/Boeing_747-400> （baike 同值） | passenger 560 人       | 吻合                                             |
| 巡航 | 957 km/h (Mach 0.85, 487 kt)                | <https://baike.baidu.com/view/327402.htm>                 | speed_kmh 991 km/h    | 游戏偏高                                           |

<a id="boeing_747_400er"></a>

### Boeing 747-400ER (Boeing_747_400ER)

| 字段 | 真实值                           | 来源 URL                                         | 游戏内当前值                 | 偏差/备注        |
| -- | ----------------------------- | ---------------------------------------------- | ---------------------- | ------------ |
| 价格 | 未找到可靠来源                       | <https://en.wikipedia.org/wiki/Boeing_747-400> | (游戏 cost_factor=298)   | 无单独目录价来源     |
| 航程 | 14,045 km (7,585 nmi)         | <https://en.wikipedia.org/wiki/Boeing_747-400> | range_km_est 14,052 km | 极吻合          |
| 座级 | 416 人(三级) / 524 人(两级)         | <https://en.wikipedia.org/wiki/Boeing_747-400> | passenger 524 人        | 两级 524 与游戏吻合 |
| 巡航 | 899 km/h (Mach 0.845, 485 kt) | <https://en.wikipedia.org/wiki/Boeing_747-400> | speed_kmh 991 km/h     | 游戏偏高         |

<a id="boeing_747_400erf"></a>

### Boeing 747-400ERF (Boeing_747_400ERF)

| 字段 | 真实值                                  | 来源 URL                                         | 游戏内当前值                | 偏差/备注    |
| -- | ------------------------------------ | ---------------------------------------------- | --------------------- | -------- |
| 价格 | 未找到可靠来源                              | <https://en.wikipedia.org/wiki/Boeing_747-400> | (游戏 cost_factor=311)  | 无单独目录价来源 |
| 航程 | 9,230 km (4,985 nmi)                 | <https://en.wikipedia.org/wiki/Boeing_747-400> | range_km_est 9,102 km | 吻合       |
| 座级 | 0 人(全货)；最大业载 248,600 lb (112,760 kg) | <https://en.wikipedia.org/wiki/Boeing_747-400> | passenger 0 人         | 吻合       |
| 巡航 | 899 km/h (Mach 0.845, 485 kt)        | <https://en.wikipedia.org/wiki/Boeing_747-400> | speed_kmh 991 km/h    | 游戏偏高     |

<a id="boeing_747_400m"></a>

### Boeing 747-400M (Boeing_747_400M)

| 字段 | 真实值                                  | 来源 URL                                                        | 游戏内当前值                 | 偏差/备注      |
| -- | ------------------------------------ | ------------------------------------------------------------- | ---------------------- | ---------- |
| 价格 | 未找到可靠来源                              | <https://en.wikipedia.org/wiki/Boeing_747-400>                | (游戏 cost_factor=293)   | 客货混装无单独目录价 |
| 航程 | 13,450 km (7,260 nmi)                | <https://baike.baidu.com/view/327425.htm> （747-400M 同值）       | range_km_est 13,200 km | 吻合         |
| 座级 | 混装典型 266 人(三级) + 主舱 6–7 货盘（全客 413 人） | <https://www.airliners.net/info/stats.main?id=100> （baidu 同值） | passenger 266 人        | 吻合         |
| 巡航 | 957 km/h (Mach 0.85, 487 kt)         | <https://baike.baidu.com/view/327425.htm>                     | speed_kmh 991 km/h     | 游戏偏高       |

<a id="boeing_747_400scd"></a>

### Boeing 747-400SCD (Boeing_747_400SCD)

| 字段 | 真实值                                            | 来源 URL                                               | 游戏内当前值                | 偏差/备注                           |
| -- | ---------------------------------------------- | ---------------------------------------------------- | --------------------- | ------------------------------- |
| 价格 | 未找到可靠来源（客改组合货 deck，无独立目录价）                     | <https://sprinkle.com/aircraft/PH-BFW> （747 406 SCD） | (游戏 cost_factor=291)  | 改装组合货 deck 无目录价                 |
| 航程 | 13,440 km (7,260 nmi)                          | <https://sprinkle.com/aircraft/PH-BFW> （747 406 SCD） | range_km_est 8,140 km | ⚠ 游戏 8,140 km 偏短（真实约 13,440 km） |
| 座级 | 组合货 deck 型，可载客（典型约 266–450 人）或全货；游戏记 0 客(纯货配置) | <https://sprinkle.com/aircraft/PH-BFW> （Seats 450）   | passenger 0 人         | SCD 为可载货/客的组合 deck；游戏按纯货记 0     |
| 巡航 | 911 km/h (492 kt, Mach ~0.85)                  | <https://sprinkle.com/aircraft/PH-BFW>               | speed_kmh 991 km/h    | 游戏偏高                            |

<a id="boeing_747_8f"></a>

### Boeing 747-8F (Boeing_747_8F)

| 字段 | 真实值                           | 来源 URL                                       | 游戏内当前值                | 偏差/备注 |
| -- | ----------------------------- | -------------------------------------------- | --------------------- | ----- |
| 价格 | US$419.2 million (2019)       | <https://en.wikipedia.org/wiki/Boeing_747-8> | (游戏 cost_factor=322)  | 合理    |
| 航程 | 8,130 km (4,390 nmi, 最大业载)    | <https://en.wikipedia.org/wiki/Boeing_747-8> | range_km_est 8,195 km | 吻合    |
| 座级 | 0 人(全货)；业载 308,000 lb (140 t) | <https://en.wikipedia.org/wiki/Boeing_747-8> | passenger 0 人         | 吻合    |
| 巡航 | 898 km/h (Mach 0.845, 485 kt) | <https://en.wikipedia.org/wiki/Boeing_747-8> | speed_kmh 1007 km/h   | 游戏偏高  |

<a id="boeing_747_8i"></a>

### Boeing 747-8I (Boeing_747_8I)

| 字段 | 真实值                             | 来源 URL                                       | 游戏内当前值                 | 偏差/备注                 |
| -- | ------------------------------- | -------------------------------------------- | ---------------------- | --------------------- |
| 价格 | US$418.4 million (2019)         | <https://en.wikipedia.org/wiki/Boeing_747-8> | (游戏 cost_factor=321)   | 合理                    |
| 航程 | 15,000 km (8,000 nmi, 三级 467 人) | <https://en.wikipedia.org/wiki/Boeing_747-8> | range_km_est 14,658 km | 接近（真实 15,000 km）      |
| 座级 | 467 人(三级典型)                     | <https://en.wikipedia.org/wiki/Boeing_747-8> | passenger 467 人        | 吻合                    |
| 巡航 | 908 km/h (Mach 0.855, 490 kt)   | <https://en.wikipedia.org/wiki/Boeing_747-8> | speed_kmh 1007 km/h    | 游戏偏高（接近最大速度 Mach 0.9） |

<a id="boeing_757_200"></a>

### Boeing 757-200 (Boeing_757_200)

| 字段 | 真实值                                                   | 来源 URL                                            | 游戏内当前值                | 偏差/备注 |
| -- | ----------------------------------------------------- | ------------------------------------------------- | --------------------- | ----- |
| 价格 | US$65 million (2002)                                  | <https://aerocorner.com/aircraft/boeing-757-200/> | (游戏 cost_factor=79)   | 合理    |
| 航程 | 7,130 km (3,850 nmi, 满载) / 7,250 km (3,915 nmi, 两级典型) | <https://en.wikipedia.org/wiki/Boeing_757>        | range_km_est 7,508 km | 接近    |
| 座级 | 200 人(两级典型) / 最高 239 人                                | <https://en.wikipedia.org/wiki/Boeing_757>        | passenger 200 人       | 吻合    |
| 巡航 | 858 km/h (Mach 0.8, ~463 kt)                          | <https://en.wikipedia.org/wiki/Boeing_757>        | speed_kmh 934 km/h    | 游戏偏高  |

<a id="boeing_757_200f"></a>

### Boeing 757-200F (Boeing_757_200F)

| 字段 | 真实值                          | 来源 URL                                                                            | 游戏内当前值                | 偏差/备注       |
| -- | ---------------------------- | --------------------------------------------------------------------------------- | --------------------- | ----------- |
| 价格 | US$60 million                | <https://www.deagel.com/Airliners/Boeing-757-200F_a000203002.aspx> （Unitary Cost） | (游戏 cost_factor=82)   | 二级市场来源，合理量级 |
| 航程 | 5,830 km (3,150 nmi, 满载)     | <https://en.wikipedia.org/wiki/Boeing_757>                                        | range_km_est 5,775 km | 极吻合         |
| 座级 | 0 人(全货)；最大业载 39,800 kg       | <https://en.wikipedia.org/wiki/Boeing_757>                                        | passenger 0 人         | 吻合          |
| 巡航 | 858 km/h (Mach 0.8, ~463 kt) | <https://en.wikipedia.org/wiki/Boeing_757>                                        | speed_kmh 934 km/h    | 游戏偏高        |

<a id="boeing_767_200"></a>

### Boeing 767-200 (Boeing_767_200)

| 字段 | 真实值                                                 | 来源 URL                                                                                                             | 游戏内当前值                | 偏差/备注                                   |
| -- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | --------------------- | --------------------------------------- |
| 价格 | US$160.2 million                                    | <https://aerocorner.com/aircraft/boeing-767-200/> （未标注年份；Wikipedia 仅列 767-200ER 同价 US$160.2M，基型原始目录价约 US$45M/1982） | (游戏 cost_factor=127)  | aerocorner 列价偏高（疑似等效/ER 价）；基型原始约 US$45M |
| 航程 | 7,200 km (3,900 nmi, 典型) / 7,130 km (3,850 nmi, 设计) | <https://en.wikipedia.org/wiki/Boeing_767>                                                                         | range_km_est 7,068 km | 吻合                                      |
| 座级 | 216 人(两级典型) / 最高 255–290 人                          | <https://en.wikipedia.org/wiki/Boeing_767>                                                                         | passenger 181 人       | ⚠ 游戏 181 偏低（真实典型 216）                   |
| 巡航 | 858 km/h (Mach 0.8, ~463 kt)                        | <https://en.wikipedia.org/wiki/Boeing_767>                                                                         | speed_kmh 910 km/h    | 游戏偏高（接近最大速度 ~893 km/h）                  |

---

## 汇总备注

- 座级（passenger）：747-400/400ER/400M/8I/757-200/757-200F 与游戏高度吻合；747-400D(560)与 747-300M(245)/400M(266) 混装/国内型也合理。
- 航程（range_km_est）：多数吻合或接近；⚠ 747-400D（游戏 3,300 vs 真实 10,000 km）与 747-400SCD（游戏 8,140 vs 真实 13,440 km）明显偏短，建议校正。747-400BCF 真实约 8,250 km 亦高于游戏 7,508 km。
- 巡航（speed_kmh）：全部机型游戏值均高于真实典型巡航约 8–12%（多为接近最大速度取值），属系统性偏差，非单架问题。
- 价格字段：客改货（BCF/SCD）、客货混装（300M/400M）、国内型（400D）及 400ER/ERF 无独立可靠目录价来源，已标"未找到可靠来源"。

<a id="boeing_767_200er"></a>

### Boeing 767-200ER (Boeing_767_200ER)

| 字段 | 真实值                                                      | 来源 URL                                     | 游戏内当前值                | 偏差/备注                           |
| -- | -------------------------------------------------------- | ------------------------------------------ | --------------------- | ------------------------------- |
| 价格 | 未列入 2019 目录（已停产）；历史单位成本约 US$144M（维基 zh 单位成本 US$1.441 亿）  | <https://en.wikipedia.org/wiki/Boeing_767> | (游戏 cost_factor=131)  | 2019 目录只列 300ER/300F；base 型早已停产 |
| 航程 | 典型 12,200 km (6,590 nmi) @181 人；最大 11,825 km (6,385 nmi) | <https://en.wikipedia.org/wiki/Boeing_767> | range_km_est 13475 km | 游戏偏高约 10%（取最大值口径）               |
| 座级 | 181 人（典型/两舱）；最大约 255                                     | <https://en.wikipedia.org/wiki/Boeing_767> | passenger 181 人       | 匹配                              |
| 巡航 | Mach 0.80（约 858 km/h）                                    | <https://en.wikipedia.org/wiki/Boeing_767> | speed_kmh 910 km/h    | 游戏偏高约 6%                        |

<a id="boeing_767_300"></a>

### Boeing 767-300 (Boeing_767_300)

| 字段 | 真实值                                                                              | 来源 URL                                            | 游戏内当前值               | 偏差/备注    |
| -- | -------------------------------------------------------------------------------- | ------------------------------------------------- | -------------------- | -------- |
| 价格 | US$217.9M（2019，aerocorner 标注；2019 波音目录仅列 300ER，base -300 二手/历史更低，标注可能与 300ER 混淆） | <https://aerocorner.com/aircraft/boeing-767-300/> | (游戏 cost_factor=148) | 口径需谨慎    |
| 航程 | 7,200 km (3,900 nmi)（典型）                                                         | <https://en.wikipedia.org/wiki/Boeing_767>        | range_km_est 7810 km | 游戏偏高约 8% |
| 座级 | 269 人（典型）；最大 351                                                                 | <https://en.wikipedia.org/wiki/Boeing_767>        | passenger 269 人      | 匹配（典型）   |
| 巡航 | Mach 0.80（约 858 km/h）                                                            | <https://en.wikipedia.org/wiki/Boeing_767>        | speed_kmh 910 km/h   | 游戏偏高约 6% |

<a id="boeing_767_300er"></a>

### Boeing 767-300ER (Boeing_767_300ER)

| 字段 | 真实值                       | 来源 URL                                     | 游戏内当前值                | 偏差/备注          |
| -- | ------------------------- | ------------------------------------------ | --------------------- | -------------- |
| 价格 | US$217.9M（2019 单位成本）      | <https://en.wikipedia.org/wiki/Boeing_767> | (游戏 cost_factor=155)  | 与 767-300 同源口径 |
| 航程 | 11,070 km (5,980 nmi)（典型） | <https://en.wikipedia.org/wiki/Boeing_767> | range_km_est 10972 km | 几乎一致           |
| 座级 | 218 人（典型）；最大 351          | <https://en.wikipedia.org/wiki/Boeing_767> | passenger 218 人       | 匹配（典型）         |
| 巡航 | Mach 0.80（约 858 km/h）     | <https://en.wikipedia.org/wiki/Boeing_767> | speed_kmh 910 km/h    | 游戏偏高约 6%       |

<a id="boeing_767_300f"></a>

### Boeing 767-300F (Boeing_767_300F)

| 字段 | 真实值                                 | 来源 URL                                     | 游戏内当前值               | 偏差/备注    |
| -- | ----------------------------------- | ------------------------------------------ | -------------------- | -------- |
| 价格 | US$220.3M（2019）；2019 波音目录 US$212.2M | <https://en.wikipedia.org/wiki/Boeing_767> | (游戏 cost_factor=152) | 货机       |
| 航程 | 6,025 km (3,225 nmi)（最大载荷航程，货机）     | <https://en.wikipedia.org/wiki/Boeing_767> | range_km_est 5968 km | 几乎一致     |
| 座级 | 货机（0 乘客）；24 主舱货板 + 30 LD2           | <https://en.wikipedia.org/wiki/Boeing_767> | passenger 0 人        | 匹配（货机）   |
| 巡航 | Mach 0.80（约 858 km/h）               | <https://en.wikipedia.org/wiki/Boeing_767> | speed_kmh 910 km/h   | 游戏偏高约 6% |

<a id="boeing_767_400er"></a>

### Boeing 767-400ER (Boeing_767_400ER)

| 字段 | 真实值                                | 来源 URL                                                | 游戏内当前值                | 偏差/备注     |
| -- | ---------------------------------- | ----------------------------------------------------- | --------------------- | --------- |
| 价格 | US$225.0M（目录价；历史/二手约 US$248M 口径不一） | <https://airlineplanes.com/aircraft/boeing-767-400er> | (游戏 cost_factor=158)  | 仅 38 架，稀有 |
| 航程 | 10,415 km (6,472 mi)（典型）           | <https://airlineplanes.com/aircraft/boeing-767-400er> | range_km_est 10312 km | 几乎一致      |
| 座级 | 245 人（典型）；最大 375                   | <https://airlineplanes.com/aircraft/boeing-767-400er> | passenger 245 人       | 匹配（典型）    |
| 巡航 | 851 km/h（529 mph）                  | <https://airlineplanes.com/aircraft/boeing-767-400er> | speed_kmh 941 km/h    | 游戏偏高约 11% |

<a id="boeing_777x"></a>

### Boeing 777X (Boeing_777X)

| 字段 | 真实值                                       | 来源 URL                                                     | 游戏内当前值                | 偏差/备注    |
| -- | ----------------------------------------- | ---------------------------------------------------------- | --------------------- | -------- |
| 价格 | US$425.8M（2019 目录，777-9）；US$426M（2018 列价） | <https://en.wikipedia.org/wiki/Boeing_777X>                | (游戏 cost_factor=305)  | 取 777-9  |
| 航程 | 14,820 km (8,000 nmi)（777-9，典型）           | <https://en.wikipedia.org/wiki/Boeing_777X>                | range_km_est 14080 km | 游戏偏低约 5% |
| 座级 | 414 人（两舱）/ 349 人（三舱）；777-9 最大约 426        | <https://en.wikipedia.org/wiki/Boeing_777X>                | passenger 426 人       | 匹配（最大两舱） |
| 巡航 | Mach 0.85（约 903 km/h）                     | <https://simpleflying.com/how-fast-the-boeing-777x-flies/> | speed_kmh 905 km/h    | 几乎一致     |

<a id="boeing_777_200"></a>

### Boeing 777-200 (Boeing_777_200)

| 字段 | 真实值                                        | 来源 URL                                     | 游戏内当前值               | 偏差/备注                  |
| -- | ------------------------------------------ | ------------------------------------------ | -------------------- | ---------------------- |
| 价格 | 未列入 2019 目录（已停产，仅列 -200ER）；历史约 US$110–130M | <https://en.wikipedia.org/wiki/Boeing_777> | (游戏 cost_factor=241) | 2019 目录无 base -200     |
| 航程 | 9,700 km (5,240 nmi) @305 人（三舱）            | <https://en.wikipedia.org/wiki/Boeing_777> | range_km_est 9598 km | 几乎一致                   |
| 座级 | 305 人（三舱）；最大约 440                          | <https://en.wikipedia.org/wiki/Boeing_777> | passenger 400 人      | 游戏取中间值（400 介于 305–440） |
| 巡航 | Mach 0.83–0.84（约 896 km/h）                 | <https://en.wikipedia.org/wiki/Boeing_777> | speed_kmh 951 km/h   | 游戏偏高约 6%               |

<a id="boeing_777_200er"></a>

### Boeing 777-200ER (Boeing_777_200ER)

| 字段 | 真实值                              | 来源 URL                                              | 游戏内当前值                | 偏差/备注          |
| -- | -------------------------------- | --------------------------------------------------- | --------------------- | -------------- |
| 价格 | US$306.6M（2019 目录）               | <https://aerocorner.com/aircraft/boeing-777-200er/> | (游戏 cost_factor=237)  | —              |
| 航程 | 13,084 km (7,065 nmi) @301 人（三舱） | <https://en.wikipedia.org/wiki/Boeing_777>          | range_km_est 14162 km | 游戏偏高约 8%       |
| 座级 | 301 人（三舱）；最大约 440                | <https://en.wikipedia.org/wiki/Boeing_777>          | passenger 314 人       | 接近（314≈301 三舱） |
| 巡航 | Mach 0.83–0.84（约 896 km/h）       | <https://en.wikipedia.org/wiki/Boeing_777>          | speed_kmh 951 km/h    | 游戏偏高约 6%       |

<a id="boeing_777_200f"></a>

### Boeing 777-200F (Boeing_777_200F)

| 字段 | 真实值                                                    | 来源 URL                                     | 游戏内当前值               | 偏差/备注          |
| -- | ------------------------------------------------------ | ------------------------------------------ | -------------------- | -------------- |
| 价格 | US$352.3M（2019 目录）                                     | <https://en.wikipedia.org/wiki/Boeing_777> | (游戏 cost_factor=270) | 货机（777F）       |
| 航程 | 18,057 km (9,750 nmi)（轻载）；9,200 km (4,970 nmi)（最大结构载荷） | <https://en.wikipedia.org/wiki/Boeing_777> | range_km_est 8992 km | 接近最大载荷口径（9200） |
| 座级 | 货机（0 乘客）；4 超员座 + 2 铺                                   | <https://en.wikipedia.org/wiki/Boeing_777> | passenger 0 人        | 匹配（货机）         |
| 巡航 | Mach 0.83–0.84（约 896 km/h）                             | <https://en.wikipedia.org/wiki/Boeing_777> | speed_kmh 951 km/h   | 游戏偏高约 6%       |

<a id="boeing_777_200lr"></a>

### Boeing 777-200LR (Boeing_777_200LR)

| 字段 | 真实值                           | 来源 URL                                              | 游戏内当前值                | 偏差/备注    |
| -- | ----------------------------- | --------------------------------------------------- | --------------------- | -------- |
| 价格 | US$346.9M（2019 目录）            | <https://aerocorner.com/aircraft/boeing-777-200lr/> | (游戏 cost_factor=266)  | —        |
| 航程 | 15,844 km (8,555 nmi)（最大设计航程） | <https://en.wikipedia.org/wiki/Boeing_777>          | range_km_est 17188 km | 游戏偏高约 8% |
| 座级 | 301 人（三舱典型）；最大约 440           | <https://en.wikipedia.org/wiki/Boeing_777>          | passenger 314 人       | 接近       |
| 巡航 | Mach 0.83–0.84（约 896 km/h）    | <https://en.wikipedia.org/wiki/Boeing_777>          | speed_kmh 951 km/h    | 游戏偏高约 6% |

<a id="boeing_777_300"></a>

### Boeing 777-300 (Boeing_777_300)

| 字段 | 真实值                                | 来源 URL                                            | 游戏内当前值                | 偏差/备注    |
| -- | ---------------------------------- | ------------------------------------------------- | --------------------- | -------- |
| 价格 | US$279M（aerocorner 标注，年份未注明）       | <https://aerocorner.com/aircraft/boeing-777-300/> | (游戏 cost_factor=262)  | 年份不明，作参考 |
| 航程 | 11,121 km (6,005 nmi) @368 人（三舱）   | <https://en.wikipedia.org/wiki/Boeing_777>        | range_km_est 11000 km | 几乎一致     |
| 座级 | 368 人（三舱）/ 451 人（两舱）/ 550 人（全经济最大） | <https://en.wikipedia.org/wiki/Boeing_777>        | passenger 451 人       | 匹配（两舱）   |
| 巡航 | Mach 0.83–0.84（约 896 km/h）         | <https://en.wikipedia.org/wiki/Boeing_777>        | speed_kmh 951 km/h    | 游戏偏高约 6% |

<a id="boeing_777_300er"></a>

### Boeing 777-300ER (Boeing_777_300ER)

| 字段 | 真实值                              | 来源 URL                                              | 游戏内当前值                | 偏差/备注          |
| -- | -------------------------------- | --------------------------------------------------- | --------------------- | -------------- |
| 价格 | US$375.5M（2019 目录）               | <https://aerocorner.com/aircraft/boeing-777-300er/> | (游戏 cost_factor=288)  | —              |
| 航程 | 13,650 km (7,370 nmi) @392 人（两舱） | <https://en.wikipedia.org/wiki/Boeing_777>          | range_km_est 14548 km | 游戏偏高约 6%       |
| 座级 | 392 人（两舱）；最大约 550                | <https://en.wikipedia.org/wiki/Boeing_777>          | passenger 386 人       | 接近（386≈392 两舱） |
| 巡航 | Mach 0.839（约 916 km/h，FL300）     | <https://en.wikipedia.org/wiki/Boeing_777>          | speed_kmh 951 km/h    | 游戏偏高约 4%       |

<a id="boeing_787_10"></a>

### Boeing 787-10 (Boeing_787_10)

| 字段 | 真实值                          | 来源 URL                                                | 游戏内当前值                | 偏差/备注    |
| -- | ---------------------------- | ----------------------------------------------------- | --------------------- | -------- |
| 价格 | US$338.4M（2019 目录）           | <https://en.wikipedia.org/wiki/Boeing_787_Dreamliner> | (游戏 cost_factor=230)  | —        |
| 航程 | 11,720 km (6,330 nmi) @336 人 | <https://en.wikipedia.org/wiki/Boeing_787_Dreamliner> | range_km_est 11908 km | 几乎一致     |
| 座级 | 336 人（典型）；最大约 440            | <https://en.wikipedia.org/wiki/Boeing_787_Dreamliner> | passenger 318 人       | 游戏偏低约 5% |
| 巡航 | Mach 0.85（约 903 km/h）        | <https://en.wikipedia.org/wiki/Boeing_787_Dreamliner> | speed_kmh 943 km/h    | 游戏偏高约 4% |

<a id="boeing_787_8"></a>

### Boeing 787-8 (Boeing_787_8)

| 字段 | 真实值                          | 来源 URL                                                | 游戏内当前值                | 偏差/备注     |
| -- | ---------------------------- | ----------------------------------------------------- | --------------------- | --------- |
| 价格 | US$248.3M（2019 目录）           | <https://en.wikipedia.org/wiki/Boeing_787_Dreamliner> | (游戏 cost_factor=189)  | —         |
| 航程 | 13,529 km (7,305 nmi) @248 人 | <https://en.wikipedia.org/wiki/Boeing_787_Dreamliner> | range_km_est 15042 km | 游戏偏高约 11% |
| 座级 | 248 人（典型）；最大约 381            | <https://en.wikipedia.org/wiki/Boeing_787_Dreamliner> | passenger 242 人       | 接近        |
| 巡航 | Mach 0.85（约 903 km/h）        | <https://en.wikipedia.org/wiki/Boeing_787_Dreamliner> | speed_kmh 943 km/h    | 游戏偏高约 4%  |

<a id="boeing_787_9"></a>

### Boeing 787-9 (Boeing_787_9)

| 字段 | 真实值                          | 来源 URL                                                | 游戏内当前值                | 偏差/备注     |
| -- | ---------------------------- | ----------------------------------------------------- | --------------------- | --------- |
| 价格 | US$292.5M（2020；2019 目录同值）    | <https://aerocorner.com/aircraft/boeing-787-9/>       | (游戏 cost_factor=223)  | —         |
| 航程 | 14,010 km (7,565 nmi) @296 人 | <https://en.wikipedia.org/wiki/Boeing_787_Dreamliner> | range_km_est 15592 km | 游戏偏高约 11% |
| 座级 | 296 人（典型）；最大约 420            | <https://en.wikipedia.org/wiki/Boeing_787_Dreamliner> | passenger 280 人       | 游戏偏低约 5%  |
| 巡航 | Mach 0.85（约 903 km/h）        | <https://en.wikipedia.org/wiki/Boeing_787_Dreamliner> | speed_kmh 943 km/h    | 游戏偏高约 4%  |

---

## 汇总要点

- **座级**：绝大多数机型游戏值与真实典型/两舱座级吻合或接近（767 全系、777-300、777X、777-200ER/LR、777-300ER 误差 <5%）。
- **航程**：767、777-300/777X、787-10 几乎一致；777-200ER/LR、787-8/9 游戏偏高约 8–11%（取了偏大口径）；777-200F 接近最大载荷口径。
- **巡航**：真实全系约 858（767）/ 896–916（777）/ 903（777X、787）km/h；游戏统一给到 910–951 km/h，整体偏高约 4–11%，767 系偏差最大。
- **价格**：2019 目录价基本可取；base 767-200 / 777-200 已停产无目录价，用历史单位成本/估算并标注；767-300 的 aerocorner 标价疑似与 300ER 混淆，已在备注说明。
- **未抓到可靠来源的字段**：无（全部字段均有标注来源；个别停产型价格以历史/估算口径并注明）。

### 庞巴迪 · Bombardier

<a id="bombardier_crj1000"></a>

### Bombardier CRJ1000 (Bombardier_CRJ1000)

| 字段 | 真实值                                            | 来源 URL                                                                                                                                                                                                                                               | 游戏内当前值               | 偏差/备注            |
| -- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ---------------- |
| 价格 | $24.8 million（2018 折让价；名录约 $25m）               | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （2018 折让 $24.8M）；https://aerocorner.com/aircraft/bombardier-crj-1000/ （$25M 2018）                                                                                                                  | (游戏 cost_factor=44)  | 现实目录价仅参考         |
| 航程 | 典型 2,698 km（1,457 nmi）；最大约 3,056 km（1,650 nmi） | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （base 1,457 nmi / 2,698 km）；<https://aerocorner.com/aircraft/bombardier-crj-1000/> （3,004 km 典型）；<https://pdf.aeroexpo.online/pdf/bombardier/crj1000/169445-15819.html> （max 1,650 nmi / 3,056 km） | range_km_est 2612 km | 接近典型航程；与最大差约 15% |
| 座级 | 最大 104（单舱）/ 两舱约 97–100                         | <https://aerocorner.com/aircraft/bombardier-crj-1000/> （104 economy · 100 business）；<https://pdf.aeroexpo.online/pdf/bombardier/crj1000/169445-15819.html> （双舱 97 / 单舱 100 / 最大 104）                                                                 | passenger 100 人      | 与两舱典型值一致         |
| 巡航 | 829 km/h（Mach 0.78 正常）；最大 871 km/h（Mach 0.82）  | <https://aerocorner.com/aircraft/bombardier-crj-1000/> （cruise 829 km/h）；<https://pdf.aeroexpo.online/pdf/bombardier/crj1000/169445-15819.html> （max 0.82M / 871 km/h）                                                                               | speed_kmh 850 km/h   | 略高于正常巡航，接近最大巡航   |

---

<a id="bombardier_crj1000el"></a>

### Bombardier CRJ1000EL (Bombardier_CRJ1000EL)

| 字段 | 真实值                                           | 来源 URL                                                                             | 游戏内当前值               | 偏差/备注                     |
| -- | --------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------- | ------------------------- |
| 价格 | 同 CRJ1000，约 $24.8M（2018 折让）                   | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （CRJ1000 折让价；EL 无单独报价）           | (游戏 cost_factor=45)  | 现实目录价仅参考；EL 为减重型          |
| 航程 | 1,910 km（1,030 nmi）EuroLite，减重 MTOW 80,969 lb | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （CRJ1000EL 1,030 nmi / 1,910 km） | range_km_est 1788 km | 接近（EL 航程最短，比 base 短约 30%） |
| 座级 | 最大 104（单舱）                                    | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （CRJ1000EL 104）                  | passenger 100 人      | 座级同基础型                    |
| 巡航 | 829 km/h（同基础型，EL 不改速度）                        | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （未列 EL 单独速度）                     | speed_kmh 850 km/h   | 沿用 CRJ1000 巡航             |

注：CRJ1000EL = EuroLite，为符合欧洲机场减重/噪声限制而降 MTOW，航程反而比标准型更短（约 1,910 km vs 2,698 km）。游戏 EL 航程(1788)明显短于 base(2612)，方向正确。

---

<a id="bombardier_crj100er"></a>

### Bombardier CRJ-100ER (Bombardier_CRJ100ER)

| 字段 | 真实值                                           | 来源 URL                                                                                                                                                                                | 游戏内当前值               | 偏差/备注                           |
| -- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------- |
| 价格 | $18.3M（1994 单机成本）；上限约 $39.7M（2006）            | <https://a.osmarks.net/content/wikipedia_en_all_maxi_2020-08/A/CRJ100> （Unit cost US$18.3M 1994）；https://www.airports-worldwide.com/articles/article0892.php （US$24–39.7m as of 2006） | (游戏 cost_factor=22)  | 现实目录价仅参考                        |
| 航程 | 约 3,000 km（1,620 nmi）ER                       | <https://www.airplanes24.net/airplanes/10-bombardier-crj200> （CRJ100 ER: 3,000 km / 1,620 nmi，源 Jane's 2006）                                                                          | range_km_est 2970 km | 几乎一致（维基规格表另列 ER 2,417 km，见下方备注） |
| 座级 | 50 典型 / 最大 52                                 | <https://en.wikipedia.org/wiki/Bombardier_CRJ100> （典型 50，最大 52）                                                                                                                       | passenger 50 人       | 完全一致                            |
| 巡航 | 786 km/h（Mach 0.74 正常）；最大 860 km/h（Mach 0.81） | <https://en.wikipedia.org/wiki/Bombardier_CRJ100> （Mach .74 / 786 km/h 正常；Mach .81 / 860 km/h 高速）                                                                                     | speed_kmh 814 km/h   | 介于正常与高速巡航之间                     |

注：维基规格表 CRJ100 行将 ER/LR 列标为 2,417 km / 3,056 km（即 1,305 / 1,650 nmi），与 Jane's(airplanes24) 的 ER 3,000 km / LR 3,710 km 不一致；游戏 ER/LR 值(2970 / 3685) 与 Jane's 吻合，故采用 Jane's 作为 ER/LR 航程依据。

---

<a id="bombardier_crj100lr"></a>

### Bombardier CRJ-100LR (Bombardier_CRJ100LR)

| 字段 | 真实值                                        | 来源 URL                                                                                                       | 游戏内当前值               | 偏差/备注       |
| -- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | -------------------- | ----------- |
| 价格 | 同 CRJ100 家族，约 $18.3M（1994）                 | <https://a.osmarks.net/content/wikipedia_en_all_maxi_2020-08/A/CRJ100> （家族单机成本）                              | (游戏 cost_factor=25)  | 现实目录价仅参考    |
| 航程 | 约 3,710 km（2,003 nmi）LR                    | <https://www.airplanes24.net/airplanes/10-bombardier-crj200> （CRJ100 LR: 3,710 km / 2,003 nmi，源 Jane's 2006） | range_km_est 3685 km | 几乎一致        |
| 座级 | 50 典型 / 最大 52                              | <https://en.wikipedia.org/wiki/Bombardier_CRJ100> （50 典型，最大 52）                                              | passenger 50 人       | 完全一致        |
| 巡航 | 786 km/h（Mach 0.74）；最大 860 km/h（Mach 0.81） | <https://en.wikipedia.org/wiki/Bombardier_CRJ100>                                                            | speed_kmh 814 km/h   | 介于正常与高速巡航之间 |

---

<a id="bombardier_crj200er"></a>

### Bombardier CRJ-200ER (Bombardier_CRJ200ER)

| 字段 | 真实值                                        | 来源 URL                                                                                                                                                | 游戏内当前值               | 偏差/备注       |
| -- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------- |
| 价格 | 约 $24.4M（新机名录均值） / 区间 $18–40M              | <https://www.sunairlines.net/bombardier-crj200/price> （list ~$24.375M）；https://www.airports-worldwide.com/articles/article0892.php （US$24–39.7m 2006） | (游戏 cost_factor=26)  | 现实目录价仅参考    |
| 航程 | 约 3,045 km（1,644 nmi）ER                    | <https://www.airplanes24.net/airplanes/10-bombardier-crj200> （CRJ200 ER: 3,045 km / 1,644 nmi，源 Jane's 2006）                                          | range_km_est 3025 km | 几乎一致        |
| 座级 | 50 典型 / 最大 52                              | <https://en.wikipedia.org/wiki/Bombardier_CRJ100> （CRJ200 同 50）                                                                                       | passenger 50 人       | 完全一致        |
| 巡航 | 786 km/h（Mach 0.74）；最大 860 km/h（Mach 0.81） | <https://en.wikipedia.org/wiki/Bombardier_CRJ100> （CRJ200 同 CRJ100 速度）                                                                                | speed_kmh 814 km/h   | 介于正常与高速巡航之间 |

---

<a id="bombardier_crj200lr"></a>

### Bombardier CRJ-200LR (Bombardier_CRJ200LR)

| 字段 | 真实值                                        | 来源 URL                                                                                                               | 游戏内当前值               | 偏差/备注       |
| -- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------- |
| 价格 | 约 $24.4M（新机名录均值） / 区间 $18–40M              | <https://www.sunairlines.net/bombardier-crj200/price> ；<https://www.airports-worldwide.com/articles/article0892.php> | (游戏 cost_factor=28)  | 现实目录价仅参考    |
| 航程 | 约 3,713 km（2,004 nmi）LR                    | <https://www.airplanes24.net/airplanes/10-bombardier-crj200> （CRJ200 LR: 3,713 km / 2,004 nmi，源 Jane's 2006）         | range_km_est 3685 km | 几乎一致        |
| 座级 | 50 典型 / 最大 52                              | <https://en.wikipedia.org/wiki/Bombardier_CRJ100>                                                                    | passenger 50 人       | 完全一致        |
| 巡航 | 786 km/h（Mach 0.74）；最大 860 km/h（Mach 0.81） | <https://en.wikipedia.org/wiki/Bombardier_CRJ100>                                                                    | speed_kmh 814 km/h   | 介于正常与高速巡航之间 |

---

<a id="bombardier_crj700"></a>

### Bombardier CRJ-700 (Bombardier_CRJ700)

| 字段 | 真实值                                    | 来源 URL                                                                                                                                         | 游戏内当前值               | 偏差/备注      |
| -- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ---------- |
| 价格 | $24–25 million（1999 名录）                | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （listed at $24–25 million 1999）；https://aerocorner.com/aircraft/bombardier-crj-700/ （$24.4M） | (游戏 cost_factor=22)  | 现实目录价仅参考   |
| 航程 | 3,152 km（1,702 nmi）base（68 座）          | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （CRJ700 1,702 nmi / 3,152 km）                                                                | range_km_est 2228 km | 游戏偏低约 29%  |
| 座级 | 最大 78（702 型）/ 典型 70（701 型）             | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （68/70/78 因型号而异）                                                                             | passenger 70 人       | 与典型 70 座一致 |
| 巡航 | 876 km/h（Mach 0.825 最大）；正常巡航约 829 km/h | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （对比表 Mach .825 = 876 km/h）                                                                   | speed_kmh 830 km/h   | 接近正常巡航     |

---

<a id="bombardier_crj700er"></a>

### Bombardier CRJ-700ER (Bombardier_CRJ700ER)

| 字段 | 真实值                         | 来源 URL                                                                            | 游戏内当前值               | 偏差/备注      |
| -- | --------------------------- | --------------------------------------------------------------------------------- | -------------------- | ---------- |
| 价格 | 同 CRJ700 家族，约 $24–25M（1999） | <https://en.wikipedia.org/wiki/Bombardier_CRJ700>                                 | (游戏 cost_factor=24)  | 现实目录价仅参考   |
| 航程 | 3,763 km（2,032 nmi）ER（68 座） | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （CRJ700ER 2,032 nmi / 3,763 km） | range_km_est 2750 km | 游戏偏低约 27%  |
| 座级 | 最大 68–78                    | <https://en.wikipedia.org/wiki/Bombardier_CRJ700>                                 | passenger 70 人       | 与典型 70 座一致 |
| 巡航 | 876 km/h（Mach 0.825 最大）     | <https://en.wikipedia.org/wiki/Bombardier_CRJ700>                                 | speed_kmh 830 km/h   | 接近正常巡航     |

---

<a id="bombardier_crj900"></a>

### Bombardier CRJ-900 (Bombardier_CRJ900)

| 字段 | 真实值                                      | 来源 URL                                                                                                                                         | 游戏内当前值               | 偏差/备注     |
| -- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | --------- |
| 价格 | $28–29M（1999 初始）/ 名录 $48M（2018，市场约 $24M） | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （1999 $28–29M；2018 list $48M）；<https://aerocorner.com/aircraft/bombardier-crj-900/> （$46.5M） | (游戏 cost_factor=27)  | 现实目录价仅参考  |
| 航程 | 2,500 km（1,350 nmi）base（MTOW 80,500 lb）  | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （CRJ900 1,350 nmi / 2,500 km）                                                                | range_km_est 1925 km | 游戏偏低约 23% |
| 座级 | 最大 90                                    | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （CRJ900 up to 90）                                                                            | passenger 88 人       | 接近最大座级    |
| 巡航 | 829 km/h（巡航）/ 871 km/h（Mach 0.82 最大）     | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （cruise 829 km/h, Mach 0.82 / 871 km/h）                                                      | speed_kmh 846 km/h   | 介于巡航与最大之间 |

---

<a id="bombardier_crj900er"></a>

### Bombardier CRJ-900ER (Bombardier_CRJ900ER)

| 字段 | 真实值                                   | 来源 URL                                                                            | 游戏内当前值               | 偏差/备注     |
| -- | ------------------------------------- | --------------------------------------------------------------------------------- | -------------------- | --------- |
| 价格 | 同 CRJ900 家族，约 $28–48M                 | <https://en.wikipedia.org/wiki/Bombardier_CRJ700>                                 | (游戏 cost_factor=28)  | 现实目录价仅参考  |
| 航程 | 2,950 km（1,593 nmi）ER（MTOW 82,500 lb） | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （CRJ900ER 1,593 nmi / 2,950 km） | range_km_est 2365 km | 游戏偏低约 20% |
| 座级 | 最大 90                                 | <https://en.wikipedia.org/wiki/Bombardier_CRJ700>                                 | passenger 88 人       | 接近最大座级    |
| 巡航 | 829 km/h（巡航）/ 871 km/h（最大）            | <https://en.wikipedia.org/wiki/Bombardier_CRJ700>                                 | speed_kmh 846 km/h   | 介于巡航与最大之间 |

---

<a id="bombardier_crj900lr"></a>

### Bombardier CRJ-900LR (Bombardier_CRJ900LR)

| 字段 | 真实值                                   | 来源 URL                                                                            | 游戏内当前值               | 偏差/备注     |
| -- | ------------------------------------- | --------------------------------------------------------------------------------- | -------------------- | --------- |
| 价格 | 同 CRJ900 家族，约 $28–48M                 | <https://en.wikipedia.org/wiki/Bombardier_CRJ700>                                 | (游戏 cost_factor=29)  | 现实目录价仅参考  |
| 航程 | 3,385 km（1,828 nmi）LR（MTOW 84,500 lb） | <https://en.wikipedia.org/wiki/Bombardier_CRJ700> （CRJ900LR 1,828 nmi / 3,385 km） | range_km_est 2778 km | 游戏偏低约 18% |
| 座级 | 最大 90                                 | <https://en.wikipedia.org/wiki/Bombardier_CRJ700>                                 | passenger 90 人       | 完全一致      |
| 巡航 | 829 km/h（巡航）/ 871 km/h（最大）            | <https://en.wikipedia.org/wiki/Bombardier_CRJ700>                                 | speed_kmh 846 km/h   | 介于巡航与最大之间 |

---

## 批次小结

- 座级：CRJ100/200 全系 50（与游戏一致）；CRJ700 典型 70（游戏 70 一致）；CRJ900 最大 90（游戏 88/90 接近）；CRJ1000 两舱约 100（游戏 100 一致）。整体匹配良好。
- 航程：CRJ100/200 的 ER/LR 游戏值(2970/3685) 与 Jane's 数据(3000/3710)几乎一致；CRJ700/900/1000 游戏航程普遍比维基低 18–29%，呈系统性偏低。
- 巡航：CRJ700/900/1000 游戏值(830–850)落在真实巡航(829)与最大(871–876)之间，合理；CRJ100/200 游戏 814 介于正常(786)与高速(860)之间。
- 价格：游戏 `cost_factor` 仅为相对系数，已附现实目录价（USD，注年份）作参考，无法直接对应。
- 来源覆盖：aerocorner（CRJ700/900/1000/200 概览，含价格/航程/座级/巡航）、英文维基（CRJ700 系对比表含各 ER/LR 航程与价格，CRJ100 系含座级/巡航）、airplanes24（Jane's 2006，CRJ100/200 ER/LR 航程）、sunairlines（CRJ200 名录价）。CRJ100 专属 aerocorner slug 404（已用维基/airplanes24 替代）；airliners.net slug 亦 404。

<a id="bombardier_dash_8_100"></a>

### Bombardier Dash 8-100 (Bombardier_Dash_8_100)

| 字段 | 真实值                                                                             | 来源 URL                                                                                                         | 游戏内当前值               | 偏差/备注                        |
| -- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------- | ---------------------------- |
| 价格 | ≈ US$12.5M（年份未注明；Aerocorner 与维基均未给 Series 100 目录价，modernairliners 列机身成本 M$12.5） | <https://modernairliners.com/bombardier-dhc-dash-8>                                                            | cost_factor=9        | 真实目录价参考；无明确年份源               |
| 航程 | 最大 1,020 nmi ≈ 1,889 km（维基，MTOW/SL/ISA）；Aerocorner 列 1,125 nmi ≈ 2,083 km（口径偏长） | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8> ; <https://aerocorner.com/aircraft/bombardier-q100> | range_km_est 1870 km | 游戏 1870 km 接近维基最大 1889 km，合理 |
| 座级 | 37–40 人（最大 40；典型 37–39）                                                         | <https://aerocorner.com/aircraft/bombardier-q100> ; <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8> | passenger 39 人       | 一致                           |
| 巡航 | 270 kt ≈ 500 km/h（高速巡航）                                                         | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8>                                                     | speed_kmh 499 km/h   | 一致                           |

---

<a id="bombardier_dash_8_200"></a>

### Bombardier Dash 8-200 (Bombardier_Dash_8_200)

| 字段 | 真实值                                                                       | 来源 URL                                                                                                           | 游戏内当前值               | 偏差/备注                         |
| -- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------- |
| 价格 | US$12 million（2000 年）                                                     | <https://aerocorner.com/aircraft/bombardier-q200>                                                                | cost_factor=9        | 真实目录价参考                       |
| 航程 | 典型 925 nmi ≈ 1,713 km（modernairliners）；最大 1,125 nmi ≈ 2,084 km（维基，Q200 列） | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8> ; <https://modernairliners.com/bombardier-dhc-dash-8> | range_km_est 1705 km | 游戏 1705 km 与典型载荷 1713 km 几乎一致 |
| 座级 | 37–40 人（最大 40；典型 37）                                                      | <https://aerocorner.com/aircraft/bombardier-q200>                                                                | passenger 39 人       | 一致                            |
| 巡航 | 289 kt ≈ 535 km/h（高速巡航）                                                   | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8>                                                       | speed_kmh 547 km/h   | 游戏略高约 +2.2%，可接受               |

---

<a id="bombardier_dash_8_200q"></a>

### Bombardier Dash 8-200Q (Bombardier_Dash_8_200Q)

| 字段 | 真实值                                                          | 来源 URL                                                                                                           | 游戏内当前值               | 偏差/备注                         |
| -- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------- |
| 价格 | US$12 million（2000 年，同 Series 200）                           | <https://aerocorner.com/aircraft/bombardier-q200>                                                                | cost_factor=9        | Q200=Series 200 加 ANVS 静音，价格同 |
| 航程 | 典型 925 nmi ≈ 1,713 km；最大 1,125 nmi ≈ 2,084 km（与 200 同，仅静音改型） | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8> ; <https://modernairliners.com/bombardier-dhc-dash-8> | range_km_est 1705 km | 同 200；游戏值合理                   |
| 座级 | 37–40 人（与 200 同）                                             | <https://aerocorner.com/aircraft/bombardier-q200>                                                                | passenger 39 人       | 一致                            |
| 巡航 | 289 kt ≈ 535 km/h（与 200 同）                                   | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8>                                                       | speed_kmh 547 km/h   | 同 200，略高约 +2.2%               |

---

<a id="bombardier_dash_8_300"></a>

### Bombardier Dash 8-300 (Bombardier_Dash_8_300)

| 字段 | 真实值                                                                                         | 来源 URL                                                                                                           | 游戏内当前值               | 偏差/备注                      |
| -- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------- | -------------------------- |
| 价格 | US$14.3M（2000 年，维基）；Aerocorner 列 US$18.6M（2007 年）                                           | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8> ; <https://aerocorner.com/aircraft/bombardier-q300>   | cost_factor=14       | 两源年份不同，取 2000 年 $14.3M 作基准 |
| 航程 | 典型 841 nmi ≈ 1,558 km（modernairliners）；最大 924 nmi ≈ 1,711 km（维基）；长航程油箱 1,362 nmi ≈ 2,522 km | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8> ; <https://modernairliners.com/bombardier-dhc-dash-8> | range_km_est 1540 km | 游戏 1540 km 接近典型载荷 1558 km  |
| 座级 | 50–56 人（最大 56；典型 50）                                                                        | <https://aerocorner.com/aircraft/bombardier-q300>                                                                | passenger 50 人       | 一致                         |
| 巡航 | 287 kt ≈ 532 km/h（高速巡航）                                                                     | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8>                                                       | speed_kmh 531 km/h   | 一致                         |

---

<a id="bombardier_dash_8_300q"></a>

### Bombardier Dash 8-300Q (Bombardier_Dash_8_300Q)

| 字段 | 真实值                                             | 来源 URL                                                                                                           | 游戏内当前值               | 偏差/备注                         |
| -- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------- |
| 价格 | US$14.3M（2000 年）/ US$18.6M（2007 年，同 Series 300） | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8> ; <https://aerocorner.com/aircraft/bombardier-q300>   | cost_factor=14       | Q300=Series 300 加 ANVS 静音，价格同 |
| 航程 | 典型 1,558 km；最大 1,711 km；长航程 2,522 km（与 300 同）   | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8> ; <https://modernairliners.com/bombardier-dhc-dash-8> | range_km_est 1540 km | 同 300，合理                      |
| 座级 | 50–56 人（与 300 同）                                | <https://aerocorner.com/aircraft/bombardier-q300>                                                                | passenger 50 人       | 一致                            |
| 巡航 | 287 kt ≈ 532 km/h（与 300 同）                      | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8>                                                       | speed_kmh 531 km/h   | 一致                            |

---

<a id="bombardier_dash_8_400q"></a>

### Bombardier Dash 8-400Q (Bombardier_Dash_8_400Q)

| 字段 | 真实值                                                                     | 来源 URL                                                                                                           | 游戏内当前值               | 偏差/备注                        |
| -- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------- | ---------------------------- |
| 价格 | US$32.2 million（2017 年，维基；Aerocorner 列 $32.2M 未注年）                      | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8> ; <https://aerocorner.com/aircraft/bombardier-q400>   | cost_factor=22       | 真实目录价参考                      |
| 航程 | 最大 1,100 nmi ≈ 2,040 km（维基，典型）；长航程 1,567 mi ≈ 2,522 km（modernairliners） | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8> ; <https://modernairliners.com/bombardier-dhc-dash-8> | range_km_est 2502 km | 游戏 2502 km 与长航程 2522 km 几乎一致 |
| 座级 | 典型 68–78 人；最大 90 人（高密度）；Aerocorner 列 68 商务 / 78 经济                      | <https://aerocorner.com/aircraft/bombardier-q400> ; <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8>   | passenger 78 人       | 游戏取典型经济 78 人，一致              |
| 巡航 | 300–360 kt（556–667 km/h），高速巡航 360 kt ≈ 667 km/h                         | <https://en.wikipedia.org/wiki/De_Havilland_Canada_Dash_8>                                                       | speed_kmh 668 km/h   | 游戏取高速巡航 667 km/h，几乎一致        |

---

## 批次小结

- 6 架座级、巡航均与真实值吻合良好（误差多在 ±2% 内，巡航基本 1:1）。
- 航程：游戏 `range_km_est`（base×5.5）与各型「典型/长航程」口径接近；其中 100/200/300 接近维基/modernairliners 的典型载荷值，400Q 接近长航程油箱值。
- 价格：真实目录价均高于游戏 cost_factor 系数（属相对系数，仅作参考），Dash 8-100 无明确年份目录价源（Aerocorner/维基未列 Series 100 价，modernairliners 列 $12.5M 未注年）。
- Q 系列（200Q/300Q/400Q）性能与对应序号一致，仅静音改型，已注明。

### 布里顿-诺曼 · Britten-Norman

<a id="britten_norman_bn2b"></a>

### Britten-Norman BN-2B Islander (BRITTEN_NORMAN_BN2B)

| 字段 | 真实值                                    | 来源 URL                                                  | 游戏内当前值               | 偏差/备注          |
| -- | -------------------------------------- | ------------------------------------------------------- | -------------------- | -------------- |
| 价格 | 未找到可靠来源（无公开USD目录价）                     | <https://en.wikipedia.org/wiki/Britten-Norman_Islander> | (游戏 cost_factor=14)  | —              |
| 航程 | 1,398 km（869 mi / 755 nmi，标准燃油，130 kn） | <https://en.wikipedia.org/wiki/Britten-Norman_Islander> | range_km_est 1072 km | 偏差：游戏低估约330 km |
| 座级 | 9 人（最大，1机组+9客）                         | <https://en.wikipedia.org/wiki/Britten-Norman_Islander> | passenger 9 人        | 一致             |
| 巡航 | 240 km/h（150 mph / 130 kn，59%功率）       | <https://en.wikipedia.org/wiki/Britten-Norman_Islander> | speed_kmh 257 km/h   | 接近（游戏略高）       |

<a id="britten_norman_bn2t"></a>

### Britten-Norman BN-2T Turbine Islander (BRITTEN_NORMAN_BN2T)

| 字段 | 真实值                                     | 来源 URL                                                  | 游戏内当前值               | 偏差/备注                |
| -- | --------------------------------------- | ------------------------------------------------------- | -------------------- | -------------------- |
| 价格 | 未找到可靠来源（无公开USD目录价）                      | <https://en.wikipedia.org/wiki/Britten-Norman_Islander> | (游戏 cost_factor=14)  | —                    |
| 航程 | 未找到可靠来源（维基未单列BN-2T航程；涡桨型通常略长于BN-2B）     | <https://en.wikipedia.org/wiki/Britten-Norman_Islander> | range_km_est 1342 km | 真实BN-2T专项航程未列        |
| 座级 | 最多 9 人                                  | <https://en.wikipedia.org/wiki/Britten-Norman_Islander> | passenger 9 人        | 一致                   |
| 巡航 | 未找到可靠来源（维基未单列BN-2T巡航；涡桨型估约260–300 km/h） | <https://en.wikipedia.org/wiki/Britten-Norman_Islander> | speed_kmh 326 km/h   | BN-2T专项巡航未列，游戏取涡桨较高值 |

### 中国商飞 · COMAC

<a id="comac_c909"></a>

### COMAC C909 (ARJ21) (COMAC_C909)

| 字段 | 真实值                                                | 来源 URL                                      | 游戏内当前值               | 偏差/备注                  |
| -- | -------------------------------------------------- | ------------------------------------------- | -------------------- | ---------------------- |
| 价格 | 未找到可靠来源（无公开USD目录价）                                 | <https://en.wikipedia.org/wiki/Comac_ARJ21> | (游戏 cost_factor=65)  | 2024年11月由ARJ21更名C909   |
| 航程 | STD 2,200 km（1,200 nmi）/ ER 3,700 km（2,000 nmi），满载 | <https://en.wikipedia.org/wiki/Comac_ARJ21> | range_km_est 3702 km | 一致（取ER 3,700 km）       |
| 座级 | 78 人（两舱）/ 90 人（单级最大）                               | <https://en.wikipedia.org/wiki/Comac_ARJ21> | passenger 90 人       | 一致（取单级最大）              |
| 巡航 | 828 km/h（Mach 0.78）；最大Mach 0.82=870 km/h           | <https://en.wikipedia.org/wiki/Comac_ARJ21> | speed_kmh 886 km/h   | 偏差：游戏接近最大巡航870，高于常规828 |

<a id="comac_c919"></a>

### COMAC C919 (COMAC_C919)

| 字段 | 真实值                                   | 来源 URL                                     | 游戏内当前值               | 偏差/备注                                     |
| -- | ------------------------------------- | ------------------------------------------ | -------------------- | ----------------------------------------- |
| 价格 | US$101M（2022年5月，653百万元人民币）            | <https://en.wikipedia.org/wiki/Comac_C919> | (游戏 cost_factor=73)  | 真实USD目录价；aerocorner列"$1M(2012)"为占位错误值，未采用 |
| 航程 | STD 4,075 km / ER 5,555 km（2,999 nmi） | <https://en.wikipedia.org/wiki/Comac_C919> | range_km_est 5610 km | 接近（取ER 5,555 km）                          |
| 座级 | 158 人（两舱 8J+150Y）/ 最大 192             | <https://en.wikipedia.org/wiki/Comac_C919> | passenger 158 人      | 一致（取两舱）                                   |
| 巡航 | 835 km/h（Mach 0.785）                  | <https://en.wikipedia.org/wiki/Comac_C919> | speed_kmh 902 km/h   | 偏差：游戏约高67 km/h                            |

<a id="comac_c929"></a>

### COMAC C929 (COMAC_C929)

| 字段 | 真实值                           | 来源 URL                                     | 游戏内当前值                | 偏差/备注                        |
| -- | ----------------------------- | ------------------------------------------ | --------------------- | ---------------------------- |
| 价格 | 未找到可靠来源（研发中，无最终目录价）           | <https://en.wikipedia.org/wiki/Comac_C929> | (游戏 cost_factor=220)  | 中俄联合(CR929)后由中国独立研制，仍在详细设计阶段 |
| 航程 | 约 12,000 km（C929-600，2024年目标） | <https://en.wikipedia.org/wiki/Comac_C929> | range_km_est 12001 km | 一致（取-600目标值）                 |
| 座级 | 280 人（三舱，-600）；目标 280–400     | <https://en.wikipedia.org/wiki/Comac_C929> | passenger 280 人       | 一致（取-600三舱）                  |
| 巡航 | 约 908 km/h（Mach 0.85）         | <https://en.wikipedia.org/wiki/Comac_C929> | speed_kmh 945 km/h    | 偏差：游戏略高约37 km/h；规格未冻结        |

### 塞斯纳 · Cessna

<a id="cessna_208"></a>

### Cessna 208 Caravan (CESSNA_208)

| 字段 | 真实值                                                  | 来源 URL                                             | 游戏内当前值               | 偏差/备注           |
| -- | ---------------------------------------------------- | -------------------------------------------------- | -------------------- | --------------- |
| 价格 | US$2.32M（2023；208B Grand Caravan EX 为 US$2.61M/2023） | <https://en.wikipedia.org/wiki/Cessna_208_Caravan> | (游戏 cost_factor=18)  | 历史新机目录价；游戏为相对系数 |
| 航程 | 1,980 km（1,070 nmi）                                  | <https://en.wikipedia.org/wiki/Cessna_208_Caravan> | range_km_est 1980 km | 完全一致            |
| 座级 | 9 人（典型）；13 人（FAR Part 23 豁免）；最高 14 人                 | <https://en.wikipedia.org/wiki/Cessna_208_Caravan> | passenger 13 人       | 游戏取豁免后 13 座，合理  |
| 巡航 | 344 km/h（186 kn）                                     | <https://en.wikipedia.org/wiki/Cessna_208_Caravan> | speed_kmh 344 km/h   | 完全一致            |

<a id="cessna_208b"></a>

### Cessna 208B Grand Caravan (CESSNA_208B)

| 字段 | 真实值                             | 来源 URL                                             | 游戏内当前值               | 偏差/备注                           |
| -- | ------------------------------- | -------------------------------------------------- | -------------------- | ------------------------------- |
| 价格 | US$2.61M（2023，Grand Caravan EX） | <https://en.wikipedia.org/wiki/Cessna_208_Caravan> | (游戏 cost_factor=19)  | 历史新机目录价                         |
| 航程 | 1,785 km（964 nmi，208B EX）       | <https://en.wikipedia.org/wiki/Cessna_208_Caravan> | range_km_est 1980 km | 游戏沿用基础型 208 的 1980 km，208B 实际略短 |
| 座级 | 14 人（最高）                        | <https://en.wikipedia.org/wiki/Cessna_208_Caravan> | passenger 14 人       | 一致                              |
| 巡航 | 344 km/h（186 kn）                | <https://en.wikipedia.org/wiki/Cessna_208_Caravan> | speed_kmh 344 km/h   | 一致                              |

<a id="cessna_402"></a>

### Cessna 402 (CESSNA_402)

| 字段 | 真实值                                    | 来源 URL                                     | 游戏内当前值               | 偏差/备注                 |
| -- | -------------------------------------- | ------------------------------------------ | -------------------- | --------------------- |
| 价格 | 未找到可靠来源（维基未列价）                         | <https://en.wikipedia.org/wiki/Cessna_401> | (游戏 cost_factor=12)  | 历史/二手价难核实             |
| 航程 | 2,358 km（1,273 nmi，402C 经济巡航@10,000ft） | <https://en.wikipedia.org/wiki/Cessna_401> | range_km_est 1298 km | 游戏偏低（约为真实 55%）        |
| 座级 | 10 人（Utiliner/Commuter 最高）             | <https://en.wikipedia.org/wiki/Cessna_401> | passenger 8 人        | 略低                    |
| 巡航 | 263 km/h（142 kn，经济巡航）                  | <https://en.wikipedia.org/wiki/Cessna_401> | speed_kmh 380 km/h   | 游戏偏高（接近最大速度 428 km/h） |

<a id="cessna_404"></a>

### Cessna 404 Titan (CESSNA_404)

| 字段 | 真实值                              | 来源 URL                                           | 游戏内当前值               | 偏差/备注       |
| -- | -------------------------------- | ------------------------------------------------ | -------------------- | ----------- |
| 价格 | 未找到可靠来源（维基/ aerocorner 均未列价）     | <https://en.wikipedia.org/wiki/Cessna_404_Titan> | (游戏 cost_factor=13)  | 历史/二手价难核实   |
| 航程 | 3,410 km（1,840 nmi）              | <https://en.wikipedia.org/wiki/Cessna_404_Titan> | range_km_est 2398 km | 游戏偏低（约 70%） |
| 座级 | 10 人（Titan Ambassador 最高；规格表列 8） | <https://en.wikipedia.org/wiki/Cessna_404_Titan> | passenger 9 人        | 合理          |
| 巡航 | 302 km/h（163 kn，经济巡航@20,000ft）   | <https://en.wikipedia.org/wiki/Cessna_404_Titan> | speed_kmh 330 km/h   | 接近（游戏略高）    |

<a id="cessna_408"></a>

### Cessna 408 SkyCourier (CESSNA_408)

| 字段 | 真实值                                        | 来源 URL                                                   | 游戏内当前值               | 偏差/备注                   |
| -- | ------------------------------------------ | -------------------------------------------------------- | -------------------- | ----------------------- |
| 价格 | US$5.5M（2017，FedEx 订货）；客运型 2024 年 US$8.35M | <https://aerocorner.com/aircraft/cessna-408-skycourier/> | (游戏 cost_factor=18)  | 新机目录价；维基亦载 2023/2024 价位 |
| 航程 | 1,700 km（920 nmi， Ferry 最大）；19 座典型仅 715 km | <https://en.wikipedia.org/wiki/Cessna_408_SkyCourier>    | range_km_est 1672 km | 游戏取 Ferry 航程，吻合         |
| 座级 | 19 人                                       | <https://en.wikipedia.org/wiki/Cessna_408_SkyCourier>    | passenger 19 人       | 一致                      |
| 巡航 | 390 km/h（210 kn，最大巡航）                      | <https://en.wikipedia.org/wiki/Cessna_408_SkyCourier>    | speed_kmh 388 km/h   | 一致                      |

<a id="cessna_414"></a>

### Cessna 414 Chancellor (CESSNA_414)

| 字段 | 真实值                              | 来源 URL                                     | 游戏内当前值               | 偏差/备注        |
| -- | -------------------------------- | ------------------------------------------ | -------------------- | ------------ |
| 价格 | 未找到可靠来源（维基未列价）                   | <https://en.wikipedia.org/wiki/Cessna_414> | (游戏 cost_factor=12)  | 历史/二手价难核实    |
| 航程 | 2,458 km（1,327 nmi，@10,000ft）    | <https://en.wikipedia.org/wiki/Cessna_414> | range_km_est 2458 km | 完全一致         |
| 座级 | 8 人（最高；infobox "six/eight-seat"） | <https://en.wikipedia.org/wiki/Cessna_414> | passenger 7 人        | 略低（规格表列 4-6） |
| 巡航 | 339 km/h（183 kn，经济巡航）            | <https://en.wikipedia.org/wiki/Cessna_414> | speed_kmh 360 km/h   | 接近（游戏略高）     |

<a id="cessna_421"></a>

### Cessna 421 Golden Eagle (CESSNA_421)

| 字段 | 真实值                                    | 来源 URL                                     | 游戏内当前值               | 偏差/备注      |
| -- | -------------------------------------- | ------------------------------------------ | -------------------- | ---------- |
| 价格 | 未找到可靠来源（维基未列价）                         | <https://en.wikipedia.org/wiki/Cessna_421> | (游戏 cost_factor=14)  | 历史/二手价难核实  |
| 航程 | 2,754 km（1,487 nmi，421C 经济巡航@25,000ft） | <https://en.wikipedia.org/wiki/Cessna_421> | range_km_est 2756 km | 完全一致       |
| 座级 | 6 人（421C 规格）；后期型最高 10 人                | <https://en.wikipedia.org/wiki/Cessna_421> | passenger 8 人        | 介于规格与后期型之间 |
| 巡航 | 440 km/h（240 kn，75% 功率@25,000ft）       | <https://en.wikipedia.org/wiki/Cessna_421> | speed_kmh 420 km/h   | 接近         |

### 康维尔 · Convair

<a id="convair_880"></a>

### Convair 880 (CONVAIR_880)

| 字段 | 真实值                                    | 来源 URL                                                                                       | 游戏内当前值               | 偏差/备注                |
| -- | -------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------- | -------------------- |
| 价格 | 未找到可靠来源（无公开USD目录价；通用动力项目亏损，无单机价）       | <https://en.wikipedia.org/wiki/Convair_880> ; <https://aerocorner.com/aircraft/convair-880/> | (游戏 cost_factor=35)  | —                    |
| 航程 | 4,578 km（2,472 nmi，22型）/ 4,636 km（22M） | <https://en.wikipedia.org/wiki/Convair_880> ; <https://aerocorner.com/aircraft/convair-880/> | range_km_est 5599 km | 偏差：游戏高估约1,000 km     |
| 座级 | 110 人（最大）                              | <https://en.wikipedia.org/wiki/Convair_880> ; <https://aerocorner.com/aircraft/convair-880/> | passenger 100 人      | 游戏略低                 |
| 巡航 | 990 km/h（534.5 kn，最大巡航）；经济巡航 Mach 0.82 | <https://en.wikipedia.org/wiki/Convair_880> ; <https://aerocorner.com/aircraft/convair-880/> | speed_kmh 910 km/h   | 偏差：游戏取经济巡航附近，低于最大990 |

<a id="convair_990"></a>

### Convair 990 (CONVAIR_990)

| 字段 | 真实值                        | 来源 URL                                      | 游戏内当前值               | 偏差/备注       |
| -- | -------------------------- | ------------------------------------------- | -------------------- | ----------- |
| 价格 | 未找到可靠来源（无公开USD目录价）         | <https://en.wikipedia.org/wiki/Convair_990> | (游戏 cost_factor=39)  | —           |
| 航程 | 6,115 km（3,302 nmi，990A）   | <https://en.wikipedia.org/wiki/Convair_990> | range_km_est 6116 km | 一致（几乎完全相同）  |
| 座级 | 最多 149 人（990A）             | <https://en.wikipedia.org/wiki/Convair_990> | passenger 120 人      | 偏差：游戏低于真实最大 |
| 巡航 | 896 km/h（484 kn，Mach 0.84） | <https://en.wikipedia.org/wiki/Convair_990> | speed_kmh 896 km/h   | 一致          |

---

### 巴航工 · Embraer

<a id="embraer_e175_e2"></a>

### Embraer E175-E2 (EMBRAER_E175_E2)

| 字段 | 真实值                                                                             | 来源 URL                                                                                                                                                                                                                | 游戏内当前值               | 偏差/备注                                |
| -- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------ |
| 价格 | US$46.8 million（2013 目录价）；现行目录约 US$56.4M                                        | <https://en.wikipedia.org/wiki/Embraer_E-Jet_E2> （交叉：<https://www.airplaneupdate.com/2019/02/embraer-e175-e2.html> US$46.8M；https://www.aeroflap.com.br/en/saiba-quanto-custa-um-aviao-e-jet-da-embraer/ 现行 US$56.4M） | cost_factor=26       | 游戏系数 26，未对应真实目录价；真实 2013 目录 US$46.8M |
| 航程 | 3,700 km（2,000 nmi，满载；维基）；AR 型 3,735 km（2,017 nmi）；手册另列高速巡航 5,280 km（2,850 nmi） | <https://en.wikipedia.org/wiki/Embraer_E-Jet_E2> （交叉：wikiwand 2,017 nmi/3,735 km）                                                                                                                                     | range_km_est=3702 km | 几乎完全吻合（3702 vs 3700）                 |
| 座级 | 两舱 80 人（8J+72Y，wikiwand）/ 三舱 80（12J+12W+56Y）；最大 90（单舱）                          | <https://en.wikipedia.org/wiki/Embraer_E-Jet_E2> （交叉：<https://extension.wikiwand.com/zh/articles/> 两舱80/最大90）                                                                                                         | passenger=88         | 88 介于两舱80与最大90之间，合理                  |
| 巡航 | 833 km/h（Mach 0.78，@35,000 ft）；最大 Mach 0.82（876 km/h）                           | <https://en.wikipedia.org/wiki/Embraer_E-Jet_E2>                                                                                                                                                                      | speed_kmh=886        | 游戏 886 接近最大 876，高于典型巡航 833           |

---

<a id="embraer_e190_e2"></a>

### Embraer E190-E2 (EMBRAER_E190_E2)

| 字段 | 真实值                                                                                  | 来源 URL                                                                                                                                                                                                                                                                            | 游戏内当前值               | 偏差/备注                  |
| -- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ---------------------- |
| 价格 | US$53.6 million（2013 目录价）；2018 报价约 US$60.8M；现行目录约 US$64.6M；airlineplanes 列价 US$59.1M | <https://en.wikipedia.org/wiki/Embraer_E-Jet_E2> （交叉：<https://aviatorinsider.com/airplane-brands/embraer-190/> US$60.8M 2018；https://www.aeroflap.com.br/en/saiba-quanto-custa-um-aviao-e-jet-da-embraer/ US$64.6M；<https://airlineplanes.com/aircraft/embraer-e190-e2> US$59.1M） | cost_factor=65       | 游戏系数 65，接近真实目录量级       |
| 航程 | 5,460 km（2,950 nmi，满载）；手册高速巡航 5,280 km（2,850 nmi）                                    | <https://en.wikipedia.org/wiki/Embraer_E-Jet_E2> （交叉：airlineplanes 5,330 km）                                                                                                                                                                                                      | range_km_est=5296 km | 接近（5296 vs 5460，差 ~3%） |
| 座级 | 三舱 97（9J+20W+68Y）；最大 114（单舱）                                                         | <https://en.wikipedia.org/wiki/Embraer_E-Jet_E2>                                                                                                                                                                                                                                  | passenger=97         | 97 正好等于三舱座级，吻合         |
| 巡航 | 833 km/h（Mach 0.78）；最大 876 km/h（Mach 0.82）                                           | <https://en.wikipedia.org/wiki/Embraer_E-Jet_E2>                                                                                                                                                                                                                                  | speed_kmh=886        | 游戏 886 接近最大 876        |

---

<a id="embraer_erj135"></a>

### Embraer ERJ-135 (EMBRAER_ERJ135)

| 字段 | 真实值                                                                     | 来源 URL                                                                                                               | 游戏内当前值               | 偏差/备注                |
| -- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------- | -------------------- |
| 价格 | US$16.5 million（年份未在页面标注）；维基无独立 ERJ-135 目录价（同族 1989–1996 年估计 US$11–15M） | <https://aerocorner.com/aircraft/embraer-erj-135/> （交叉：<https://en.wikipedia.org/wiki/Embraer_ERJ_family> 无独立 135 价） | cost_factor=14       | 游戏系数 14，量级合理；真实价年份不明 |
| 航程 | 3,240 km（1,750 nmi，ERJ-135LR）；约 3,241 km                                | <https://en.wikipedia.org/wiki/Embraer_ERJ_family> （交叉：aerocorner 文 "near 1,750 nmi / 3,241 km"）                     | range_km_est=3250 km | 几乎吻合（3250 vs 3240）   |
| 座级 | 37 人（最大）                                                                | <https://aerocorner.com/aircraft/embraer-erj-135/> （交叉：维基 37）                                                        | passenger=37         | 完全吻合                 |
| 巡航 | 831 km/h（Mach 0.78，最大巡航）；aerocorner 实时均值约 704 km/h（380 kt）              | <https://en.wikipedia.org/wiki/Embraer_ERJ_family> （交叉：aerocorner 最大巡航 Mach 0.78）                                    | speed_kmh=834        | 几乎吻合（834 vs 831）     |

---

<a id="embraer_erj140"></a>

### Embraer ERJ-140 (EMBRAER_ERJ140)

| 字段 | 真实值                           | 来源 URL                                                                                                                              | 游戏内当前值               | 偏差/备注                    |
| -- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------ |
| 价格 | US$15.2 million（2000）         | <https://aerocorner.com/aircraft/embraer-erj-140/> （交叉：<https://en.wikipedia.org/wiki/Embraer_ERJ_family> "launch cost ≈ US$15.2M"） | cost_factor=14       | 两源一致 US$15.2M；游戏系数 14 合理 |
| 航程 | 3,060 km（1,650 nmi，ERJ-140LR） | <https://en.wikipedia.org/wiki/Embraer_ERJ_family> （交叉：aerocorner 同族）                                                               | range_km_est=3052 km | 几乎吻合（3052 vs 3060）       |
| 座级 | 44 人（最大）                      | <https://aerocorner.com/aircraft/embraer-erj-140/> （交叉：维基 44）                                                                       | passenger=44         | 完全吻合                     |
| 巡航 | 831 km/h（Mach 0.78，最大巡航）      | <https://en.wikipedia.org/wiki/Embraer_ERJ_family>                                                                                  | speed_kmh=834        | 几乎吻合（834 vs 831）         |

---

<a id="embraer_e170lr"></a>

### Embraer 170 LR (Embraer_E170LR)

| 字段 | 真实值                                                                                 | 来源 URL                                                                                                | 游戏内当前值               | 偏差/备注                    |
| -- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------- | ------------------------ |
| 价格 | US$41 million（2016）                                                                 | <https://aerocorner.com/aircraft/embraer-170/> （维基未列 E170 独立价）                                        | cost_factor=25       | 游戏系数 25，量级合理             |
| 航程 | 基础 E170：3,982 km（2,150 nmi）；LR 为同型高 MTOW 远程型，航程更高（aerocorner 估约 3,889 km/2,100 nmi） | <https://en.wikipedia.org/wiki/Embraer_E-Jet> （交叉：aerocorner embraer-170 "near 2,100 nmi / 3,889 km"） | range_km_est=3850 km | 接近（3850 vs 3982 基础值）     |
| 座级 | 两舱 66（6J+60Y）；最大 78                                                                 | <https://en.wikipedia.org/wiki/Embraer_E-Jet> （交叉：aerocorner 78）                                      | passenger=78         | 78 = 最大座级，吻合             |
| 巡航 | 829 km/h（Mach 0.78）；最大 871 km/h（Mach 0.82）；aerocorner 称"接近 Mach 0.80"               | <https://en.wikipedia.org/wiki/Embraer_E-Jet> （交叉：aerocorner embraer-170）                             | speed_kmh=886        | 游戏 886 接近最大 871，高于典型 829 |

---

<a id="embraer_e170std"></a>

### Embraer 170 STD (Embraer_E170STD)

| 字段 | 真实值                                         | 来源 URL                                         | 游戏内当前值               | 偏差/备注                                                    |
| -- | ------------------------------------------- | ---------------------------------------------- | -------------------- | -------------------------------------------------------- |
| 价格 | US$41 million（2016，无 STD 独立价，同 E170 系列）     | <https://aerocorner.com/aircraft/embraer-170/> | cost_factor=24       | 游戏系数 24，略低于 LR                                           |
| 航程 | 基础 E170：3,982 km（2,150 nmi）；STD 即标准型，航程同基础值 | <https://en.wikipedia.org/wiki/Embraer_E-Jet>  | range_km_est=3300 km | 游戏 3300 低于真实基础 3982（STD/LR 游戏差值 550 km，真实 STD 与 LR 差距很小） |
| 座级 | 两舱 66；最大 78                                 | <https://en.wikipedia.org/wiki/Embraer_E-Jet>  | passenger=78         | = 最大座级                                                   |
| 巡航 | 829 km/h（Mach 0.78）；最大 871 km/h             | <https://en.wikipedia.org/wiki/Embraer_E-Jet>  | speed_kmh=886        | 同 E170LR                                                 |

---

<a id="embraer_e175lr"></a>

### Embraer 175 LR (Embraer_E175LR)

| 字段 | 真实值                                                                     | 来源 URL                                                                                                           | 游戏内当前值               | 偏差/备注                |
| -- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------- | -------------------- |
| 价格 | US$45.7 million（2016）；维基记 2018 二手价约 US$27M（非目录）                         | <https://aerocorner.com/aircraft/embraer-175/> （交叉：<https://en.wikipedia.org/wiki/Embraer_E-Jet> 2018 价值 US$27M） | cost_factor=27       | 游戏系数 27 接近真实目录量级     |
| 航程 | 基础 E175：4,074 km（2,200 nmi）；LR 为高 MTOW 远程型（更高）；airlineplanes 列 3,700 km | <https://en.wikipedia.org/wiki/Embraer_E-Jet> （交叉：<https://airlineplanes.com/aircraft/embraer-e175> 3,700 km）    | range_km_est=3850 km | 接近（3850 vs 4074 基础值） |
| 座级 | 两舱 76（12J+64Y）；最大 88                                                    | <https://en.wikipedia.org/wiki/Embraer_E-Jet> （交叉：aerocorner 86–88）                                              | passenger=86         | 86 接近最大 88，合理        |
| 巡航 | 829 km/h（Mach 0.78）；最大 871 km/h                                         | <https://en.wikipedia.org/wiki/Embraer_E-Jet>                                                                    | speed_kmh=886        | 游戏 886 接近最大 871      |

---

<a id="embraer_e175std"></a>

### Embraer 175 STD (Embraer_E175STD)

| 字段 | 真实值                                  | 来源 URL                                         | 游戏内当前值               | 偏差/备注                                           |
| -- | ------------------------------------ | ---------------------------------------------- | -------------------- | ----------------------------------------------- |
| 价格 | US$45.7 million（2016，无 STD 独立价）      | <https://aerocorner.com/aircraft/embraer-175/> | cost_factor=26       | 游戏系数 26                                         |
| 航程 | 基础 E175：4,074 km（2,200 nmi）；STD 即标准型 | <https://en.wikipedia.org/wiki/Embraer_E-Jet>  | range_km_est=3300 km | 游戏 3300 明显低于真实 4074（STD/LR 差值游戏设 550 km，真实差距很小） |
| 座级 | 两舱 76；最大 88                          | <https://en.wikipedia.org/wiki/Embraer_E-Jet>  | passenger=86         | 接近最大 88                                         |
| 巡航 | 829 km/h（Mach 0.78）；最大 871 km/h      | <https://en.wikipedia.org/wiki/Embraer_E-Jet>  | speed_kmh=886        | 同 E175LR                                        |

---

## 汇总备注

- **ERJ-135 / ERJ-140**：游戏四字段与真实值高度吻合（座级、航程、巡航几乎一致），仅价格系数无年份标注来源。
- **E175-E2 / E190-E2**：aerocorner 对应页面 404，主源改用英文维基；座级与航程吻合良好，游戏 speed_kmh(886) 取的是接近最大速度(Mach 0.82≈876) 而非典型巡航(833)。
- **E170 / E175（STD 与 LR）**：游戏对 STD/LR 的 range 差值(550 km)放大了真实差距——真实 STD 与 LR 航程差距很小（同基础机体、仅 MTOW 不同）；座级取最大布局合理；speed_kmh(886) 同样偏高。
- 价格字段：游戏 cost_factor 为相对系数，已在备注对照真实目录价（USD），非 1:1 换算。

<a id="embraer_e190ar"></a>

### Embraer 190 AR (Embraer_E190AR)

| 字段 | 真实值                                                     | 来源 URL                                                                                    | 游戏内当前值               | 偏差/备注                                     |
| -- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------- |
| 价格 | $51 million（目录参考价）                                      | <https://aerocorner.com/aircraft/embraer-190/>                                            | (游戏 cost_factor=59)  | 同机身型号；cost_factor 为相对系数                   |
| 航程 | AR 超程型（最长），较 LR 增 50 nmi（93 km）；基准型 2,450 nmi（4,537 km） | <https://en.wikipedia.org/wiki/Embraer_E-Jet> + <https://www.embraer.com/e-jets/e190/en/> | range_km_est 4400 km | 游戏 AR 4400 km，与基准 4,537 km 很接近；为家族最长，排序正确 |
| 座级 | 100 人（单级@32"）/ 最大 114 人                                 | <https://www.embraer.com/e-jets/e190/en/>                                                 | passenger 106 人      | 合理                                        |
| 巡航 | Mach 0.78（829 km/h，典型）；最大 0.82 Mach（约 871 km/h）         | <https://en.wikipedia.org/wiki/Embraer_E-Jet>                                             | speed_kmh 886 km/h   | 略高于最大巡航                                   |

<a id="embraer_e190lr"></a>

### Embraer 190 LR (Embraer_E190LR)

| 字段 | 真实值                                                                 | 来源 URL                                         | 游戏内当前值               | 偏差/备注                           |
| -- | ------------------------------------------------------------------- | ---------------------------------------------- | -------------------- | ------------------------------- |
| 价格 | $51 million（目录参考价）                                                  | <https://aerocorner.com/aircraft/embraer-190/> | (游戏 cost_factor=60)  | 同机身型号，真实目录价一致；cost_factor 为相对系数 |
| 航程 | LR 长程型，高于 STD；E190 家族基准 2,450 nmi（4,537 km），AR 较 LR 增 50 nmi（93 km） | <https://en.wikipedia.org/wiki/Embraer_E-Jet>  | range_km_est 4208 km | 游戏 LR 4208 km，接近基准上限，排序正确       |
| 座级 | 100 人（单级@32"）/ 最大 114 人                                             | <https://www.embraer.com/e-jets/e190/en/>      | passenger 106 人      | 合理                              |
| 巡航 | Mach 0.78（829 km/h，典型）；最大 0.82 Mach（约 871 km/h）                     | <https://en.wikipedia.org/wiki/Embraer_E-Jet>  | speed_kmh 886 km/h   | 略高于最大巡航                         |

<a id="embraer_e190std"></a>

### Embraer 190 STD (Embraer_E190STD)

| 字段 | 真实值                                             | 来源 URL                                                                                    | 游戏内当前值               | 偏差/备注                                            |
| -- | ----------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------ |
| 价格 | $51 million（目录参考价，aerocorner 未注年份）              | <https://aerocorner.com/aircraft/embraer-190/>                                            | (游戏 cost_factor=65)  | cost_factor 为相对系数；真实目录价约 $51M 作参考                |
| 航程 | ~2,400 nmi（约 4,448 km，E190 基准型）；子型号 STD<LR<AR   | <https://www.embraer.com/e-jets/e190/en/> + <https://en.wikipedia.org/wiki/Embraer_E-Jet> | range_km_est 3300 km | 游戏 STD 3300 km 偏低于基准 4,448 km；子型号排序 STD<LR<AR 正确 |
| 座级 | 100 人（单级@32"）/ 96 人（双级 8J+88Y）/ 最大 114 人        | <https://www.embraer.com/e-jets/e190/en/>                                                 | passenger 106 人      | 游戏 106 介于单级典型与最大之间，合理                            |
| 巡航 | Mach 0.78（829 km/h，典型）；最大 0.82 Mach（约 871 km/h） | <https://en.wikipedia.org/wiki/Embraer_E-Jet> + <https://www.embraer.com/e-jets/e190/en/> | speed_kmh 886 km/h   | 游戏 886 km/h 略高于最大巡航 871 km/h，基本合理                |

<a id="embraer_e195ar"></a>

### Embraer 195 AR (Embraer_E195AR)

| 字段 | 真实值                         | 来源 URL                                         | 游戏内当前值               | 偏差/备注                             |
| -- | --------------------------- | ---------------------------------------------- | -------------------- | --------------------------------- |
| 价格 | $53.5 million（2019，目录参考价）   | <https://aerocorner.com/aircraft/embraer-195/> | (游戏 cost_factor=37)  | 同机身；cost_factor 为相对系数             |
| 航程 | 4,077 km（AR 超程型，最长）         | <https://aerocorner.com/aircraft/embraer-195/> | range_km_est 4042 km | 游戏 4042 km 与真实 AR 4,077 km 几乎一致 ✔ |
| 座级 | 100 人（双级 12J+88Y）/ 最大 124 人 | <https://en.wikipedia.org/wiki/Embraer_E-Jet>  | passenger 118 人      | 合理                                |
| 巡航 | Mach 0.78（829 km/h）         | <https://en.wikipedia.org/wiki/Embraer_E-Jet>  | speed_kmh 886 km/h   | 略高于典型巡航                           |

<a id="embraer_e195lr"></a>

### Embraer 195 LR (Embraer_E195LR)

| 字段 | 真实值                         | 来源 URL                                         | 游戏内当前值               | 偏差/备注                             |
| -- | --------------------------- | ---------------------------------------------- | -------------------- | --------------------------------- |
| 价格 | $53.5 million（2019，目录参考价）   | <https://aerocorner.com/aircraft/embraer-195/> | (游戏 cost_factor=37)  | 同机身；cost_factor 为相对系数             |
| 航程 | 3,334 km（LR 长程型）            | <https://aerocorner.com/aircraft/embraer-195/> | range_km_est 3300 km | 游戏 3300 km 与真实 LR 3,334 km 几乎一致 ✔ |
| 座级 | 100 人（双级 12J+88Y）/ 最大 124 人 | <https://en.wikipedia.org/wiki/Embraer_E-Jet>  | passenger 118 人      | 合理                                |
| 巡航 | Mach 0.78（829 km/h）         | <https://en.wikipedia.org/wiki/Embraer_E-Jet>  | speed_kmh 886 km/h   | 略高于典型巡航                           |

<a id="embraer_e195std"></a>

### Embraer 195 STD (Embraer_E195STD)

| 字段 | 真实值                                      | 来源 URL                                                                                         | 游戏内当前值               | 偏差/备注                              |
| -- | ---------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------- | ---------------------------------- |
| 价格 | $53.5 million（2019，目录参考价）                | <https://aerocorner.com/aircraft/embraer-195/>                                                 | (游戏 cost_factor=37)  | cost_factor 为相对系数；真实目录价约 $53.5M    |
| 航程 | 2,594 km（STD 标准型，aerocorner Performance） | <https://aerocorner.com/aircraft/embraer-195/>                                                 | range_km_est 2558 km | 游戏 2558 km 与真实 STD 2,594 km 几乎一致 ✔ |
| 座级 | 100 人（双级 12J+88Y）/ 最大 124 人              | <https://en.wikipedia.org/wiki/Embraer_E-Jet> + <https://aerocorner.com/aircraft/embraer-195/> | passenger 118 人      | 游戏 118 介于双级与最大之间，合理                |
| 巡航 | Mach 0.78（829 km/h）                      | <https://en.wikipedia.org/wiki/Embraer_E-Jet>                                                  | speed_kmh 886 km/h   | 游戏 886 略高于典型巡航 829 km/h            |

<a id="embraer_e195_e2"></a>

### Embraer E195-E2 (Embraer_E195_E2)

| 字段 | 真实值                                                   | 来源 URL                                           | 游戏内当前值               | 偏差/备注                                          |
| -- | ----------------------------------------------------- | ------------------------------------------------ | -------------------- | ---------------------------------------------- |
| 价格 | $60.4 million（2013 单位成本）                              | <https://en.wikipedia.org/wiki/Embraer_E-Jet_E2> | (游戏 cost_factor=44)  | cost_factor 为相对系数；aerocorner 对应页面 404 未找到，改用维基 |
| 航程 | 3,000 nmi（5,600 km，brochure 满客航程，2024 升级后）            | <https://en.wikipedia.org/wiki/Embraer_E-Jet_E2> | range_km_est 4802 km | 游戏 4802 km 低于真实 5,600 km，偏差约 -14%              |
| 座级 | 120 人（三级 12J+24W+84Y）/ 最大 146 人                       | <https://en.wikipedia.org/wiki/Embraer_E-Jet_E2> | passenger 132 人      | 游戏 132 介于三级与最大之间，合理                            |
| 巡航 | Mach 0.78（833 km/h，@35,000 ft）；最大 0.82 Mach（876 km/h） | <https://en.wikipedia.org/wiki/Embraer_E-Jet_E2> | speed_kmh 890 km/h   | 游戏 890 高于最大巡航 876 km/h，略偏高                     |

<a id="embraer_erj145"></a>

### Embraer 145 (ERJ-145) (Embraer_ERJ145)

| 字段 | 真实值                                                      | 来源 URL                                                                                                  | 游戏内当前值               | 偏差/备注                                                   |
| -- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------- |
| 价格 | $21 million（aerocorner 当前参考）；历史 ~$14.5M（1995）/$15M（1996） | <https://aerocorner.com/aircraft/embraer-erj-145/> + <https://en.wikipedia.org/wiki/Embraer_ERJ_family> | (游戏 cost_factor=14)  | 游戏 intro_year=1994，历史价约 $14.5–15M 更贴合；cost_factor 为相对系数 |
| 航程 | 2,000 nmi（3,700 km，家族上限；145XR 同值）                        | <https://aerocorner.com/aircraft/embraer-erj-145/> + <https://en.wikipedia.org/wiki/Embraer_ERJ_family> | range_km_est 2832 km | 游戏 2832 km 低于真实 3,700 km，偏差约 -23%                       |
| 座级 | 50 人（典型）/ 最大 60 人                                        | <https://aerocorner.com/aircraft/embraer-erj-145/> + <https://en.wikipedia.org/wiki/Embraer_ERJ_family> | passenger 50 人       | 与真实典型座级完全一致 ✔                                           |
| 巡航 | Mach 0.78（829 km/h，基准）；最大 0.80 Mach（852 km/h，XR）         | <https://en.wikipedia.org/wiki/Embraer_ERJ_family> + <https://aerocorner.com/aircraft/embraer-erj-145/> | speed_kmh 829 km/h   | 游戏 829 km/h 与真实典型巡航 829 km/h 完全一致 ✔                     |

---

## 来源清单（实际读取）

- <https://aerocorner.com/aircraft/embraer-190/> （E190 价格/座级/巡航；Performance 子型号区间未列出）
- <https://aerocorner.com/aircraft/embraer-195/> （E195 价格$53.5M2019、座级、STD/LR/AR 航程 2594/3334/4077 km）
- <https://aerocorner.com/aircraft/embraer-erj-145/> （ERJ-145 价格$21M、座级50、航程3704km、最大速度833km/h）
- <https://www.embraer.com/e-jets/e190/en/> （E190 官方：0.82 Mach、114座、2,450nm/4537km、典型96双级/100单级）
- <https://en.wikipedia.org/wiki/Embraer_E-Jet> （E190/E195 巡航 Mach0.78=829km/h、双级/最大座级、子型号 AR 增程说明）
- <https://en.wikipedia.org/wiki/Embraer_E-Jet_E2> （E195-E2：$60.4M2013、满客航程5600km、120三级/146最大、巡航833km/h）
- <https://en.wikipedia.org/wiki/Embraer_ERJ_family> （ERJ-145：50/60座、3700km、Mach0.78/0.80、历史价$14.5–15M）
- 未找到可靠来源（404）：aerocorner 的 embraer-e190 / embraer-e195-e2 / embraer-195-e2 页面（E2 改用维基百科 E-Jet E2 页）

## 小结

- E195 三个子型号（STD/LR/AR）游戏航程与真实值几乎一致（误差<2%）。✔
- ERJ-145 座级(50)与巡航(829km/h)与真实完全一致；航程偏低约 23%。
- E190 子型号排序正确，游戏航程略低于官方基准(4537km)。
- E195-E2 航程(4802km)低于真实满客航程(5600km)约14%；巡航(890)略高于最大巡航(876)。
- 巡航速度整体游戏值偏高 3–7%（更接近最大巡航/马赫上限）。

### 福克 · Fokker

<a id="fokker_f27"></a>

### Fokker F27 Friendship (FOKKER_F27)

| 字段 | 真实值                           | 来源 URL                                                | 游戏内当前值               | 偏差/备注       |
| -- | ----------------------------- | ----------------------------------------------------- | -------------------- | ----------- |
| 价格 | £239,000（1960，RDa.6 型；未给 USD） | <https://en.wikipedia.org/wiki/Fokker_F27_Friendship> | (游戏 cost_factor=14)  | 仅英镑历史价      |
| 航程 | 2,600 km（1,400 nmi）           | <https://en.wikipedia.org/wiki/Fokker_F27_Friendship> | range_km_est 1600 km | 游戏偏低（约 62%） |
| 座级 | 52 人（最高；规格 44-52）             | <https://en.wikipedia.org/wiki/Fokker_F27_Friendship> | passenger 50 人       | 接近          |
| 巡航 | 460 km/h（250 kn）              | <https://en.wikipedia.org/wiki/Fokker_F27_Friendship> | speed_kmh 470 km/h   | 接近          |

<a id="fokker_f28"></a>

### Fokker F28 Fellowship (FOKKER_F28)

| 字段 | 真实值                                              | 来源 URL                                     | 游戏内当前值               | 偏差/备注       |
| -- | ------------------------------------------------ | ------------------------------------------ | -------------------- | ----------- |
| 价格 | 未找到可靠来源（维基未列价）                                   | <https://en.wikipedia.org/wiki/Fokker_F28> | (游戏 cost_factor=27)  | 历史/二手价难核实   |
| 航程 | 1,668 km（F28-2000，最大业载）至 2,872 km（F28-3000/4000） | <https://en.wikipedia.org/wiki/Fokker_F28> | range_km_est 2002 km | 介于各型之间，合理   |
| 座级 | 65-85 人（F28-4000 最高 85）                          | <https://en.wikipedia.org/wiki/Fokker_F28> | passenger 75 人       | 接近 F28-4000 |
| 巡航 | 808-848 km/h（最大巡航 458 kn；无马赫）                    | <https://en.wikipedia.org/wiki/Fokker_F28> | speed_kmh 820 km/h   | 接近（取低段）     |

<a id="fokker_f100"></a>

### Fokker 100 (Fokker_F100)

| 字段 | 真实值                                                 | 来源 URL                                     | 游戏内当前值               | 偏差/备注                 |
| -- | --------------------------------------------------- | ------------------------------------------ | -------------------- | --------------------- |
| 价格 | 未找到可靠来源（维基未列单价）                                     | <https://en.wikipedia.org/wiki/Fokker_100> | (游戏 cost_factor=27)  | 仅 1989 年 75 架总价订单，非单价 |
| 航程 | 3,170 km（1,710 nmi，Tay Mk650，最大业载）；Mk620 为 2,450 km | <https://en.wikipedia.org/wiki/Fokker_100> | range_km_est 3135 km | 吻合 Mk650              |
| 座级 | 122 人（最大）；97 人（两舱）                                  | <https://en.wikipedia.org/wiki/Fokker_100> | passenger 107 人      | 介于两舱与最大之间             |
| 巡航 | 845 km/h（456 kn，Mach 0.77）                          | <https://en.wikipedia.org/wiki/Fokker_100> | speed_kmh 846 km/h   | 完全一致                  |

<a id="fokker_f70"></a>

### Fokker 70 (Fokker_F70)

| 字段 | 真实值                    | 来源 URL                                    | 游戏内当前值               | 偏差/备注     |
| -- | ---------------------- | ----------------------------------------- | -------------------- | --------- |
| 价格 | 未找到可靠来源（维基未列价）         | <https://en.wikipedia.org/wiki/Fokker_70> | (游戏 cost_factor=18)  | 历史/二手价难核实 |
| 航程 | 3,410 km（1,841 nmi）    | <https://en.wikipedia.org/wiki/Fokker_70> | range_km_est 3382 km | 接近        |
| 座级 | 85 人（单级最高）/ 72 人（两舱）   | <https://en.wikipedia.org/wiki/Fokker_70> | passenger 79 人       | 接近两舱偏上    |
| 巡航 | 845 km/h（456 kn，无马赫标注） | <https://en.wikipedia.org/wiki/Fokker_70> | speed_kmh 838 km/h   | 接近        |

### 通用原子 · General Atomics

<a id="general_atomics_do228"></a>

### General Atomics DO 228 (GENERAL_ATOMICS_DO228)

| 字段 | 真实值                                                                                                     | 来源 URL                                         | 游戏内当前值               | 偏差/备注                                   |
| -- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------- | --------------------------------------- |
| 价格 | 无公开美元目录价（多为军用/特殊任务型）；最接近参考：RUAG Dornier 228NG 客机型 €5.2M（2010，未给美元换算）。通用原子 2020–21 收购产线后 Do228 NXT 无公开报价 | <https://en.wikipedia.org/wiki/Dornier_Do_228> | (游戏 cost_factor=14)  | 军用/特战改装为主，无可靠公开美元价                      |
| 航程 | 最大(转场) 2,363 km（1,276 nmi，547 kg 载荷）；典型(1,960 kg 载荷) 396 km（214 nmi）                                    | <https://en.wikipedia.org/wiki/Dornier_Do_228> | range_km_est 1028 km | 游戏取中间值；真实客货混合航程远低于 1028 km，转场可达 2363 km |
| 座级 | 19 人（228NG / HAL 19座型；原 228-100 为 15 座）                                                                 | <https://en.wikipedia.org/wiki/Dornier_Do_228> | passenger 19 人       | 一致                                      |
| 巡航 | 413 km/h（223 kt）                                                                                        | <https://en.wikipedia.org/wiki/Dornier_Do_228> | speed_kmh 432 km/h   | 接近（游戏略高 ~19 km/h）                       |

### 霍克·西德利 · Hawker_Siddeley

<a id="hs_trident"></a>

### Hawker Siddeley Trident (HS_TRIDENT)

| 字段 | 真实值                                                                                  | 来源 URL                                                  | 游戏内当前值               | 偏差/备注                |
| -- | ------------------------------------------------------------------------------------ | ------------------------------------------------------- | -------------------- | -------------------- |
| 价格 | US$7.8M（1972）                                                                        | <https://en.wikipedia.org/wiki/Hawker_Siddeley_Trident> | (游戏 cost_factor=37)  | 1972 年单位成本           |
| 航程 | 最大 4,350 km（2,350 nmi，Trident 2E）；Trident 1C 3,260 km；3B 3,600 km；Trident 1 2,170 km | <https://en.wikipedia.org/wiki/Hawker_Siddeley_Trident> | range_km_est 3856 km | 游戏取 2E/3B 之间，合理      |
| 座级 | 典型 101–115 人（2E 115）；3B 180 人；高密度可达 149–180                                          | <https://en.wikipedia.org/wiki/Hawker_Siddeley_Trident> | passenger 150 人      | 介于典型与 3B 之间，合理       |
| 巡航 | 约 980 km/h（>610 mph）；巡航 Mach 0.86–0.88；表列 FL300 巡航 937 km/h（1C）/917 km/h（1E）         | <https://en.wikipedia.org/wiki/Hawker_Siddeley_Trident> | speed_kmh 999 km/h   | 接近（游戏略高，约 Mach 0.94） |

### 伊尔 · Ilyushin

<a id="ilyushin_il114"></a>

### Ilyushin Il-114 (ILYUSHIN_IL114)

| 字段 | 真实值                                                                  | 来源 URL                                                                                                                               | 游戏内当前值                | 偏差/备注                       |
| -- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------- | --------------------------- |
| 价格 | 估算 US$10–11M（2008年币值；科普中国记2000年币值约US$10M，airplaneupdate记US$11M/2008） | <https://www.airplaneupdate.com/2019/03/ilyushin-il-114.html> ；<https://cloud.kepuchina.cn/newSearch/imgText?id=6973812556090904576> | (游戏 cost_factor=14)   | 量级合理，游戏系数偏低                 |
| 航程 | 1,000 km（Il-114 最大载重）/ 1,400 km（Il-114-100）/ ~2,000 km（Il-114-300）   | <https://en.wikipedia.org/wiki/Ilyushin_Il-114>                                                                                      | range_km_est 1,199 km | 基本吻合 base 型（游戏取约1,000 km 级） |
| 座级 | 64（基本型）/ 68（Il-114-300）                                              | <https://en.wikipedia.org/wiki/Ilyushin_Il-114>                                                                                      | passenger 64 人        | 一致                          |
| 巡航 | 470 km/h（高速巡航）/ 500 km/h（最大）                                         | <https://en.wikipedia.org/wiki/Ilyushin_Il-114>                                                                                      | speed_kmh 500 km/h    | 一致                          |

<a id="ilyushin_il18"></a>

### Ilyushin Il-18 (ILYUSHIN_IL18)

| 字段 | 真实值                               | 来源 URL                                         | 游戏内当前值                | 偏差/备注   |
| -- | --------------------------------- | ---------------------------------------------- | --------------------- | ------- |
| 价格 | 未找到可靠来源（老式机，无公开目录价）               | —                                              | (游戏 cost_factor=25)   | 无可靠来源   |
| 航程 | 6,500 km（Il-18D，最大燃油+6,500 kg 载荷） | <https://en.wikipedia.org/wiki/Ilyushin_Il-18> | range_km_est 6,501 km | 一致      |
| 座级 | 65–120（最大120）                     | <https://en.wikipedia.org/wiki/Ilyushin_Il-18> | passenger 110 人       | 合理（取中值） |
| 巡航 | 625 km/h                          | <https://en.wikipedia.org/wiki/Ilyushin_Il-18> | speed_kmh 625 km/h    | 一致      |

<a id="ilyushin_il96"></a>

### Ilyushin Il-96 (ILYUSHIN_IL96)

| 字段 | 真实值                                                                          | 来源 URL                                                                                                 | 游戏内当前值                 | 偏差/备注             |
| -- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------- | ----------------- |
| 价格 | 估算 ~US$130–300M（无公开成交价；媒体对比A330约US$120M，四发Il-96约US$131M—网易；400M原型预算约US$163M） | <https://www.163.com/dy/article/I5HI60UE0535B99I.html> ；<https://en.wikipedia.org/wiki/Ilyushin_Il-96> | (游戏 cost_factor=187)   | 游戏系数偏高但量级合理       |
| 航程 | 10,000 km（Il-96-300）/ ~11,000 km（262座两舱）/ 11,482 km（Il-96M）                  | <https://en.wikipedia.org/wiki/Ilyushin_Il-96>                                                         | range_km_est 11,000 km | 一致                |
| 座级 | 262（两舱，Il-96-300）/ 最多300；Il-96-400 两舱386/最多436                               | <https://en.wikipedia.org/wiki/Ilyushin_Il-96>                                                         | passenger 280 人        | 合理                |
| 巡航 | 850–870 km/h（Mach 0.78–0.84）                                                 | <https://en.wikipedia.org/wiki/Ilyushin_Il-96>                                                         | speed_kmh 926 km/h     | 游戏值偏高（现实约850–870） |

<a id="ilyushin_62"></a>

### Ilyushin Il-62 (Ilyushin_62)

| 字段 | 真实值                            | 来源 URL                                         | 游戏内当前值                | 偏差/备注   |
| -- | ------------------------------ | ---------------------------------------------- | --------------------- | ------- |
| 价格 | 未找到可靠来源（老式机，无公开目录价）            | —                                              | (游戏 cost_factor=169)  | 无可靠来源   |
| 航程 | 10,000 km（Il-62M）              | <https://en.wikipedia.org/wiki/Ilyushin_Il-62> | range_km_est 9,900 km | 一致      |
| 座级 | 168–186（Il-62M，最大186）；基本型最多198 | <https://en.wikipedia.org/wiki/Ilyushin_Il-62> | passenger 168 人       | 一致（取低值） |
| 巡航 | 900 km/h（Il-62M）；基本型约850 km/h  | <https://en.wikipedia.org/wiki/Ilyushin_Il-62> | speed_kmh 822 km/h    | 游戏值偏低   |

<a id="ilyushin_76"></a>

### Ilyushin Il-76 (Ilyushin_76)

| 字段 | 真实值                                                      | 来源 URL                                            | 游戏内当前值                | 偏差/备注      |
| -- | -------------------------------------------------------- | ------------------------------------------------- | --------------------- | ---------- |
| 价格 | ~US$50M（2008，aerocorner 列表价）                             | <https://aerocorner.com/aircraft/ilyushin-il-76/> | (游戏 cost_factor=44)   | 合理         |
| 航程 | 设计目标5,000 km（载40 t，维基设计需求）；实际最大载重约4,400 km，转场可达~6,000 km | <https://en.wikipedia.org/wiki/Ilyushin_Il-76>    | range_km_est 6,600 km | 游戏取转场上限，略高 |
| 座级 | 0（货运/战略运输机，载货40–60 t，或伞兵约145–225人）                       | <https://aerocorner.com/aircraft/ilyushin-il-76/> | passenger 0 人         | 一致（货机，无客座） |
| 巡航 | ~852 km/h（460 kt）                                        | <https://aerocorner.com/aircraft/ilyushin-il-76/> | speed_kmh 798 km/h    | 合理（游戏略低）   |

### 伊尔库特 · Irkut

<a id="irkut_mc21"></a>

### Irkut MC-21 (IRKUT_MC21)

| 字段 | 真实值                                         | 来源 URL                                                                                                                        | 游戏内当前值                | 偏差/备注  |
| -- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------ |
| 价格 | MC-21-200 US$72M，MC-21-300 US$91M（估算，约2013） | <https://en.wikipedia.org/wiki/Irkut_MC-21>                                                                                   | (游戏 cost_factor=73)   | 游戏系数偏低 |
| 航程 | 6,000 km（MC-21-300 两舱）；MC-21-200 6,400 km   | <https://en.wikipedia.org/wiki/Irkut_MC-21>                                                                                   | range_km_est 6,000 km | 一致     |
| 座级 | 163（两舱，MC-21-300）/ 最多211；MC-21-200 最多165    | <https://en.wikipedia.org/wiki/Irkut_MC-21>                                                                                   | passenger 180 人       | 合理     |
| 巡航 | 870 km/h（Mach 0.80–0.82）                    | <http://www.aircrafttotal.nl/Yakovlev_MC21_Airliner.html> ；<https://airlines-inform.com/commercial-aircraft/Irkut-MS-21.html> | speed_kmh 902 km/h    | 游戏值略高  |

### LET · LET

<a id="let_l410"></a>

### LET L-410 (LET_L410)

| 字段 | 真实值                                                                  | 来源 URL                                    | 游戏内当前值               | 偏差/备注                  |
| -- | -------------------------------------------------------------------- | ----------------------------------------- | -------------------- | ---------------------- |
| 价格 | 未找到可靠来源（维基无价；公开网络检索未得可信目录价）                                          | <https://en.wikipedia.org/wiki/Let_L-410> | (游戏 cost_factor=14)  | 无公开美元目录价               |
| 航程 | 1,500 km（810 nmi，UVP-E20，1,800 kg 载荷）；原始型 1,520 km；L 410 NG 2,500 km | <https://en.wikipedia.org/wiki/Let_L-410> | range_km_est 1380 km | 略低于 UVP-E20 标称 1500 km |
| 座级 | 19 人（UVP-E20 / UVP-E 生产型最大）；UVP 仅 15 人                               | <https://en.wikipedia.org/wiki/Let_L-410> | passenger 19 人       | 一致                     |
| 巡航 | 405 km/h（219 kt，UVP-E20 最大巡航）；NG 413 km/h                            | <https://en.wikipedia.org/wiki/Let_L-410> | speed_kmh 405 km/h   | 完全一致                   |

### 洛克希德 · Lockheed

<a id="lockheed_l1011"></a>

### Lockheed L-1011 TriStar (LOCKHEED_L1011)

| 字段 | 真实值                                               | 来源 URL                                                  | 游戏内当前值               | 偏差/备注               |
| -- | ------------------------------------------------- | ------------------------------------------------------- | -------------------- | ------------------- |
| 价格 | US$20M（1972；约 2024 年 $113M）                       | <https://en.wikipedia.org/wiki/Lockheed_L-1011_TriStar> | (游戏 cost_factor=155) | 历史新机目录价             |
| 航程 | 9,899 km（5,345 nmi，L-1011-500 最大业载）；-1 为 4,963 km | <https://en.wikipedia.org/wiki/Lockheed_L-1011_TriStar> | range_km_est 9894 km | 吻合 -500             |
| 座级 | 256 人（混合级，-1）；最高 400（出口限制）                        | <https://en.wikipedia.org/wiki/Lockheed_L-1011_TriStar> | passenger 256 人      | 完全一致                |
| 巡航 | 963-972 km/h（520-525 kn）；Mmo Mach 0.9             | <https://en.wikipedia.org/wiki/Lockheed_L-1011_TriStar> | speed_kmh 983 km/h   | 略高（接近 Mmo 956 km/h） |

<a id="lockheed_l188"></a>

### Lockheed L-188 Electra (LOCKHEED_L188)

| 字段 | 真实值                                  | 来源 URL                                                 | 游戏内当前值               | 偏差/备注       |
| -- | ------------------------------------ | ------------------------------------------------------ | -------------------- | ----------- |
| 价格 | 未找到可靠来源（维基未列价）                       | <https://en.wikipedia.org/wiki/Lockheed_L-188_Electra> | (游戏 cost_factor=18)  | 历史/二手价难核实   |
| 航程 | 4,460 km（2,410 nmi，典型）；最大业载 3,500 km | <https://en.wikipedia.org/wiki/Lockheed_L-188_Electra> | range_km_est 3998 km | 接近典型值       |
| 座级 | 98 人（高密度最高）                          | <https://en.wikipedia.org/wiki/Lockheed_L-188_Electra> | passenger 100 人      | 基本一致        |
| 巡航 | 600 km/h（324 kn）                     | <https://en.wikipedia.org/wiki/Lockheed_L-188_Electra> | speed_kmh 515 km/h   | 游戏偏低（约 86%） |

<a id="lockheed_l049_constellation"></a>

### Lockheed L-049 Constellation (Lockheed_L049_Constellation)

| 字段 | 真实值                                             | 来源 URL                                                       | 游戏内当前值               | 偏差/备注                      |
| -- | ----------------------------------------------- | ------------------------------------------------------------ | -------------------- | -------------------------- |
| 价格 | US$450,000（≈1940，研制期 Excalibur/L-049 设计售价，非交付价） | <https://en.wikipedia.org/wiki/Lockheed_L-049_Constellation> | (游戏 cost_factor=35)  | 仅战前设计估值，无交付目录价             |
| 航程 | 6,429 km（3,472 nmi，最大燃油）；最大业载 3,685 km          | <https://en.wikipedia.org/wiki/Lockheed_L-049_Constellation> | range_km_est 7315 km | 游戏取最大燃油 6429 之上再偏高（约 +14%） |
| 座级 | 81 人（最高；规格 40-81）                               | <https://en.wikipedia.org/wiki/Lockheed_L-049_Constellation> | passenger 81 人       | 完全一致                       |
| 巡航 | 504 km/h（272 kn，313 mph）                        | <https://en.wikipedia.org/wiki/Lockheed_L-049_Constellation> | speed_kmh 504 km/h   | 完全一致                       |

### 麦道 · McDonnell_Douglas

<a id="douglas_dc3"></a>

### Douglas DC-3 (DOUGLAS_DC3)

| 字段 | 真实值                                         | 来源 URL                                                                                         | 游戏内当前值               | 偏差/备注                      |
| -- | ------------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------- | -------------------------- |
| 价格 | $79,000（1936 新机出厂价；维基交叉为 $60,000–$80,000）   | <https://aerocorner.com/aircraft/douglas-dc-3/> ; <https://en.wikipedia.org/wiki/Douglas_DC-3> | (游戏 cost_factor=25)  | 活塞机仅历史出厂价                  |
| 航程 | 2,400 km（典型）/ 2,540 km（最大燃油，1,370 nmi）      | <https://en.wikipedia.org/wiki/Douglas_DC-3>                                                   | range_km_est 2602 km | 基本一致（游戏 2602 vs 真实最大 2540） |
| 座级 | 21–32 人（典型）/ 32 人（最大）                       | <https://aerocorner.com/aircraft/douglas-dc-3/> ; <https://en.wikipedia.org/wiki/Douglas_DC-3> | passenger 30 人       | 合理（游戏 30 在 21–32 区间）       |
| 巡航 | 333 km/h（207 mph，介绍值）/ 339 km/h（183 kn，规格表） | <https://en.wikipedia.org/wiki/Douglas_DC-3>                                                   | speed_kmh 333 km/h   | 完全一致                       |

---

<a id="douglas_dc6"></a>

### Douglas DC-6 (DOUGLAS_DC6)

| 字段 | 真实值                                                                                          | 来源 URL                                       | 游戏内当前值               | 偏差/备注                          |
| -- | -------------------------------------------------------------------------------------------- | -------------------------------------------- | -------------------- | ------------------------------ |
| 价格 | 未找到可靠原始美元出厂价；来源仅列英镑 £210,000–£230,000（1946–47），按 1947 年汇率≈$4.03/£ 折算约 $0.85M–$0.93M（折算值仅供参考） | <https://en.wikipedia.org/wiki/Douglas_DC-6> | (游戏 cost_factor=35)  | 活塞机，来源无 USD；GBP 引自 Flight 1960 |
| 航程 | 7,377 km（3,983 nmi，DC-6）/ 7,995 km（4,317 nmi，DC-6B 最大燃油）                                     | <https://en.wikipedia.org/wiki/Douglas_DC-6> | range_km_est 8398 km | 游戏略高（8398 vs 真实 7995）          |
| 座级 | 48–68 人（DC-6）/ 42–89 人（DC-6B）                                                                | <https://en.wikipedia.org/wiki/Douglas_DC-6> | passenger 81 人       | 偏高（真实典型约 53–68；81 接近 DC-6B 上限） |
| 巡航 | 501 km/h（311 mph，DC-6）/ 507 km/h（DC-6A）                                                      | <https://en.wikipedia.org/wiki/Douglas_DC-6> | speed_kmh 504 km/h   | 基本一致                           |

---

<a id="douglas_dc7"></a>

### Douglas DC-7 (DOUGLAS_DC7)

| 字段 | 真实值                                                                   | 来源 URL                                       | 游戏内当前值               | 偏差/备注                          |
| -- | --------------------------------------------------------------------- | -------------------------------------------- | -------------------- | ------------------------------ |
| 价格 | $823,308（新机基础型，约 1953–58）；DC-7B $982,226（1955）；DC-7C $1,155,560（1956） | <https://en.wikipedia.org/wiki/Douglas_DC-7> | (游戏 cost_factor=35)  | 活塞机历史出厂价（Flight 1960 / Jane's） |
| 航程 | 9,069 km（4,897 nmi，DC-7C 最大燃油）；基础型更低                                  | <https://en.wikipedia.org/wiki/Douglas_DC-7> | range_km_est 9202 km | 基本一致（游戏 9202 vs 7C 最大 9069）    |
| 座级 | 最多 105 人（DC-7C）/ 典型更少                                                 | <https://en.wikipedia.org/wiki/Douglas_DC-7> | passenger 95 人       | 合理（典型配置低于 105）                 |
| 巡航 | 557 km/h（346 mph，301 kn，DC-7C）                                        | <https://en.wikipedia.org/wiki/Douglas_DC-7> | speed_kmh 504 km/h   | 游戏偏低约 53 km/h（约 -9.5%）         |

---

<a id="douglas_dc10_10"></a>

### Douglas DC-10-10 (Douglas_DC10_10)

| 字段 | 真实值                                               | 来源 URL                                                  | 游戏内当前值               | 偏差/备注                  |
| -- | ------------------------------------------------- | ------------------------------------------------------- | -------------------- | ---------------------- |
| 价格 | $20,000,000（1972 列表价，DC-10 家族通用；无 -10 单独报价）       | <https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-10> | (游戏 cost_factor=139) | 家族共用价                  |
| 航程 | 6,500 km（3,500 nmi，规格表）/ 6,100 km（3,300 nmi，典型载荷） | <https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-10> | range_km_est 6050 km | 基本一致                   |
| 座级 | 270 人（两舱：222Y+48J）/ 最多 399（出口限 380）               | <https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-10> | passenger 255 人      | 接近两舱 270（低 15）         |
| 巡航 | 876 km/h（Mach 0.82，473 kn）/ MMo 940 km/h          | <https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-10> | speed_kmh 983 km/h   | 游戏偏高约 107 km/h（约 +12%） |

---

<a id="douglas_dc10_30"></a>

### Douglas DC-10-30 (Douglas_DC10_30)

| 字段 | 真实值                                                                | 来源 URL                                                  | 游戏内当前值                | 偏差/备注                                         |
| -- | ------------------------------------------------------------------ | ------------------------------------------------------- | --------------------- | --------------------------------------------- |
| 价格 | $20,000,000（1972 列表价通用；无 -30 单独报价）                                 | <https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-10> | (游戏 cost_factor=155)  | 家族共用价                                         |
| 航程 | 9,600 km（5,200 nmi，规格表）/ 10,010 km（5,410 nmi，典型载荷）；-30ER 10,620 km | <https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-10> | range_km_est 10505 km | 游戏 10505 接近典型载荷 10010 / ER 10620；基础型规格表为 9600 |
| 座级 | 270 人（两舱）/ 最多 399                                                  | <https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-10> | passenger 255 人       | 接近两舱 270                                      |
| 巡航 | 876 km/h（Mach 0.82）                                                | <https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-10> | speed_kmh 983 km/h    | 游戏偏高约 107 km/h（约 +12%）                        |

---

<a id="douglas_dc10_40"></a>

### Douglas DC-10-40 (Douglas_DC10_40)

| 字段 | 真实值                                               | 来源 URL                                                  | 游戏内当前值               | 偏差/备注                  |
| -- | ------------------------------------------------- | ------------------------------------------------------- | -------------------- | ---------------------- |
| 价格 | $20,000,000（1972 列表价通用；无 -40 单独报价）                | <https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-10> | (游戏 cost_factor=146) | 家族共用价（P\&W 发动机型，原 -20） |
| 航程 | 9,400 km（5,100 nmi，规格表）/ 9,250 km（5,000 nmi，典型载荷） | <https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-10> | range_km_est 9158 km | 基本一致                   |
| 座级 | 270 人（两舱）/ 最多 399                                 | <https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-10> | passenger 255 人      | 接近两舱 270               |
| 巡航 | 876 km/h（Mach 0.82）                               | <https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-10> | speed_kmh 983 km/h   | 游戏偏高约 107 km/h（约 +12%） |

---

<a id="douglas_dc8_10"></a>

### Douglas DC-8-10 (Douglas_DC8_10)

| 字段 | 真实值                                                                     | 来源 URL                                                                                                                    | 游戏内当前值               | 偏差/备注             |
| -- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------- |
| 价格 | ~$5.8M（1955 年 30 架 DC-8A 订单共 $175M，折合每架≈$5.83M；非单独列表价；现代二手 $1.8M–$3.6M） | <https://airwaysmag.com/new-post/maiden-douglas-dc-8> ; <https://www.businessairnews.com/hb_aircraftpage.html?recnum=DC8> | (游戏 cost_factor=37)  | 订单折算价，无单独出厂目录价    |
| 航程 | 6,960 km（3,760 nmi，最大载荷）                                                | <https://en.wikipedia.org/wiki/Douglas_DC-8>                                                                              | range_km_est 6902 km | 基本一致              |
| 座级 | 177 人（最大）                                                               | <https://en.wikipedia.org/wiki/Douglas_DC-8>                                                                              | passenger 177 人      | 完全一致              |
| 巡航 | 895 km/h（Mach 0.82，483 kn）                                              | <https://en.wikipedia.org/wiki/Douglas_DC-8> ; <https://www.modernairliners.com/douglas-dc8/>                             | speed_kmh 902 km/h   | 基本一致（游戏略高 7 km/h） |

---

<a id="douglas_dc8_20"></a>

### Douglas DC-8-20 (Douglas_DC8_20)

| 字段 | 真实值                        | 来源 URL                                                | 游戏内当前值               | 偏差/备注   |
| -- | -------------------------- | ----------------------------------------------------- | -------------------- | ------- |
| 价格 | ~$5.8M（同上 1955 订单折算；无单独报价） | <https://airwaysmag.com/new-post/maiden-douglas-dc-8> | (游戏 cost_factor=38)  | 家族共用参考价 |
| 航程 | 7,500 km（4,050 nmi）        | <https://en.wikipedia.org/wiki/Douglas_DC-8>          | range_km_est 7425 km | 基本一致    |
| 座级 | 177 人（最大）                  | <https://en.wikipedia.org/wiki/Douglas_DC-8>          | passenger 177 人      | 完全一致    |
| 巡航 | 895 km/h（Mach 0.82）        | <https://en.wikipedia.org/wiki/Douglas_DC-8>          | speed_kmh 902 km/h   | 基本一致    |

---

<a id="douglas_dc8_30"></a>

### Douglas DC-8-30 (Douglas_DC8_30)

| 字段 | 真实值                 | 来源 URL                                                | 游戏内当前值               | 偏差/备注            |
| -- | ------------------- | ----------------------------------------------------- | -------------------- | ---------------- |
| 价格 | ~$5.8M（同上参考；无单独报价）  | <https://airwaysmag.com/new-post/maiden-douglas-dc-8> | (游戏 cost_factor=39)  | 家族共用参考价          |
| 航程 | 7,417 km（4,005 nmi） | <https://en.wikipedia.org/wiki/Douglas_DC-8>          | range_km_est 7342 km | 基本一致（游戏略低 75 km） |
| 座级 | 177 人（最大）           | <https://en.wikipedia.org/wiki/Douglas_DC-8>          | passenger 177 人      | 完全一致             |
| 巡航 | 895 km/h（Mach 0.82） | <https://en.wikipedia.org/wiki/Douglas_DC-8>          | speed_kmh 902 km/h   | 基本一致             |

---

<a id="douglas_dc8_40"></a>

### Douglas DC-8-40 (Douglas_DC8_40)

| 字段 | 真实值                                              | 来源 URL                                                | 游戏内当前值               | 偏差/备注               |
| -- | ------------------------------------------------ | ----------------------------------------------------- | -------------------- | ------------------- |
| 价格 | ~$5.8M（同上参考；无单独报价）                               | <https://airwaysmag.com/new-post/maiden-douglas-dc-8> | (游戏 cost_factor=38)  | 家族共用参考价             |
| 航程 | 9,830 km（5,310 nmi，-40）/ 7,800 km（4,200 nmi，-43） | <https://en.wikipedia.org/wiki/Douglas_DC-8>          | range_km_est 9735 km | 基本一致（接近 -40 的 9830） |
| 座级 | 177 人（最大）                                        | <https://en.wikipedia.org/wiki/Douglas_DC-8>          | passenger 177 人      | 完全一致                |
| 巡航 | 895 km/h（Mach 0.82）                              | <https://en.wikipedia.org/wiki/Douglas_DC-8>          | speed_kmh 902 km/h   | 基本一致                |

---

<a id="douglas_dc8_50"></a>

### Douglas DC-8-50 (Douglas_DC8_50)

| 字段 | 真实值                                               | 来源 URL                                                | 游戏内当前值                | 偏差/备注                |
| -- | ------------------------------------------------- | ----------------------------------------------------- | --------------------- | -------------------- |
| 价格 | ~$5.8M（同上参考；无单独报价）                                | <https://airwaysmag.com/new-post/maiden-douglas-dc-8> | (游戏 cost_factor=41)   | 家族共用参考价              |
| 航程 | 10,843 km（5,855 nmi，-50）/ 8,700 km（4,700 nmi，-55） | <https://en.wikipedia.org/wiki/Douglas_DC-8>          | range_km_est 10725 km | 基本一致（接近 -50 的 10843） |
| 座级 | 189 人（最大，-50/55）                                  | <https://en.wikipedia.org/wiki/Douglas_DC-8>          | passenger 189 人       | 完全一致                 |
| 巡航 | 895 km/h（Mach 0.82）                               | <https://en.wikipedia.org/wiki/Douglas_DC-8>          | speed_kmh 902 km/h    | 基本一致                 |

---

<a id="douglas_dc9_10"></a>

### Douglas DC-9-10 (Douglas_DC9_10)

| 字段 | 真实值                                                                        | 来源 URL                                                                                                                                                                                          | 游戏内当前值               | 偏差/备注                              |
| -- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ---------------------------------- |
| 价格 | 未找到可靠历史出厂目录价；2024–25 二手挂牌约 $485,000–$6,500,000（按配置/机况，DC-9-10 多落低端）        | <https://avpay.aero/aircraft-for-sale/model/mcdonnell-douglas-dc-9-10>                                                                                                                          | (游戏 cost_factor=38)  | 历史出厂价缺失，仅有现代二手区间                   |
| 航程 | 约 2,343 km（1,265 nmi，最大）/ 1,760 km（950 nmi，50 人典型）；最大载荷仅 1,055 km（570 nmi） | <https://www.airliners.net/aircraft-data/stats.main?id=276> ; <https://avpay.aero/aircraft-for-sale/model/mcdonnell-douglas-dc-9-10> ; <https://plane.spottingworld.com/McDonnell_Douglas_DC-9> | range_km_est 2915 km | 游戏偏高约 570 km（约 +24%）；真实最大约 2343 km |
| 座级 | 90 人（单级最大）/ 典型 80（单级）或 72（混合舱）                                             | <https://www.airliners.net/aircraft-data/stats.main?id=276> ; <https://plane.spottingworld.com/McDonnell_Douglas_DC-9>                                                                          | passenger 90 人       | 完全一致（取最大座级）                        |
| 巡航 | 903 km/h（561 mph，488 kn，Mach≈0.85）/ 经济巡航 885 km/h                          | <https://www.airliners.net/aircraft-data/stats.main?id=276> ; <https://plane.spottingworld.com/McDonnell_Douglas_DC-9> ; <https://www.thisdayinaviation.com/tag/long-beach-airport/>            | speed_kmh 902 km/h   | 几乎完全一致                             |

---

## 汇总备注

- 活塞机（DC-3/DC-6/DC-7）：仅有历史出厂价或英镑价，已注明；DC-3 与 DC-7 有可靠 USD，DC-6 仅有 GBP（已折算参考）。
- DC-10 三型：唯一可靠价为 1972 年 $20M 家族列表价，无分型号报价；巡航真实约 876 km/h，游戏统一填 983 km/h，系统性偏高约 12%。
- DC-8 五型：无分型号出厂目录价，采用 1955 年 30 架 $175M 订单折算的 ~$5.8M 作参考；座级与巡航游戏值高度吻合（DC-8-50 座级 189 完全一致）。
- DC-9-10：座级 90、巡航 902 km/h 与真实几乎完全一致；航程游戏 2915 km 明显高于真实最大约 2343 km。
- aerocorner 实际读取成功的家族页：DC-3、DC-8；DC-6/DC-7/DC-10/DC-9 家族页均 404，改用维基与 WebSearch（airliners.net / avpay / spottingworld / airwaysmag）交叉核对。

<a id="douglas_dc9_20"></a>

### Douglas DC-9-20 (Douglas_DC9_20)

| 字段 | 真实值                                               | 来源 URL                                                       | 游戏内当前值                | 偏差/备注                                      |
| -- | ------------------------------------------------- | ------------------------------------------------------------ | --------------------- | ------------------------------------------ |
| 价格 | 未找到可靠来源                                           | —                                                            | (游戏 cost_factor=38)   | aerocorner 页面无价格；维基信息框 41.5–48.5M 为错误值，未采用 |
| 航程 | 2,687 km（1,450 nmi，最大燃油）；1,852 km（1,000 nmi，最大业载） | <https://aerocorner.com/aircraft/mcdonnell-douglas-dc-9-20/> | range_km_est 2,942 km | 接近；游戏略高                                    |
| 座级 | 90 人（最大）                                          | <https://aerocorner.com/aircraft/mcdonnell-douglas-dc-9-20/> | passenger 90 人        | 一致                                         |
| 巡航 | 898 km/h（485 kt，最大巡航，DC-9 家族值）                    | <https://aerocorner.com/aircraft/mcdonnell-douglas-dc-9-30/> | speed_kmh 902 km/h    | 基本一致                                       |

<a id="douglas_dc9_30"></a>

### Douglas DC-9-30 (Douglas_DC9_30)

| 字段 | 真实值                     | 来源 URL                                                       | 游戏内当前值                | 偏差/备注          |
| -- | ----------------------- | ------------------------------------------------------------ | --------------------- | -------------- |
| 价格 | 未找到可靠来源                 | —                                                            | (游戏 cost_factor=42)   | aerocorner 无价格 |
| 航程 | 2,778 km（1,500 nmi，典型）  | <https://aerocorner.com/aircraft/mcdonnell-douglas-dc-9-30/> | range_km_est 3,052 km | 游戏略高           |
| 座级 | 115 人（经济）；最多 127 人（高密度） | <https://aerocorner.com/aircraft/mcdonnell-douglas-dc-9-30/> | passenger 115 人       | 一致             |
| 巡航 | 898 km/h（485 kt，最大巡航）   | <https://aerocorner.com/aircraft/mcdonnell-douglas-dc-9-30/> | speed_kmh 918 km/h    | 接近             |

<a id="douglas_dc9_40"></a>

### Douglas DC-9-40 (Douglas_DC9_40)

| 字段 | 真实值                                    | 来源 URL                                                              | 游戏内当前值                | 偏差/备注      |
| -- | -------------------------------------- | ------------------------------------------------------------------- | --------------------- | ---------- |
| 价格 | 520 万美元（1972）                          | <https://aerocorner.com/aircraft/mcdonnell-douglas-dc-9-40/> （亦见维基） | (游戏 cost_factor=43)   | 真实价远低于后期机型 |
| 航程 | 约 2,880 km（最大，交叉来源；aerocorner/维基正文未单列） | <https://baike.baidu.com/view/3227725.htm>                          | range_km_est 2,860 km | 基本一致       |
| 座级 | 125 人（最大）                              | <https://aerocorner.com/aircraft/mcdonnell-douglas-dc-9-40/>        | passenger 125 人       | 一致         |
| 巡航 | 898 km/h（485 kt，最大巡航，家族值）              | <https://aerocorner.com/aircraft/mcdonnell-douglas-dc-9-30/>        | speed_kmh 894 km/h    | 一致         |

<a id="douglas_dc9_50"></a>

### Douglas DC-9-50 (Douglas_DC9_50)

| 字段 | 真实值                   | 来源 URL                                                       | 游戏内当前值                | 偏差/备注      |
| -- | --------------------- | ------------------------------------------------------------ | --------------------- | ---------- |
| 价格 | 520 万美元（1972）         | <https://aerocorner.com/aircraft/mcdonnell-douglas-dc-9-50/> | (游戏 cost_factor=44)   | 真实价远低于后期机型 |
| 航程 | 2,408 km（1,300 nmi）   | <https://aerocorner.com/aircraft/mcdonnell-douglas-dc-9-50/> | range_km_est 3,300 km | 游戏偏高约 37%  |
| 座级 | 139 人（最大）             | <https://aerocorner.com/aircraft/mcdonnell-douglas-dc-9-50/> | passenger 135 人       | 接近         |
| 巡航 | 898 km/h（485 kt，最大巡航） | <https://aerocorner.com/aircraft/mcdonnell-douglas-dc-9-50/> | speed_kmh 918 km/h    | 接近         |

<a id="mcdonnell_douglas_md11"></a>

### McDonnell Douglas MD-11 (McDonnell_Douglas_MD11)

| 字段 | 真实值                                         | 来源 URL                                                           | 游戏内当前值                 | 偏差/备注    |
| -- | ------------------------------------------- | ---------------------------------------------------------------- | ---------------------- | -------- |
| 价格 | 1.475 亿美元（1999）；区间 1.32–1.475 亿（1999）       | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-11/> （维基同） | (游戏 cost_factor=137)   | —        |
| 航程 | 12,455 km（6,725 nmi，典型 298 人）；最大约 13,200 km | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-11>          | range_km_est 12,540 km | 基本一致     |
| 座级 | 293 人（头等布局）/ 323 人（34J+289Y）/ 410 人（最大全经济）  | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-11>          | passenger 293 人        | 一致       |
| 巡航 | 886 km/h（Mach 0.83）；aerocorner 约 905 km/h   | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-11>          | speed_kmh 943 km/h     | 游戏偏高约 6% |

<a id="mcdonnell_douglas_md11f"></a>

### McDonnell Douglas MD-11F (McDonnell_Douglas_MD11F)

| 字段 | 真实值                         | 来源 URL                                                     | 游戏内当前值                | 偏差/备注              |
| -- | --------------------------- | ---------------------------------------------------------- | --------------------- | ------------------ |
| 价格 | 1.475 亿美元（1999）参考（货机无独立目录价） | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-11/> | (游戏 cost_factor=137)  | 货机无单列价，沿用 MD-11 客机 |
| 航程 | 6,543 km（3,533 nmi，最大业载）    | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-11>    | range_km_est 7,232 km | 游戏略高               |
| 座级 | 0（全货机）                      | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-11>    | passenger 0 人         | 一致                 |
| 巡航 | 886 km/h（Mach 0.83）         | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-11>    | speed_kmh 943 km/h    | 游戏偏高约 6%           |

<a id="mcdonnell_douglas_md81"></a>

### McDonnell Douglas MD-81 (McDonnell_Douglas_MD81)

| 字段 | 真实值                                | 来源 URL                                                     | 游戏内当前值                | 偏差/备注            |
| -- | ---------------------------------- | ---------------------------------------------------------- | --------------------- | ---------------- |
| 价格 | 5,000 万美元（年份未标注）                   | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-81/> | (游戏 cost_factor=46)   | aerocorner 未注明年份 |
| 航程 | 2,898 km（1,565 nmi，典型 155 人）       | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-80>    | range_km_est 2,888 km | 基本一致             |
| 座级 | 155 人（混合/全经济）；最多 172 人             | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-81/> | passenger 155 人       | 一致               |
| 巡航 | 840 km/h（455 kt，最大巡航）；典型约 811 km/h | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-81/> | speed_kmh 814 km/h    | 基本一致             |

<a id="mcdonnell_douglas_md82"></a>

### McDonnell Douglas MD-82 (McDonnell_Douglas_MD82)

| 字段 | 真实值                                     | 来源 URL                                                                           | 游戏内当前值                | 偏差/备注 |
| -- | --------------------------------------- | -------------------------------------------------------------------------------- | --------------------- | ----- |
| 价格 | 4,150 万美元（1999）                         | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-82/>                       | (游戏 cost_factor=51)   | —     |
| 航程 | 3,800 km（2,050 nmi，典型 155 人）            | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-80> （aerocorner 同 2,050 nmi） | range_km_est 3,768 km | 基本一致  |
| 座级 | 155 人（两舱典型）；最多 167–172 人                | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-82/>                       | passenger 155 人       | 一致    |
| 巡航 | 811 km/h（438 kt，典型）；最大 898 km/h（485 kt） | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-80>                          | speed_kmh 814 km/h    | 基本一致  |

<a id="mcdonnell_douglas_md83"></a>

### McDonnell Douglas MD-83 (McDonnell_Douglas_MD83)

| 字段 | 真实值                                                           | 来源 URL                                                     | 游戏内当前值                | 偏差/备注 |
| -- | ------------------------------------------------------------- | ---------------------------------------------------------- | --------------------- | ----- |
| 价格 | 4,850 万美元（1990）                                               | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-83/> | (游戏 cost_factor=57)   | —     |
| 航程 | 4,637 km（2,504 nmi，典型 155 人）；约 4,720 km（aerocorner 2,550 nmi） | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-80>    | range_km_est 4,592 km | 基本一致  |
| 座级 | 155 人（两舱典型）；最多 167–172 人                                      | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-83/> | passenger 155 人       | 一致    |
| 巡航 | 811 km/h（典型）；最大 874 km/h（472 kt）                              | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-83/> | speed_kmh 841 km/h    | 接近    |

<a id="mcdonnell_douglas_md87"></a>

### McDonnell Douglas MD-87 (McDonnell_Douglas_MD87)

| 字段 | 真实值                                                      | 来源 URL                                                                           | 游戏内当前值                | 偏差/备注         |
| -- | -------------------------------------------------------- | -------------------------------------------------------------------------------- | --------------------- | ------------- |
| 价格 | 4,150 万美元（1990）                                          | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-87/>                       | (游戏 cost_factor=49)   | —             |
| 航程 | 5,400 km（2,900 nmi，最大/带副油箱）；4,390 km（2,370 nmi，典型 130 人） | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-80> （aerocorner 同 2,900 nmi） | range_km_est 4,345 km | 游戏偏低（取典型值则接近） |
| 座级 | 130 人（两舱）；最多 139 人                                       | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-87/>                       | passenger 130 人       | 一致            |
| 巡航 | 811 km/h（典型）；最大 870 km/h（470 kt）                         | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-87/>                       | speed_kmh 814 km/h    | 基本一致          |

<a id="mcdonnell_douglas_md88"></a>

### McDonnell Douglas MD-88 (McDonnell_Douglas_MD88)

| 字段 | 真实值                                                   | 来源 URL                                                     | 游戏内当前值                | 偏差/备注     |
| -- | ----------------------------------------------------- | ---------------------------------------------------------- | --------------------- | --------- |
| 价格 | 4,850 万美元（1980，aerocorner 标注）                         | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-88/> | (游戏 cost_factor=51)   | 年份标注偏早，存疑 |
| 航程 | 4,637 km（2,504 nmi，带副油箱）；3,800 km（2,050 nmi，典型 155 人） | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-80>    | range_km_est 3,768 km | 取典型值一致    |
| 座级 | 155 人（两舱典型）；最多 167 人                                  | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-88/> | passenger 155 人       | 一致        |
| 巡航 | 811 km/h（典型）；最大 874 km/h（472 kt）                      | <https://aerocorner.com/aircraft/mcdonnell-douglas-md-88/> | speed_kmh 814 km/h    | 基本一致      |

<a id="mcdonnell_douglas_md90"></a>

### McDonnell Douglas MD-90 (McDonnell_Douglas_MD90)

| 字段 | 真实值                                                    | 来源 URL                                                  | 游戏内当前值                | 偏差/备注          |
| -- | ------------------------------------------------------ | ------------------------------------------------------- | --------------------- | -------------- |
| 价格 | 4,150–4,850 万美元                                        | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-90> | (游戏 cost_factor=59)   | —              |
| 航程 | 3,787 km（2,045 nmi，典型 153 人）；最大 4,547 km（2,455 nmi，ER） | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-90> | range_km_est 5,115 km | 游戏偏高约 12%（取典型） |
| 座级 | 153–158 人（两舱）；最多 172 人                                 | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-90> | passenger 155 人       | 一致             |
| 巡航 | 812 km/h（Mach 0.76）                                    | <https://en.wikipedia.org/wiki/McDonnell_Douglas_MD-90> | speed_kmh 841 km/h    | 游戏偏高约 4%       |

---

### PZL · PZL

<a id="pzl_an28"></a>

### PZL AN-28 (PZL_AN28)

| 字段 | 真实值                                              | 来源 URL                                        | 游戏内当前值               | 偏差/备注             |
| -- | ------------------------------------------------ | --------------------------------------------- | -------------------- | ----------------- |
| 价格 | 未找到可靠来源（维基仅列安-28，无美元价；PZL M-28 Skytruck 亦无公开目录价） | <https://en.wikipedia.org/wiki/Antonov_An-28> | (游戏 cost_factor=14)  | 无公开美元目录价          |
| 航程 | 1,365 km（737 nmi，最大燃油、1,000 kg 载荷）               | <https://en.wikipedia.org/wiki/Antonov_An-28> | range_km_est 1452 km | 游戏略高于真实最大 1365 km |
| 座级 | 15 人（正文）/ 17 人（性能表，含 2 名机组外）                     | <https://en.wikipedia.org/wiki/Antonov_An-28> | passenger 19 人       | 游戏偏高（真实 15–17）    |
| 巡航 | 335 km/h（181 kt，3,000 m）                         | <https://en.wikipedia.org/wiki/Antonov_An-28> | speed_kmh 335 km/h   | 完全一致              |

### 皮拉图斯 · Pilatus

<a id="pilatus_pc12"></a>

### Pilatus PC-12 (PILATUS_PC12)

| 字段 | 真实值                                                                  | 来源 URL                                        | 游戏内当前值               | 偏差/备注                  |
| -- | -------------------------------------------------------------------- | --------------------------------------------- | -------------------- | ---------------------- |
| 价格 | US$4.39M（2019 基础价 PC-12NGX）；通常配置至 US$5.369M（2019）；2023 装备价 US$6.028M | <https://en.wikipedia.org/wiki/Pilatus_PC-12> | (游戏 cost_factor=14)  | 2019–2023 目录价          |
| 航程 | 3,417 km（1,845 nmi，HSC/VFR 储备，PC-12NG）                               | <https://en.wikipedia.org/wiki/Pilatus_PC-12> | range_km_est 2992 km | 游戏低于真实 3417 km（约 -12%） |
| 座级 | 9 人（最大；6–9 座配置）                                                      | <https://en.wikipedia.org/wiki/Pilatus_PC-12> | passenger 9 人        | 一致                     |
| 巡航 | 528 km/h（285 kt）                                                     | <https://en.wikipedia.org/wiki/Pilatus_PC-12> | speed_kmh 528 km/h   | 完全一致                   |

<a id="pilatus_pc24"></a>

### Pilatus PC-24 (PILATUS_PC24)

| 字段 | 真实值                                                                    | 来源 URL                                                                                                   | 游戏内当前值               | 偏差/备注                     |
| -- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------- |
| 价格 | US$10.7M（2019 订单价）；2017 取证价 US$8.9M；2023 装备价 US$12.2M                  | <https://aerocorner.com/aircraft/pilatus-pc-24/> （主源）；<https://en.wikipedia.org/wiki/Pilatus_PC-24> （交叉） | (游戏 cost_factor=27)  | 2019 目录价                  |
| 航程 | 典型 3,700 km（2,000 nmi，6 人/1,200 lb 载荷，NBAA IFR）；转场 3,932 km（2,123 nmi） | <https://en.wikipedia.org/wiki/Pilatus_PC-24>                                                            | range_km_est 3702 km | 与典型 3700 km 几乎完全一致        |
| 座级 | 10 人（±1–2 机组）                                                          | <https://en.wikipedia.org/wiki/Pilatus_PC-24>                                                            | passenger 12 人       | 游戏偏高（真实 10）               |
| 巡航 | 最大 810 km/h（440 kt，Mach 0.74 高速巡航）                                     | <https://en.wikipedia.org/wiki/Pilatus_PC-24>                                                            | speed_kmh 787 km/h   | 接近（游戏取约 Mach 0.74 高速巡航下沿） |

### 雷神 · Raytheon

<a id="raytheon_beech1900d"></a>

### Raytheon Beech 1900D (RAYTHEON_BEECH1900D)

| 字段 | 真实值                                                                    | 来源 URL                                          | 游戏内当前值               | 偏差/备注              |
| -- | ---------------------------------------------------------------------- | ----------------------------------------------- | -------------------- | ------------------ |
| 价格 | US$3.95M（1991，1900D Airliner）                                          | <https://en.wikipedia.org/wiki/Beechcraft_1900> | (游戏 cost_factor=14)  | 1991 目录价           |
| 航程 | 转场 2,306 km（1,245 nmi）；19 座满客 707 km（382 nmi）；IFR 满客 1,260 km（680 nmi） | <https://en.wikipedia.org/wiki/Beechcraft_1900> | range_km_est 1798 km | 游戏取满客 IFR 与转场之间，合理 |
| 座级 | 19 人                                                                   | <https://en.wikipedia.org/wiki/Beechcraft_1900> | passenger 19 人       | 一致                 |
| 巡航 | 518 km/h（280 kt TAS，FL230）                                             | <https://en.wikipedia.org/wiki/Beechcraft_1900> | speed_kmh 518 km/h   | 完全一致               |

### 南方飞机 · SUD

<a id="sud_caravelle_iii"></a>

### SUD Caravelle III (SUD_CARAVELLE_III)

| 字段 | 真实值                                                                                 | 来源 URL                                                                                       | 游戏内当前值               | 偏差/备注                                 |
| -- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------- |
| 价格 | 无 III 型专属公开价；全系列公开单位成本 US$5.5M（1972，对应末型 Caravelle 12），非 III 型                      | <https://en.wikipedia.org/wiki/Sud_Aviation_Caravelle> （交叉佐证：中文维基镜像同样列「单位成本 550 万美元 (1972)」） | (游戏 cost_factor=27)  | III 型无可靠专属美元目录价                       |
| 航程 | 初始 I/III/VI 型 1,650–2,500 km（890–1,350 nmi）；后期 10/11 型 2,800–3,300 km；12 型 3,200 km | <https://en.wikipedia.org/wiki/Sud_Aviation_Caravelle>                                       | range_km_est 3602 km | 游戏超出 III 型上限 2500 km，更接近后期 10/11/12 型 |
| 座级 | 80 人（性能表 I/III/VI）；正文称初始 I/III/VI 可坐 90–99 人                                        | <https://en.wikipedia.org/wiki/Sud_Aviation_Caravelle>                                       | passenger 80 人       | 与性能表一致（正文运营配置可达 90–99）                |
| 巡航 | 746–845 km/h（403–456 kt，I/III/VI 最大巡航）                                              | <https://en.wikipedia.org/wiki/Sud_Aviation_Caravelle>                                       | speed_kmh 805 km/h   | 在标称区间 746–845 内，一致                    |

### 苏霍伊 · Sukhoi

<a id="sukhoi_ssj100"></a>

### Sukhoi Superjet 100 (SUKHOI_SSJ100)

| 字段 | 真实值                                | 来源 URL                                                                                                      | 游戏内当前值                | 偏差/备注   |
| -- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------- | ------- |
| 价格 | US$50.1M（2018，aerocorner 列表价）      | <https://aerocorner.com/aircraft/sukhoi-superjet-100/>                                                      | (游戏 cost_factor=65)   | 合理      |
| 航程 | ~3,048 km（95B 基本型）/ 4,578 km（95LR） | <https://en.wikipedia.org/wiki/Sukhoi_Superjet_100>                                                         | range_km_est 3,047 km | 一致（基本型） |
| 座级 | 87–98（典型）；1舱最多108（95LR）            | <https://aerocorner.com/aircraft/sukhoi-superjet-100/> ；<https://en.wikipedia.org/wiki/Sukhoi_Superjet_100> | passenger 92 人        | 合理      |
| 巡航 | 828–870 km/h（Mach 0.78–0.81）       | <https://aerocorner.com/aircraft/sukhoi-superjet-100/> ；<https://en.wikipedia.org/wiki/Sukhoi_Superjet_100> | speed_kmh 886 km/h    | 合理      |

### 图波列夫 · Tupolev

<a id="tupolev_tu204"></a>

### Tupolev Tu-204 (TUPOLEV_TU204)

| 字段 | 真实值                                           | 来源 URL                                                                                            | 游戏内当前值                | 偏差/备注             |
| -- | --------------------------------------------- | ------------------------------------------------------------------------------------------------- | --------------------- | ----------------- |
| 价格 | US$37M（2007，aerocorner）；Tu-204SM 估算 US$40–47M | <https://aerocorner.com/aircraft/tupolev-tu-204/> ；<https://en.wikipedia.org/wiki/Tupolev_Tu-204> | (游戏 cost_factor=79)   | 合理                |
| 航程 | 4,300 km（Tu-204-100 最大载重）/ 可达6,500 km（最大燃油）   | <https://aerocorner.com/aircraft/tupolev-tu-204/> ；<https://en.wikipedia.org/wiki/Tupolev_Tu-204> | range_km_est 4,301 km | 一致（最大载重）          |
| 座级 | 172–210（最多210）                                | <https://aerocorner.com/aircraft/tupolev-tu-204/> ；<https://en.wikipedia.org/wiki/Tupolev_Tu-204> | passenger 190 人       | 合理                |
| 巡航 | 810–850 km/h                                  | <https://en.wikipedia.org/wiki/Tupolev_Tu-204> ；<https://aerocorner.com/aircraft/tupolev-tu-204/> | speed_kmh 934 km/h    | 游戏值偏高（现实约810–850） |

<a id="tupolev_tu214"></a>

### Tupolev Tu-214 (TUPOLEV_TU214)

| 字段 | 真实值                                                                   | 来源 URL                                                                                                | 游戏内当前值                | 偏差/备注                 |
| -- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------------------- | --------------------- |
| 价格 | ~US$30M（2006年币值估算；图-204-100/214单价约3000万—shapcshicdc）；军用型报价更高(~US$65M) | <http://www.shapcshicdc.cn/hangardetails/16187.html> ；<https://en.wikipedia.org/wiki/Tupolev_Tu-204>  | (游戏 cost_factor=79)   | 合理                    |
| 航程 | 4,340 km（最大载重）/ 5,650 km（满载客）/ VIP 可达9,200 km                         | <https://en.wikipedia.org/wiki/Tupolev_Tu-204> ；<https://www.airport-technology.com/projects/tupolev> | range_km_est 7,200 km | 游戏值偏高（取客机满载约5,650更典型） |
| 座级 | 164–210（最多210）                                                        | <https://en.wikipedia.org/wiki/Tupolev_Tu-204> ；<https://www.airport-technology.com/projects/tupolev> | passenger 200 人       | 合理                    |
| 巡航 | 810–850 km/h                                                          | <https://en.wikipedia.org/wiki/Tupolev_Tu-204>                                                        | speed_kmh 934 km/h    | 游戏值偏高（现实约810–850）     |

<a id="tupolev_tu134"></a>

### Tupolev Tu-134 (Tupolev_Tu134)

| 字段 | 真实值                            | 来源 URL                                                                                            | 游戏内当前值                | 偏差/备注      |
| -- | ------------------------------ | ------------------------------------------------------------------------------------------------- | --------------------- | ---------- |
| 价格 | 未找到可靠来源（老式机，无公开目录价）            | —                                                                                                 | (游戏 cost_factor=32)   | 无可靠来源      |
| 航程 | 1,900–3,000 km（航程）/ 转场3,200 km | <https://en.wikipedia.org/wiki/Tupolev_Tu-134>                                                    | range_km_est 1,870 km | 游戏值偏低（取低值） |
| 座级 | 最多84（Tu-134A）                  | <https://en.wikipedia.org/wiki/Tupolev_Tu-134> ；<https://aerocorner.com/aircraft/tupolev-tu-134/> | passenger 80 人        | 合理         |
| 巡航 | 850 km/h                       | <https://en.wikipedia.org/wiki/Tupolev_Tu-134>                                                    | speed_kmh 902 km/h    | 游戏值略高      |

<a id="tupolev_tu154b"></a>

### Tupolev Tu-154B (Tupolev_Tu154B)

| 字段 | 真实值                         | 来源 URL                                                                                            | 游戏内当前值                | 偏差/备注 |
| -- | --------------------------- | ------------------------------------------------------------------------------------------------- | --------------------- | ----- |
| 价格 | US$45M（2008，aerocorner 列表价） | <https://aerocorner.com/aircraft/tupolev-tu-154/>                                                 | (游戏 cost_factor=41)   | 合理    |
| 航程 | 5,280 km（Tu-154B-2 最大燃油）    | <https://en.wikipedia.org/wiki/Tupolev_Tu-154>                                                    | range_km_est 4,042 km | 游戏值偏低 |
| 座级 | 114–180（最多180）              | <https://aerocorner.com/aircraft/tupolev-tu-154/> ；<https://en.wikipedia.org/wiki/Tupolev_Tu-154> | passenger 150 人       | 合理    |
| 巡航 | 850 km/h                    | <https://aerocorner.com/aircraft/tupolev-tu-154/> ；<https://en.wikipedia.org/wiki/Tupolev_Tu-154> | speed_kmh 951 km/h    | 游戏值偏高 |

<a id="tupolev_tu154m"></a>

### Tupolev Tu-154M (Tupolev_Tu154M)

| 字段 | 真实值                         | 来源 URL                                                                                            | 游戏内当前值                | 偏差/备注         |
| -- | --------------------------- | ------------------------------------------------------------------------------------------------- | --------------------- | ------------- |
| 价格 | US$45M（2008，aerocorner 列表价） | <https://aerocorner.com/aircraft/tupolev-tu-154/>                                                 | (游戏 cost_factor=41)   | 合理            |
| 航程 | 6,600 km（Tu-154M 最大燃油）      | <https://en.wikipedia.org/wiki/Tupolev_Tu-154>                                                    | range_km_est 4,042 km | 游戏值偏低（M型现实更长） |
| 座级 | 114–180（最多180）              | <https://aerocorner.com/aircraft/tupolev-tu-154/> ；<https://en.wikipedia.org/wiki/Tupolev_Tu-154> | passenger 150 人       | 合理            |
| 巡航 | 850 km/h                    | <https://aerocorner.com/aircraft/tupolev-tu-154/> ；<https://en.wikipedia.org/wiki/Tupolev_Tu-154> | speed_kmh 951 km/h    | 游戏值偏高         |

### 维克斯 · Vickers

<a id="vickers_vc10"></a>

### Vickers VC10 (VICKERS_VC10)

| 字段 | 真实值                                  | 来源 URL                                       | 游戏内当前值               | 偏差/备注        |
| -- | ------------------------------------ | -------------------------------------------- | -------------------- | ------------ |
| 价格 | 未找到可靠来源（仅 £1.75M 早期保本价，非售价）；无 USD    | <https://en.wikipedia.org/wiki/Vickers_VC10> | (游戏 cost_factor=169) | 仅英镑保本估算      |
| 航程 | 9,410 km（5,080 nmi，Type 1101）        | <https://en.wikipedia.org/wiki/Vickers_VC10> | range_km_est 9900 km | 接近（游戏偏高约 5%） |
| 座级 | 151 人（最大）；135 人（两舱）                  | <https://en.wikipedia.org/wiki/Vickers_VC10> | passenger 145 人      | 接近最大         |
| 巡航 | 890 km/h（480 kn，经济巡航@38,000ft；无马赫标注） | <https://en.wikipedia.org/wiki/Vickers_VC10> | speed_kmh 822 km/h   | 游戏偏低（约 92%）  |

<a id="vickers_viscount"></a>

### Vickers Viscount (VICKERS_VISCOUNT)

| 字段 | 真实值                                                        | 来源 URL                                           | 游戏内当前值               | 偏差/备注        |
| -- | ---------------------------------------------------------- | ------------------------------------------------ | -------------------- | ------------ |
| 价格 | £235,000（1953，基础成本；仅英镑）                                    | <https://en.wikipedia.org/wiki/Vickers_Viscount> | (游戏 cost_factor=14)  | 仅英镑历史价       |
| 航程 | 2,220 km（1,200 nmi，Type 810）                               | <https://en.wikipedia.org/wiki/Vickers_Viscount> | range_km_est 2772 km | 游戏偏高（约 +25%） |
| 座级 | 75 人（Type 810 最高）                                          | <https://en.wikipedia.org/wiki/Vickers_Viscount> | passenger 60 人       | 偏低           |
| 巡航 | 未给精确巡航；Type 810 最大速度 566 km/h（306 kn），Type 700 巡航 496 km/h | <https://en.wikipedia.org/wiki/Vickers_Viscount> | speed_kmh 525 km/h   | 介于巡航与最大之间    |

---

## 汇总备注

- 高度吻合（真实与游戏几乎一致）：Cessna 208/208B（速度、航程、座级）、Cessna 408（座级/巡航/航程）、Cessna 414/421（航程）、Fokker 100（巡航）、Fokker 70、L-1011（座级/航程）、L-049（座级/巡航/速度）、DHC-6-400（全部）。
- 价格：多数活塞/涡桨支线小飞机（Cessna 402/404/414/421、Fokker F28/F100/F70、L-188、VC10）维基未列 USD 目录价；标注「未找到可靠来源」。有可靠价的：Cessna 208/208B（$2.32M/$2.61M 2023）、Cessna 408（$5.5M 2017）、L-1011（$20M 1972）、DHC-6-400（$7.25M 2023）；英镑历史价：F27、Comet、Viscount、VC10(保本)、L-049(设计估值)。
- 明显偏差关注：Cessna 402 航程游戏偏低（1298 vs 2358）；L-188 巡航游戏偏低（515 vs 600）；de Havilland Comet 座级游戏偏高（90 vs 81 典型）且航程无可靠来源核对；Viscount 航程游戏偏高、座级偏低。

### 雅克福列夫 · Yakovlev

<a id="yakovlev_yak40"></a>

### Yakovlev Yak-40 (YAKOVLEV_YAK40)

| 字段 | 真实值                        | 来源 URL                                                                                              | 游戏内当前值                | 偏差/备注          |
| -- | -------------------------- | --------------------------------------------------------------------------------------------------- | --------------------- | -------------- |
| 价格 | US$1M（1972，aerocorner 列表价） | <https://aerocorner.com/aircraft/yakovlev-yak-40/>                                                  | (游戏 cost_factor=20)   | 合理（老式机低价）      |
| 航程 | 1,800 km（最大载重）             | <https://en.wikipedia.org/wiki/Yakovlev_Yak-40>                                                     | range_km_est 2,502 km | 游戏值偏高（现实1,800） |
| 座级 | 32（最大）                     | <https://aerocorner.com/aircraft/yakovlev-yak-40/> ；<https://en.wikipedia.org/wiki/Yakovlev_Yak-40> | passenger 32 人        | 一致             |
| 巡航 | 550 km/h（最大巡航）             | <https://aerocorner.com/aircraft/yakovlev-yak-40/> ；<https://en.wikipedia.org/wiki/Yakovlev_Yak-40> | speed_kmh 500 km/h    | 合理             |

<a id="yakovlev_yak42"></a>

### Yakovlev Yak-42 (YAKOVLEV_YAK42)

| 字段 | 真实值                    | 来源 URL                                             | 游戏内当前值                | 偏差/备注           |
| -- | ---------------------- | -------------------------------------------------- | --------------------- | --------------- |
| 价格 | US$36M（aerocorner，无年份） | <https://aerocorner.com/aircraft/yakovlev-yak-42/> | (游戏 cost_factor=30)   | 游戏系数偏低          |
| 航程 | 2,200 nm ≈ 4,074 km    | <https://aerocorner.com/aircraft/yakovlev-yak-42/> | range_km_est 2,898 km | 游戏值偏低（现实约4,074） |
| 座级 | 96–120（最多120）          | <https://aerocorner.com/aircraft/yakovlev-yak-42/> | passenger 120 人       | 一致              |
| 巡航 | 740 km/h（400 kt）       | <https://aerocorner.com/aircraft/yakovlev-yak-42/> | speed_kmh 740 km/h    | 一致              |

### 德哈维兰 · de Havilland

<a id="dehavilland_comet"></a>

### de Havilland Comet (DEHAVILLAND_COMET)

| 字段 | 真实值                                       | 来源 URL                                             | 游戏内当前值               | 偏差/备注              |
| -- | ----------------------------------------- | -------------------------------------------------- | -------------------- | ------------------ |
| 价格 | £1.14M（≈1958，Comet 4 基础价；仅英镑，无 USD）       | <https://en.wikipedia.org/wiki/De_Havilland_Comet> | (游戏 cost_factor=37)  | 仅英镑历史价             |
| 航程 | 未找到可靠来源（维基未给出精确 km 航程；Comet 4 称"更长航程"无数字） | <https://en.wikipedia.org/wiki/De_Havilland_Comet> | range_km_est 7398 km | 游戏值疑似取自其他来源，维基无法核对 |
| 座级 | 74-81 人（Comet 4 典型）；最高 119（4C 包机布局）       | <https://en.wikipedia.org/wiki/De_Havilland_Comet> | passenger 90 人       | 偏高（超出典型 81）        |
| 巡航 | 790 km/h（490 mph，BOAC 运营时速；无精确 kt/马赫）     | <https://en.wikipedia.org/wiki/De_Havilland_Comet> | speed_kmh 740 km/h   | 接近                 |

<a id="dehavilland_dhc6_400"></a>

### de Havilland DHC-6-400 Twin Otter (DEHAVILLAND_DHC6_400)

| 字段 | 真实值                                     | 来源 URL                                                               | 游戏内当前值               | 偏差/备注                |
| -- | --------------------------------------- | -------------------------------------------------------------------- | -------------------- | -------------------- |
| 价格 | US$7.25M（2023，装备价）                      | <https://en.wikipedia.org/wiki/De_Havilland_Canada_DHC-6_Twin_Otter> | (游戏 cost_factor=22)  | 新机目录价                |
| 航程 | 1,480 km（799 nmi，Ferry）；选装翼尖油箱 1,832 km | <https://en.wikipedia.org/wiki/De_Havilland_Canada_DHC-6_Twin_Otter> | range_km_est 1298 km | 游戏偏低（约 88% 标准 Ferry） |
| 座级 | 19 人                                    | <https://en.wikipedia.org/wiki/De_Havilland_Canada_DHC-6_Twin_Otter> | passenger 19 人       | 一致                   |
| 巡航 | 337 km/h（182 kn，最大巡航@FL100）             | <https://en.wikipedia.org/wiki/De_Havilland_Canada_DHC-6_Twin_Otter> | speed_kmh 337 km/h   | 完全一致                 |
