# 占位机型待办清单（TODO）

本模组目前共有 **71 款机型使用的是「占位图形」**——它们的机型逻辑、真实参数、涂装切换都已完整接入并编译进 `.grf`，
但**飞机像素精灵图暂借用了相近机型的占位图**（因为每款机型需要 5 个飞行状态 × 8 帧的手绘像素精灵，属于美术资产）。

本文档记录这 71 款机型的真实参数、当前占位图形来源，以及把它替换成真实像素图的具体任务。

> 说明：本仓库是上游 `RvP93/WorldAirlinersSet` 的独立续作。这些占位机型是本地新增内容，
> 上游并不包含，因此「替换真实图形」属于本续作的后续美术工作。

## 占位机制如何工作

每款占位机型的 `.pnml` 里，`#define IMAGEFILE` 指向的是 **donor 机型目录的 PNG**（而非本目录）。
NML 编译时直接读取 donor 的真实精灵表，因此能正常编译、在游戏里显示——只是机身外形是 donor 的样子。

替换真实图形时，只需：

1. 在本机型目录下绘制真实的精灵 PNG（保持与 donor **相同的精灵布局坐标**）；
2. 把该 `.pnml` 里所有 `#define IMAGEFILE "src/gfx/<donor>/.../*.png"` 改为指向本目录的 PNG；
3. 重新编译 `bin/AeroLinersSet.grf`，逻辑零改动。

## 待办清单（71 款）

