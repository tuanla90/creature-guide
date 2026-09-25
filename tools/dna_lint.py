"""Soát DNA của tập — phần máy bắt được của docs/DNA.md (bài học rút từ các vòng duyệt).

    from dna_lint import lint_episode
    for msg in lint_episode(c, plan, order): ...

`c` là module content.py, `plan` là dict từ drafts/4-scene-plan.json (hoặc None). Trả về danh sách
cảnh báo (chuỗi). Mỗi cảnh báo mang mã DNA (D1…) để tra ngược sang docs/DNA.md.
"""
import re

# ---- D1 · từ ngữ canon: chữ nào đã bị duyệt gạch thì bắt lại ở đây ------------------------------
TERMS = [
    # (mẫu, ngôn ngữ, sửa thành, mã DNA)
    (r"\bnết\b", "vi", "“đặc tính” — từ game thủ Việt quen gọi", "D1"),
    (r"\btemperament", "en", "“trait”", "D1"),
    (r"\bnhụy\b", "vi", "“cấu trúc giống hạt” — canon không nói đó là nhụy thật", "D1"),
    (r"\bpistil\b", "en", "“seed-like structure”", "D1"),
    (r"(?<!lục )\bxanh lam\b", "vi", "“xanh lục lam” — kiểm màu canon, đừng rút gọn màu", "D6"),
    (r"\btiêu nắng\b", "vi", "“tiêu hao năng lượng” — chữ tổng quát, không chữ tự chế", "D13"),
    (r"\bthu,? (và )?chi\b|cột “chi”", "vi", "“năng lực · cái giá” — không dùng ẩn dụ sổ sách", "D13"),
    (r"\bincome\b|\bexpense\b", "en", "“what it can do · what it costs”", "D13"),
]

# ---- D2 · dè dặt: câu nói về cơ chế bên trong phải có chữ rào ----------------------------------
MECH = {"vi": r"\b(kho|dự trữ|tiêu sạch|tiêu hao|cạn kiệt|dốc cạn)\b",
        "en": r"\b(store|reserve|paid for|used up)\b"}
HEDGE = {"vi": r"\b(ngờ|có lẽ|có thể|tôi nghĩ|tôi tin|hình như|dường như|chưa chắc|không chứng minh|đoán|danh lục|dòng|người ta|kể|bảo)\b",
         "en": r"\b(suspect\w*|perhaps|maybe|might|may|seem\w*|believe|think|guess|cannot prove|catalogue|say|says|told)\b"}


def sentences(text):
    return [p.strip() for p in re.split(r"(?<=[.!?…])\s+|\n+", text) if p.strip()]


def lint_terms(bid, text, lang):
    out = []
    for pat, lg, fix, code in TERMS:
        if lg == lang:
            for m in re.finditer(pat, text, re.I):
                out.append(f"{code} beat {bid} {lang.upper()}: “{m.group(0)}” → {fix}")
    return out


def lint_hedge(bid, text, lang):
    out = []
    for s in sentences(text):
        if re.search(MECH[lang], s, re.I) and not re.search(HEDGE[lang], s, re.I):
            out.append(f"D2 beat {bid} {lang.upper()}: nói cơ chế bên trong như sự thật — thêm chữ rào "
                       f"(ngờ rằng / có lẽ) hoặc dẫn danh lục: “{s[:70]}…”")
    return out


# ---- D3 · chữ dành riêng cho câu hỏi xương sống ----------------------------------------------
def lint_reserved(c, order):
    """content.py khai RESERVED = {"hạt": "củ · nụ · hoa"}: chữ ấy chỉ được dùng trong câu có nhắc
    danh lục, trong câu hỏi xương sống (có SPINE_KEY), hoặc ở beat cuối. Chỗ khác dùng chữ theo giai đoạn."""
    reserved = getattr(c, "RESERVED", {})
    spine = getattr(c, "SPINE_KEY", "")
    out = []
    if not reserved:
        return out
    last = order[-1] if order else None
    for bid in order:
        if bid == last:
            continue
        for s in sentences(c.BEATS.get(bid, "")):
            for word, instead in reserved.items():
                if re.search(rf"(?<!giống )\b{word}\b", s, re.I) and not re.search(r"danh lục|\bdòng\b", s) \
                        and not (spine and spine in s):
                    out.append(f"D3 beat {bid} VI: “{word}” ngoài câu hỏi xương sống / trích danh lục — "
                               f"theo giai đoạn dùng {instead}: “{s[:60]}…”")
    return out


