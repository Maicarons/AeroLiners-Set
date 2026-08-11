"""从 AeroLiners-Set 的 .pnml 源文件提取全部机型与涂装数据，生成 VitePress 机队图鉴页面（简体中文 + 英文）。

与旧版 tools/gen_aircraft_md.py 的区别：
  - 路径适配 G:/GitHub/AeroLiners-Set；
  - 扩展厂商中文名映射（新增 AVIC / Cessna / 等 16 家）；
  - 双语输出：docs/aircraft/(zh) 与 docs/en/aircraft/(en)；
  - **非破坏**：复用 docs/public/aircraft 现有预览图，不重切、不删除；
    无预览图的新占位机用「占位精灵待替换」提示代替图网格；
  - 修复统计与制造商索引，使其覆盖全部机型。

用法:
    python tools/gen_aircraft_docs.py
"""
from __future__ import annotations

import os
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(r"G:/GitHub/AeroLiners-Set")
DOCS = ROOT / "docs"
PUBLIC = DOCS / "public"
WAS = ROOT / "WAS.pnml"
LANG_EN = ROOT / "lang" / "english.lng"
LANG_ZH = ROOT / "lang" / "chinese_simplified.lng"
TRAD = ROOT / "lang" / "chinese_traditional.lng"
OUT_PUBLIC = PUBLIC / "aircraft"
OUT_DOCS_ZH = DOCS / "aircraft"
OUT_DOCS_EN = DOCS / "en" / "aircraft"

# 厂商中文名（覆盖全部出现过的制造商；旧的 15 家 + 新续作新增的 16 家）
MFR_ZH = {
    "Airbus": "空中客车",
    "Antonov": "安东诺夫",
    "ATR": "ATR",
    "BAC": "BAC",
    "BAe": "英国宇航",
    "Boeing": "波音",
    "Bombardier": "庞巴迪",
    "Embraer": "巴航工业",
    "Fokker": "福克",
    "Ilyushin": "伊留申",
    "Lockheed": "洛克希德",
    "McDonnell_Douglas": "麦克唐纳·道格拉斯",
    "SUD": "SUD 宇航",
    "Tupolev": "图波列夫",
    "COMAC": "中国商飞",
    # 新续作新增
    "AVIC": "中航工业",
    "Britten-Norman": "布里顿-诺曼",
    "Cessna": "塞斯纳",
    "Convair": "康维尔",
    "de Havilland": "德哈维兰",
    "General Atomics": "通用原子",
    "Hawker_Siddeley": "霍克·西德利",
    "Irkut": "伊尔库特",
    "LET": "LET",
    "Pilatus": "皮拉图斯",
    "PZL": "PZL",
    "Raytheon": "雷神",
    "Sukhoi": "苏霍伊",
    "Vickers": "维克斯",
    "Yakovlev": "雅克夫列夫",
}

AIRCRAFT_TYPE_ZH = {
    "AIRCRAFT_TYPE_SMALL": "小型",
    "AIRCRAFT_TYPE_MEDIUM": "中型",
    "AIRCRAFT_TYPE_LARGE": "大型",
    "AIRCRAFT_TYPE_HELICOPTER": "直升机",
}

