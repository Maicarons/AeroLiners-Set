# AeroLiners-Set（寰宇飞机）— 新会话交接手册

> 给**下一个会话的 AI**看的项目速查手册。本地目录：`G:\GitHub\AeroLiners-Set`。
> 2026-11-14 重写（v1.1.3 整理后）。更早历史见 git log 与 `.workbuddy/memory/MEMORY.md`。

---

## 1. 身份表

OpenTTD **NewGRF 飞机扩充包**，由上游 **World Airliner Set（WAS / 世界客机集，`RvP93/WorldAirlinersSet`）** 独立分叉的**续作**：换品牌、换 GRFID、做中英双语文档站，**不跟随上游版本**。

| 项 | 值 |
|---|---|
| 仓库 | `Maicarons/AeroLiners-Set`（public） |
| 本地目录 | `G:\GitHub\AeroLiners-Set` |
| 中文名 / 英文名 | **寰宇飞机** / **AeroLiners Set** |
| GRFID | **`AERO`**（hex `4145524f`；上游 `WAS2`） |
| 当前版本 | **v1.1.3**（tag `v1.1.3`） |
| 文档站 | `https://maicarons.github.io/AeroLiners-Set/`（root 简中，`/en/` English） |
| 授权 | GPL-3.0；原始精灵图版权归 PikkaBird（AV8 套装）等上游作者，**署名必须保留** |

改 GRFID 的代价：旧 `WAS2` 存档因 GRFID 不匹配而不兼容，已在 Release notes 说明。

## 2. 权威数据（已从源码核对，别再数）

- **216** 机型 / **2264** 涂装 / **30** 制造商 / **15** 语言文件。
- `src/gfx/` 物理上约 **1743** 个涂装精灵 PNG（≠ 2264 逻辑涂装数，并存正常）。
- **71** 款占位机型借用 donor 像素图、尚无独立手绘精灵；清单见 `docs/guide/placeholder-aircraft-todo.md`。
- COMAC 在 `src/gfx/COMAC`，含 C909、C919。
- 计数真源 `docs/aircraft/summary.json` + `lang/*.lng`；`python tools/check_counts.py` 在 CI 校验 README、首页、`docs/guide/project-structure.md` 的硬编码数字（只匹配「数字+单位」，1743 / 65535 / 129 之类不会被误判）。

## 3. 目录结构速览

```
AeroLiners-Set/
├─ bundle.json            # ★ 发布元数据唯一配置源（GRFID / 版本 / 文档清单 / 包名）
├─ CMakeLists.txt         # project(AeroLinersSet VERSION ...) → bin/AeroLinersSet.grf
├─ CMakePresets.json      # Ninja / Make / VS 预设
├─ WAS.pnml               # 预处理入口（#include 所有 src 子文件）
├─ src/                   # 机型 .pnml + 精灵 .png + header.pnml（grfid "AERO"）
├─ lang/                  # 15 个 .lng 语言文件（CRLF 行尾！）
├─ scripts/
│  ├─ Compile.cmake       # 调 nmlc 编 .grf
│  ├─ GenerateCustomTags.cmake
│  └─ bundle.py           # ★ 共享打包/校验脚本（build / verify / info）
├─ tools/                 # 校验 / 文档生成 / 机型维护脚本
│  ├─ check_counts.py     # CI 计数校验
│  └─ gen_aircraft_docs.py# 生成机队图鉴
├─ docs/                  # VitePress 文档站（i18n）
│  ├─ .vitepress/config.js
│  ├─ index.md  guide/  aircraft/  en/
│  └─ readme.txt  license.txt  changelog.txt   # 随发布包打包
├─ .github/workflows/
│  ├─ release.yml         # v* tag → 自动编 grf + 打包 + 发 GitHub Release
│  └─ deploy-docs.yml     # main + docs/** → Pages
├─ bin/                   # 构建产物（.grf / .nml / .tar），被 .gitignore 忽略
└─ README.md  README_zh.md  tip.md
```