# ---- D4 · nhịp giữ chân: sự cố đầu tiên, câu hứa, cài – trả -------------------------------------
RATE_VI = 3.3          # tiếng/giây, VBee đọc thong thả (đo trên timings tập 001)
INCIDENT_BY = 240      # giây: sự cố đầu tiên phải tới trước phút thứ tư
PROMISE_BY = 0.30      # câu hứa phải nằm trong 30% đầu tập


def est_starts(c, order, gap=2.2, plan=None):
    t, starts = 0.0, {}
    for bid in order:
        if plan and plan["beats"].get(bid, {}).get("chapter"):
            t += gap
        starts[bid] = t
        t += len(re.findall(r"[\wÀ-ỹ]+", c.BEATS.get(bid, ""))) / RATE_VI
    return starts, t


def lint_story(c, plan, order, gap=2.2):
    out = []
    if not plan:
        return ["D4 chưa có drafts/4-scene-plan.json — không soát được sự cố / câu hứa / cài – trả"]
    beats = plan["beats"]
    starts, total = est_starts(c, order, gap, plan)
    inc = [b for b in order if beats.get(b, {}).get("incident")]
    if not inc:
        out.append("D4 plan chưa đánh dấu beat nào \"incident\": true — sự cố đầu tiên (con vật gặp nguy) nằm đâu?")
    elif starts[inc[0]] > INCIDENT_BY:
        out.append(f"D4 sự cố đầu tiên (beat {inc[0]}) tới ở ~{starts[inc[0]] / 60:.1f} phút — phải trước "
                   f"{INCIDENT_BY // 60} phút: rút các beat trước nó hoặc đưa một mối nguy nhỏ lên sớm")
    pro = [b for b in order if beats.get(b, {}).get("promise")]
    if not pro:
        out.append("D4 plan chưa đánh dấu beat \"promise\": true — cuối hồi 1 phải có một câu hứa điều sắp tới")
    elif starts[pro[0]] > total * PROMISE_BY:
        out.append(f"D4 câu hứa (beat {pro[0]}) nằm ở {starts[pro[0]] / total:.0%} tập — phải trong {PROMISE_BY:.0%} đầu")
    sets, pays = {}, {}
    for b in order:
        for k in beats.get(b, {}).get("sets", []):
            sets.setdefault(k, b)
        for k in beats.get(b, {}).get("pays", []):
            pays[k] = b
    for k, b in sets.items():
        if k not in pays:
            out.append(f"D5 beat {b} cài “{k}” mà không beat nào trả (\"pays\") — trả hoặc bỏ cài")
        elif order.index(pays[k]) <= order.index(b):
            out.append(f"D5 “{k}” được trả (beat {pays[k]}) trước khi cài (beat {b})")
    for k, b in pays.items():
        if k not in sets:
            out.append(f"D5 beat {b} trả “{k}” mà chưa cài ở đâu — người xem không có gì để nhớ lại")
    return out


# ---- D5 · con có mã phải quay lại SAU khi cá thể trung tâm đổi ----------------------------------
def lint_codes(c, order, central="K-01", plan=None):
    out = []
    text = {b: c.BEATS.get(b, "") for b in order}
    codes = sorted({m for t in text.values() for m in re.findall(r"\b[A-Z]-\d{2}\b", t)} - {central})
    change = next((b for b in order if plan and plan["beats"].get(b, {}).get("change")), None)
    for code in codes:
        where = [b for b in order if code in text[b]]
        if len(where) < 2:
            out.append(f"D5 {code} chỉ có mặt ở beat {where[0]} — có mã là phải quay lại, không thì bỏ mã")
        elif change and order.index(where[-1]) <= order.index(change):
            out.append(f"D5 {code} không quay lại sau lần đổi hình (beat {change}) — người xem chờ cuộc tái ngộ")
    return out