# 双语文案
LABELS = {
    "zh": {
        "index_title": "# 机队图鉴",
        "intro": "寰宇飞机 (AeroLiners Set) 收录了来自多家制造商的真实世界客机。本图鉴按制造商分类，展示全部机型与涂装预览。",
        "stats": "## 统计",
        "total_ac": "机型总数",
        "total_liv": "涂装总数",
        "total_mfr": "制造商数",
        "mfr_index_h": "## 制造商索引",
        "mfr_index_cols": "| 制造商 | 机型数 | 涂装数 | 图鉴页 |",
        "mfr_index_sep": "|---|---|---|---|",
        "all_h": "## 全部机型速览",
        "all_cols": "| 机型 | 制造商 | 引入年份 | 涂装数 | 详情 |",
        "all_sep": "|---|---|---|---|---|",
        "page_intro": "本页收录 **{mfr_zh}** 制造的 {n} 款机型，共 {liv} 张涂装预览图（含默认灰阶）。",
        "attr": {
            "intro_year": "引入年份",
            "passenger": "乘客容量",
            "mail": "邮件容量",
            "speed": "巡航速度",
            "range": "设计航程",
            "accel": "加速性能",
            "type": "机型类别",
            "cost": "成本系数",
        },
        "livery_h": "### 涂装预览（{n} 种）",
        "placeholder_note": "> ⚠️ 本机型当前使用**占位精灵**（复用 donor 机型外形），涂装预览图将在替换真实像素图后自动生成。游戏内仍按真实参数与涂装切换运行。",
        "no_livery": "_本机型暂无额外涂装。_",
    },
    "en": {
        "index_title": "# Fleet Gallery",
        "intro": "AeroLiners Set (寰宇飞机) collects real-world airliners from many manufacturers. This gallery categorizes all models with livery previews.",
        "stats": "## Statistics",
        "total_ac": "Total aircraft",
        "total_liv": "Total liveries",
        "total_mfr": "Manufacturers",
        "mfr_index_h": "## Manufacturer Index",
        "mfr_index_cols": "| Manufacturer | Models | Liveries | Gallery |",
        "mfr_index_sep": "|---|---|---|---|",
        "all_h": "## All Models at a Glance",
        "all_cols": "| Model | Manufacturer | Intro year | Liveries | Details |",
        "all_sep": "|---|---|---|---|---|",
        "page_intro": "This page collects **{mfr_zh}**'s {n} models, with {liv} livery preview images (including default greyscale).",
        "attr": {
            "intro_year": "Intro year",
            "passenger": "Passengers",
            "mail": "Mail",
            "speed": "Cruise speed",
            "range": "Design range",
            "accel": "Acceleration",
            "type": "Class",
            "cost": "Cost factor",
        },
        "livery_h": "### Livery previews ({n})",
        "placeholder_note": "> ⚠️ This model currently uses a **placeholder sprite** (reusing a donor airframe). Livery preview images will be generated automatically once real pixel art replaces it. In-game it still runs with real parameters and livery switching.",
        "no_livery": "_No extra liveries for this model._",
    },
}


def load_lang(path: Path) -> dict[str, str]:
    d: dict[str, str] = {}
    if not path.exists():
        return d
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            m = re.match(r"^(STR_\w+)\s*:(.*)$", line.rstrip("\r\n"))
            if m:
                d[m.group(1)] = m.group(2).strip()
    return d


lang_en = load_lang(LANG_EN)
lang_zh = load_lang(LANG_ZH)
lang_trad = load_lang(TRAD)


def mfr_slug(mfr_en: str) -> str:
    """厂商目录名 → 安全的页面文件名（保留下划线，空格转连字符）。"""
    return mfr_en.lower().replace(" ", "-")


def safe_filename(name: str) -> str:
    s = re.sub(r"[^\w\-]+", "_", name)
    return s.strip("_") or "unknown"


def parse_switch_block(text: str, switch_name: str) -> str | None:
    pattern = re.compile(
        r"switch\s*\(\s*FEAT_AIRCRAFT\s*,\s*SELF\s*,\s*" + re.escape(switch_name) + r"\b.*?\{(.*?)^\s*\}",
        re.S | re.M,
    )
    m = pattern.search(text)
    return m.group(1) if m else None


def re_search_int(text: str, pattern: str) -> int | None:
    m = re.search(pattern, text)
    return int(m.group(1)) if m else None