| # | 机型 | 中文名 | 引入年* | 座级 | 航程 | 速度(km/h) | 成本 | 当前占位图形来源 | 替换优先级 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | COMAC C909 | 中国商飞 C909 | 2015 | 90 | 600 | 850 | 65 | `Embraer/E190/E190STD` | 🔴 高（外形差异大） |
| 2 | COMAC C919 | 中国商飞 C919 | 2023 | 158 | 1020 | 839 | 73 | `Airbus/A320/A320-200` | 🔴 高（国产旗舰） |
| 3 | Airbus A220-300 | 空客 A220-300 | 2016 | 145 | 1090 | 870 | 92 | `Airbus/A320/A320neo` | 🔴 高（真实是 CSeries，外形最不像） |
| 4 | Airbus A319neo | 空客 A319neo | 2017 | 160 | 1200 | 839 | 95 | `Airbus/A320/A320neo` | 🟡 中 |
| 5 | Airbus A321neo | 空客 A321neo | 2016 | 220 | 1400 | 839 | 108 | `Airbus/A320/A320neo` | 🟡 中 |
| 6 | Boeing 737 MAX 9 | 波音 737 MAX 9 | 2018 | 178 | 1250 | 839 | 106 | `Boeing/B737/B737MAX8` | 🟢 低（与 MAX 8 接近） |
| 7 | Boeing 737 MAX 10 | 波音 737 MAX 10 | 2021 | 230 | 1300 | 839 | 112 | `Boeing/B737/B737MAX9` | 🟢 低 |
| 8 | Boeing 787-10 | 波音 787-10 | 2018 | 330 | 2400 | 902 | 230 | `Boeing/B787/B787-9` | 🟢 低 |
| 9 | Airbus A330-900neo | 空客 A330-900neo | 2018 | 300 | 2600 | 871 | 190 | `Airbus/A330/A330-300` | 🟢 低 |
| 10 | Airbus A350-1000 | 空客 A350-1000 | 2018 | 366 | 2950 | 905 | 235 | `Airbus/A350/A350-900` | 🟢 低 |
| 11 | Boeing 777X | 波音 777X | 2020 | 426 | 3400 | 896 | 305 | `Boeing/B777/B777-300ER` | 🟡 中（折叠翼尖特征明显） |
| 12 | Embraer E195-E2 | 巴航工 E195-E2 | 2019 | 146 | 1050 | 890 | 44 | `Embraer/E195/E195LR` | 🟡 中（E2 是小翼后掠新造型） |
| 13 | Airbus A321XLR | 空客 A321XLR | 2024 | 150 | 1020 | 902 | 73 | `Airbus/A320/A320-200` | 🟢 低（与 A320 同族加长型） |
| 14 | Embraer E190-E2 | 巴航工 E190-E2 | 2018 | 106 | 600 | 886 | 65 | `Embraer/E190/E190STD` | 🟡 中（E2 新后掠小翼） |
| 15 | Airbus A220-100 | 空客 A220-100 | 2016 | 165 | 1165 | 833 | 101 | `Airbus/A320/A320neo` | 🔴 高（CSeries 外形差异大） |
| 16 | ATR 72-600 | ATR 72-600 | 2010 | 74 | 295 | 515 | 18 | `ATR/ATR72/72-500` | 🟢 低（同族 -600 型） |
| 17 | ATR 42-600 | ATR 42-600 | 2012 | 48 | 280 | 564 | 14 | `ATR/ATR42/42-500` | 🟢 低（同族 -600 型） |
| 18 | Boeing 737 MAX 7 | 波音 737 MAX 7 | 2024 | 162 | 1205 | 975 | 101 | `Boeing/B737/B737MAX8` | 🟢 低（MAX 系列缩短型） |
| 19 | Airbus A330-800neo | 空客 A330-800neo | 2018 | 295 | 1950 | 926 | 187 | `Airbus/A330/A330-300` | 🟢 低（同族） |
| 20 | Sukhoi Superjet 100 | 苏霍伊 Superjet 100 | 2011 | 106 | 600 | 886 | 65 | `Embraer/E190/E190STD` | 🟡 中（俄制支线，外形接近 E190） |
| 21 | Irkut MC-21 | 伊尔库特 MC-21 | 2024 | 150 | 1020 | 902 | 73 | `Airbus/A320/A320-200` | 🟡 中（俄制窄体，翼型不同） |
| 22 | COMAC C929 | 中国商飞 C929 | 2030 | 315 | 2700 | 945 | 220 | `Airbus/A350/A350-900` | 🟢 低（宽体，与 A350 接近） |
| 23 | Embraer E175-E2 | 巴航工 E175-E2 | 2027 | 86 | 600 | 886 | 26 | `Embraer/E175/E175STD` | 🟢 低（占位借用） |
| 24 | Boeing 757-300 | 波音 757-300 | 1999 | 200 | 1365 | 934 | 79 | `Boeing/B757/B757-200` | 🟢 低（占位借用） |
| 25 | Boeing 777-8 | 波音 777-8 | 2027 | 451 | 2000 | 951 | 262 | `Boeing/B777/B777-300` | 🟢 低（占位借用） |
| 26 | Antonov An-148 | 安东诺夫 安-148 | 2009 | 106 | 600 | 886 | 65 | `Embraer/E190/E190STD` | 🟢 低（占位借用） |
| 27 | Antonov An-158 | 安东诺夫 安-158 | 2010 | 106 | 600 | 886 | 65 | `Embraer/E190/E190STD` | 🟢 低（占位借用） |
| 28 | Tupolev Tu-204 | 图波列夫 图-204 | 1992 | 200 | 1365 | 934 | 79 | `Boeing/B757/B757-200` | 🟢 低（占位借用） |
| 29 | Tupolev Tu-214 | 图波列夫 图-214 | 1996 | 200 | 1365 | 934 | 79 | `Boeing/B757/B757-200` | 🟢 低（占位借用） |
| 30 | Ilyushin Il-96 | 伊尔-96 | 1992 | 295 | 1950 | 926 | 187 | `Airbus/A330/A330-300` | 🟢 低（占位借用） |
| 31 | Ilyushin Il-114 | 伊尔-114 | 1997 | 48 | 280 | 564 | 14 | `ATR/ATR42/42-500` | 🟢 低（占位借用） |
| 32 | Yakovlev Yak-40 | 雅克夫列夫 Yak-40 | 1968 | 147 | 1155 | 999 | 37 | `Boeing/B727/B727-200` | 🟢 低（占位借用） |
| 33 | Yakovlev Yak-42 | 雅克夫列夫 Yak-42 | 1980 | 147 | 1155 | 999 | 37 | `Boeing/B727/B727-200` | 🟢 低（占位借用） |
| 34 | Douglas DC-3 | 道格拉斯 DC-3 | 1936 | 48 | 280 | 564 | 14 | `ATR/ATR42/42-500` | 🟢 低（占位借用） |
| 35 | Douglas DC-6 | 道格拉斯 DC-6 | 1946 | 81 | 1330 | 504 | 35 | `Lockheed/Constellation/L049 Constellation` | 🟢 低（占位借用） |
| 36 | Douglas DC-7 | 道格拉斯 DC-7 | 1953 | 81 | 1330 | 504 | 35 | `Lockheed/Constellation/L049 Constellation` | 🟢 低（占位借用） |
| 37 | Lockheed L-188 Electra | 洛克希德 L-188 伊莱克特拉 | 1959 | 74 | 295 | 515 | 18 | `ATR/ATR72/72-500` | 🟢 低（占位借用） |
| 38 | Lockheed L-1011 TriStar | 洛克希德 L-1011 三星 | 1972 | 255 | 1910 | 983 | 155 | `McDonnell_Douglas/DC10/DC10-30` | 🟢 低（占位借用） |
| 39 | de Havilland Comet | 德哈维兰 彗星 | 1952 | 115 | 635 | 870 | 37 | `BAC/1-11/1-11-500` | 🟢 低（占位借用） |
| 40 | Vickers Viscount | 维克斯 子爵 | 1953 | 48 | 280 | 564 | 14 | `ATR/ATR42/42-500` | 🟢 低（占位借用） |
| 41 | Vickers VC10 | 维克斯 VC10 | 1962 | 168 | 1800 | 822 | 169 | `Ilyushin/Il62` | 🟢 低（占位借用） |
| 42 | Fokker F27 | 福克 F27 | 1958 | 48 | 280 | 564 | 14 | `ATR/ATR42/42-500` | 🟢 低（占位借用） |
| 43 | Fokker F28 | 福克 F28 | 1969 | 107 | 570 | 846 | 27 | `Fokker/F100` | 🟢 低（占位借用） |
| 44 | Convair 880 | 康维尔 880 | 1960 | 128 | 755 | 910 | 29 | `Boeing/B737/B737-300` | 🟢 低（占位借用） |
| 45 | Convair 990 | 康维尔 990 | 1961 | 128 | 755 | 910 | 29 | `Boeing/B737/B737-300` | 🟢 低（占位借用） |
| 46 | Hawker Siddeley Trident | 霍克·西德利 三叉戟 | 1964 | 147 | 1155 | 999 | 37 | `Boeing/B727/B727-200` | 🟢 低（占位借用） |
| 47 | Boeing 747SP | 波音 747SP | 1976 | 366 | 2000 | 967 | 265 | `Boeing/B747/B747-200` | 🟢 低（占位借用） |
| 48 | Ilyushin Il-18 | 伊尔-18 | 1957 | 74 | 295 | 515 | 18 | `ATR/ATR72/72-500` | 🟢 低（占位借用） |
| 49 | Cessna 208 Caravan | 塞斯纳 208 凯旋 | 1984 | 13 | 360 | 344 | 18 | `ATR/ATR72/72-500` | 🟢 低（占位借用；真实涡桨） |
| 50 | Cessna 208B Grand Caravan | 塞斯纳 208B 大凯旋 | 1986 | 14 | 360 | 344 | 19 | `ATR/ATR72/72-500` | 🟢 低（占位借用；真实涡桨） |
| 51 | Cessna 402 | 塞斯纳 402 | 1966 | 8 | 236 | 380 | 12 | `ATR/ATR42/42-500` | 🟢 低（占位借用；真实活塞双发） |
| 52 | Cessna 404 Titan | 塞斯纳 404 泰坦 | 1976 | 9 | 436 | 330 | 13 | `ATR/ATR42/42-500` | 🟢 低（占位借用；真实活塞双发） |
| 53 | Cessna 414 Chancellor | 塞斯纳 414 校长 | 1969 | 7 | 447 | 360 | 12 | `ATR/ATR42/42-500` | 🟢 低（占位借用；真实活塞双发） |
| 54 | Cessna 421 Golden Eagle | 塞斯纳 421 金鹰 | 1967 | 8 | 501 | 420 | 14 | `ATR/ATR42/42-500` | 🟢 低（占位借用；真实活塞双发） |
| 55 | Airbus A321LR | 空客 A321LR | 2018 | 206 | 1345 | 830 | 84 | `Airbus/A320/A321-200` | 🟢 低（真实 A321 加长型，donor 即 A321-200） |
| 56 | Antonov An-140 | 安东诺夫 安-140 | 2002 | 52 | 382 | 575 | 14 | `ATR/ATR42/42-600` | 🟢 低（占位借用；真实涡桨） |
| 57 | AVIC MA-60 | 中航工业 MA-60 | 2000 | 60 | 249 | 430 | 14 | `ATR/ATR42/42-600` | 🟢 低（占位借用；真实涡桨） |
| 58 | AVIC MA-600 | 中航工业 MA-600 | 2010 | 60 | 251 | 430 | 18 | `ATR/ATR72/72-600` | 🟢 低（占位借用；真实涡桨） |
| 59 | AVIC Y-7-200 | 中航工业 运-7-200 | 1984 | 52 | 282 | 420 | 14 | `Fokker/F27` | 🟢 低（占位借用；真实涡桨） |
| 60 | Britten-Norman BN-2B Islander | 布里顿-诺曼 BN-2B 岛民 | 1967 | 9 | 195 | 257 | 14 | `ATR/ATR42/42-600` | 🟢 低（占位借用；真实活塞双发） |
| 61 | Britten-Norman BN-2T Turbine Islander | 布里顿-诺曼 BN-2T 涡桨岛民 | 1978 | 9 | 244 | 326 | 14 | `ATR/ATR42/42-600` | 🟢 低（占位借用；真实涡桨） |
| 62 | Cessna 408 SkyCourier | 塞斯纳 408 SkyCourier | 2022 | 19 | 304 | 388 | 18 | `ATR/ATR72/72-600` | 🟢 低（占位借用；真实涡桨） |
| 63 | de Havilland DHC-6-400 Twin Otter | 德哈维兰 DHC-6-400 双水獭 | 1986 | 19 | 236 | 337 | 22 | `Bombardier/Dash_8/Dash_8-400Q` | 🟢 低（占位借用；真实涡桨） |
| 64 | Embraer ERJ-135 | 巴航工 ERJ-135 | 1999 | 37 | 591 | 834 | 14 | `Embraer/E145/ERJ145` | 🟢 低（占位借用；真实支线喷气机） |
| 65 | Embraer ERJ-140 | 巴航工 ERJ-140 | 2001 | 44 | 555 | 834 | 14 | `Embraer/E145/ERJ145` | 🟢 低（占位借用；真实支线喷气机） |
| 66 | General Atomics DO 228 | 通用原子 DO 228 | 1983 | 19 | 187 | 432 | 14 | `ATR/ATR42/42-600` | 🟢 低（占位借用；真实涡桨） |
| 67 | LET L-410 | 列特 L-410 | 1971 | 19 | 251 | 405 | 14 | `ATR/ATR42/42-600` | 🟢 低（占位借用；真实涡桨） |
| 68 | Pilatus PC-12 | 皮拉图斯 PC-12 | 1994 | 9 | 544 | 528 | 14 | `ATR/ATR42/42-600` | 🟢 低（占位借用；真实单发涡桨） |
| 69 | Pilatus PC-24 | 皮拉图斯 PC-24 | 2018 | 12 | 673 | 787 | 27 | `Fokker/F100` | 🟢 低（占位借用；真实公务喷气机） |
| 70 | PZL/Antonov AN-28 Skytruck | 安东诺夫 AN-28 空中卡车 | 1975 | 19 | 264 | 335 | 14 | `Fokker/F27` | 🟢 低（占位借用；真实涡桨） |
| 71 | Raytheon Beech 1900D Airliner | 雷神 1900D 空运者 | 1990 | 19 | 327 | 518 | 14 | `ATR/ATR42/42-600` | 🟢 低（占位借用；真实涡桨） |

