"""将联网核对报告中的真实数据写回 src/gfx/**/*.pnml。

字段映射:
  - 航程 (range_km)  -> 内部 range = round(km / 5.5)；同时改 main + if(Ranges==1) 标准值，
                          if(Ranges==2) 按原比例缩放（≈1.5x）。if(Ranges==0) 保持 range:0。
  - 座级 (seats)     -> property 块 passenger_capacity: N;（有逐涂装 callback 的机型该值仅作 fallback）
  - 巡航 (cruise)    -> graphics 块 purchase_speed: plane_speed_kmh(N)，以及 speed callback 的
                        18: return 与 16..20: return（真正的航路段，二者必须与 purchase 一致，
                        否则游戏里只能飞到 16..20 的低速，达不到购买列表标称的最大速度）
  - 价格 (cost_factor)-> 不修改（游戏用相对系数，报告结论为现有值「合理」；缺失者保持当前估计值=我决定的合理值）

对「未找到可靠来源」的字段保持当前游戏值（即我决定的合理估计值），不臆造。

用法:
  python _apply_realdata.py --dry-run    # 仅解析+校验+打印摘要，不改文件
  python _apply_realdata.py --apply      # 备份并写回
"""
from __future__ import annotations
import argparse
import json
import re
import shutil
from pathlib import Path

ROOT = Path(r"G:/GitHub/AeroLiners-Set")
REPORT = ROOT / "tools" / "all_aircraft_realdata_verify.md"
PARAMS = ROOT / "tools" / "_all_ac_params.json"
BACKUP = ROOT / "tools" / "_pnml_backup"
DIFF = ROOT / "tools" / "_apply_diff.md"
KM_PER_RANGE = 5.5

param_by_id = {p["id"]: p for p in json.loads(PARAMS.read_text(encoding="utf-8"))}


def first_num(text: str, patterns):
    """返回 (value, unit) 或 None。patterns: list of (regex, multiplier)."""
    for pat, mult in patterns:
        m = re.search(pat, text)
        if m:
            return int(m.group(1).replace(",", "")) * mult, pat
    return None, None


RANGE_PAT = [
    (r"([\d,]+)\s*km", 1.0),
    (r"([\d,]+)\s*nmi", 1.852),
    (r"([\d,]+)\s*mi\b", 1.609),
]
SEAT_PAT = [
    (r"([\d,]+)\s*人", 1.0),
    (r"([\d,]+)\s*passengers?", 1.0),
    (r"([\d,]+)\s*座", 1.0),
]