def parse_aircraft(rel: str) -> dict | None:
    pnml_path = ROOT / rel
    text = pnml_path.read_text(encoding="utf-8", errors="replace")

    m = re.search(r"item\s*\(\s*FEAT_AIRCRAFT\s*,\s*(\w+)\s*\)", text)
    if not m:
        print(f"  跳过 {rel}：未找到 item(FEAT_AIRCRAFT, ...)")
        return None
    ac_id = m.group(1)

    # 购买帧裁切坐标（占位机也内联存在；取不到则置 None，不影响文档生成）
    purchase = None
    m = re.search(r"purchase_sprite\(\s*\w+\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", text)
    if m:
        px, py, pw, ph = (int(g) for g in m.groups())
        purchase = {"x": px, "y": py, "w": pw, "h": ph}

    image_files = re.findall(r'#define\s+IMAGEFILE\s+"([^"]+)"', text)

    name_key = None
    m = re.search(r"name:\s*string\(\s*(STR_AIRV_\w+)\s*\)", text)
    if m:
        name_key = m.group(1)

    intro_year = None
    m = re.search(r"get_plane_year\(\s*([0-9]+)\s*\)", text)
    if m:
        intro_year = int(m.group(1)) - 2  # get_plane_year(year) = year - 2
    else:
        m = re.search(r"introduction_date:\s*date\s*\(\s*([0-9]+)\s*,", text)
        if m:
            intro_year = int(m.group(1))

    passenger = re_search_int(text, r"passenger_capacity:\s*([0-9]+)")
    mail = re_search_int(text, r"mail_capacity:\s*([0-9]+)")
    accel = re_search_int(text, r"acceleration:\s*([0-9]+)")
    cost_factor = re_search_int(text, r"cost_factor:\s*([0-9]+)")
    base_range = re_search_int(text, r"range:\s*([0-9]+)")

    aircraft_type = None
    m = re.search(r"aircraft_type:\s*(AIRCRAFT_TYPE_\w+)", text)
    if m:
        aircraft_type = m.group(1)

    speed_kmh = re_search_int(text, r"purchase_speed:\s*plane_speed_kmh\(\s*([0-9]+)\s*\)")

    # cargo_subtype_text：index -> STR_VLIV key（用于涂装名）
    vkey_by_index: dict[int, str] = {}
    body = parse_switch_block(text, f"{ac_id}_cargo_subtype_text")
    if body:
        for idx, vkey in re.findall(r"\b(\d+):\s*string\(\s*(STR_VLIV_\w+)\s*\)", body):
            vkey_by_index[int(idx)] = vkey

    # 制造商：include 路径 src/gfx/<Mfr>/... 取第 3 段
    mfr_en = rel.split("/")[2]

    # 由 vkey 解析出的「逻辑涂装数」（游戏内真实涂装数，含占位机）
    in_game_liveries = max(len(vkey_by_index), len(image_files), 0)

    # 预览图目录是否存在（决定是否能渲染图网格）
    preview_dir = OUT_PUBLIC / ac_id
    has_preview = preview_dir.is_dir()

    # 组装按 index 的涂装名（用于图网格标签）
    liveries_by_index: dict[int, dict] = {}
    for idx, vkey in vkey_by_index.items():
        liveries_by_index[idx] = {
            "name_en": lang_en.get(vkey, ""),
            "name_zh": lang_zh.get(vkey, lang_en.get(vkey, "")),
        }

    return {
        "id": ac_id,
        "name_key": name_key,
        "name_en": lang_en.get(name_key, ac_id) if name_key else ac_id,
        "name_zh": lang_zh.get(name_key, lang_en.get(name_key, ac_id)) if name_key else ac_id,
        "mfr_en": mfr_en,
        "mfr_zh": MFR_ZH.get(mfr_en, mfr_en),
        "intro_year": intro_year,
        "passenger": passenger,
        "mail": mail,
        "accel": accel,
        "cost_factor": cost_factor,
        "base_range": base_range,
        "aircraft_type": aircraft_type,
        "aircraft_type_zh": AIRCRAFT_TYPE_ZH.get(aircraft_type or "", aircraft_type or ""),
        "speed_kmh": speed_kmh,
        "purchase": purchase,
        "in_game_liveries": in_game_liveries,
        "has_preview": has_preview,
        "liveries_by_index": liveries_by_index,
    }


def make_attr_table(ac: dict, L: dict) -> str:
    a = L["attr"]
    lines = ["| 属性 | 数值 |", "|---|---|"]
    if ac["intro_year"] is not None:
        lines.append(f"| {a['intro_year']} | {ac['intro_year']} |")
    if ac["passenger"] is not None:
        lines.append(f"| {a['passenger']} | {ac['passenger']} |")
    if ac["mail"] is not None:
        lines.append(f"| {a['mail']} | {ac['mail']} |")
    if ac["speed_kmh"] is not None:
        lines.append(f"| {a['speed']} | {ac['speed_kmh']} km/h |")
    if ac["base_range"] is not None:
        lines.append(f"| {a['range']} | {ac['base_range']} |")
    if ac["accel"] is not None:
        lines.append(f"| {a['accel']} | {ac['accel']} |")
    if ac["aircraft_type_zh"]:
        lines.append(f"| {a['type']} | {ac['aircraft_type_zh']} |")
    if ac["cost_factor"] is not None:
        lines.append(f"| {a['cost']} | {ac['cost_factor']} |")
    return "\n".join(lines)