> \* 引入年为 `get_plane_year(year) = year - 2` 计算后的实际可购买年份。
>
> \*\* 第 13–71 款为 **本次新增 / 修正** 的占位机（13–22 于 2026-08 初加入，23–48 于 2026-08-07 补充，49–54 塞斯纳于 2026-08-09 加入，**55–71 于 2026-08-09 从上游 WAS 完整机型清单比对缺口补齐**——含剔除已改名覆盖项 ARJ21→C909）。其中 **49–71 已按真实规格 OVERRIDE**（座级 / 航程 / 速度 / 成本列为真实值）；其余占位机的同名列为 donor 占位有效值（见「当前占位图形来源」列），并非该机型真实参数。
> 绘制真实图形时，应一并把性能参数替换为该机型真实数据。

## 各机型详情与替换步骤

### 1. COMAC C909（原 ARJ21）
- 源文件：`src/gfx/COMAC/C909/C909.pnml`
- 占位来源：`src/gfx/Embraer/E190/E190STD/*.png`（支线喷气机外形，与 C909 量级接近，但发动机/尾翼不同）
- 建议涂装：国航、东航、南航、海航、厦航（已接入）
- 替换任务：绘制 5 状态 × 8 帧的 C909 真实侧视像素图，放到 `src/gfx/COMAC/C909/`，改 `IMAGEFILE` 指向。