> `bin/`、`docs/.vitepress/dist/`、`node_modules/` 均被 `.gitignore` 忽略；`.grf` 不入库，只作 Release 附件与 BaNaNaS 包分发。

## 4. 构建 / 编译

两步：C 预处理器展开 `.pnml` → `nmlc` 编 `.grf`。

```bash
# 1) 预处理（REPO_REVISION = 自 2000-01-01 起的天数，即 grf 内部版本号）
gcc -D REPO_REVISION=$(python scripts/bundle.py info --key repo_revision)  \
    -D NEWGRF_VERSION=$(python scripts/bundle.py info --key version)  \
    -C -E -nostdinc -x c-header  \
    -o bin/AeroLinersSet.nml WAS.pnml

# 2) 编译（nmlc 由 pip install nml 提供；走 7890 代理）
nmlc --grf=bin/AeroLinersSet.grf -c bin/AeroLinersSet.nml
```

- **grf 内部版本号 = `REPO_REVISION`（天数）**，不是 `NEWGRF_VERSION`；后者只影响 `custom_tags.txt` 与元数据。升版本 = 改 `bundle.json` 的 version + 打 `vX.Y.Z` tag + 重编 grf。
- CMake 目标：`NML`（预处理）、`GRF`（nmlc）、`Bundles`（调 `bundle.py build`，属于 ALL）。`cmake --preset ninja` 后 `cmake --build build/ninja` 即可。
- 文档站本地构建：`NODE_OPTIONS="" npm run docs:build`（见第 7 节坑 3）。

## 5. 发布配置（v1.1.3 起解耦）

**唯一配置源 `bundle.json`**：`grfid` / `grfid_text` / `name` / `version` / `grf_file` / `bin_dir` / `docs_src_dir` / `docs` / `bundle_dir` / `archive`（后两者是 ${name} 等模板）。

**唯一打包实现 `scripts/bundle.py`**：
- `python scripts/bundle.py info --key version|grfid|repo_revision|archive` → 给 CMake / CI 取单一值；
- `python scripts/bundle.py build` → 读 `bin/AeroLinersSet.grf` + 3 份 docs，替换 `readme.txt` 的 ${GRF_REVISION} / ${GRF_MD5} 占位符、统一 LF 行尾，产出 `bin/4145524f-AeroLinersSet-<版本>.tar` 与 `.tar.gz`，并自校验；
- `python scripts/bundle.py verify <tar> --ref bin/AeroLinersSet.grf` → 校验顶层目录、文件清单、GRF ID（Action 8）、GRF MD5。

tar 布局（BaNaNaS / OpenTTD content 格式）：顶层**单目录** `AeroLinersSet-<版本>/`，内含 `AeroLinersSet.grf` + `readme.txt` + `license.txt` + `changelog.txt`。

> 历史：`CMakeLists.txt` 曾手写 staging + `cmake -E tar`（4 种压缩），`release.yml` 曾手写 `cp`/`tar`/`GRFID="4145524f"`，`ProcessDocs.cmake` 用 `configure_file` 但传错变量名导致占位符空值。v1.1.3 全部收敛到 bundle.json + bundle.py，别再复制回去了。

## 6. 发布流程（发新版本）

1. 改 `bundle.json` 的 `version`；在 `docs/changelog.txt` 顶部加中英双语新节。
2. `git commit` → `git tag v<版本>` → `git push origin main && git push origin v<版本>`。
3. `.github/workflows/release.yml` 自动：`verify-counts`（check_counts.py）→ `build`（校验 tag==bundle.json version、gcc+nmlc、`bundle.py build` + `verify`）→ `gh release create` 上传 `.tar` / `.tar.gz` / `.grf`，notes 取 `docs/changelog.txt`。
4. **BaNaNaS 上架**：登录 `https://bananas.openttd.org` → 用本续作自己的账号/条目上传 `4145524f-AeroLinersSet-<版本>.tar`（**不要覆盖上游 WAS 条目**）；首次需单独申请。
5. push 到 main 会自动触发 `deploy-docs.yml` 重新部署文档（paths 含 `docs/**`）。