def make_livery_grid(ac: dict, L: dict) -> str:
    preview_dir = OUT_PUBLIC / ac["id"]
    if not preview_dir.is_dir():
        return L["placeholder_note"]
    files = sorted(preview_dir.glob("*.png"))
    if not files:
        return L["no_livery"]
    parts = ['<div class="livery-grid">']
    for fp in files:
        try:
            idx = int(fp.name.split("_")[0])
        except ValueError:
            idx = -1
        liv = ac["liveries_by_index"].get(idx, {})
        en = liv.get("name_en", "")
        zh = liv.get("name_zh", "")
        if not zh and not en:
            zh = fp.stem
        if zh and en and zh != en:
            label = f"{zh}<br><small>{en}</small>"
        else:
            label = zh or en or fp.stem
        img_path = f"/aircraft/{ac['id']}/{fp.name}"
        parts.append(
            f'  <div class="livery-card">\n'
            f'    <img src="{img_path}" alt="{zh or en}" loading="lazy">\n'
            f'    <div class="livery-name">{label}</div>\n'
            f"  </div>"
        )
    parts.append("</div>")
    return "\n".join(parts)


def livery_count(ac: dict) -> int:
    """文档展示用的涂装数：有预览图取实际文件数，否则取游戏内逻辑涂装数。"""
    preview_dir = OUT_PUBLIC / ac["id"]
    if preview_dir.is_dir():
        n = len(list(preview_dir.glob("*.png")))
        if n:
            return n
    return ac["in_game_liveries"]


def build_mfr_page(mfr_en: str, aircrafts: list[dict], lang: str) -> str:
    L = LABELS[lang]
    mfr_zh = aircrafts[0]["mfr_zh"]
    total_liv = sum(livery_count(a) for a in aircrafts)
    if lang == "en":
        title = f"# {mfr_en}"
        intro = L["page_intro"].format(mfr_zh=mfr_en, n=len(aircrafts), liv=total_liv)
    else:
        title = f"# {mfr_zh} ({mfr_en})"
        intro = L["page_intro"].format(mfr_zh=mfr_zh, n=len(aircrafts), liv=total_liv)
    lines = [title, "", intro, "", "---", ""]
    for ac in aircrafts:
        if lang == "en":
            heading = f"## {ac['name_en']} {{#{ac['id'].lower()}}}"
        else:
            heading = f"## {ac['name_zh']} <small>({ac['name_en']})</small> {{#{ac['id'].lower()}}}"
        lines.extend(
            [
                heading,
                "",
                f"- **内部 ID**：`{ac['id']}`",
                f"- **英文名**：{ac['name_en']}",
                "",
                make_attr_table(ac, L),
                "",
                L["livery_h"].format(n=livery_count(ac)),
                "",
                make_livery_grid(ac, L),
                "",
                "---",
                "",
            ]
        )
    return "\n".join(lines)