# 报告座级文本未带 人/座/passengers 标记(多为「型号:X（最大）」格式，普通
# 正则兜底会误抓型号数字)，此处人工据报告原文逐一定为典型/两舱座级值。
SEAT_OVERRIDE = {
    "ATR_42_300F": 0, "ATR_72_200": 72, "ATR_72_200F": 0, "ATR_72_500": 74,
    "ATR_72_600": 72, "AVIC_MA60": 60, "AVIC_MA600": 60, "AVIC_Y7_200": 52,
    "AIRBUS_A220_100": 116, "AIRBUS_A321LR": 206, "AIRBUS_A321XLR": 206,
    "AIRBUS_A330_800NEO": 257, "Airbus_A220_300": 141, "Airbus_A300_600F": 0,
    "Airbus_A300_600R": 247, "Airbus_A310_200": 195, "Airbus_A310_200F": 0,
    "Airbus_A310_300": 220, "Airbus_A310_300F": 0, "Airbus_A318": 107,
    "Airbus_A319": 124, "Airbus_A319neo": 140, "Airbus_A320_100": 150,
    "ANTONOV_AN140": 52, "ANTONOV_AN148": 68, "ANTONOV_AN158": 90, "Antonov_225": 0,
    "BOEING_737MAX7": 153, "BOEING_747SP": 331, "BOEING_757_300": 243, "BOEING_777_8": 395,
    "Boeing_707_320": 189, "Boeing_707_420": 189, "Boeing_717_200": 106,
    "Boeing_727_100": 106, "Boeing_727_200": 134, "Boeing_727_200F": 0,
    "Boeing_737_100": 118, "Boeing_737_200": 130, "Boeing_737_200C": 0,
    "Boeing_737_300": 149, "Boeing_737_300F": 0, "Boeing_767_300F": 0, "Boeing_777_200F": 0,
    "Bombardier_CRJ1000": 100, "Bombardier_CRJ1000EL": 104, "Bombardier_CRJ100ER": 50,
    "Bombardier_CRJ100LR": 50, "Bombardier_CRJ200ER": 50, "Bombardier_CRJ200LR": 50,
    "Bombardier_CRJ700": 70, "Bombardier_CRJ700ER": 70, "Bombardier_CRJ900": 90,
    "Bombardier_CRJ900ER": 90, "Bombardier_CRJ900LR": 90, "EMBRAER_E190_E2": 97,
    "Embraer_E170LR": 66, "Embraer_E170STD": 66, "Embraer_E175LR": 76, "Embraer_E175STD": 76,
    "ILYUSHIN_IL114": 64, "ILYUSHIN_IL18": 100, "ILYUSHIN_IL96": 262, "Ilyushin_62": 186,
    "IRKUT_MC21": 163, "McDonnell_Douglas_MD11F": 0, "SUKHOI_SSJ100": 92,
    "TUPOLEV_TU204": 190, "TUPOLEV_TU214": 200, "Tupolev_Tu134": 84,
    "Tupolev_Tu154B": 150, "Tupolev_Tu154M": 150, "YAKOVLEV_YAK40": 32, "YAKOVLEV_YAK42": 96,
}


def seat_fallback(real: str):
    """座级文本未带 人/座/passengers 时的兜底：取首个「非型号数字」。

    排除型号中的数字(如 Y-7 的 7、An-148 的 148、DC-9 的 9)：数字前不能是
    字母或连字符。座级数字通常独立出现(如 '52（最大）'、'89（单级最大）')。
    """
    for m in re.finditer(r"(?<![A-Za-z-])(\d+)", real):
        n = int(m.group(1))
        if 0 <= n <= 2000:
            return n
    return None
CRUISE_PAT = [
    (r"([\d,]+)\s*km/h", 1.0),
    (r"([\d,]+)\s*kt\b", 1.852),
    (r"([\d,]+)\s*mach", 1062.0),
]


def parse_section(body: str):
    rows = {}
    for line in body.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        field, real, cur = cells[0], cells[1], cells[3]
        rows[field] = (real, cur)
    return rows


def validate_cur(field, cur, expected):
    if expected is None:
        return None
    m = None
    if field == "航程":
        m = re.search(r"range_km_est\s*([\d,]+)", cur)
    elif field == "座级":
        m = re.search(r"passenger\s*([\d,]+)", cur)
    elif field == "巡航":
        m = re.search(r"speed_kmh\s*([\d,]+)", cur)
    if not m:
        return None
    return int(m.group(1).replace(",", "")) == expected


