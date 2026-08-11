# -*- coding: utf-8 -*-
"""抽取全部占位机型的当前在役参数（解析实际生成的 .pnml，含已烘焙的 OVERRIDES）。
判定标准：.pnml 含 '占位机型' 注释即为占位机。
输出 JSON 到 tools/_ph_params.json，并打印摘要。
"""
import os, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def parse_pnml(path, force=False):
    with open(path, encoding="utf-8", errors="replace") as f:
        t = f.read()
    if (not force) and ("占位机型" not in t):
        return None
    # donor 名（来自注释，兼容旧「自动克隆自 donor X.pnml」与新「图形复用 donor X 的精灵表」两种写法）
    md = re.search(r'donor\s+([A-Za-z0-9_]+)', t)
    donor = md.group(1) if md else "?"
    # 主 item property 块（兼容逗号前后有无空格两种写法）
    mi = re.search(r'item\s*\(FEAT_AIRCRAFT\s*,\s*\w+\)\s*\{.*?property\s*\{(.*?)\}', t, re.DOTALL)
    prop = mi.group(1) if mi else ""
    def field(name):
        mm = re.search(r'(?<![A-Za-z_])%s:\s*([^;\n]+);' % re.escape(name), prop)
        return mm.group(1).strip() if mm else None
    cap = field("passenger_capacity")
    mail = field("mail_capacity")
    accel = field("acceleration")
    rng = field("range")
    atype = field("aircraft_type")
    # 引入年：introduction_date: date(get_plane_year(Y), 1, 1);  intro = Y-2
    mid = re.search(r'get_plane_year\((\d+)\)', prop)
    year_field = int(mid.group(1)) if mid else None
    intro_year = (year_field - 2) if year_field else None
    # graphics 块：cost_factor / purchase_speed
    mg = re.search(r'graphics\s*\{(.*?)\}', t, re.DOTALL)
    gfx = mg.group(1) if mg else ""
    def gfield(name):
        mm = re.search(r'(?<![A-Za-z_])%s:\s*([^;\n]+);' % re.escape(name), gfx)
        return mm.group(1).strip() if mm else None
    cost = gfield("cost_factor")
    ps = gfield("purchase_speed")
    # 巡航速度：speed switch 的 18 状态 plane_speed_kmh(N)
    ms = re.search(r'18:\s*return plane_speed_kmh\((\d+)\)', t)
    cruise = int(ms.group(1)) if ms else None
    # purchase_speed 内也可能有 plane_speed_kmh
    if ps and not cruise:
        mps = re.search(r'plane_speed_kmh\((\d+)\)', ps)
        if mps: cruise = int(mps.group(1))
    # 名称 STR_AIRV
    mn = re.search(r'name:\s*string\((STR_AIRV_\w+)\)', prop)
    sid = mn.group(1) if mn else "?"
    return {
        "id": sid,
        "file": os.path.relpath(path, ROOT),
        "donor": donor,
        "intro_year": intro_year,
        "plane_year": year_field,
        "passenger_capacity": int(cap) if cap and cap.isdigit() else cap,
        "mail_capacity": int(mail) if mail and mail.isdigit() else mail,
        "acceleration": accel,
        "range_internal": int(rng) if rng and rng.isdigit() else rng,
        "range_km_est": (round(int(rng)*5.5) if rng and rng.isdigit() else None),
        "aircraft_type": atype,
        "cost_factor": cost,
        "cruise_kmh": cruise,
    }

# 旧 add_aircraft.py 生成的 12 款占位机（无「占位机型」标记），单独补充
EXTRA_PLACEHOLDER = [
    "src/gfx/Airbus/A220/A220-300/A220-300.pnml",
    "src/gfx/Airbus/A320/A319neo/A319neo.pnml",
    "src/gfx/Airbus/A321/A321neo/A321neo.pnml",
    "src/gfx/Airbus/A330/A330-900neo/A330-900neo.pnml",
    "src/gfx/Airbus/A350/A350-1000/A350-1000.pnml",
    "src/gfx/Boeing/B737/B737MAX10/B737MAX10.pnml",
    "src/gfx/Boeing/B737/B737MAX9/B737MAX9.pnml",
    "src/gfx/Boeing/B777/B777X/B777X.pnml",
    "src/gfx/Boeing/B787/B787-10/B787-10.pnml",
    "src/gfx/COMAC/C909/C909.pnml",
    "src/gfx/COMAC/C919/C919.pnml",
    "src/gfx/Embraer/E195/E195_E2/E195_E2.pnml",
]

def main():
    files = glob.glob(os.path.join(ROOT, "src", "gfx", "**", "*.pnml"), recursive=True)
    files = [os.path.normpath(p) for p in files]
    extra = set(os.path.normpath(os.path.join(ROOT, p)) for p in EXTRA_PLACEHOLDER)
    rows = []
    for p in files:
        if p in extra:
            r = parse_pnml(p, force=True)
            if r:
                rows.append(r)
            continue
        r = parse_pnml(p)
        if r:
            rows.append(r)
    rows.sort(key=lambda x: x["id"])
    out = os.path.join(ROOT, "tools", "_ph_params.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    print("占位机总数: %d" % len(rows))
    print("无 OVERRIDES 关键项（需重点核对）请对照 generator OVERRIDES。")
    # 打印简表
    for r in rows:
        print("%-26s donor=%-22s intro=%-5s cap=%-4s mail=%-3s cruise=%-4s rng_int=%-5s rng_km≈%-6s cost=%s" % (
            r["id"], r["donor"], r["intro_year"], r["passenger_capacity"],
            r["mail_capacity"], r["cruise_kmh"], r["range_internal"],
            r["range_km_est"], r["cost_factor"]))

if __name__ == "__main__":
    main()
