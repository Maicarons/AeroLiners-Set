"""抽取 AeroLiners-Set 全部机型(216)的当前游戏内参数，作联网核对基准。

输出:
  tools/_all_ac_params.json  -- 机器可读
  tools/_all_ac_params.txt   -- 人类可读清单(按厂商)

换算约定(已实证):
  - 真实航程 km ≈ 内部 base_range × 5.5   (range: 内部值 ÷ 5.5 = km)
  - speed_kmh 直接是巡航 km/h
  - passenger 直接是座级(乘客)
  - cost_factor 是相对价格系数(游戏不存绝对美元价)
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(r"G:/GitHub/AeroLiners-Set")
WAS = ROOT / "WAS.pnml"
LANG_EN = ROOT / "lang" / "english.lng"
LANG_ZH = ROOT / "lang" / "chinese_simplified.lng"

MFR_ZH = {
    "Airbus": "空中客车", "Antonov": "安东诺夫", "ATR": "ATR", "BAC": "BAC",
    "BAe": "英国宇航", "Boeing": "波音", "Bombardier": "庞巴迪", "Embraer": "巴航工业",
    "Fokker": "福克", "Ilyushin": "伊留申", "Lockheed": "洛克希德",
    "McDonnell_Douglas": "麦克唐纳·道格拉斯", "SUD": "SUD 宇航", "Tupolev": "图波列夫",
    "COMAC": "中国商飞", "AVIC": "中航工业", "Britten-Norman": "布里顿-诺曼",
    "Cessna": "塞斯纳", "Convair": "康维尔", "de Havilland": "德哈维兰",
    "General Atomics": "通用原子", "Hawker_Siddeley": "霍克·西德利", "Irkut": "伊尔库特",
    "LET": "LET", "Pilatus": "皮拉图斯", "PZL": "PZL", "Raytheon": "雷神",
    "Sukhoi": "苏霍伊", "Vickers": "维克斯", "Yakovlev": "雅克夫列夫",
}

KM_PER_RANGE_UNIT = 5.5  # base_range(内部) * 5.5 ≈ 真实 km


def load_lang(path: Path) -> dict:
    d = {}
    if not path.exists():
        return d
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^(STR_\w+)\s*:(.*)$", line.rstrip("\r\n"))
        if m:
            d[m.group(1)] = m.group(2).strip()
    return d


lang_en = load_lang(LANG_EN)
lang_zh = load_lang(LANG_ZH)


def re_int(text: str, pat: str):
    m = re.search(pat, text)
    return int(m.group(1)) if m else None


def main():
    was_text = WAS.read_text(encoding="utf-8", errors="replace")
    includes = []
    for line in was_text.splitlines():
        m = re.search(r'#include\s+"([^"]+\.pnml)"', line)
        if m and m.group(1).startswith("src/gfx/"):
            includes.append(m.group(1))
    print(f"发现 {len(includes)} 个机型源文件")

    out = []
    for rel in includes:
        p = ROOT / rel
        if not p.exists():
            print(f"  缺失: {rel}")
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"item\s*\(\s*FEAT_AIRCRAFT\s*,\s*(\w+)\s*\)", text)
        if not m:
            print(f"  跳过(无 item): {rel}")
            continue
        ac_id = m.group(1)
        name_key = None
        mm = re.search(r"name:\s*string\(\s*(STR_AIRV_\w+)\s*\)", text)
        if mm:
            name_key = mm.group(1)
        intro_year = None
        mm = re.search(r"get_plane_year\(\s*([0-9]+)\s*\)", text)
        if mm:
            intro_year = int(mm.group(1)) - 2
        else:
            mm = re.search(r"introduction_date:\s*date\s*\(\s*([0-9]+)\s*,", text)
            if mm:
                intro_year = int(mm.group(1))
        passenger = re_int(text, r"passenger_capacity:\s*([0-9]+)")
        cost_factor = re_int(text, r"cost_factor:\s*([0-9]+)")
        base_range = re_int(text, r"range:\s*([0-9]+)")
        speed = re_int(text, r"purchase_speed:\s*plane_speed_kmh\(\s*([0-9]+)\s*\)")
        mfr_en = rel.split("/")[2]

        range_km = round(base_range * KM_PER_RANGE_UNIT) if base_range is not None else None
        out.append({
            "id": ac_id,
            "name_en": lang_en.get(name_key, ac_id) if name_key else ac_id,
            "name_zh": lang_zh.get(name_key, lang_en.get(name_key, ac_id)) if name_key else ac_id,
            "mfr_en": mfr_en,
            "mfr_zh": MFR_ZH.get(mfr_en, mfr_en),
            "intro_year": intro_year,
            "passenger": passenger,
            "speed_kmh": speed,
            "base_range": base_range,
            "range_km_est": range_km,
            "cost_factor": cost_factor,
            "src": rel,
        })

    out.sort(key=lambda a: (a["mfr_en"], a["id"]))
    (ROOT / "tools" / "_all_ac_params.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"解析 {len(out)} 款")

    # 人类可读清单
    lines = [f"总计 {len(out)} 款\n"]
    cur = None
    for a in out:
        if a["mfr_en"] != cur:
            cur = a["mfr_en"]
            lines.append(f"\n### {a['mfr_zh']} ({cur})")
        lines.append(
            f"- {a['id']:28s} | {a['name_zh']} / {a['name_en']:22s} | 年{a['intro_year']} "
            f"| 座{a['passenger']} | 巡航{a['speed_kmh']}km/h | 航程{a['range_km_est']}km "
            f"(r={a['base_range']}) | 价系数{a['cost_factor']}"
        )
    (ROOT / "tools" / "_all_ac_params.txt").write_text("\n".join(lines), encoding="utf-8")
    print("写出 _all_ac_params.json / .txt")


if __name__ == "__main__":
    main()