# ---- D15 · con số vật lý: suy từ canon, luôn ước lượng, tối đa hai con số cả tập -----------------
UNIT = r"\d[\d.,]*\s*(?:k?W\b|kJ\b|J\b|N\b|joule|newton|watt|kilowatt|oát|jun|niu-tơn|%|°|độ\b|phần trăm|percent)"
APPROX = r"(~|khoảng|chừng|ước|độ chừng|about|roughly|around|some)\s*$"


def lint_numbers(c, order):
    out, hits = [], []
    for bid in order:
        for lang, text in (("vi", c.BEATS.get(bid, "")), ("en", getattr(c, "BEATS_EN", {}).get(bid, ""))):
            for m in re.finditer(UNIT, text, re.I):
                hits.append((bid, lang))
                if re.search(r"%|phần trăm|percent", m.group(0), re.I):
                    out.append(f"D15 beat {bid} {lang.upper()}: “{m.group(0)}” — không dùng phần trăm / chỉ số")
                elif not re.search(APPROX, text[max(0, m.start() - 14):m.start()], re.I):
                    out.append(f"D15 beat {bid} {lang.upper()}: “{m.group(0)}” — số ước lượng phải có “khoảng / ~ / about”")
    for lang in ("vi", "en"):
        n = sum(1 for _, lg in hits if lg == lang)
        if n > 2:
            out.append(f"D15 {lang.upper()}: {n} con số vật lý trong lời dẫn — tối đa 2 cả tập, còn lại để trên trang sổ")
    return out


# ---- D16 · chữ trên hình (trang sổ, nhãn, chú thích) không mang tên game --------------------------
GAME_ONSCREEN = r"vine whip|solar ?beam|razor leaf|sleep powder|leech seed|bulbapedia|pok[eé]dex|pok[eé]mon|\bgen\s*[ivx\d]+\b|\bhp\b|\bstats?\b"
TEXT_KEYS = {"text", "lines", "label", "caption", "title", "sub", "kicker", "body", "note", "to", "vi", "en", "value"}


def lint_onscreen(scenes):
    out = []

    def walk(node, bid):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in TEXT_KEYS and isinstance(v, (str, list)):
                    for s in ([v] if isinstance(v, str) else v):
                        if isinstance(s, str):
                            for m in re.finditer(GAME_ONSCREEN, s, re.I):
                                out.append(f"D16 beat {bid}: chữ trên hình “{m.group(0)}” — tả việc cơ quan làm, nguồn chỉ nằm ở NGUON")
                walk(v, bid)
        elif isinstance(node, list):
            for v in node:
                walk(v, bid)
    for bid, s in (scenes or {}).items():
        if not bid.startswith("_"):
            walk(s, bid)
    return out


# ---- D19 · chữ trên trang sổ: hai ngôn ngữ, giới hạn theo bản dài hơn (SCENE-TYPES, Giới hạn chữ) ----
NOTE_MAX, NOTES_PAGE, NOTES_SPREAD, LABEL_MAX, LABELS_PAGE, VALUE_MAX = 80, 5, 8, 22, 6, 16
DIAGRAMS = {"force", "energy-bar", "energy-flow", "phase", "field-map", "day-timeline", "life-timeline"}


def _langs(t):
    return t if isinstance(t, dict) else {"vi": t}


