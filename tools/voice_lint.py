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
    return out + lint_simile(bid, text, lang)


SIMILE = {"vi": r"\bnhư (một|những|hai|lá|con|tiếng|ngọn|người|thể một)\b|\by như\b",
          "en": r"\blike an?\b|\bas \w+ as\b|\bthe way (people|a|an)\b"}


def lint_simile(bid, text, lang):
    """Luật 8 · không kịch: mỗi đoạn nhiều nhất một hình ảnh so sánh."""
    out = []
    for para in [p for p in text.split("\n") if p.strip()]:
        n = len(re.findall(SIMILE[lang], para, re.I))
        if n > 1:
            out.append(f"beat {bid} {lang.upper()}: {n} so sánh trong một đoạn — kịch, giữ một: “{para[:60]}…”")
    return out


STOP = set("""about after again against because before being below between could every first from have here
their there these those through under until where which while would should other still never always
whole little great until again them they this that with into only just what when your""".split())
TIME_OPEN = re.compile(r"^(in the \w+ (month|week|year|season)|at the end|by now|on the \w+ (day|night)|"
                       r"from (that|then)|that night|the next|every (day|night|afternoon|morning))", re.I)


def lint_bridges(order, beats_en, acts):
    """Luật 2 · chỗ đổi hồi phải có cầu nối: câu mở hồi mới nhắc lại một chữ của beat trước, hoặc mở
    bằng một mốc thời gian. Soát trên bản EN (từ tiếng Anh tách nghĩa rõ hơn âm tiết tiếng Việt)."""
    out = []
    words = lambda s: {w.lower()[:6] for w in re.findall(r"[A-Za-z]{5,}", s) if w.lower() not in STOP}
    for a, b in zip(order, order[1:]):
        if acts.get(a) == acts.get(b) or a not in beats_en or b not in beats_en:
            continue
        first = re.split(r"(?<=[.!?])\s+", beats_en[b].strip())[0]
        if TIME_OPEN.match(first):
            continue
        if not words(first) & words(beats_en[a]):
            out.append(f"beat {a} → {b} (đổi hồi): câu mở “{first[:70]}…” không móc vào beat trước — thêm cầu nối")
    return out