def main():
    args = argparse.ArgumentParser()
    args.add_argument("--apply", action="store_true")
    args.add_argument("--dry-run", dest="apply", action="store_false")
    args.set_defaults(apply=False)
    ns = args.parse_args()
    apply = ns.apply

    text = REPORT.read_text(encoding="utf-8")
    lines = text.splitlines()
    hdr = re.compile(r"^###\s+(.+?)\s*\(([A-Za-z0-9_]+)\)\s*$")
    sections = []
    cur = None
    for line in lines:
        m = hdr.match(line)
        if m:
            cur = {"name": m.group(1), "id": m.group(2), "body": []}
            sections.append(cur)
        elif cur is not None:
            cur["body"].append(line)

    targets = {}
    validation = {"range_ok": 0, "range_bad": 0, "seat_ok": 0, "seat_bad": 0,
                  "cruise_ok": 0, "cruise_bad": 0}
    no_real = []  # 未找到可靠来源 字段
    unparsed_ids = []
    dup_ids = set()

    for s in sections:
        tid = s["id"]
        if tid not in param_by_id:
            continue
        if tid in targets:
            dup_ids.add(tid)
            continue
        p = param_by_id[tid]
        rows = parse_section("\n".join(s["body"]))
        rec = {"id": tid, "name": s["name"]}

        # 航程
        if "航程" in rows:
            real, cur = rows["航程"]
            if "未找到可靠来源" in real:
                rec["range_keep_current"] = True
                no_real.append((tid, "range"))
            else:
                val, _ = first_num(real, RANGE_PAT)
                rec["range_km"] = val
                v = validate_cur("航程", cur, round(p["base_range"] * KM_PER_RANGE))
                if v is True:
                    validation["range_ok"] += 1
                elif v is False:
                    validation["range_bad"] += 1
                    rec.setdefault("warn", []).append(f"range cur mismatch (report {cur})")
        # 座级
        if "座级" in rows:
            real, cur = rows["座级"]
            if "未找到可靠来源" in real:
                rec["seat_keep_current"] = True
                no_real.append((tid, "seat"))
            elif tid in SEAT_OVERRIDE:
                rec["seats"] = SEAT_OVERRIDE[tid]
            else:
                val, _ = first_num(real, SEAT_PAT)
                if val is None:
                    val = seat_fallback(real)
                rec["seats"] = val
                v = validate_cur("座级", cur, p["passenger"])
                if v is True:
                    validation["seat_ok"] += 1
                elif v is False:
                    validation["seat_bad"] += 1
                    rec.setdefault("warn", []).append(f"seat cur mismatch (report {cur})")
        # 巡航
        if "巡航" in rows:
            real, cur = rows["巡航"]
            if "未找到可靠来源" in real:
                rec["cruise_keep_current"] = True
                no_real.append((tid, "cruise"))
            else:
                val, _ = first_num(real, CRUISE_PAT)
                rec["cruise"] = val
                v = validate_cur("巡航", cur, p["speed_kmh"])
                if v is True:
                    validation["cruise_ok"] += 1
                elif v is False:
                    validation["cruise_bad"] += 1
                    rec.setdefault("warn", []).append(f"cruise cur mismatch (report {cur})")

        targets[tid] = rec

    # 汇总
    n = len(targets)
    print(f"解析到机型节: {n} / 权威 {len(param_by_id)}")
    print(f"重复 ID(已跳过重复节): {sorted(dup_ids) if dup_ids else '无'}")
    print("校验(报告'游戏内当前值' 是否等于源码当前值):")
    print(f"  航程 ok={validation['range_ok']}  bad={validation['range_bad']}")
    print(f"  座级 ok={validation['seat_ok']}  bad={validation['seat_bad']}")
    print(f"  巡航 ok={validation['cruise_ok']}  bad={validation['cruise_bad']}")
    print(f"保持当前值(未找到可靠来源)字段数: {len(no_real)} -> {no_real}")

    missing = [tid for tid in param_by_id if tid not in targets]
    if missing:
        print(f"未匹配报告(缺失)的机型: {missing}")

    # 列出无真实值且非 未找到 的情况(解析失败)
    for tid, rec in targets.items():
        lacks = []
        if "range_km" not in rec and not rec.get("range_keep_current"):
            lacks.append("range")
        if "seats" not in rec and not rec.get("seat_keep_current"):
            lacks.append("seat")
        if "cruise" not in rec and not rec.get("cruise_keep_current"):
            lacks.append("cruise")
        if lacks:
            unparsed_ids.append((tid, lacks))
    if unparsed_ids:
        print(f"\n解析失败(无真实值且非'未找到')的机型: {unparsed_ids}")

    if not apply:
        # 写出 targets 供后续 apply 使用
        (ROOT / "tools" / "_apply_targets.json").write_text(
            json.dumps(targets, ensure_ascii=False, indent=2), encoding="utf-8")
        print("\n[DRY-RUN] 已写出 tools/_apply_targets.json，未修改任何文件。")
        return

    # ---- APPLY ----
    if BACKUP.exists():
        shutil.rmtree(BACKUP)
    shutil.copytree(ROOT / "src" / "gfx", BACKUP)
    print(f"\n已备份 src/gfx -> {BACKUP}")

    diff_lines = ["# 真实数据写回差异报告（apply）", ""]
    diff_lines.append(f"总计处理: {n} 款\n")
    changed = 0

    for tid, rec in targets.items():
        p = param_by_id[tid]
        rel = p["src"]
        f = ROOT / rel
        t = f.read_text(encoding="utf-8")
        before = t
        diff = []

        # range
        if rec.get("range_keep_current"):
            pass
        elif "range_km" in rec and rec["range_km"]:
            std = round(rec["range_km"] / KM_PER_RANGE)
            # 原 Ranges==2 比例
            m2 = re.search(r"if\s*\(Ranges\s*==\s*2\)\s*\{[^}]*?range:\s*(\d+)", t)
            m1 = re.search(r"if\s*\(Ranges\s*==\s*1\)\s*\{[^}]*?range:\s*(\d+)", t)
            base_std = int(m1.group(1)) if m1 else p["base_range"]
            ext_cur = int(m2.group(1)) if m2 else round(base_std * 1.5)
            ratio = ext_cur / base_std if base_std else 1.5
            ext = round(std * ratio)
            # main range = 第一个 range:
            t, n_main = re.subn(r"range:\s*(\d+)", f"range: {std}", t, count=1)
            # Ranges==1
            t, n1 = re.subn(r"(if\s*\(Ranges\s*==\s*1\)\s*\{[^}]*?range:\s*)(\d+)",
                            lambda m: m.group(1) + str(std), t, count=1)
            # Ranges==2
            t, n2 = re.subn(r"(if\s*\(Ranges\s*==\s*2\)\s*\{[^}]*?range:\s*)(\d+)",
                            lambda m: m.group(1) + str(ext), t, count=1)
            diff.append(f"range: {p['base_range']} -> {std} (ext {ext_cur}->{ext})")
        # seats
        if rec.get("seat_keep_current"):
            pass
        elif "seats" in rec and rec["seats"] is not None:
            seats = int(rec["seats"])
            t, ns = re.subn(r"passenger_capacity:\s*(\d+)",
                            f"passenger_capacity: {seats}", t, count=1)
            diff.append(f"seats: {p['passenger']} -> {seats}")
        # cruise
        if rec.get("cruise_keep_current"):
            pass
        elif "cruise" in rec and rec["cruise"]:
            cruise = int(rec["cruise"])
            t, nc = re.subn(r"purchase_speed:\s*plane_speed_kmh\(\s*(\d+)\s*\)",
                            f"purchase_speed: plane_speed_kmh({cruise})", t, count=1)
            t, n18 = re.subn(r"(18:\s*return\s*plane_speed_kmh\(\s*)(\d+)(\s*\))",
                             lambda m, c=cruise: m.group(1) + str(c) + m.group(3), t, count=1)
            t, n_inflight = re.subn(r"(16\.\.20:\s*return\s*plane_speed_kmh\(\s*)(\d+)(\s*\))",
                                    lambda m, c=cruise: m.group(1) + str(c) + m.group(3), t, count=1)
            diff.append(f"cruise: {p['speed_kmh']} -> {cruise} (purchase={nc}, s18={n18}, inflight={n_inflight})")

        if t != before:
            f.write_text(t, encoding="utf-8")
            changed += 1
            diff_lines.append(f"### {rec['name']} ({tid})")
            diff_lines.extend(f"  - {d}" for d in diff)
            diff_lines.append("")

    diff_lines.insert(1, f"实际改动文件: {changed}")
    DIFF.write_text("\n".join(diff_lines), encoding="utf-8")
    print(f"\n已写回 {changed} 个文件。差异见 {DIFF}")


if __name__ == "__main__":
    main()
