# 从源码构建

寰宇飞机 使用 **CMake** 组织构建流程：先把 `.pnml` 源文件经 **C 预处理器** 展开为单一 `.nml`，
再用 **nmlc** 编译成最终的 `.grf`，最后打包成 `.tar` 系列发布包。

## 构建依赖

| 工具 | 用途 | 获取 |
| --- | --- | --- |
| **C 编译器（GCC/clang/MSVC）** | 仅用作 C 预处理器，展开 `.pnml` 中的 `#include`/`#define` | 系统自带 / MinGW |
| **nmlc** | 把 `.nml` 编译为 `.grf`（NML 编译器） | <https://github.com/OpenTTD/nml/releases/latest> |
| **Python** ≥ 3.10 | 运行 `scripts/bundle.py`：替换文档占位符、打包并自校验 | <https://www.python.org/downloads/> |
| **CMake** ≥ 3.24 | 构建系统（解析 `bundle.json`） | 系统包管理器 |
| **生成器**：Ninja / Make / VS | 实际执行构建 | 任选其一 |

> Windows 用户：安装 **MSYS2 + MinGW** 即可一次性获得 make、gcc、sed、awk 等全部工具。
> 其余类 Unix 系统通常已自带。

## 构建步骤

### 1. 配置（configure）

使用 CMake Presets 选择生成器（生成的文件会落到 `build/<generator>/`）：

```bash
# Ninja
cmake --preset ninja

# 或 Make
cmake --preset make

# 或 Visual Studio 2022
cmake --preset vs
```

### 2. 构建（build）

```bash
# Ninja（默认非详细输出）
cmake --build build/ninja --preset ninja-default

# Make
cmake --build build/make --preset make-default

# Visual Studio
cmake --build build/vs2022 --preset vs-default
```

构建会依次执行以下自定义目标：

1. **NML** —— 用 C 预处理器把 `WAS.pnml`（`src/header.pnml` 等汇总）展开为 `bin/AeroLinersSet.nml`。
2. **GRF** —— 调用 `nmlc` 把 `.nml` 编译为 `bin/AeroLinersSet.grf`。
3. **Bundles**（默认 `ALL`） —— 调用 `scripts/bundle.py`，按 `bundle.json` 把 `.grf` 与文档
   （`readme.txt` / `license.txt` / `changelog.txt`）打包成 BaNaNaS 格式的
   `4145524f-AeroLinersSet-<版本>.tar` 与 `.tar.gz`，并自动校验布局、GRFID 与 MD5。

构建产物位于 `bin/` 目录。

### 3. 清理与重编译

```bash
cmake --build build/ninja --target clean        # 清理中间产物
# 或针对单个目标
cmake --build build/ninja --target NML
cmake --build build/ninja --target GRF
```

### 详细输出（verbose）

需要查看完整命令行时，使用带 `-verbose` 后缀的 build preset（会设置 `CMAKE_VERBOSE_MAKEFILE=on` 与 `VERBOSE=on`）：

```bash
cmake --build build/ninja --preset ninja-verbose
```

## 构建流程示意

```text
WAS.pnml (include 汇总)
   │  C 预处理器 (gcc -E)
   ▼
AeroLinersSet.nml
   │  nmlc -c
   ▼
AeroLinersSet.grf
   │  scripts/bundle.py build（占位符 / 打包 / 自校验）
   ▼
4145524f-AeroLinersSet-<版本>.tar(.gz)  (BaNaNaS 发布包)
```

## 注意事项

- **版本号 / 修订**：发布版本号、GRFID、随包文档清单与包名统一写在根目录 `bundle.json`；
  `CMakeLists.txt` 与 CI 都通过 `scripts/bundle.py` 读取它，不再各自硬编码。
  `CMakeLists.txt` 通过 `string(TIMESTAMP)` 计算「自 2000 年起的天数」作为 `REPO_REVISION`，
  用于 NewGRF 的 `version` 字段；`scripts/bundle.py` 用同一公式把修订号与 `.grf` 的 MD5
  填入随包 `readme.txt`。
- **多人游戏兼容性**：如果你**修改了源码**，编译出的 `.grf` 将无法与官方版本的 寰宇飞机 在多人游戏中兼容。
  不同的 `grfcodec`/`nmlc` 版本也会改变 GRF 校验和，导致不兼容。
- **不要手改 `Makefile` / `CMakeCache.txt`**：它们由 CMake 生成。

返回：[项目结构 →](/guide/project-structure) ｜ 下一步：[涂装与图形 →](/guide/liveries)