### 2. COMAC C919
- 源文件：`src/gfx/COMAC/C919/C919.pnml`
- 占位来源：`src/gfx/Airbus/A320/A320-200/*.png`（窄体客机外形，C919 整体轮廓类似，但机头/翼型不同）
- 建议涂装：国航、东航、南航、海航、厦航（已接入）
- 替换任务：绘制 C919 真实像素图放入 `src/gfx/COMAC/C919/`。

### 3. Airbus A220-300
- 源文件：`src/gfx/Airbus/A220/A220-300/A220-300.pnml`
- 占位来源：`src/gfx/Airbus/A320/A320neo/*.png`（**外形差异最大**——A220 是 CSeries，机身更短粗、小翼独特）
- 替换优先级最高，最该优先换图。

### 4–12. 其余机型
- 源自对应 donor 目录（见上表「当前占位图形来源」列）。
- 这些机型与 donor 多为同系列加长/衍生（如 MAX 10←MAX 9、787-10←787-9），外形接近，替换优先级较低；
  其中 **Boeing 777X**（折叠翼尖）和 **Embraer E195-E2**（新后掠小翼）的建议优先于同系列加长机型。

### 13–54. 本次新增的 42 款占位机（2026-08 初 10 款 + 2026-08-07 再 26 款 + 2026-08-09 塞斯纳 6 款）

