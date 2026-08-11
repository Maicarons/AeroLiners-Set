# 寰宇飞机（AeroLiners Set）

> 本仓库 `Maicarons/AeroLiners-Set` 是 OpenTTD NewGRF 项目 **World Airliner Set（WAS，世界客机集）** 的**独立续作（fork / continuation）**：在沿用上游机型与图形资源的基础上，更换了全新中文品牌「寰宇飞机」、英文品牌「AeroLiners Set」与 GRFID（`AERO`），并完成文档中英双语化（i18n）。代码与图形内容源自上游，本仓库在此之上持续维护与扩展。

[![GitHub Release](https://img.shields.io/github/v/release/Maicarons/AeroLiners-Set?label=Release)](https://github.com/Maicarons/AeroLiners-Set/releases)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](docs/license.txt)

---

## 这是什么？

**寰宇飞机（AeroLiners Set）** 是一个 [OpenTTD](https://www.openttd.org/) 的 **NewGRF**（新图形资源包）。
它收录了现实世界中近期与历史上的客机与货机，并且让每一架飞机都能通过**改装（refit）**换上对应航空公司的**真实涂装**。

- 大部分原始飞机图形由 **PikkaBird** 创作，最初包含在 AV8 套装中；WAS 在此基础上加入了真实涂装，部分机型由 WAS 团队自行绘制。
- 借助 OpenTTD 的 NewGRF 引擎池支持，本套装最多可包含 **65535** 架飞机，而不再受旧版 48 架的限制。
- 当前收录 **216** 个机型、**2264** 种涂装，覆盖 **30** 家制造商，并提供 **15** 种界面语言文件。
- 可与其他飞机 NewGRF 同时加载，互不冲突。
- 项目以 **GNU General Public License v3.0** 发布。

> ℹ️ **关于品牌与兼容性**：本续作将上游的 `WAS2` 更换为全新的 GRFID `AERO`，并启用新中文名「寰宇飞机」与英文名「AeroLiners Set」。这意味着**使用旧 WAS 存档的游戏在加载本套装时会被视为不同 NewGRF**（旧存档中的飞机不会自动对应到本套装）——这是更换 GRFID 的固有代价。

## 文档中心

完整的安装、参数、构建、涂装、翻译与贡献指南都在中英双语文档站：

👉 **[寰宇飞机 文档站](https://maicarons.github.io/AeroLiners-Set/)**（VitePress 源码位于 `docs/`，可在本地 `npm run docs:dev` 预览；支持简体中文 / English 切换，并预留多语言接口）

| 你想做的事 | 去这里 |
| --- | --- |
| 了解项目背景与目标 | [项目简介](docs/guide/introduction.md) |
| 把套装装进 OpenTTD 玩游戏 | [安装与使用](docs/guide/installation.md) |
| 了解可调节的 NewGRF 参数 | [NewGRF 参数](docs/guide/parameters.md) |
| 搞清楚目录里都是什么 | [项目结构](docs/guide/project-structure.md) |
| 从源码自己编译 `.grf` | [从源码构建](docs/guide/building.md) |
| 给飞机加涂装 / 画图 | [涂装与图形](docs/guide/liveries.md) |
| 帮忙翻译界面文字 | [语言翻译](docs/guide/translating.md) |
| 提交代码或反馈问题 | [贡献指南](docs/guide/contributing.md) |

---

## 下载与安装

### 方式一：下载 Release（推荐）

从本仓库的 [GitHub Releases](https://github.com/Maicarons/AeroLiners-Set/releases) 页面下载 `AeroLinersSet.grf`，放入 OpenTTD 的 `newgrf` 目录（Windows 下通常在 `文档/OpenTTD/newgrf`），然后在游戏内「新图形」窗口中点击「添加」并启用即可。

> 中文名称需要你在 OpenTTD 的语言设置中选择**简体中文**或**繁体中文**后才会显示。

### 方式二：从 BaNaNaS 下载（仅稳定版，英文界面，上游原版）

在 OpenTTD 游戏内的「内容下载」列表中搜索 *World Airliner Set*，点击「下载」即可。该渠道提供的是**上游英文原版**（GRFID 仍为 `WAS2`），并非本续作「寰宇飞机」。如需本续作的中文品牌与最新内容，请使用方式一。

### 启用与游玩

1. 打开 OpenTTD →「新图形」设置窗口 →「添加」，选择 **AeroLiners Set（寰宇飞机）**。
2. 点击「应用设置」并新建游戏。
3. 建造任意一架飞机后，点击**改装（Refit）**按钮，会看到货物列表，每种货物后方标注了对应的航空公司涂装。选择想要的涂装，点击「改装车辆」即可。

---

## NewGRF 参数

在「新图形」窗口选中本套装后，可设置以下参数（设置入口：选中后点击「参数」或「设置」）：

| 参数 | 说明 |
| --- | --- |
| **启用标准飞机** | 是否同时启用 OpenTTD 自带的默认飞机。 |
| **启用航程设置** | 是否限制飞机的「最大飞行距离」。关闭后所有飞机航程不限。 |
| **航程限制** | 在「启用航程设置」打开时生效：`正常航程` / `加长航程` / `关闭航程`。 |
| **购买成本系数** | 调整购买价格：`0` = 1/16 倍，默认 `4` = 不变，`8` = 16 倍。 |
| **运营成本系数** | 调整运营成本：`0` = 1/16 倍，默认 `4` = 不变，`8` = 16 倍。 |

---

## 从源码编译（进阶）

> 通常你**不需要**自己编译，直接下载 Release 即可。只有当你想获取最新改动或自行修改时才需要。

构建管线为：`.pnml` →（C 预处理器）→ `.nml` →（nmlc）→ `.grf`。所需工具：

- **C 预处理器**（GCC / clang 均可，用于展开 `.pnml` 中的 `#include` 与宏）
- **nmlc**（NewGRF 编译器，`pip install nml`）
- 构建环境：make / cmake 等（CMake 已配置好 `NML`、`GRF`、`Bundles` 等目标）

简略步骤（以本仓库已验证的手动管线为例）：

```bash
# 1. 计算 REPO_REVISION（自 2000-01-01 起的天数），预处理生成 .nml
gcc -D REPO_REVISION=$(python3 -c "import datetime;print((datetime.datetime.now(datetime.timezone.utc)-datetime.datetime(2000,1,1,tzinfo=datetime.timezone.utc)).days)") \
    -D NEWGRF_VERSION=1.1.1 -C -E -nostdinc -x c-header \
    -o bin/AeroLinersSet.nml WAS.pnml

# 2. 编译为 .grf
nmlc --grf=bin/AeroLinersSet.grf -c bin/AeroLinersSet.nml
```

更完整的说明见 [从源码构建](docs/guide/building.md)。

> 注意：语言文件（`.lng`）不被 `.pnml` `#include`，而是由 nmlc 在 `lang/` 目录中自动拾取。因此**修改了翻译后必须重新运行 nmlc**，新译文才会被烘焙进 `.grf`。

---

## 翻译说明

本仓库已包含 **15** 种界面语言文件（含简体中文、繁体中文与多种欧洲语言）。

- `lang/chinese_simplified.lng` — 简体中文（`##grflangid 0x56`）
- `lang/chinese_traditional.lng` — 繁体中文（`##grflangid 0x62`，采用台湾用字，由 OpenCC `s2tw` 转换 + 台湾航司命名规则生成）

翻译原则：航司与机型以**官方/通用中文名**为准；同国多家航司（如西班牙、委内瑞拉、葡萄牙）靠音译或全称区分，避免玩家在涂装列表里混淆。机型代号（ATR/BAC/波音/空客等）按航空领域惯例保留拉丁原名。

想参与翻译或订正，请参见 [语言翻译](docs/guide/translating.md)。

---

## 许可证与版权

- **代码与图形**：GNU General Public License v3.0，详见 [docs/license.txt](docs/license.txt)。
- **原始图形归属**：大部分飞机图形源自 **PikkaBird** 的 AV8 套装，使用时请为其署名。
- 本续作的中文品牌、文档与维护工作：同样以 GPL-3.0 发布。

---

## 致谢与链接

- 上游开发主页：<https://dev.openttdcoop.org/projects/worldairlineset>
- 上游官方论坛：<http://worldairlinerset.forumotion.com/>
- TT-Forums 讨论帖：<http://www.tt-forums.net/viewtopic.php?t=39227>
- 上游代码仓库：<https://github.com/RvP93/WorldAirlinersSet>
- 寰宇飞机 文档站：<https://maicarons.github.io/AeroLiners-Set/>

**World Airliner Set 团队**（上游）：Beardie、DJNekkid、Frank、Yorick、Faddypainter、RvP93、Aras、Audigex（开发）；EXTSpotter、Dimme、Simozzz、Trainboy2004、Firzafp 等（美术）。

**特别感谢**：PikkaBird（原始图形）、ludde（创造 OpenTTD）、Petern（加入 NewGRF 引擎池，使海量飞机成为可能）、Chris Sawyer（创造 Transport Tycoon），以及所有译者与问题反馈者。

---

*本 README 由寰宇飞机 续作维护，若与上游 `readme.txt` 存在差异，以本文件为准。*
