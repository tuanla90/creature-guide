"""Soát giọng văn lời dẫn — phần máy bắt được của docs/VOICE.md.

    from voice_lint import lint_beat
    for msg in lint_beat("02", text_vi, "vi"): ...

Trả về danh sách cảnh báo (chuỗi). Không có gì là lỗi chặn: câu ngắn đôi khi là cố ý — nhưng mỗi cảnh
báo phải được đọc.
"""
import re

SHORT = {"vi": 6, "en": 5}          # câu ngắn: ≤ ngần này tiếng (VI) / từ (EN)
PLURAL_VI = r"(đàn|bầy|những|các|hai|ba|bốn|năm|sáu|bảy|tám|chín|mười|mấy|vài)\b"
PLURAL_EN = r"\b(two|three|four|five|six|seven|eight|nine|ten|herd|group|the others|animals|both|these|those|\w+s)\b"
CALQUES = [
    (r"điều tôi gạch chân", "dịch sát — “điều khiến tôi phải ghi đậm vào sổ”"),
    (r"\bđập vào mắt\b", "sáo — tả cái gì làm nó nổi lên"),
]


def sentences(text):
    parts = re.split(r"(?<=[.!?…])\s+|\n+", text)
    return [p.strip() for p in parts if p.strip()]


def size(s, lang):
    words = re.findall(r"[\wÀ-ỹ’'-]+", s)
    return len(words)


def lint_beat(bid, text, lang):
    out = []
    ss = sentences(text)
    short = [i for i, s in enumerate(ss) if size(s, lang) <= SHORT[lang] and not s.endswith("?")]
    if len(short) > 1:
        out.append(f"beat {bid} {lang.upper()}: {len(short)} câu ngắn — tối đa một mỗi beat: "
                   + " · ".join(f"“{ss[i]}”" for i in short[:4]))
    for a, b in zip(short, short[1:]):
        if b == a + 1:
            out.append(f"beat {bid} {lang.upper()}: hai câu ngắn liền nhau “{ss[a]}” “{ss[b]}” — nhịp báo cáo, gộp lại")
            break
    if ss:
        first = ss[0]
        if lang == "vi" and re.match(r"chúng\b(?! (ta|tôi|mình))", first, re.I):
            out.append(f"beat {bid} VI: mở beat bằng “chúng” — chưa có danh từ số nhiều nào đứng trước")
        if lang == "en" and re.match(r"they\b", first, re.I):
            out.append(f"beat {bid} EN: opens with “They” — name the animals first")
    if lang == "vi":
        # "chúng" giữa beat mà trong đoạn trước nó không có danh từ số nhiều
        for para in [p for p in text.split("\n") if p.strip()]:
            m = re.search(r"\bchúng\b(?! (ta|tôi|mình))", para, re.I)      # "chúng ta" không phải đại từ trôi
            if m and not re.search(PLURAL_VI, para[:m.start()], re.I):
                out.append(f"beat {bid} VI: “chúng” chưa có chủ trong đoạn: “{para[:60]}…”")
        for m in re.finditer(r"(?<!những )(?<!các )\bcon (đấy|đó|kia)\b", text, re.I):   # "những con kia" thì tự nhiên
            out.append(f"beat {bid} VI: “{m.group(0)}” — gọi bằng danh từ đầy đủ")
        for m in re.finditer(r"\btrảng\b(?! cỏ)", text, re.I):
            out.append(f"beat {bid} VI: “trảng” đứng một mình — viết đủ “trảng cỏ”")
        for pat, why in CALQUES:
            for m in re.finditer(pat, text, re.I):
                out.append(f"beat {bid} VI: “{m.group(0)}” — {why}")
    return out