这 10 款均由 `tools/gen_placeholder_aircraft.py` 自动生成：克隆 donor 的精灵网格宏与机型参数，仅替换标识符 / 名称 / 引入年份，并接入 donor 的前 5 个涂装（复用 donor 已有 `STR_VLIV_*` 字符串，零新增 livery 字符串负担）。逻辑与 C919 完全一致。

| # | 机型 | 生成文件 | 占位来源（donor 目录） |
| --- | --- | --- | --- |
| 13 | Airbus A321XLR | `src/gfx/Airbus/A321/A321XLR/A321XLR.pnml` | `Airbus/A320/A320-200` |
| 14 | Embraer E190-E2 | `src/gfx/Embraer/E190/E190-E2/E190-E2.pnml` | `Embraer/E190/E190STD` |
| 15 | Airbus A220-100 | `src/gfx/Airbus/A220/A220-100/A220-100.pnml` | `Airbus/A320/A320neo` |
| 16 | ATR 72-600 | `src/gfx/ATR/ATR72/72-600/72-600.pnml` | `ATR/ATR72/72-500` |
| 17 | ATR 42-600 | `src/gfx/ATR/ATR42/42-600/42-600.pnml` | `ATR/ATR42/42-500` |
| 18 | Boeing 737 MAX 7 | `src/gfx/Boeing/B737/B737MAX7/B737MAX7.pnml` | `Boeing/B737/B737MAX8` |
| 19 | Airbus A330-800neo | `src/gfx/Airbus/A330/A330-800neo/A330-800neo.pnml` | `Airbus/A330/A330-300` |
| 20 | Sukhoi Superjet 100 | `src/gfx/Sukhoi/SSJ100/SSJ100.pnml` | `Embraer/E190/E190STD` |
| 21 | Irkut MC-21 | `src/gfx/Irkut/MC21/MC21.pnml` | `Airbus/A320/A320-200` |
| 22 | COMAC C929 | `src/gfx/COMAC/C929/C929.pnml` | `Airbus/A350/A350-900` |
| 23 | Embraer E175-E2 | `src/gfx/Embraer/E175/E175-E2/E175-E2.pnml` | `Embraer/E175/E175STD` |
| 24 | Boeing 757-300 | `src/gfx/Boeing/B757/B757-300/B757-300.pnml` | `Boeing/B757/B757-200` |
| 25 | Boeing 777-8 | `src/gfx/Boeing/B777/B777-8/B777-8.pnml` | `Boeing/B777/B777-300` |
| 26 | Antonov An-148 | `src/gfx/Antonov/An148/An148.pnml` | `Embraer/E190/E190STD` |
| 27 | Antonov An-158 | `src/gfx/Antonov/An158/An158.pnml` | `Embraer/E190/E190STD` |
| 28 | Tupolev Tu-204 | `src/gfx/Tupolev/Tu204/Tu204.pnml` | `Boeing/B757/B757-200` |
| 29 | Tupolev Tu-214 | `src/gfx/Tupolev/Tu214/Tu214.pnml` | `Boeing/B757/B757-200` |
| 30 | Ilyushin Il-96 | `src/gfx/Ilyushin/Il96/Il96.pnml` | `Airbus/A330/A330-300` |
| 31 | Ilyushin Il-114 | `src/gfx/Ilyushin/Il114/Il114.pnml` | `ATR/ATR42/42-500` |
| 32 | Yakovlev Yak-40 | `src/gfx/Yakovlev/Yak40/Yak40.pnml` | `Boeing/B727/B727-200` |
| 33 | Yakovlev Yak-42 | `src/gfx/Yakovlev/Yak42/Yak42.pnml` | `Boeing/B727/B727-200` |
| 34 | Douglas DC-3 | `src/gfx/McDonnell_Douglas/DC3/DC3.pnml` | `ATR/ATR42/42-500` |
| 35 | Douglas DC-6 | `src/gfx/McDonnell_Douglas/DC6/DC6.pnml` | `Lockheed/Constellation/L049 Constellation` |
| 36 | Douglas DC-7 | `src/gfx/McDonnell_Douglas/DC7/DC7.pnml` | `Lockheed/Constellation/L049 Constellation` |
| 37 | Lockheed L-188 Electra | `src/gfx/Lockheed/L188/L188.pnml` | `ATR/ATR72/72-500` |
| 38 | Lockheed L-1011 TriStar | `src/gfx/Lockheed/L1011/L1011.pnml` | `McDonnell_Douglas/DC10/DC10-30` |
| 39 | de Havilland Comet | `src/gfx/de Havilland/Comet/Comet.pnml` | `BAC/1-11/1-11-500` |
| 40 | Vickers Viscount | `src/gfx/Vickers/Viscount/Viscount.pnml` | `ATR/ATR42/42-500` |
| 41 | Vickers VC10 | `src/gfx/Vickers/VC10/VC10.pnml` | `Ilyushin/Il62` |
| 42 | Fokker F27 | `src/gfx/Fokker/F27/F27.pnml` | `ATR/ATR42/42-500` |
| 43 | Fokker F28 | `src/gfx/Fokker/F28/F28.pnml` | `Fokker/F100` |
| 44 | Convair 880 | `src/gfx/Convair/880/880.pnml` | `Boeing/B737/B737-300` |
| 45 | Convair 990 | `src/gfx/Convair/990/990.pnml` | `Boeing/B737/B737-300` |
| 46 | Hawker Siddeley Trident | `src/gfx/Hawker_Siddeley/Trident/Trident.pnml` | `Boeing/B727/B727-200` |
| 47 | Boeing 747SP | `src/gfx/Boeing/B747/B747SP/B747SP.pnml` | `Boeing/B747/B747-200` |
| 48 | Ilyushin Il-18 | `src/gfx/Ilyushin/Il18/Il18.pnml` | `ATR/ATR72/72-500` |
| 49 | Cessna 208 Caravan | `src/gfx/Cessna/208/208/208.pnml` | `ATR/ATR72/72-500` |
| 50 | Cessna 208B Grand Caravan | `src/gfx/Cessna/208B/208B/208B.pnml` | `ATR/ATR72/72-500` |
| 51 | Cessna 402 | `src/gfx/Cessna/402/402/402.pnml` | `ATR/ATR42/42-500` |
| 52 | Cessna 404 Titan | `src/gfx/Cessna/404/404/404.pnml` | `ATR/ATR42/42-500` |
| 53 | Cessna 414 Chancellor | `src/gfx/Cessna/414/414/414.pnml` | `ATR/ATR42/42-500` |
| 54 | Cessna 421 Golden Eagle | `src/gfx/Cessna/421/421/421.pnml` | `ATR/ATR42/42-500` |
| 55 | Airbus A321LR | `src/gfx/Airbus/A321/A321LR/A321LR.pnml` | `Airbus/A320/A321-200` |
| 56 | Antonov An-140 | `src/gfx/Antonov/An140/An140.pnml` | `ATR/ATR42/42-600` |
| 57 | AVIC MA-60 | `src/gfx/AVIC/MA60/MA60.pnml` | `ATR/ATR42/42-600` |
| 58 | AVIC MA-600 | `src/gfx/AVIC/MA600/MA600.pnml` | `ATR/ATR72/72-600` |
| 59 | AVIC Y-7-200 | `src/gfx/AVIC/Y7-200/Y7-200.pnml` | `Fokker/F27` |
| 60 | Britten-Norman BN-2B Islander | `src/gfx/Britten-Norman/BN-2B/BN-2B.pnml` | `ATR/ATR42/42-600` |
| 61 | Britten-Norman BN-2T Turbine Islander | `src/gfx/Britten-Norman/BN-2T/BN-2T.pnml` | `ATR/ATR42/42-600` |
| 62 | Cessna 408 SkyCourier | `src/gfx/Cessna/408/408/408.pnml` | `ATR/ATR72/72-600` |
| 63 | de Havilland DHC-6-400 Twin Otter | `src/gfx/de Havilland/DHC6-400/DHC6-400.pnml` | `Bombardier/Dash_8/Dash_8-400Q` |
| 64 | Embraer ERJ-135 | `src/gfx/Embraer/ERJ135/ERJ135/ERJ135.pnml` | `Embraer/E145/ERJ145` |
| 65 | Embraer ERJ-140 | `src/gfx/Embraer/ERJ140/ERJ140/ERJ140.pnml` | `Embraer/E145/ERJ145` |
| 66 | General Atomics DO 228 | `src/gfx/General Atomics/DO228/DO228.pnml` | `ATR/ATR42/42-600` |
| 67 | LET L-410 | `src/gfx/LET/L410/L410.pnml` | `ATR/ATR42/42-600` |
| 68 | Pilatus PC-12 | `src/gfx/Pilatus/PC12/PC12.pnml` | `ATR/ATR42/42-600` |
| 69 | Pilatus PC-24 | `src/gfx/Pilatus/PC24/PC24.pnml` | `Fokker/F100` |
| 70 | PZL/Antonov AN-28 Skytruck | `src/gfx/PZL/AN28/AN28.pnml` | `Fokker/F27` |
| 71 | Raytheon Beech 1900D Airliner | `src/gfx/Raytheon/Beech1900D/Beech1900D.pnml` | `ATR/ATR42/42-600` |

