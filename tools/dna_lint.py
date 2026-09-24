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
]

# ---- D2 · dè dặt: câu nói về cơ chế bên trong phải có chữ rào ----------------------------------
MECH = {"vi": r"\b(kho|dự trữ|tiêu sạch|cạn kiệt|dốc cạn)\b",
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


def lint_episode(c, plan, order, gap=2.2):
    out = []
    for bid in order:
        vi, en = c.BEATS.get(bid, ""), getattr(c, "BEATS_EN", {}).get(bid, "")
        out += lint_terms(bid, vi, "vi") + lint_hedge(bid, vi, "vi")
        if en:
            out += lint_terms(bid, en, "en") + lint_hedge(bid, en, "en")
    out += lint_reserved(c, order)
    out += lint_story(c, plan, order, gap)
    out += lint_codes(c, order, plan=plan)
    return out
