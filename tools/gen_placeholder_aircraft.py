# -*- coding: utf-8 -*-
"""生成占位机型 pnml：克隆 donor 的精灵网格宏 + 机型参数，只换标识符/名称/上线年份，
接 donor 前 N 个 livery（复用 donor 已有的 STR_VLIV 字符串），零新 livery 字符串负担。

用法：
    python tools/gen_placeholder_aircraft.py
每个 target 会：
  - 在 src/gfx/<manu>/<fam>/<var>/<var>.pnml 生成占位 pnml（借用 donor PNG，逻辑零改动）
  - 向 lang/english.lng + chinese_simplified/traditional 追加 STR_AIRV_<ID> / STR_VLIV_<ID>
  - 向 WAS.pnml 的 // Sort order 之前插入 #include
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 仓库根
N_LIVERIES = 5

# 每款占位机的目标定义
TARGETS = [
    # ===== 本轮新增 10 款占位机（年份已核对） =====
    dict(id="AIRBUS_A321XLR",  dir="src/gfx/Airbus/A321/A321XLR/A321XLR.pnml",
         donor="src/gfx/Airbus/A320/A320-200/A320-200.pnml",
         name_en="Airbus A321XLR", name_zh="空客 A321XLR", year=2024),
    dict(id="EMBRAER_E190_E2", dir="src/gfx/Embraer/E190/E190-E2/E190-E2.pnml",
         donor="src/gfx/Embraer/E190/E190STD/E190STD.pnml",
         name_en="Embraer E190-E2", name_zh="巴航工 E190-E2", year=2018),
    dict(id="AIRBUS_A220_100", dir="src/gfx/Airbus/A220/A220-100/A220-100.pnml",
         donor="src/gfx/Airbus/A320/A320neo/A320neo.pnml",
         name_en="Airbus A220-100", name_zh="空客 A220-100", year=2016),
    dict(id="ATR_72_600",      dir="src/gfx/ATR/ATR72/72-600/72-600.pnml",
         donor="src/gfx/ATR/ATR72/72-500/72-500.pnml",
         name_en="ATR 72-600", name_zh="ATR 72-600", year=2011),   # 商业服役 2011（首飞 2010）
    dict(id="ATR_42_600",      dir="src/gfx/ATR/ATR42/42-600/42-600.pnml",
         donor="src/gfx/ATR/ATR42/42-500/42-500.pnml",
         name_en="ATR 42-600", name_zh="ATR 42-600", year=2012),
    dict(id="BOEING_737MAX7",  dir="src/gfx/Boeing/B737/B737MAX7/B737MAX7.pnml",
         donor="src/gfx/Boeing/B737/B737MAX8/B737MAX8.pnml",
         name_en="Boeing 737 MAX 7", name_zh="波音 737 MAX 7", year=2026),  # FAA 认证 2026 夏末
    dict(id="AIRBUS_A330_800NEO", dir="src/gfx/Airbus/A330/A330-800neo/A330-800neo.pnml",
         donor="src/gfx/Airbus/A330/A330-300/A330-300.pnml",
         name_en="Airbus A330-800neo", name_zh="空客 A330-800neo", year=2020),  # 首商业 2020-11
    dict(id="SUKHOI_SSJ100",   dir="src/gfx/Sukhoi/SSJ100/SSJ100.pnml",
         donor="src/gfx/Embraer/E190/E190STD/E190STD.pnml",
         name_en="Sukhoi Superjet 100", name_zh="苏霍伊 Superjet 100", year=2011),
    dict(id="IRKUT_MC21",      dir="src/gfx/Irkut/MC21/MC21.pnml",
         donor="src/gfx/Airbus/A320/A320-200/A320-200.pnml",
         name_en="Irkut MC-21", name_zh="伊尔库特 MC-21", year=2024),
    dict(id="COMAC_C929",       dir="src/gfx/COMAC/C929/C929.pnml",
         donor="src/gfx/Airbus/A350/A350-900/A350-900.pnml",
         name_en="COMAC C929", name_zh="中国商飞 C929", year=2030),
    # ===== A 档：同族低成本扩展 =====
    dict(id="EMBRAER_E175_E2", dir="src/gfx/Embraer/E175/E175-E2/E175-E2.pnml",
         donor="src/gfx/Embraer/E175/E175STD/E175STD.pnml",
         name_en="Embraer E175-E2", name_zh="巴航工 E175-E2", year=2027),
    dict(id="BOEING_757_300",  dir="src/gfx/Boeing/B757/B757-300/B757-300.pnml",
         donor="src/gfx/Boeing/B757/B757-200/B757-200.pnml",
         name_en="Boeing 757-300", name_zh="波音 757-300", year=1999),
    dict(id="BOEING_777_8",    dir="src/gfx/Boeing/B777/B777-8/B777-8.pnml",
         donor="src/gfx/Boeing/B777/B777-300/B777-300.pnml",
         name_en="Boeing 777-8", name_zh="波音 777-8", year=2027),
    dict(id="ANTONOV_AN148",   dir="src/gfx/Antonov/An148/An148.pnml",
         donor="src/gfx/Embraer/E190/E190STD/E190STD.pnml",
         name_en="Antonov An-148", name_zh="安东诺夫 安-148", year=2009),
    dict(id="ANTONOV_AN158",   dir="src/gfx/Antonov/An158/An158.pnml",
         donor="src/gfx/Embraer/E190/E190STD/E190STD.pnml",
         name_en="Antonov An-158", name_zh="安东诺夫 安-158", year=2010),
    # ===== B 档：俄制主力 =====
    dict(id="TUPOLEV_TU204",    dir="src/gfx/Tupolev/Tu204/Tu204.pnml",
         donor="src/gfx/Boeing/B757/B757-200/B757-200.pnml",
         name_en="Tupolev Tu-204", name_zh="图波列夫 图-204", year=1992),
    dict(id="TUPOLEV_TU214",    dir="src/gfx/Tupolev/Tu214/Tu214.pnml",
         donor="src/gfx/Boeing/B757/B757-200/B757-200.pnml",
         name_en="Tupolev Tu-214", name_zh="图波列夫 图-214", year=1996),
    dict(id="ILYUSHIN_IL96",    dir="src/gfx/Ilyushin/Il96/Il96.pnml",
         donor="src/gfx/Airbus/A330/A330-300/A330-300.pnml",
         name_en="Ilyushin Il-96", name_zh="伊尔-96", year=1992),
    dict(id="ILYUSHIN_IL114",   dir="src/gfx/Ilyushin/Il114/Il114.pnml",
         donor="src/gfx/ATR/ATR42/42-500/42-500.pnml",
         name_en="Ilyushin Il-114", name_zh="伊尔-114", year=1997),
    dict(id="YAKOVLEV_YAK40",   dir="src/gfx/Yakovlev/Yak40/Yak40.pnml",
         donor="src/gfx/Boeing/B727/B727-200/B727-200.pnml",
         name_en="Yakovlev Yak-40", name_zh="雅克夫列夫 Yak-40", year=1968),
    dict(id="YAKOVLEV_YAK42",   dir="src/gfx/Yakovlev/Yak42/Yak42.pnml",
         donor="src/gfx/Boeing/B727/B727-200/B727-200.pnml",
         name_en="Yakovlev Yak-42", name_zh="雅克夫列夫 Yak-42", year=1980),
    # ===== C 档：经典老飞机 =====
    dict(id="DOUGLAS_DC3",      dir="src/gfx/McDonnell_Douglas/DC3/DC3.pnml",
         donor="src/gfx/ATR/ATR42/42-500/42-500.pnml",
         name_en="Douglas DC-3", name_zh="道格拉斯 DC-3", year=1936),
    dict(id="DOUGLAS_DC6",      dir="src/gfx/McDonnell_Douglas/DC6/DC6.pnml",
         donor="src/gfx/Lockheed/Constellation/L049 Constellation/L049 Constellation.pnml",
         name_en="Douglas DC-6", name_zh="道格拉斯 DC-6", year=1946),
    dict(id="DOUGLAS_DC7",      dir="src/gfx/McDonnell_Douglas/DC7/DC7.pnml",
         donor="src/gfx/Lockheed/Constellation/L049 Constellation/L049 Constellation.pnml",
         name_en="Douglas DC-7", name_zh="道格拉斯 DC-7", year=1953),
    dict(id="LOCKHEED_L188",    dir="src/gfx/Lockheed/L188/L188.pnml",
         donor="src/gfx/ATR/ATR72/72-500/72-500.pnml",
         name_en="Lockheed L-188 Electra", name_zh="洛克希德 L-188 伊莱克特拉", year=1959),
    dict(id="LOCKHEED_L1011",   dir="src/gfx/Lockheed/L1011/L1011.pnml",
         donor="src/gfx/McDonnell_Douglas/DC10/DC10-30/DC-10-30.pnml",
         name_en="Lockheed L-1011 TriStar", name_zh="洛克希德 L-1011 三星", year=1972),
    dict(id="DEHAVILLAND_COMET", dir="src/gfx/de Havilland/Comet/Comet.pnml",
         donor="src/gfx/BAC/1-11/1-11-500/1-11-500.pnml",
         name_en="de Havilland Comet", name_zh="德哈维兰 彗星", year=1952),
    dict(id="VICKERS_VISCOUNT", dir="src/gfx/Vickers/Viscount/Viscount.pnml",
         donor="src/gfx/ATR/ATR42/42-500/42-500.pnml",
         name_en="Vickers Viscount", name_zh="维克斯 子爵", year=1953),
    dict(id="VICKERS_VC10",     dir="src/gfx/Vickers/VC10/VC10.pnml",
         donor="src/gfx/Ilyushin/Il62/Il62.pnml",
         name_en="Vickers VC10", name_zh="维克斯 VC10", year=1962),
    dict(id="FOKKER_F27",       dir="src/gfx/Fokker/F27/F27.pnml",
         donor="src/gfx/ATR/ATR42/42-500/42-500.pnml",
         name_en="Fokker F27", name_zh="福克 F27", year=1958),
    dict(id="FOKKER_F28",       dir="src/gfx/Fokker/F28/F28.pnml",
         donor="src/gfx/Fokker/F100/F100.pnml",
         name_en="Fokker F28", name_zh="福克 F28", year=1969),
    dict(id="CONVAIR_880",      dir="src/gfx/Convair/880/880.pnml",
         donor="src/gfx/Boeing/B737/B737-300/B737-300.pnml",
         name_en="Convair 880", name_zh="康维尔 880", year=1960),
    dict(id="CONVAIR_990",      dir="src/gfx/Convair/990/990.pnml",
         donor="src/gfx/Boeing/B737/B737-300/B737-300.pnml",
         name_en="Convair 990", name_zh="康维尔 990", year=1961),
    dict(id="HS_TRIDENT",       dir="src/gfx/Hawker_Siddeley/Trident/Trident.pnml",
         donor="src/gfx/Boeing/B727/B727-200/B727-200.pnml",
         name_en="Hawker Siddeley Trident", name_zh="霍克·西德利 三叉戟", year=1964),
    dict(id="BOEING_747SP",     dir="src/gfx/Boeing/B747/B747SP/B747SP.pnml",
         donor="src/gfx/Boeing/B747/B747-200/B747-200.pnml",
         name_en="Boeing 747SP", name_zh="波音 747SP", year=1976),
    dict(id="ILYUSHIN_IL18",    dir="src/gfx/Ilyushin/Il18/Il18.pnml",
         donor="src/gfx/ATR/ATR72/72-500/72-500.pnml",
         name_en="Ilyushin Il-18", name_zh="伊尔-18", year=1957),
    # ===== C 档续：塞斯纳通勤/支线（2026-08-09 新增，用户指定） =====
    dict(id="CESSNA_208",    dir="src/gfx/Cessna/208/208/208.pnml",
         donor="src/gfx/ATR/ATR72/72-500/72-500.pnml",
         name_en="Cessna 208 Caravan", name_zh="塞斯纳 208 凯旋", year=1984),
    dict(id="CESSNA_208B",   dir="src/gfx/Cessna/208B/208B/208B.pnml",
         donor="src/gfx/ATR/ATR72/72-500/72-500.pnml",
         name_en="Cessna 208B Grand Caravan", name_zh="塞斯纳 208B 大凯旋", year=1986),
    dict(id="CESSNA_402",    dir="src/gfx/Cessna/402/402/402.pnml",
         donor="src/gfx/ATR/ATR42/42-500/42-500.pnml",
         name_en="Cessna 402", name_zh="塞斯纳 402", year=1966),
    dict(id="CESSNA_404",    dir="src/gfx/Cessna/404/404/404.pnml",
         donor="src/gfx/ATR/ATR42/42-500/42-500.pnml",
         name_en="Cessna 404 Titan", name_zh="塞斯纳 404 泰坦", year=1976),
    dict(id="CESSNA_414",    dir="src/gfx/Cessna/414/414/414.pnml",
         donor="src/gfx/ATR/ATR42/42-500/42-500.pnml",
         name_en="Cessna 414 Chancellor", name_zh="塞斯纳 414 校长", year=1969),
    dict(id="CESSNA_421",    dir="src/gfx/Cessna/421/421/421.pnml",
         donor="src/gfx/ATR/ATR42/42-500/42-500.pnml",
         name_en="Cessna 421 Golden Eagle", name_zh="塞斯纳 421 金鹰", year=1967),
    # ===== 下拉清单缺口补齐（2026-08-09，用户从上游 WAS 完整机型清单比对得出；已剔除改名覆盖项 ARJ21→C909） =====
    dict(id="AIRBUS_A321LR",  dir="src/gfx/Airbus/A321/A321LR/A321LR.pnml",
         donor="src/gfx/Airbus/A320/A321-200/A321-200.pnml",
         name_en="Airbus A321LR", name_zh="空客 A321LR", year=2018),
    dict(id="ANTONOV_AN140",  dir="src/gfx/Antonov/An140/An140.pnml",
         donor="src/gfx/ATR/ATR42/42-600/42-600.pnml",
         name_en="Antonov An-140", name_zh="安东诺夫 安-140", year=2002),
    dict(id="AVIC_MA60",      dir="src/gfx/AVIC/MA60/MA60.pnml",
         donor="src/gfx/ATR/ATR42/42-600/42-600.pnml",
         name_en="AVIC MA-60", name_zh="中航工业 MA-60", year=2000),
    dict(id="AVIC_MA600",     dir="src/gfx/AVIC/MA600/MA600.pnml",
         donor="src/gfx/ATR/ATR72/72-600/72-600.pnml",
         name_en="AVIC MA-600", name_zh="中航工业 MA-600", year=2010),
    dict(id="AVIC_Y7_200",    dir="src/gfx/AVIC/Y7-200/Y7-200.pnml",
         donor="src/gfx/Fokker/F27/F27.pnml",
         name_en="AVIC Y-7-200", name_zh="中航工业 运-7-200", year=1984),
    dict(id="BRITTEN_NORMAN_BN2B", dir="src/gfx/Britten-Norman/BN-2B/BN-2B.pnml",
         donor="src/gfx/ATR/ATR42/42-600/42-600.pnml",
         name_en="Britten-Norman BN-2B Islander", name_zh="布里顿-诺曼 BN-2B 岛民", year=1967),
    dict(id="BRITTEN_NORMAN_BN2T", dir="src/gfx/Britten-Norman/BN-2T/BN-2T.pnml",
         donor="src/gfx/ATR/ATR42/42-600/42-600.pnml",
         name_en="Britten-Norman BN-2T Turbine Islander", name_zh="布里顿-诺曼 BN-2T 涡桨岛民", year=1978),
    dict(id="CESSNA_408",     dir="src/gfx/Cessna/408/408/408.pnml",
         donor="src/gfx/ATR/ATR72/72-600/72-600.pnml",
         name_en="Cessna 408 SkyCourier", name_zh="塞斯纳 408 SkyCourier", year=2022),
    dict(id="DEHAVILLAND_DHC6_400", dir="src/gfx/de Havilland/DHC6-400/DHC6-400.pnml",
         donor="src/gfx/Bombardier/Dash_8/Dash_8-400Q/Dash_8-400Q.pnml",
         name_en="de Havilland DHC-6-400 Twin Otter", name_zh="德哈维兰 DHC-6-400 双水獭", year=1986),
    dict(id="EMBRAER_ERJ135", dir="src/gfx/Embraer/ERJ135/ERJ135/ERJ135.pnml",
         donor="src/gfx/Embraer/E145/ERJ145/ERJ145.pnml",
         name_en="Embraer ERJ-135", name_zh="巴航工 ERJ-135", year=1999),
    dict(id="EMBRAER_ERJ140", dir="src/gfx/Embraer/ERJ140/ERJ140/ERJ140.pnml",
         donor="src/gfx/Embraer/E145/ERJ145/ERJ145.pnml",
         name_en="Embraer ERJ-140", name_zh="巴航工 ERJ-140", year=2001),
    dict(id="GENERAL_ATOMICS_DO228", dir="src/gfx/General Atomics/DO228/DO228.pnml",
         donor="src/gfx/ATR/ATR42/42-600/42-600.pnml",
         name_en="General Atomics DO 228", name_zh="通用原子 DO 228", year=1983),
    dict(id="LET_L410",       dir="src/gfx/LET/L410/L410.pnml",
         donor="src/gfx/ATR/ATR42/42-600/42-600.pnml",
         name_en="LET L-410", name_zh="列特 L-410", year=1971),
    dict(id="PILATUS_PC12",   dir="src/gfx/Pilatus/PC12/PC12.pnml",
         donor="src/gfx/ATR/ATR42/42-600/42-600.pnml",
         name_en="Pilatus PC-12", name_zh="皮拉图斯 PC-12", year=1994),
    dict(id="PILATUS_PC24",   dir="src/gfx/Pilatus/PC24/PC24.pnml",
         donor="src/gfx/Fokker/F100/F100.pnml",
         name_en="Pilatus PC-24", name_zh="皮拉图斯 PC-24", year=2018),
    dict(id="PZL_AN28",       dir="src/gfx/PZL/AN28/AN28.pnml",
         donor="src/gfx/Fokker/F27/F27.pnml",
         name_en="PZL/Antonov AN-28 Skytruck", name_zh="安东诺夫 AN-28 空中卡车", year=1975),
    dict(id="RAYTHEON_BEECH1900D", dir="src/gfx/Raytheon/Beech1900D/Beech1900D.pnml",
         donor="src/gfx/ATR/ATR42/42-600/42-600.pnml",
         name_en="Raytheon Beech 1900D Airliner", name_zh="雷神 1900D 空运者", year=1990),
]


# 量级不符占位机的真实参数覆盖：重跑生成器时仍保留修正，避免被 donor 克隆值覆盖。
# 字段：cap=座级 cruise=巡航km/h rng=range内部单位 cost=cost_factor mail=邮货
# range 内部单位 ≈ 真实航程km / 5.5（由 A320-200 / B737-800 反推）。
# 真实参数覆盖（航程/座级全量核对，2026-08-07）。重跑生成器时仍保留，避免被 donor 克隆值覆盖。
# 字段：cap=座级 cruise=巡航km/h rng=range内部单位 cost=cost_factor mail=邮货
# range 内部单位 ≈ 真实航程km / 5.5（由 A320-200/B737-800/B747-400/A380 反推验证）。
# 未给 cruise/cost 的机型沿用 donor 原值（克隆巡航已较真实）。
OVERRIDES = {
    # === 经典老机 / 支线（先前修正，本轮复核航程） ===
    "DOUGLAS_DC3":      dict(cap=30,  cruise=333, rng=473,  cost=25, mail=3),
    "YAKOVLEV_YAK40":   dict(cap=32,  cruise=500, rng=455,  cost=20, mail=4),
    "YAKOVLEV_YAK42":   dict(cap=120, cruise=740, rng=527,  cost=30, mail=16),
    "ANTONOV_AN148":    dict(cap=80,  cruise=830, rng=564,  cost=50, mail=8),
    "ILYUSHIN_IL18":    dict(cap=110, cruise=625, rng=1182, cost=25, mail=10),
    "CONVAIR_880":      dict(cap=100, cruise=910, rng=1018, cost=35, mail=12),
    "CONVAIR_990":      dict(cap=120, cruise=896, rng=1112, cost=42, mail=14),
    "ILYUSHIN_IL114":   dict(cap=64,  cruise=500, rng=218,  cost=14, mail=7),
    "DEHAVILLAND_COMET":dict(cap=90,  cruise=740, rng=1345, cost=37, mail=7),
    "FOKKER_F27":       dict(cap=50,  cruise=470, rng=291,  cost=14, mail=5),
    "VICKERS_VISCOUNT": dict(cap=60,  cruise=525, rng=504,  cost=14, mail=6),
    "FOKKER_F28":       dict(cap=75,  cruise=820, rng=364,  cost=27, mail=8),
    "AIRBUS_A220_100":  dict(cap=120, cruise=829, rng=1145, cost=80, mail=12),
    # === 本轮航程/座级全量修正（用户点名 A321XLR 等长途改型） ===
    "AIRBUS_A321XLR":   dict(cap=210,            rng=1582, mail=21),   # 206-220座 / 8700km
    "AIRBUS_A330_800NEO":dict(cap=264,           rng=2727, mail=26),   # 257-271座 / 15000km
    "ANTONOV_AN158":    dict(cap=90,             rng=509,  mail=9),    # 86-99座 / ~2800km
    "ATR_42_600":       dict(cap=48,             rng=245,  mail=5),    # 48-50座 / 1345km
    "ATR_72_600":       dict(cap=72,             rng=249,  mail=7),    # 68-78座 / 1370km
    "BOEING_737MAX7":   dict(cap=150,            rng=1273, mail=15),   # 138-172座 / 7000km
    "BOEING_747SP":     dict(cap=320,            rng=2236, mail=32),   # 276-440座 / 12300km
    "BOEING_757_300":   dict(cap=243,            rng=1273, mail=24),   # 243座 / ~7000km
    "BOEING_777_8":     dict(cap=365,            rng=3036, mail=37),   # 350-375座 / 16700km
    "COMAC_C929":       dict(cap=280,            rng=2182, mail=28),   # 280座 / 12000km
    "DOUGLAS_DC6":      dict(cap=81,             rng=1527, mail=8),    # 81座 / 8400km
    "DOUGLAS_DC7":      dict(cap=95,             rng=1673, mail=10),   # 95-105座 / 9200km
    "EMBRAER_E175_E2":  dict(cap=88,             rng=673,  mail=9),    # 80-96座 / 3735km
    "EMBRAER_E190_E2":  dict(cap=97,             rng=963,  mail=10),   # 97座 / 5278km
    "HS_TRIDENT":       dict(cap=150,            rng=701,  mail=15),   # 115-180座 / 3860km
    "IRKUT_MC21":       dict(cap=180,            rng=1091, mail=18),   # 165-211座 / 6000km
    "LOCKHEED_L188":    dict(cap=100,            rng=727,  mail=10),   # ~100座 / 4000km
    "LOCKHEED_L1011":   dict(cap=256,            rng=1799, mail=26),   # 256座 / 9899km
    "SUKHOI_SSJ100":    dict(cap=92,             rng=554,  mail=9),    # 87-98座 / 3048km
    "TUPOLEV_TU204":    dict(cap=190,            rng=782,  mail=19),   # 164-210座 / 4300km
    "TUPOLEV_TU214":    dict(cap=200,            rng=1309, mail=20),   # 200座 / 7200km
    "VICKERS_VC10":     dict(cap=145,            rng=1800, mail=15),   # 135-151座 / 9000km
    "ILYUSHIN_IL96":    dict(cap=280,            rng=2000, mail=28),   # 235-300座 / 11000km
    # === 塞斯纳通勤/支线（2026-08-09 新增，真实规格；range 内部≈km/5.5） ===
    "CESSNA_208":   dict(cap=13, cruise=344, rng=360,  cost=18, mail=2),  # 9-14座 / ~1980km / 涡桨
    "CESSNA_208B":  dict(cap=14, cruise=344, rng=360,  cost=19, mail=2),  # 14座 / ~1980km / 涡桨
    "CESSNA_402":   dict(cap=8,  cruise=380, rng=236,  cost=12, mail=1),  # 6-8座 / ~1300km / 活塞双发
    "CESSNA_404":   dict(cap=9,  cruise=330, rng=436,  cost=13, mail=1),  # 6-10座 / ~2400km / 活塞双发
    "CESSNA_414":   dict(cap=7,  cruise=360, rng=447,  cost=12, mail=1),  # 6-8座 / ~2460km / 活塞双发
    "CESSNA_421":   dict(cap=8,  cruise=420, rng=501,  cost=14, mail=1),  # 6-8座 / ~2754km / 活塞双发
    # === 下拉清单缺口补齐（2026-08-09）真实规格；range 内部≈km/5.5，mail≈cap/10 ===
    "AIRBUS_A321LR":        dict(cap=206, cruise=830, rng=1345, mail=21),  # 206座(单级) / 7400km
    "ANTONOV_AN140":        dict(cap=52,  cruise=575, rng=382,  mail=5),   # 52座 / 2100km
    "AVIC_MA60":            dict(cap=60,  cruise=430, rng=249,  mail=6),   # 60座 / 1370km
    "AVIC_MA600":           dict(cap=60,  cruise=430, rng=251,  mail=6),   # 60座 / 1380km
    "AVIC_Y7_200":          dict(cap=52,  cruise=420, rng=282,  mail=5),   # 52座 / 1550km
    "BRITTEN_NORMAN_BN2B":  dict(cap=9,   cruise=257, rng=195,  mail=1),   # 9座 / 1075km / 活塞(占位音效用涡桨)
    "BRITTEN_NORMAN_BN2T":  dict(cap=9,   cruise=326, rng=244,  mail=1),   # 9座 / 1340km
    "CESSNA_408":           dict(cap=19,  cruise=388, rng=304,  mail=2),   # 19座 / 1670km
    "DEHAVILLAND_DHC6_400": dict(cap=19,  cruise=337, rng=236,  mail=2),   # 19座 / 1300km
    "EMBRAER_ERJ135":       dict(cap=37,  cruise=834, rng=591,  mail=4),   # 37座 / 3250km
    "EMBRAER_ERJ140":       dict(cap=44,  cruise=834, rng=555,  mail=4),   # 44座 / 3050km
    "GENERAL_ATOMICS_DO228":dict(cap=19,  cruise=432, rng=187,  mail=2),   # 19座 / 1030km
    "LET_L410":             dict(cap=19,  cruise=405, rng=251,  mail=2),   # 19座 / 1380km
    "PILATUS_PC12":         dict(cap=9,   cruise=528, rng=544,  mail=1),   # 9座 / 2990km / 单发涡桨
    "PILATUS_PC24":         dict(cap=12,  cruise=787, rng=673,  mail=1),   # 12座 / 3700km / 公务喷气机
    "PZL_AN28":             dict(cap=19,  cruise=335, rng=264,  mail=2),   # 19座 / 1450km
    "RAYTHEON_BEECH1900D":  dict(cap=19,  cruise=518, rng=327,  mail=2),   # 19座 / 1800km
}


def parse_donor(path):
    with open(os.path.join(ROOT, path), encoding="utf-8", errors="replace") as f:
        t = f.read()
    d = {}
    # 捕获精灵网格宏本体（到首个 \n#define IMAGEFILE 之前为止，剔除尾部游离 IMAGEFILE 片段）
    m = re.search(r'(#define (\w+_sprite_layout_template)\(name\).*?)\n#define IMAGEFILE', t, re.DOTALL)
    if not m:
        raise RuntimeError("template macro not found in %s" % path)
    donor_macro = m.group(2)                      # Airbus_A320_200_sprite_layout_template
    assert donor_macro.endswith('_sprite_layout_template'), donor_macro
    d['donor_id'] = donor_macro[:-len('_sprite_layout_template')]   # Airbus_A320_200
    d['template'] = m.group(1)
    m = re.search(r'purchase_sprite\(\w+,\s*([^)]+)\)', t)
    d['purchase'] = [x.strip() for x in m.group(1).split(',')]
    imgs = re.findall(r'#define IMAGEFILE\s+"([^"]+)"', t)
    d['greyscale'] = imgs[0]
    d['liveries'] = [os.path.splitext(os.path.basename(p))[0] for p in imgs[1:]]
    mt = re.search(r'switch \(FEAT_AIRCRAFT, SELF, \w+_cargo_subtype_text, cargo_subtype\)\s*\{(.*?)\}', t, re.DOTALL)
    vliv = {}
    if mt:
        for line in mt.group(1).splitlines():
            mm = re.match(r'\s*(\d+):\s*string\((STR_VLIV_\w+)\)', line)
            if mm:
                vliv[int(mm.group(1))] = mm.group(2)
    d['vliv'] = vliv
    # 注意：部分 donor 主 item 写成 "FEAT_AIRCRAFT ,"（逗号后有空格），而 Ranges 子块写成
    # "FEAT_AIRCRAFT,"（无空格）。故 (1) 容忍逗号两侧空白；(2) 要求 property 块内含
    # passenger_capacity —— 只有主 item 有该字段，Ranges 子块仅有 range: 会落空，从而精确锁定主 item。
    mi = re.search(r'item \(FEAT_AIRCRAFT\s*,\s*\w+\)\s*\{\s*property\s*\{([^}]*passenger_capacity[^}]*)\}', t, re.DOTALL)
    prop = mi.group(1)
    def field(name):
        mm = re.search(r'(?<![A-Za-z_])%s:\s*([^\n;]+);' % re.escape(name), prop)
        return mm.group(1).strip() if mm else None
    d['prop'] = {k: field(k) for k in [
        'aircraft_type', 'misc_flags', 'cargo_allow_refit', 'reliability_decay',
        'loading_speed', 'passenger_capacity', 'mail_capacity', 'acceleration', 'range',
        'vehicle_life', 'model_life', 'retire_early', 'sound_effect']}
    mg = re.search(r'graphics\s*\{(.*?)\}', t, re.DOTALL)
    gfx = mg.group(1)
    def gfield(name):
        mm = re.search(r'(?<![A-Za-z_])%s:\s*([^\n;]+);' % re.escape(name), gfx)
        return mm.group(1).strip() if mm else None
    d['gfx'] = {k: gfield(k) for k in ['cost_factor', 'purchase_running_cost_factor', 'purchase_speed']}
    # flight_state() 后面紧跟 switch 的第二个右括号，写成 \)? 兼容有无该括号两种情况
    ms = re.search(r'(switch \(FEAT_AIRCRAFT, SELF, \w+_speed, flight_state\(\)\)?\s*\{.*?\})', t, re.DOTALL)
    d['speed'] = ms.group(1) if ms else None
    mr = re.search(r'(switch \(FEAT_AIRCRAFT, SELF, \w+_running_cost_factor, flight_state\(\)\)?\s*\{.*?\})', t, re.DOTALL)
    d['rc'] = mr.group(1) if mr else None
    mrg = re.search(r'(if \(Ranges == 0\).*)\Z', t, re.DOTALL)
    d['ranges'] = mrg.group(1) if mrg else None
    return d


def gen_pnml(tgt, d):
    ID, DON = tgt['id'], d['donor_id']
    template = d['template'].replace('#define %s_sprite_layout_template(name)' % DON,
                                      '#define %s_sprite_layout_template(name)' % ID)
    px = d['purchase']
    grey_path = d['greyscale']
    livs = d['liveries'][:N_LIVERIES]
    vlivs = [d['vliv'].get(i) for i in range(1, len(livs) + 1)]
    ov = OVERRIDES.get(ID)
    P = d['prop']; G = d['gfx']
    cap = ov['cap'] if (ov and 'cap' in ov) else P['passenger_capacity']
    mail = ov['mail'] if (ov and 'mail' in ov) else P['mail_capacity']
    range_val = ov['rng'] if (ov and 'rng' in ov) else P['range']
    cost = ov['cost'] if (ov and 'cost' in ov) else G['cost_factor']
    # 速度缩放因子：目标巡航 / donor 巡航（18 状态）
    if ov and 'cruise' in ov:
        _sp = re.search(r'18:\s*return plane_speed_kmh\((\d+)\)', d['speed'] or '')
        sf = ov['cruise'] / int(_sp.group(1)) if _sp else 1.0
    else:
        sf = 1.0
    purchase_speed = G['purchase_speed']
    if sf != 1.0:
        purchase_speed = re.sub(r'plane_speed_kmh\((\d+)\)',
                                lambda mm: 'plane_speed_kmh(%d)' % round(int(mm.group(1)) * sf), purchase_speed)
    speed = (d['speed'] or '').replace(DON, ID)
    if sf != 1.0:
        speed = re.sub(r'plane_speed_kmh\((\d+)\)',
                       lambda mm: 'plane_speed_kmh(%d)' % round(int(mm.group(1)) * sf), speed)
    rc = (d['rc'] or '').replace(DON, ID)
    ranges = (d['ranges'] or '').replace(DON, ID)
    if ov and 'rng' in ov and P['range']:
        rf = ov['rng'] / int(P['range'])
        ranges = re.sub(r'range: (\d+);',
                        lambda mm: 'range: %d;' % (round(int(mm.group(1)) * rf) if int(mm.group(1)) != 0 else 0),
                        ranges)
    L = []
    L.append("// %s" % tgt['name_en'])
    L.append("// 占位机型：图形复用 donor %s 的精灵表；待真实像素图完成后替换本目录 PNG 即可，逻辑无需改动。" % DON)
    L.append("")
    L.append(template)
    L.append("")
    L.append("// 灰阶基底（占位复用 %s 灰阶图）" % DON)
    L.append('#define IMAGEFILE  "%s"' % grey_path)
    L.append("purchase_sprite(%s, %s)" % (ID, ", ".join(px)))
    L.append("%s_sprite_layout_template(%s_Greyscale)" % (ID, ID))
    L.append("#undef IMAGEFILE")
    basedir = grey_path.rsplit('/', 1)[0]
    for base in livs:
        L.append('#define IMAGEFILE  "%s/%s.png"' % (basedir, base))
        L.append("%s_sprite_layout_template(%s_%s)" % (ID, ID, base))
        L.append("#undef IMAGEFILE")
    L.append("")
    keys = ['Greyscale'] + livs
    for k in keys:
        L.append("switch (FEAT_AIRCRAFT, SELF, %s_%s, flight_state())" % (ID, k))
        L.append("{")
        L.append("  15: %s_%s_Climbing;" % (ID, k))
        L.append("  18: %s_%s_Flight;" % (ID, k))
        L.append("  21: %s_%s_Landing;" % (ID, k))
        L.append("  22: %s_%s_Touchdown;" % (ID, k))
        L.append("      %s_%s_Grounded;" % (ID, k))
        L.append("}")
        L.append("")
    L.append("switch (FEAT_AIRCRAFT, SELF, %s_sprites, cargo_subtype)" % ID)
    L.append("{")
    for i, base in enumerate(livs, 1):
        L.append("  %d: %s_%s;" % (i, ID, base))
    L.append("     %s_Greyscale;" % ID)
    L.append("}")
    L.append("")
    if rc:
        L.append(rc)
    else:
        L.append("switch (FEAT_AIRCRAFT, SELF, %s_running_cost_factor, flight_state())" % ID)
        L.append("{")
        L.append("  plane_RC(77)")
        L.append("}")
    L.append("")
    if speed:
        L.append(speed)
    else:
        L.append("switch (FEAT_AIRCRAFT, SELF, %s_speed, flight_state())" % ID)
        L.append("{")
        L.append("  12..13: return plane_speed_kmh(257);")
        L.append("  15: return plane_speed_kmh(362);")
        L.append("  18: return plane_speed_kmh(902);")
        L.append("  16..20: return plane_speed_kmh(467);")
        L.append("  21..22: return plane_speed_kmh(233);")
        L.append("          return plane_speed_kmh(201);")
        L.append("}")
    L.append("")
    L.append("switch (FEAT_AIRCRAFT, SELF, %s_sound_effect, extra_callback_info1)" % ID)
    L.append("{")
    L.append('  SOUND_EVENT_START     : sound("src/sound/av_turbogo.wav");')
    L.append('  SOUND_EVENT_TOUCHDOWN : sound("src/sound/av_landturbo.wav");')
    L.append("                          return CB_RESULT_NO_SOUND;")
    L.append("}")
    L.append("")
    L.append("switch (FEAT_AIRCRAFT, SELF, %s_cargo_subtype_text, cargo_subtype)" % ID)
    L.append("{")
    L.append("  0: string(STR_VLIV_%s);" % ID)
    for i, v in enumerate(vlivs, 1):
        L.append("  %d: string(%s);" % (i, v))
    L.append("     return CB_RESULT_NO_TEXT;")
    L.append("}")
    L.append("")
    L.append("switch (FEAT_AIRCRAFT, SELF, %s_cargo_subtype_capacity, cargo_subtype)" % ID)
    L.append("{")
    for i in range(1, len(livs) + 1):
        L.append("  %d: return %s;" % (i, cap))
    L.append("     return %s;" % cap)
    L.append("}")
    L.append("")
    L.append("item (FEAT_AIRCRAFT, %s)" % ID)
    L.append("{")
    L.append("  property")
    L.append("  {")
    L.append("    name: string(STR_AIRV_%s);" % ID)
    L.append("    climates_available: get_climates_available();")
    L.append("    introduction_date: date(get_plane_year(%d), 1, 1);" % tgt['year'])
    L.append("    vehicle_life: %s;" % P['vehicle_life'])
    L.append("    model_life: %s;" % P['model_life'])
    L.append("    retire_early: %s;" % P['retire_early'])
    L.append("")
    L.append("    sprite_id: SPRITE_ID_NEW_AIRCRAFT;")
    if P['aircraft_type']: L.append("    aircraft_type: %s;" % P['aircraft_type'])
    # donor 已自带 bitmask([...]) 包裹，原样输出，避免双重包裹（bitmask(bitmask(...)) / [[...]]）。
    if P['misc_flags']:
        mf = P['misc_flags'].strip()
        L.append("    misc_flags: %s;" % (mf if mf.startswith('bitmask(') else 'bitmask(%s)' % mf))
    if P['cargo_allow_refit']:
        car = P['cargo_allow_refit'].strip()
        L.append("    cargo_allow_refit: %s;" % (car if car.startswith('[') else '[%s]' % car))
    L.append("    reliability_decay: %s;" % P['reliability_decay'])
    L.append("    loading_speed: %s;" % P['loading_speed'])
    L.append("    passenger_capacity: %s;" % cap)
    L.append("    mail_capacity: %s;" % mail)
    L.append("    acceleration: %s;" % P['acceleration'])
    L.append("    range: %s;" % range_val)
    # 音效取 donor 原值（多数 SOUND_TAKEOFF_JET；A330/C929 类大飞机为 SOUND_TAKEOFF_JET_BIG）
    L.append("    sound_effect: %s;" % (P['sound_effect'] or 'SOUND_TAKEOFF_JET'))
    L.append("  }")
    L.append("  graphics {")
    L.append("    default: %s_sprites;" % ID)
    L.append("    purchase: %s_purchase_sprite;" % ID)
    L.append("    colour_mapping: PALETTE_CC_FIRST;")
    L.append("")
    L.append("    cargo_subtype_text: %s_cargo_subtype_text;" % ID)
    L.append("    passenger_capacity: %s_cargo_subtype_capacity;" % ID)
    L.append("    speed: %s_speed;" % ID)
    L.append("    running_cost_factor: %s_running_cost_factor;" % ID)
    L.append("    sound_effect: %s_sound_effect;" % ID)
    L.append("")
    L.append("    cost_factor: %s;" % cost)
    L.append("    purchase_running_cost_factor: %s;" % G['purchase_running_cost_factor'])
    L.append("    purchase_speed: %s;" % purchase_speed)
    L.append("  }")
    L.append("}")
    L.append("")
    if ranges:
        L.append(ranges)
    return "\n".join(L)


def update_lang(tgt):
    entries = {
        "lang/english.lng": (tgt['name_en'], "Generic Livery"),
        "lang/chinese_simplified.lng": (tgt['name_zh'], "通用涂装"),
        "lang/chinese_traditional.lng": (tgt['name_zh'], "通用塗裝"),
    }
    for path, (name, liv) in entries.items():
        fp = os.path.join(ROOT, path)
        with open(fp, encoding="utf-8", errors="replace") as f:
            content = f.read()
        if "STR_AIRV_%s" % tgt['id'] in content:
            continue  # 已存在则跳过
        block = "\nSTR_AIRV_%-52s:%s\nSTR_VLIV_%-51s:%s\n" % (
            tgt['id'] + " ", name, tgt['id'] + " ", liv)
        # 追加到文件末尾（NML 字符串顺序无关）
        content = content.rstrip("\n") + block
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        print("  + lang %s" % path)


def update_was(tgt):
    fp = os.path.join(ROOT, "WAS.pnml")
    with open(fp, encoding="utf-8", errors="replace") as f:
        content = f.read()
    inc = '#include "%s"' % tgt['dir']
    if inc in content:
        return
    # 插在 // Sort order 之前
    marker = "// Sort order"
    if marker in content:
        content = content.replace(marker, inc + "\n\n" + marker, 1)
    else:
        content = content.rstrip("\n") + "\n" + inc + "\n"
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
    print("  + WAS.pnml include")


def main():
    for tgt in TARGETS:
        print("== %s (%s) ==" % (tgt['id'], tgt['dir']))
        d = parse_donor(tgt['donor'])
        out = gen_pnml(tgt, d)
        outpath = os.path.join(ROOT, tgt['dir'])
        os.makedirs(os.path.dirname(outpath), exist_ok=True)
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(out)
        print("  wrote %s (donor=%s, liveries=%d)" % (tgt['dir'], d['donor_id'], min(N_LIVERIES, len(d['liveries']))))
        update_lang(tgt)
        update_was(tgt)
    print("\nDONE. Generated %d placeholder aircraft." % len(TARGETS))


if __name__ == "__main__":
    main()