- ATR 72-600 / 42-600 与本次新增的塞斯纳 208 / 208B（真实涡桨，donor 借 ATR72）均为涡桨音效；塞斯纳 402 / 404 / 414 / 421 为真实活塞双发，但占位暂借 ATR42 涡桨精灵与音效，后续换真实图形时需改回活塞音效。其余占位机为喷气。
- 第 55–71 款（2026-08-09 缺口补齐）：A321LR 借 A321-200 真实外形（喷气，最贴近）；An-140 / MA-60 / MA-600 / Y-7-200 / BN-2B / BN-2T / Cessna 408 / DHC-6-400 / DO 228 / LET 410 / PC-12 / AN-28 / Beech 1900D 为真实涡桨（占位于 ATR42-600 / ATR72-600 / F27 / Dash8-400Q 精灵）；ERJ-135 / ERJ-140 为真实支线喷气机（借 ERJ145 精灵）；PC-24 为真实公务喷气机（借 F100 精灵）。BN-2B 真实为活塞双发，占位暂借 ATR42 涡桨音效，后续换图时改回。
- A220-100 与已有的 A220-300 同借 `A320neo` 精灵——二者真实均为 CSeries，外形差异最大，建议优先换图。
- C929 引入年设为 2030（`get_plane_year(2030)`），属面向未来的宽体占位。

## 如何贡献真实图形

1. 在对应机型目录下绘制精灵表 PNG，保持与 donor 相同的精灵布局（可用 donor 的 PNG 作为坐标参考）。
2. 修改该 `.pnml` 的 `#define IMAGEFILE` 指向本目录。
3. 本地重新编译（见 [从源码构建](/guide/building)），确认游戏内显示正确。
4. 提交 PR / 推送到本仓库，更新本文档对应行的替换状态。

## 自动化脚本

- `tools/add_aircraft.py`：克隆 donor 机型生成占位机型 `.pnml`（生成上面第 1–12 款）。
- `tools/gen_placeholder_aircraft.py`：本次新增第 13–54 款所用的生成器，逻辑与 `add_aircraft.py` 一致——
  克隆 donor 精灵网格宏 + 机型参数，仅换标识符 / 名称 / 引入年份，接入 donor 前 5 个涂装，零新增 livery 字符串。
- `tools/gen_aircraft_md.py`：从 `WAS.pnml` 自动提取全部机型，生成 [机队图鉴](/aircraft/) 与涂装预览图。
