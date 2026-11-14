# 项目结构

寰宇飞机 是一个由 **CMake** 驱动的 NewGRF 工程，源码以 **NML** 编写，并通过 C 预处理器（`.pnml` 文件中的
`#include` 与 `#define`）组织成上千个源文件。发布元数据集中在根目录的 `bundle.json`，
打包由 `scripts/bundle.py` 统一实现。下面按目录梳理整个仓库的构成。

```
AeroLinersSet/
├── CMakeLists.txt          # 顶层构建定义（NML / GRF / Bundles 目标）
├── CMakePresets.json       # CMake 预设（Ninja / Make / VS 生成器）
├── bundle.json             # ★ 发布元数据唯一配置源（GRFID / 版本 / 文档清单 / 包名）
├── Makefile                # CMake 生成的构建入口（make / make clean）
├── WAS.pnml                # 主入口：用 #include 汇总所有飞机源文件
├── custom_tags.txt         # 构建期生成的版本/标识信息
├── bin/                    # 构建输出：.grf / .nml / 发布 tar 包（被 .gitignore 忽略）
├── build/                  # CMake 生成的中间目录
├── docs/                   # VitePress 文档站（含随包发布的 readme.txt / license.txt / changelog.txt）
├── lang/                   # 15 种语言文件（*.lng）
├── scripts/                # 构建与打包脚本
│   ├── Compile.cmake           # 调用 nmlc 编译 .grf
│   ├── GenerateCustomTags.cmake # 生成 custom_tags.txt
│   └── bundle.py               # ★ 共享打包/校验脚本（build / verify / info）
└── src/                    # 核心源码
    ├── *.pnml              # 顶层定义（header / check / basecost / cargotable ...）
    ├── gfx/                # 所有飞机，按 制造商/系列/型号 三级目录
    └── sound/              # 起降音效（.wav）
```

## 核心源码（`src/`）

| 文件 | 作用 |
| --- | --- |
| `header.pnml` | GRF 头定义：`grfid`、`name`、`url`、版本号，以及 4 个可调参数 |
| `check.pnml` | 编译器/环境检查宏 |
| `basecost.pnml` | 基础成本相关定义 |
| `cargotable.pnml` | 货物（cargo）表定义，对应可改装项 |
| `definition.pnml` | 通用宏：`get_model_life`、`get_retire_early`、`plane_speed_kmh`、`plane_RC`、`flight_state` 等 |
| `graph_templates.pnml` | 图形模板（精灵集模板宏） |
| `disable_origin.pnml` | 禁用原版飞机等开关 |
| `sort_order.pnml` | 购买列表中飞机的排序定义 |
| `gfx/` | 每个机型一个目录，内含 `.pnml`（飞机逻辑）与若干 `.png`（涂装精灵） |
| `sound/` | 起降音效文件（`av_turbogo.wav`、`av_landturbo.wav`） |

## 飞机源文件（`src/gfx/`）

- 采用三级目录结构：`制造商 / 系列 / 具体型号`。
  例如 `Boeing / B737 / B737-800 /`。
- 每个型号目录下包含：
  - 一个 **`型号.pnml`**：定义该飞机的精灵集（spriteset）、状态切换（switch）、属性（property）与图形（graphics）。
  - 若干 **`.png` 涂装文件**：每个 PNG 对应一种航空公司涂装（含一个 `(0)Greyscale.png` 作为灰阶基底）。
- 当前有 **216** 个机型 `.pnml` 文件、约 **1743** 个涂装精灵 PNG（逻辑涂装数 2264）。

```text
src/gfx/Boeing/B737/B737-800/
├── (0)Greyscale.png      # 灰阶基底涂装
├── B737-800.pnml         # 飞机逻辑 + 精灵引用
├── AerLingus.png         # 各航空公司涂装
├── Lufthansa.png
└── ...
```

## 语言文件（`lang/`）

- 15 种语言文件，覆盖 catalan、chinese_simplified、chinese_traditional、croatian、czech、dutch、english、finnish、
  german、indonesian、italian、korean、polish、russian、spanish。
- 通过 `##grflangid` 声明语言 ID，提供所有 `STR_*` 字符串的本地化（GRF 名称、参数说明、机型名、涂装名等）。
- **`.lng` 必须保持 CRLF 行尾**（NewGRF 规范）；改动翻译后需重跑 nmlc 才会进 `.grf`。

## 构建与打包脚本（`scripts/`）

| 脚本 | 作用 |
| --- | --- |
| `Compile.cmake` | 调用 `nmlc` 把 `.nml` 编译为最终 `.grf` |
| `GenerateCustomTags.cmake` | 生成 `custom_tags.txt`（版本号、GRF 文件名、日期等） |
| `bundle.py` | 读取 `bundle.json`，文档占位符替换（${GRF_REVISION}` / ${GRF_MD5}`）、打 BaNaNa 格式的 tar / tar.gz，并自校验布局、GRF ID 与 MD5 |

## 发布元数据（`bundle.json`）

`bundle.json` 是版本、GRFID、项目名、GRF 文件名、随包文档清单与归档命名的**唯一配置源**。
`CMakeLists.txt` 与 `.github/workflows/release.yml` 都通过 `scripts/bundle.py` 读取它，
不再各自复制一份 GRFID / 版本 / 文档清单。发新版本时只需改这里的 `version`，再打 `v<版本>` tag。
归档布局见 [从源码构建 →](/guide/building)；BaNaNaS 上架步骤见对应版本的 Release 说明。

返回：[NewGRF 参数 →](/guide/parameters) ｜ 下一步：[从源码构建 →](/guide/building)