def lint_notepage(scenes):
    out = []

    def check(np, bid, stack):
        notes, labels = np.get("notes", []), np.get("labels", [])
        pages = {n.get("page") for n in [np] if n.get("page")}
        cap = NOTES_SPREAD if np.get("canvas", "spread") == "spread" else NOTES_PAGE
        if len(notes) > cap:
            out.append(f"D19 beat {bid}: {len(notes)} note trên một trang sổ — tối đa {cap}")
        for n in notes:
            t = _langs(n.get("text", ""))
            if "en" not in t:
                out.append(f"D19 beat {bid}: note “{str(t.get('vi', ''))[:30]}…” chưa có bản EN — một tấm giấy, hai ngôn ngữ")
            longest = max((len(v) for v in t.values()), default=0)
            if longest > NOTE_MAX:
                out.append(f"D19 beat {bid}: note {longest} ký tự (bản dài hơn) — tối đa {NOTE_MAX}")
        if len(labels) > LABELS_PAGE:
            out.append(f"D19 beat {bid}: {len(labels)} nhãn — tối đa {LABELS_PAGE} mỗi trang")
        for lb in labels:
            s = lb.get("text", "") if isinstance(lb.get("text"), str) else " ".join(lb.get("text", {}).values())
            if len(s) > LABEL_MAX or s != s.upper():
                out.append(f"D19 beat {bid}: nhãn “{s}” — IN HOA, ≤ {LABEL_MAX} ký tự")
        for dg in np.get("diagrams", []):
            if dg.get("type") not in DIAGRAMS:
                out.append(f"D19 beat {bid}: diagram “{dg.get('type')}” không có trong ngữ pháp — {', '.join(sorted(DIAGRAMS))}")
            v = str(dg.get("value", ""))
            if v and (len(v) > VALUE_MAX or "~" not in v):
                out.append(f"D19 beat {bid}: số “{v}” — có “~”, ≤ {VALUE_MAX} ký tự (D15)")
        for x in notes + labels + np.get("crossrefs", []):
            to = str(x.get("to", ""))
            if to and not re.match(r"^(page:\d+|species:[a-z0-9-]+|catalogue)$", to):
                out.append(f"D19 beat {bid}: tham chiếu “{to}” — chỉ page:<n> · species:<loài> · catalogue")
        if any(e.get("el") == "chip" for e in stack):
            out.append(f"D19 beat {bid}: `chip` cùng khung với trang sổ — trên sổ dùng `mark` vẽ tay")
        return pages

    def walk(node, bid):
        if isinstance(node, dict):
            stack = node.get("stack")
            if isinstance(stack, list):
                for e in stack:
                    if isinstance(e, dict) and e.get("el") == "notepage":
                        check(e, bid, stack)
            for v in node.values():
                walk(v, bid)
        elif isinstance(node, list):
            for v in node:
                walk(v, bid)
    for bid, s in (scenes or {}).items():
        if not bid.startswith("_"):
            walk(s, bid)
    return out


# ---- D17 · mở tập bốn shot · D18 · loài khách có vai ---------------------------------------------
ROLES = {"predator", "prey", "competitor", "mutualist"}


def lint_opening_guests(plan, order):
    out = []
    if not plan or not order:
        return out
    first = plan["beats"].get(order[0], {}).get("scenes", [])
    if sum(1 for s in first[:2] if s.get("silent")) < 2:
        out.append(f"D17 beat {order[0]}: hai shot đầu phải không lời (\"silent\": giây) — establish rồi reveal, lời vào ở shot 3")
    guests = [g for g in plan.get("guests", []) if g.get("role") in ROLES]
    if len(guests) < 2:
        have = ", ".join(f"{g['species']} ({g['role']})" for g in guests) or "chưa có"
        out.append(f"D18 mới có {len(guests)} loài khách có vai sinh thái ({have}) — cần 2–4: predator · prey · competitor · mutualist")
    return out


def lint_episode(c, plan, order, gap=2.2, scenes=None):
    out = lint_numbers(c, order) + lint_onscreen(scenes) + lint_notepage(scenes) + lint_opening_guests(plan, order)
    for bid in order:
        vi, en = c.BEATS.get(bid, ""), getattr(c, "BEATS_EN", {}).get(bid, "")
        out += lint_terms(bid, vi, "vi") + lint_hedge(bid, vi, "vi")
        if en:
            out += lint_terms(bid, en, "en") + lint_hedge(bid, en, "en")
    out += lint_reserved(c, order)
    out += lint_story(c, plan, order, gap)
    out += lint_codes(c, order, plan=plan)
    return out