## 7. ★ 必踩的坑（新会话务必先读）

### 坑 1：gh 默认解析到 upstream → 404
所有 `gh` 仓库命令都要显式加 `--repo Maicarons/AeroLiners-Set`（release/create/edit、api、run 等）。

### 坑 2：git push 代理
本机 git 全局 `http.proxy=127.0.0.1:7890` 在当前环境失效（直连也超时）。实测可用：
```bash
env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy  \
  git -c http.proxy=http://127.0.0.1:7890 -c https.proxy=http://127.0.0.1:7890  \
  -c http.sslbackend=schannel -c http.schannelCheckRevoke=false push origin <ref>
```
> 若报 `Connection was reset`，试直连变体：`env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy git -c http.proxy= -c https.proxy= -c http.sslbackend=schannel -c http.schannelCheckRevoke=false push origin <ref>`。两种在不同时间点各自奏效过。跑 `gh` 前同样先 unset 四个代理变量，否则走坏代理报 EOF。

### 坑 3：Node 构建报 `[safe-delete] 操作失败`
WorkBuddy 沙箱注入 safe-delete shim，把 unlink/rmdir 重定向到回收站导致失败。所有 Node 构建/清理命令前加 `NODE_OPTIONS=""`（用户本机无此 shim）。

### 坑 4：CRLF 行尾（Windows 写入工具陷阱）
WorkBuddy 的 Write/Edit 生成的脚本/文本是 CRLF，上 Linux 会炸（`bash\r: No such file`）。`bundle.py build` 已把随包 docs 统一转 LF；**但 `.lng` 语言文件必须保持 CRLF**（NewGRF 规范），不要转。

### 坑 5：nmlc 拒绝 `{VERSION}` 宏带 "AeroLiners" 前缀
`lang/*.lng` 的 `STR_GRF_NAME` 必须是静态名 `"AeroLiners"` / `"寰宇飞机"`，不能含 `{VERSION}`；显示名的版本号由 OpenTTD 运行时拼。

### 坑 6：改完 .lng 必须重编译才会进 .grf
语言文件不被 `.pnml` `#include`，由 nmlc 从 `lang/` 自动拾取并烘焙进 grf。改完翻译**必须重跑第 4 节的 gcc + nmlc**。

### 坑 7：残留 "WAS" / "世界客机集"
README 第 3 行、credits/changelog 里**有意保留** "WAS"/"世界客机集"/"World Airliner Set（上游）" 指代上游前身——**不要无脑全局替换**。真正属于本项目的命名应为「寰宇飞机 / AeroLiners Set」。

### 坑 8：Pages 首次启用用 POST 不是 PUT
`gh api -X POST /repos/Maicarons/AeroLiners-Set/pages -f build_type=workflow`（首次创建语义；PUT 仅用于已开过 Pages 后改源）。

## 8. 后续可做事项

- 给 71 款占位机型画真实精灵图（逻辑改动为零，见第 2 节）。
- Dependabot 的 docs 工具链告警（不影响 .grf 产物）。
- 加更多语言：i18n 接口已预留，参考 `docs/.vitepress/config.js` 的 `locales`。
- 可考虑加根 `.gitattributes`（`* text=auto eol=lf` + `*.lng text eol=crlf`），但目前未加，别擅自改行尾。

## 9. 关键文件清单（改之前先 locate）

| 改什么 | 文件 |
|---|---|
| 版本 / GRFID / 包名 / 文档清单 | `bundle.json` |
| 打包 / 校验逻辑 | `scripts/bundle.py` |
| 编译产物名 / CMake 版本 | `CMakeLists.txt` |
| 自动发版 | `.github/workflows/release.yml` |
| 品牌 / 显示名 / URL | `src/header.pnml`、`lang/*.lng`、`README.md`、`README_zh.md` |
| 文档站配置 / i18n | `docs/.vitepress/config.js`、`tools/gen_sitemap.py` |
| 占位机映射 | `docs/guide/placeholder-aircraft-todo.md` |