def build_index(mfr_groups: OrderedDict[str, list[dict]], total_ac: int, total_liv: int, lang: str) -> str:
    L = LABELS[lang]
    lines = [
        L["index_title"],
        "",
        L["intro"],
        "",
        L["stats"],
        "",
        f"- **{L['total_ac']}**：{total_ac}",
        f"- **{L['total_liv']}**：{total_liv}（含默认灰阶基础图）",
        f"- **{L['total_mfr']}**：{len(mfr_groups)}",
        "",
        L["mfr_index_h"],
        "",
        L["mfr_index_cols"],
        L["mfr_index_sep"],
    ]
    for mfr_en, aircrafts in mfr_groups.items():
        mfr_zh = aircrafts[0]["mfr_zh"]
        n_ac = len(aircrafts)
        n_liv = sum(livery_count(a) for a in aircrafts)
        slug = mfr_slug(mfr_en)
        if lang == "en":
            label = mfr_en
            page = f"[View]({slug}.md)"
        else:
            label = f"{mfr_zh} ({mfr_en})"
            page = f"[查看]({slug}.md)"
        lines.append(f"| {label} | {n_ac} | {n_liv} | {page} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(L["all_h"])
    lines.append("")
    lines.append(L["all_cols"])
    lines.append(L["all_sep"])
    for mfr_en, aircrafts in mfr_groups.items():
        mfr_zh = aircrafts[0]["mfr_zh"]
        for ac in aircrafts:
            year = ac["intro_year"] if ac["intro_year"] is not None else "—"
            slug = mfr_slug(mfr_en)
            link = f"[详情]({slug}.md#{ac['id'].lower()})"
            name = ac["name_en"] if lang == "en" else ac["name_zh"]
            mfr_label = mfr_en if lang == "en" else mfr_zh
            lines.append(f"| {name} | {mfr_label} | {year} | {livery_count(ac)} | {link} |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    was_text = WAS.read_text(encoding="utf-8", errors="replace")
    includes = []
    for line in was_text.splitlines():
        m = re.search(r'#include\s+"([^"]+\.pnml)"', line)
        if m and m.group(1).startswith("src/gfx/"):
            includes.append(m.group(1))
    print(f"发现 {len(includes)} 个机型源文件")

    aircrafts: list[dict] = []
    for rel in includes:
        ac = parse_aircraft(rel)
        if ac:
            aircrafts.append(ac)
    print(f"成功解析 {len(aircrafts)} 个机型")

    OUT_DOCS_ZH.mkdir(parents=True, exist_ok=True)
    OUT_DOCS_EN.mkdir(parents=True, exist_ok=True)

    # 按 include 顺序（= 自然顺序）分组
    mfr_groups: OrderedDict[str, list[dict]] = OrderedDict()
    for ac in aircrafts:
        mfr_groups.setdefault(ac["mfr_en"], []).append(ac)

    # 生成简体中文
    for mfr_en, group in mfr_groups.items():
        page = build_mfr_page(mfr_en, group, "zh")
        (OUT_DOCS_ZH / f"{mfr_slug(mfr_en)}.md").write_text(page, encoding="utf-8")
        print(f"[zh] 生成 {mfr_slug(mfr_en)}.md ({len(group)} 个机型)")
    total_ac = len(aircrafts)
    total_liv = sum(livery_count(a) for a in aircrafts)
    (OUT_DOCS_ZH / "index.md").write_text(build_index(mfr_groups, total_ac, total_liv, "zh"), encoding="utf-8")
    print(f"[zh] 生成 aircraft/index.md")

    # 生成英文
    for mfr_en, group in mfr_groups.items():
        page = build_mfr_page(mfr_en, group, "en")
        (OUT_DOCS_EN / f"{mfr_slug(mfr_en)}.md").write_text(page, encoding="utf-8")
        print(f"[en] 生成 {mfr_slug(mfr_en)}.md ({len(group)} 个机型)")
    (OUT_DOCS_EN / "index.md").write_text(build_index(mfr_groups, total_ac, total_liv, "en"), encoding="utf-8")
    print(f"[en] 生成 en/aircraft/index.md")

    # 摘要
    summary = {
        "total_aircraft": total_ac,
        "total_liveries": total_liv,
        "manufacturers": [
            {
                "en": k,
                "zh": v[0]["mfr_zh"],
                "slug": mfr_slug(k),
                "aircraft": len(v),
                "liveries": sum(livery_count(a) for a in v),
                "has_preview": any(a["has_preview"] for a in v),
            }
            for k, v in mfr_groups.items()
        ],
    }
    import json
    (OUT_DOCS_ZH / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print("完成")
    print(f"  机型总数={total_ac}  涂装总数={total_liv}  制造商数={len(mfr_groups)}")
    print("  新厂商（需加入 config.js 侧边栏）：")
    for m in summary["manufacturers"]:
        if m["en"] not in (
            "Airbus", "Antonov", "ATR", "BAC", "BAe", "Boeing", "Bombardier",
            "Embraer", "Fokker", "Ilyushin", "Lockheed", "McDonnell_Douglas",
            "SUD", "Tupolev", "COMAC",
        ):
            print(f"    - {m['zh']} ({m['en']})  slug={m['slug']}")


if __name__ == "__main__":
    main()
