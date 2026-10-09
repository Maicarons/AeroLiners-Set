# 如何添加新涂装

> 真实涂装是寰宇飞机最大的特色，而这些涂装全部来自社区贡献。
> **本页假设你从没画过 NewGRF 像素图，也不懂 NML。** 跟着走一遍，你就能给本套装加上一款真实的航空公司涂装。

## 先看你能做什么

| 你的情况 | 适合的贡献 | 难度 |
| --- | --- | --- |
| 会画画，想做点看得见的 | 给已有涂装的机型加一款新航司 | ⭐ 最低，只画一张 PNG |
| 会画画，想做点有分量的 | 给「借用图形」的机型画真实外形 | ⭐⭐⭐ 画满 5 状态 × 8 帧 |
| 不确定自己画得好不好 | 先挑涂装只有 1–2 款的机型练手（见[附录 B](#附录-b涂装最少的机型推荐入门)） | ⭐ |
| 完全不想画画 | [翻译航司名字](/guide/translating) | ⭐ |

---

## 第 1 步：选一架飞机，打开它的灰阶底图

每个机型目录里都有一张 `(0)Greyscale.png`——**这就是官方提供的底图**，已经画好了机身、翅膀、发动机的像素轮廓，只是没有配色。

你的工作，就是在这张底图上涂颜色。

```text
src/gfx/Airbus/A320/A318/
├── (0)Greyscale.png        ← 打开这个
├── AirFrance.png           ← 这些是已完成的涂装，可以参考
├── BA.png
├── TAROM.png
└── A318.pnml
```

如果你想给**已经有涂装的机型**加新航司，按下面步骤走即可。
如果你想给**还没有自己图形的 73 款机型**画真实外形，见[附录 A](#附录-a尚无自己图形的机型共-73-款)——那类工作量更大，但价值也最高。

---

## 第 2 步：准备 GIMP 与 OpenTTD 调色板

OpenTTD 的 NewGRF 精灵图**不能使用任意颜色**——只能使用 OpenTTD 官方调色板中的颜色，否则编译时会报错或颜色错乱。所以第一步是把调色板装进 GIMP。

1. 安装 [GIMP](https://www.gimp.org/)（免费、开源；本流程在 GIMP 2.10 上验证）。
2. 下载 **OpenTTD 调色板文件 `ttd-newgrf-win.gpl`**，下载地址见 [TT-Forums 帖子](https://www.tt-forums.net/viewtopic.php?t=91568)。
3. 打开 GIMP → 菜单 **Windows (W) → Dockable Dialogs (D)**，在右侧面板里找到调色板区域。
4. 把 `ttd-newgrf-win.gpl` 拖进调色板面板。
5. 双击 `ttd-newgrf-win.gpl`，右侧出现官方调色板。

调色板各色块（白色 / 深蓝 / 绿色 / 银色 / 红色 等）的含义，见 [TT-Wiki: Palettes And Coordinates](https://newgrf-specs.tt-wiki.net/wiki/PalettesAndCoordinates)。

本套装开启了 `PALETTE_CC_FIRST`，因此第一组颜色就是**航空公司自定义涂装色**——尾翼和机身条纹应从这一组里取色。

---

## 第 3 步：画你的涂装

在 GIMP 中打开目标机型的 `(0)Greyscale.png`，用铅笔工具直接涂色即可。

### 精灵表的布局（重要）

这张图**不是**一张普通的飞机图片，而是一张**精灵表（spritesheet）**：横向 8 格、纵向 5 行。

| 行 | 飞行状态 | 说明 |
| --- | --- | --- |
| 1 | `Flight` | 巡航飞行 |
| 2 | `Grounded` | 停机 / 滑行 |
| 3 | `Climbing` | 起飞爬升 |
| 4 | `Touchdown` | 触地瞬间（起落架压缩） |
| 5 | `Landing` | 降落放下起落架 |

每一行的 8 格是 8 个动画帧。以 A318 为例，精确坐标写在 `A318.pnml` 里：

```c
spriteset (name##_Flight, IMAGEFILE)
{
  [  5, 5, 45, 19, -23, -10, ANIM]   // x, y, 宽, 高, 锚点x, 锚点y, 动画
  [ 55, 5, 40, 21, -20, -11, ANIM]
  [100, 5, 44, 23, -22, -12, ANIM]
  ...                                // 共 8 帧
}
spriteset (name##_Grounded, IMAGEFILE)   { /* y = 47 */ }
spriteset (name##_Climbing, IMAGEFILE)   { /* y = 99 */ }
spriteset (name##_Touchdown, IMAGEFILE)  { /* y = 146 */ }
spriteset (name##_Landing,  IMAGEFILE)   { /* y = 190 */ }
```

### 四条硬性规则

1. **PNG 尺寸必须和原图完全一致**（A318 灰阶底图是 `452 × 223` 像素）。改了尺寸，所有精灵的取图位置会全错位。
2. **不要移动任何像素**。每帧里飞机的位置由 `x, y, xrel, yrel` 精确指定，你只改颜色，不改位置。
3. **必须转换成索引色（Indexed）后导出**。GIMP 菜单 **Image (I) → Mode (M) → Indexed (I)**，确认已选中 Indexed，再导出 PNG。保存成 RGB 是最常见的失败原因。
4. **只使用调色板内的颜色**。量化时把「抖动（Dither）」设为 None，避免在像素画里产生杂色。

导出为 PNG，文件名建议用航空公司名，例如 `Emirates.png`。

---

## 第 4 步：把 PNG 接进游戏

代码改动一共 4 处，全部在对应机型的 `.pnml` 里。以 `A318.pnml` 为例：

### ① 声明精灵集

在已有的 `#define IMAGEFILE` 块后面照抄一段：

```c
#define IMAGEFILE  "src/gfx/Airbus/A320/A318/Emirates.png"
Airbus_A318_sprite_layout_template(Airbus_A318_Emirates)
#undef IMAGEFILE
```

### ② 按飞行状态切换

复制一段已有的 `flight_state()` 切换：

```c
switch (FEAT_AIRCRAFT, SELF, Airbus_A318_Emirates, flight_state())
{
  15: Airbus_A318_Emirates_Climbing;
  18: Airbus_A318_Emirates_Flight;
  21: Airbus_A318_Emirates_Landing;
  22: Airbus_A318_Emirates_Touchdown;
      Airbus_A318_Emirates_Grounded;
}
```

### ③ 分配涂装编号

在 `cargo_subtype` 切换里追加一行，编号不能和已有的重复（下面是 `7`）：

```c
switch (FEAT_AIRCRAFT, SELF, Airbus_A318_sprites, cargo_subtype)
{
  1: Airbus_A318_AirFrance;
  ...
  6: Airbus_A318_TAROM;
  7: Airbus_A318_Emirates;      // ← 新增
     Airbus_A318_Greyscale;      // 默认灰阶，必须留在最后
}
```

同时在 `cargo_subtype_text` 里加上显示名称：

```c
switch (FEAT_AIRCRAFT, SELF, Airbus_A318_cargo_subtype_text, cargo_subtype)
{
  ...
  7: string(STR_VLIV_EMIRATES);
     return CB_RESULT_NO_TEXT;
}
```

货机的话，还要在 `cargo_subtype_capacity` 里补上运力。

### ④ 添加名字字符串

涂装名称定义在 **`lang/*.lng`**（不是 `cargotable.pnml`）。至少要补 `lang/english.lng`：

```text
STR_VLIV_EMIRATES                                              : Emirates
```

其他语言可以后续再补，缺省会回退到英文。命名沿用现有惯例：全大写下划线；同一航司有多代涂装时用后缀区分（如 `STR_VLIV_AIR_CANADA_OLD` / `STR_VLIV_AIR_CANADA_NEW`）。

---

## 第 5 步：编译验证

```bash
nmlc --grf=bin/AeroLinersSet.grf -c bin/AeroLinersSet.nml
```

完整的预处理 + 编译流程见[从源码构建](/guide/building)。

装进 OpenTTD，新建游戏，买下该机型 → 点**改装（Refit）** → 应该能在货物列表里看到你新加的涂装。如果没出现，多半是第 ④ 步的 `STR_` 名字拼错了，或者编号和已有涂装冲突了。

> ⚠️ 语言文件不会被 `.pnml` 的 `#include` 展开，而是 nmlc 在编译时从 `lang/` 目录自动拾取。**改完翻译必须重新运行 nmlc**，新名字才会进 `.grf`。

---

## 第 6 步：提交

1. 把 PNG 放进对应机型目录。
2. 提交改动，开一个 Pull Request。
3. 在 PR 描述里写清楚：**航空公司、机型、涂装年代**，并附上参考图片链接（例如航空爱好者网站的官方涂装照片）。
4. 维护者会编译验证后合并。

一个小技巧：在 PR 描述里注明你的署名（例如 `Livery by @yourhandle`），我们会把美术贡献者加入[致谢名单](/guide/credits)。

---

## 常见坑

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| 编译报找不到文件 | PNG 路径或文件名大小写不对 | 路径必须与仓库完全一致；Linux 上区分大小写 |
| 涂装没出现在改装列表 | `cargo_subtype` 编号重复，或 `STR_` 名字不存在 | 检查编号唯一性与 `lang/english.lng` |
| 飞机在游戏里错位 / 缺一块 | PNG 尺寸和原图不一致 | 严格保持原尺寸 |
| 颜色全乱 / 出现奇怪色块 | 导出成了 RGB，或用了调色板外的颜色 | 转成 Indexed 后再导出 |
| 改了名字游戏里没变 | 忘记重新运行 nmlc | 语言文件靠 nmlc 拾取 |

---

## 附录 A：尚无自己图形的机型（共 73 款）

这 **73** 款机型的逻辑、参数、涂装切换都已完整接入并编译进 `.grf`，但**机身像素图是从相近机型借用的**（下表 donor 列）——所以游戏里 C919 长得像 A320、ATR 42-600 长得像 ATR 42-500。

其中：

- **71 款**是「占位机型」：`IMAGEFILE` 指向 donor 目录。替换真实图形时**只需改 `IMAGEFILE` 指向本目录，逻辑零改动**。
- **2 款**（Dash 8-200、Il-76）只有灰阶底图，**连涂装都没有**，改装列表是空的。

给它们画图时，请保持与 donor **相同的精灵布局坐标**，才能无缝替换。逐机型的参数与替换步骤见[占位机型待办](/guide/placeholder-aircraft-todo)。

| 机型 | 目录 | 当前占位外观（donor） |
| --- | --- | --- |
| Cessna 208 Caravan | `Cessna/208/208` | `ATR/ATR72/72-500` |
| Cessna 208B Grand Caravan | `Cessna/208B/208B` | `ATR/ATR72/72-500` |
| Cessna 402 | `Cessna/402/402` | `ATR/ATR42/42-500` |
| Cessna 404 Titan | `Cessna/404/404` | `ATR/ATR42/42-500` |
| Cessna 408 SkyCourier | `Cessna/408/408` | `ATR/ATR72/72-500` |
| Cessna 414 Chancellor | `Cessna/414/414` | `ATR/ATR42/42-500` |
| Cessna 421 Golden Eagle | `Cessna/421/421` | `ATR/ATR42/42-500` |
| Airbus A220-100 | `Airbus/A220/A220-100` | `Airbus/A320/A320neo` |
| Airbus A220 300 | `Airbus/A220/A220-300` | `Airbus/A320/A320neo` |
| Airbus A319neo | `Airbus/A320/A319neo` | `Airbus/A320/A320neo` |
| Airbus A321LR | `Airbus/A321/A321LR` | `Airbus/A320/A321-200` |
| Airbus A321XLR | `Airbus/A321/A321XLR` | `Airbus/A320/A320-200` |
| Airbus A321neo | `Airbus/A321/A321neo` | `Airbus/A320/A320neo` |
| Airbus A330-800neo | `Airbus/A330/A330-800neo` | `Airbus/A330/A330-300` |
| Airbus A330 900neo | `Airbus/A330/A330-900neo` | `Airbus/A330/A330-300` |
| Airbus A350 1000 | `Airbus/A350/A350-1000` | `Airbus/A350/A350-900` |
| Antonov An-140 | `Antonov/An140` | `ATR/ATR42/42-500` |
| Antonov An-148 | `Antonov/An148` | `Embraer/E190/E190STD` |
| Antonov An-158 | `Antonov/An158` | `Embraer/E190/E190STD` |
| ATR 42-600 | `ATR/ATR42/42-600` | `ATR/ATR42/42-500` |
| ATR 72-600 | `ATR/ATR72/72-600` | `ATR/ATR72/72-500` |
| AVIC MA-60 | `AVIC/MA60` | `ATR/ATR42/42-500` |
| AVIC MA-600 | `AVIC/MA600` | `ATR/ATR72/72-500` |
| AVIC Y-7-200 | `AVIC/Y7-200` | `ATR/ATR42/42-500` |
| Boeing 737 MAX 7 | `Boeing/B737/B737MAX7` | `Boeing/B737/B737MAX8` |
| Boeing 737 MAX10 | `Boeing/B737/B737MAX10` | `Boeing/B737/B737MAX8` |
| Boeing 737 MAX9 | `Boeing/B737/B737MAX9` | `Boeing/B737/B737MAX8` |
| Boeing 747SP | `Boeing/B747/B747SP` | `Boeing/B747/B747-200` |
| Boeing 757-300 | `Boeing/B757/B757-300` | `Boeing/B757/B757-200` |
| Boeing 777-8 | `Boeing/B777/B777-8` | `Boeing/B777/B777-300` |
| Boeing 777X | `Boeing/B777/B777X` | `Boeing/B777/B777-300ER` |
| Boeing 787 10 | `Boeing/B787/B787-10` | `Boeing/B787/B787-9` |
| Britten-Norman BN-2B Islander | `Britten-Norman/BN-2B` | `ATR/ATR42/42-500` |
| Britten-Norman BN-2T Turbine Islander | `Britten-Norman/BN-2T` | `ATR/ATR42/42-500` |
| COMAC C929 | `COMAC/C929` | `Airbus/A350/A350-900` |
| COMAC-C909 | `COMAC/C909` | `Embraer/E190/E190STD` |
| COMAC-C919 | `COMAC/C919` | `Airbus/A320/A320-200` |
| Convair 880 | `Convair/880` | `Boeing/B737/B737-300` |
| Convair 990 | `Convair/990` | `Boeing/B737/B737-300` |
| Bombardier-Dash8-200 | `Bombardier/Dash_8/Dash_8-200` | `Bombardier/Dash_8/Dash_8-200` |
| de Havilland Comet | `de Havilland/Comet` | `BAC/1-11/1-11-500` |
| de Havilland DHC-6-400 Twin Otter | `de Havilland/DHC6-400` | `Bombardier/Dash_8/Dash_8-400Q` |
| Embraer E175-E2 | `Embraer/E175/E175-E2` | `Embraer/E175/E175STD` |
| Embraer E190-E2 | `Embraer/E190/E190-E2` | `Embraer/E190/E190STD` |
| Embraer E195 E2 | `Embraer/E195/E195_E2` | `Embraer/E195/E195LR` |
| Embraer ERJ-135 | `Embraer/ERJ135/ERJ135` | `Embraer/E145/ERJ145` |
| Embraer ERJ-140 | `Embraer/ERJ140/ERJ140` | `Embraer/E145/ERJ145` |
| Fokker F27 | `Fokker/F27` | `ATR/ATR42/42-500` |
| Fokker F28 | `Fokker/F28` | `Fokker/F100` |
| General Atomics DO 228 | `General Atomics/DO228` | `ATR/ATR42/42-500` |
| Hawker Siddeley Trident | `Hawker_Siddeley/Trident` | `Boeing/B727/B727-200` |
| Ilyushin Il-114 | `Ilyushin/Il114` | `ATR/ATR42/42-500` |
| Ilyushin Il-18 | `Ilyushin/Il18` | `ATR/ATR72/72-500` |
| Ilyushin Il-96 | `Ilyushin/Il96` | `Airbus/A330/A330-300` |
| Ilyushin-76 | `Ilyushin/Il76` | `Ilyushin/Il76` |
| Irkut MC-21 | `Irkut/MC21` | `Airbus/A320/A320-200` |
| LET L-410 | `LET/L410` | `ATR/ATR42/42-500` |
| Lockheed L-1011 TriStar | `Lockheed/L1011` | `McDonnell_Douglas/DC10/DC10-30` |
| Lockheed L-188 Electra | `Lockheed/L188` | `ATR/ATR72/72-500` |
| Douglas DC-3 | `McDonnell_Douglas/DC3` | `ATR/ATR42/42-500` |
| Douglas DC-6 | `McDonnell_Douglas/DC6` | `Lockheed/Constellation/L049 Constellation` |
| Douglas DC-7 | `McDonnell_Douglas/DC7` | `Lockheed/Constellation/L049 Constellation` |
| Pilatus PC-12 | `Pilatus/PC12` | `ATR/ATR42/42-500` |
| Pilatus PC-24 | `Pilatus/PC24` | `Fokker/F100` |
| PZL/Antonov AN-28 Skytruck | `PZL/AN28` | `ATR/ATR42/42-500` |
| Raytheon Beech 1900D Airliner | `Raytheon/Beech1900D` | `ATR/ATR42/42-500` |
| Sukhoi Superjet 100 | `Sukhoi/SSJ100` | `Embraer/E190/E190STD` |
| Tupolev Tu-204 | `Tupolev/Tu204` | `Boeing/B757/B757-200` |
| Tupolev Tu-214 | `Tupolev/Tu214` | `Boeing/B757/B757-200` |
| Vickers VC10 | `Vickers/VC10` | `Ilyushin/Il62` |
| Vickers Viscount | `Vickers/Viscount` | `ATR/ATR42/42-500` |
| Yakovlev Yak-40 | `Yakovlev/Yak40` | `Boeing/B727/B727-200` |
| Yakovlev Yak-42 | `Yakovlev/Yak42` | `Boeing/B727/B727-200` |

---

## 附录 B：涂装最少的机型（推荐入门）

这些机型**已经有自己的像素图**，你只要在其灰阶底图上涂颜色即可，是最容易上手的第一份贡献。

| 机型 | 目录 | 现有涂装数 |
| --- | --- | --- |
| BAC 1-11-300 | `BAC/1-11/1-11-300` | 1 |
| Antonov An-124 | `Antonov/An124` | 1 |
| Antonov An-225 | `Antonov/An225` | 1 |
| BAe 146-300QT | `BAe/146-300QT` | 1 |
| Boeing 737-200C | `Boeing/B737/B737-200C` | 1 |
| Boeing 747-400ER | `Boeing/B747/B747-400ER` | 1 |
| Boeing 757-200F | `Boeing/B757/B757-200F` | 1 |
| Bombardier CRJ1000EL | `Bombardier/CRJ/CRJ1000EL` | 1 |
| Bombardier Dash 8-100 | `Bombardier/Dash_8/Dash_8-100` | 1 |
| Bombardier Dash 8-200Q | `Bombardier/Dash_8/Dash_8-200Q` | 1 |
| Embraer E195STD | `Embraer/E195/E195STD` | 1 |
| McDonnell Douglas DC10-40 | `McDonnell_Douglas/DC10/DC10-40` | 1 |
| Airbus A310-200F | `Airbus/A300/A310-200F` | 2 |
| BAC 1-11-200 | `BAC/1-11/1-11-200` | 3 |
| Airbus A310-300F | `Airbus/A300/A310-300F` | 3 |
| Airbus A330-200F | `Airbus/A330/A330-200F` | 3 |
| ATR 72-200F | `ATR/ATR72/72-200F` | 3 |
| Boeing 727-200F | `Boeing/B727/B727-200F` | 3 |
| Boeing 747-300 / -300M | `Boeing/B747/B747-300`、`B747-300M` | 3 |
| Boeing 747-8F / -8I | `Boeing/B747/B747-8F`、`B747-8I` | 3 |
| Bombardier CRJ700 / -900 / -100LR / -1000 | `Bombardier/CRJ/…` | 3 |
| Bombardier Dash 8-300 | `Bombardier/Dash_8/Dash_8-300` | 3 |
| Embraer ERJ145 / E170STD / E170LR / E175STD / E175LR / E195AR | `Embraer/…` | 3 |
| McDonnell Douglas DC8-10 / -40 / DC9-20 / -40 | `McDonnell_Douglas/…` | 3 |

（完整清单见各机型 `.pnml` 中的 `cargo_subtype_text` 切换。）

---

## 相关页面

返回：[涂装与图形](/guide/liveries) ｜ [项目结构](/guide/project-structure) ｜ [从源码构建](/guide/building) ｜ [语言翻译](/guide/translating) ｜ [贡献指南](/guide/contributing) ｜ [致谢名单](/guide/credits)