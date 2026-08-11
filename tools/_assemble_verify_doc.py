#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""汇编全部 17 个批次核对文件为一份完整 MD 文档。
以 tools/_all_ac_params.json 的 216 个权威 ID 为准，按厂商分组，
自动校验覆盖率与「未找到可靠来源」缺口，生成 tools/all_aircraft_realdata_verify.md。
"""
import json, os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "tools", "verify_raw")
PARAMS = os.path.join(ROOT, "tools", "_all_ac_params.json")
OUT = os.path.join(ROOT, "tools", "all_aircraft_realdata_verify.md")

params = json.load(open(PARAMS, encoding="utf-8"))
# 权威 ID 顺序（来自源码抽取）
order = [a["id"] for a in params]
meta = {a["id"]: a for a in params}

# 厂商中文名映射
MFR_ZH = {
    "Airbus": "空中客车", "Boeing": "波音", "McDonnell_Douglas": "麦道",
    "Bombardier": "庞巴迪", "Embraer": "巴航工", "ATR": "ATR",
    "AVIC": "中航工业", "Antonov": "安东诺夫", "BAC": "英国飞机公司",
    "BAe": "英宇航", "Britten-Norman": "布里顿-诺曼", "COMAC": "中国商飞",
    "Cessna": "塞斯纳", "Convair": "康维尔", "Fokker": "福克",
    "General Atomics": "通用原子", "Hawker_Siddeley": "霍克·西德利",
    "Ilyushin": "伊尔", "Irkut": "伊尔库特", "LET": "LET", "Lockheed": "洛克希德",
    "PZL": "PZL", "Pilatus": "皮拉图斯", "Raytheon": "雷神", "SUD": "南方飞机",
    "Sukhoi": "苏霍伊", "Tupolev": "图波列夫", "Vickers": "维克斯",
    "Yakovlev": "雅克福列夫", "de Havilland": "德哈维兰",
}

# 读取所有批次文件，解析为 {id: section_text}
sections = {}
missing_in_raw = []  # 文件里出现但不在权威列表的 ID
file_by_id = {}
for fp in sorted(glob.glob(os.path.join(RAW, "batch_*.md"))):
    txt = open(fp, encoding="utf-8").read()
    # 按 "### " 切分
    parts = re.split(r'(?m)^### ', txt)
    for p in parts[1:]:
        # 第一行是标题
        first = p.splitlines()[0]
        # 兼容两种 ID 写法：<id>ID</id> 优先；否则取标题行最后一个 (ID) 组
        # （规范 ID 通常置于末尾，避免误取如 "(ARJ21)" 这类别名括号）
        m = re.search(r'<id>([A-Za-z0-9_]+)</id>', first.strip())
        if m:
            idv = m.group(1)
        else:
            allp = re.findall(r'\(([A-Za-z0-9_]+)\)', first.strip())
            if not allp:
                continue
            idv = allp[-1]
        if idv in sections:
            continue  # 去重，保留首次出现
        sections[idv] = "### " + p.rstrip() + "\n"
        file_by_id[idv] = os.path.basename(fp)
    # 也扫描未在 ### 标题里但正文出现的 ID（极少数情况）
# 检查权威列表里哪些没在 sections 找到
not_found = [i for i in order if i not in sections]
# 反向：sections 里有但权威没有
extra = [i for i in sections if i not in meta]

# 统计「未找到可靠来源」出现次数（粗略按字段行）
def count_missing(sec):
    return sec.count("未找到可靠来源")

missing_total = sum(count_missing(s) for s in sections.values())

# ---- 组装文档 ----
L = []
L.append("# AeroLiners Set 全机队真实数据联网核对报告\n")
L.append("> 生成日期：2026-08-10  ｜  核对对象：游戏内 **全部 216 款** 机型（新旧皆含）")
L.append("> 核对字段：价格（美元目录价）、航程（km）、座级（乘客）、巡航速度（km/h）")
L.append("> 每个真实数据均标注**实际读取的来源 URL**；游戏内当前值一并列出以供对比。\n")

L.append("## 一、方法与来源说明\n")
L.append("- **数据来源优先级**：")
L.append("  1. [aerocorner.com](https://aerocorner.com/aircraft/) —— 结构化给出 Price、Seats，Range/Cruise 在正文（主源）；")
L.append("  2. 英文维基百科对应机型条目 —— 信息框/正文含 Range、Capacity、Cruise speed，有时含 Unit cost（交叉核对主用）；")
L.append("  3. [airliners.net/aircraft-data](https://www.airliners.net/aircraft-data) 及 WebSearch 补充 —— 主源 404 或字段缺失时定位可靠页面。")
L.append("- **单位折算**：航程统一为 km（海里 nm ×1.852）；巡航统一为 km/h（节 kt ×1.852；马赫按约 Mach×1062 @巡航高度折算并注明）。")
L.append("- **游戏内值含义**：`passenger`=座级、`speed_kmh`=巡航、`range_km_est`=游戏内航程估算（由内部值×5.5 反推）、`cost_factor`=相对价格系数（游戏不直接存绝对美元价，故真实价仅作参考，备注注明「游戏用相对系数」）。")
L.append("- **诚信原则**：每条真实数据均来自实际抓取的页面 URL；未能获取可靠来源的字段如实标注「未找到可靠来源」，绝不编造。\n")

L.append("## 二、覆盖率校验\n")
L.append(f"- 权威机型总数（源码抽取）：**{len(order)}**")
L.append(f"- 已核对并写入文档的机型：**{len(order)-len(not_found)}**")
L.append(f"- 缺失（未在任一研究批次找到）：**{len(not_found)}** " + (("→ " + ", ".join(not_found)) if not_found else "（无）"))
L.append(f"- 研究批次中出现但不在权威列表的冗余 ID：**{len(extra)}** " + (("→ " + ", ".join(extra)) if extra else "（无）"))
L.append(f"- 全文「未找到可靠来源」字段标注次数（粗略）：**{missing_total}**\n")

# 厂商分组索引
L.append("## 三、厂商分组索引\n")
# 按 order 顺序收集厂商
mfr_order = []
for i in order:
    mf = meta[i]["mfr_en"]
    if mf not in mfr_order:
        mfr_order.append(mf)
for mf in mfr_order:
    ids = [i for i in order if meta[i]["mfr_en"] == mf]
    zh = MFR_ZH.get(mf, mf)
    found = sum(1 for i in ids if i in sections)
    anchor = mf.replace(" ", "_").replace("/", "_")
    L.append(f"- **{zh} ({mf})** [{found}/{len(ids)}] —— " +
             ", ".join(f"[{i}](#{i.lower()})" for i in ids))

L.append("\n## 四、逐机核对明细（按厂商分组）\n")
for mf in mfr_order:
    zh = MFR_ZH.get(mf, mf)
    ids = [i for i in order if meta[i]["mfr_en"] == mf]
    L.append(f"### {zh} · {mf}\n")
    for i in ids:
        if i in sections:
            # 给每段加一个 HTML anchor 便于索引跳转
            sec = sections[i]
            # 在标题行追加不可见 anchor（用 markdown 兼容性写法：在 ### 行后加 <a id>
            sec = sec.replace("### ", f'<a id="{i.lower()}"></a>\n### ', 1)
            L.append(sec)
            L.append("")  # 空行分隔
        else:
            L.append(f'<a id="{i.lower()}"></a>\n### ⚠️ 未核对：{i}\n')
            L.append("> 该机型未在研究批次中找到对应核对结果，需补核。\n")

doc = "\n".join(L) + "\n"

# 写文件
open(OUT, "w", encoding="utf-8").write(doc)

# 控制台汇总
print("权威总数:", len(order))
print("已写入文档:", len(order) - len(not_found))
print("缺失:", not_found)
print("冗余:", extra)
print("未找到来源标注次数:", missing_total)
print("输出:", OUT, "字节:", len(doc))
