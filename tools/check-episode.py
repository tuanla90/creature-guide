"""Soát một tập trước khi thu giọng / render.

    python tools/check-episode.py kanto-001-bulbasaur

Chỉ kiểm thứ máy kiểm được. Những thứ thuộc về thẩm mỹ và nội dung
(nhịp, giọng, câu chuyện) nằm ở docs/PIPELINE.md và bộ skill.

✗ = phải sửa, ⚠ = nên xem lại, ✓ = qua. Có ✗ thì thoát mã 1.
"""

import importlib.util
import statistics
from collections import Counter
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent

# Chữ làm lộ khung: lời dẫn là nhà sinh vật học ngoài đời, không phải người chơi.
# (mẫu regex, cờ, lý do) — cờ 0 = phân biệt hoa thường, vì "ai" tiếng Việt khác "AI".
FORBIDDEN = [
    (r"lột da", re.I, "cảnh tiến hoá không có lột da (luật của kênh)"),
    (r"lột xác", re.I, "cảnh tiến hoá không có lột xác"),
    (r"thay da", re.I, "cảnh tiến hoá không có thay da"),
    (r"pok[eé]mon", re.I, "không gọi tên thương hiệu trong lời dẫn"),
    (r"pok[eé]dex", re.I, "gọi là 'cuốn danh lục'"),
    (r"\blevel\b", re.I, "thuật ngữ game"),
    (r"cấp độ", re.I, "thuật ngữ game"),
    (r"chỉ số", re.I, "thuật ngữ game"),
    (r"người chơi", re.I, "thuật ngữ game"),
    (r"màn hình", re.I, "lời dẫn không nhắc tới việc đang xem video"),
    (r"nhà sản xuất", re.I, "không nhắc tới đoàn làm phim"),
    (r"\bAI\b", 0, "không nhắc tới công cụ sinh nội dung"),
    (r"\bprompt\b", re.I, "không nhắc tới công cụ sinh nội dung"),
]

# Giới hạn chữ lower-third — dài hơn là tràn ở bản dọc 9:16.
CAP = {"text": 52, "caption": 68, "label": 46, "bg": 34}
SIZE_CAP = {"text": 4.2, "caption": 2.7}

MIN_MIN, MAX_MIN = 8, 25          # thời lượng hợp lý của một tập Long
FPS = 30
LEAD_IN = 0.4                     # pacing.leadIn trong video.config.json

# Cảnh ngắn quá thì khán giả chưa kịp nhìn đã bị cắt. Ngưỡng đo bằng giây.
# Một moment phải nuốt được XFADE 12 khung (0.4s) hoà vào cảnh sau, cộng nhịp vào/ra của Moment.
MOMENT_BAD, MOMENT_THIN = 1.2, 2.5
# Ngưỡng tuyệt đối chưa đủ: một tập có nhịp trung vị 15s thì cảnh 3s vẫn là hẫng, dù 3s nghe không
# ngắn. Nên soát thêm theo nhịp của CHÍNH tập đó — dưới ngần này lần trung vị là lệch nhịp.
MOMENT_REL = 0.25

# Nhịp hình: một tập dùng mãi một loại cảnh thì beat nào cũng giống beat nào, và câu chuyện mất
# nhịp dù lời dẫn vẫn đúng. FULL_BLEED là các element chiếm cả khung — chúng là "động từ" của hình.
BLEED = ("world", "specimen", "clip", "notepage", "anatomy")
SAME_RUN = 4          # bao nhiêu beat liên tiếp cùng một công thức hình thì báo
DOMINANT = 0.75       # một loại cảnh chiếm quá ngần này thì tập bị đơn điệu
# Callout của specimen còn cần camera đẩy tới nơi rồi thẻ mới hiện (T = 40% đoạn, tối đa 26 khung).
CALLOUT_BAD, CALLOUT_THIN = 1.2, 2.0

err, warn, ok = [], [], []
def E(m): err.append(m)
def W(m): warn.append(m)
def K(m): ok.append(m)


def load_content(d: Path):
    spec = importlib.util.spec_from_file_location("content", d / "content.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def anchored_steps(moments, dur_frames, words):
    """Dựng lại useAnchoredSteps() của engine: moment có atSec/atWord thì neo cứng, moment
    không neo thì chia phần còn lại theo trọng số w. Trả về [(start, end)] tính bằng khung."""
    lead = round(LEAD_IN * FPS)
    cursor = 0
    anchor = []
    for m in moments:
        if isinstance(m.get("atSec"), (int, float)):
            anchor.append(round(m["atSec"] * FPS)); continue
        key = str(m.get("atWord") or "").lower()
        hit = None
        if key:
            for i in range(cursor, len(words)):
                if key in str(words[i].get("w", "")).lower():
                    cursor = i + 1
                    hit = lead + round(words[i].get("s", 0) * FPS)
                    break
        anchor.append(hit)
    if anchor and anchor[0] is None:
        anchor[0] = 0
    weights = [m.get("w") or 1 for m in moments]
    starts = [0] * len(moments)
    i = 0
    while i < len(moments):
        seg_start = anchor[i] if anchor[i] is not None else 0
        if i > 0:
            seg_start = max(seg_start, starts[i - 1] + 1)
        j = i + 1
        while j < len(moments) and anchor[j] is None:
            j += 1
        seg_end = anchor[j] if j < len(moments) else dur_frames
        seg_end = min(dur_frames, max(seg_end, seg_start + (j - i)))
        span, tot, acc = seg_end - seg_start, sum(weights[i:j]) or 1, 0
        for k in range(i, j):
            starts[k] = seg_start + round(span * acc / tot)
            acc += weights[k]
        i = j
    return [(starts[k], starts[k + 1] if k + 1 < len(moments) else dur_frames)
            for k in range(len(moments))]


def split_weights(span, items):
    """segments() của engine, bản rút gọn cho callout không neo từ: chia span theo trọng số."""
    tot, acc, out = sum(items) or 1, 0, []
    for w in items:
        a = round(span * acc / tot); acc += w
        out.append(round(span * acc / tot) - a)
    return out


def walk(node, fn):
    if isinstance(node, dict):
        fn(node)
        for v in node.values():
            walk(v, fn)
    elif isinstance(node, list):
        for v in node:
            walk(v, fn)


def main(slug: str) -> int:
    d = ROOT / "videos" / slug
    if not (d / "content.py").exists():
        print(f"không thấy videos/{slug}/content.py")
        return 2

    c = load_content(d)
    scenes = json.loads((d / "scenes.json").read_text(encoding="utf-8"))
    beats = c.BEATS
    order = list(c.ORDER)

    # ---- 1. khung tập -------------------------------------------------------
    want = set(order) | {"short-outro"}
    if want != set(beats):
        E(f"ORDER và BEATS lệch nhau: chỉ ở ORDER {sorted(want - set(beats))} · chỉ ở BEATS {sorted(set(beats) - want)}")
    else:
        K(f"{len(order)} beat + short-outro, ORDER khớp BEATS")

    missing_scene = [b for b in beats if b not in scenes]
    if missing_scene:
        E(f"beat không có hình trong scenes.json: {missing_scene}")
    extra_scene = [b for b in scenes if b not in beats and not b.startswith("_")]
    if extra_scene:
        W(f"scenes.json có beat mà content.py không có: {extra_scene}")
    if "short-outro" not in beats:
        E("thiếu beat 'short-outro' -> engine chỉ dựng được bản Long, không có Short")

    # ---- 2. chữ làm lộ khung ------------------------------------------------
    hits = []
    for b, txt in beats.items():
        for pat, flags, why in FORBIDDEN:
            m = re.search(pat, txt, flags)
            if m:
                hits.append(f"beat {b}: “{m.group(0)}” — {why}")
    if hits:
        for h in hits:
            E(h)
    else:
        K("lời dẫn không có chữ làm lộ khung")

    # ---- 3. nguồn cho câu canon --------------------------------------------
    nguon = getattr(c, "NGUON", {})
    if not nguon:
        E("thiếu NGUON — mọi câu lấy từ danh lục phải ghi nguồn")
    else:
        K(f"NGUON có {len(nguon)} mục")

    # ---- 4. nhân vật khớp bảng tên -----------------------------------------
    cast = ROOT / "docs" / "CAST.md"
    if cast.exists():
        # Luật mới (docs/CAST.md): KHÔNG đặt tên riêng cho con vật. Cá thể trung tâm = đặc điểm canon
        # + mã thực địa ("Shiny Bulbasaur · K-01"), con khác gọi bằng tên loài. Nên thứ bền để đối
        # chiếu với lời dẫn là MÃ THỰC ĐỊA và ĐỊA DANH — không phải cả cụm "một con Fearow".
        body = "\n".join(beats.values())
        locs = []
        for f in (ROOT / "bible" / "locations").glob("*.json"):
            L = json.loads(f.read_text(encoding="utf-8"))
            locs.append({L["name"]["en"], L["name"]["vi"]} |
                        {v for a in L.get("areas", {}).values() for v in a.get("name", {}).values()})
        rows = [L for L in cast.read_text(encoding="utf-8").splitlines() if L.startswith("|")]
        checked = 0
        for L in rows:
            cols = [c.strip() for c in L.strip("|").split("|")]
            if len(cols) < 3 or set(cols[0]) <= set("-: ") or cols[0] == "Vai":
                continue
            role = cols[0].lower()
            if any(k in role for k in ("credit", "người kể", "tác giả")):
                continue                        # không được xuất hiện trong lời đọc — đừng bắt
            m = re.search(r"\*\*(.+?)\*\*", cols[1])
            if not m:
                continue
            n = m.group(1).strip()
            checked += 1

            # Mọi dòng phải có ô dẫn chứng (cột cuối). Ô trống / "—" là chưa tra nguồn.
            if cols[-1].strip() in ("", "—", "-"):
                E(f"“{n}” chưa có dẫn chứng trong CAST.md — ghi nguồn (game + phiên bản · anime + số "
                  f"tập · manga + chương), hoặc ghi rõ 👁 là quan sát của người kể")

            codes = re.findall(r"\bK-\d+\b", n)
            if codes:                           # cá thể có mã: mã phải có mặt trong lời
                keys, label = codes, "mã " + ", ".join(codes)
            elif "địa danh" in role or "nơi" in role:
                keys = next((sorted(s) for s in locs if n in s), [n])
                label = f"địa danh “{n}”"
            else:
                continue                        # con gọi bằng tên loài — không có gì cố định để so
            where = [b for b in order if any(k in beats.get(b, "") for k in keys)]
            if not where:
                W(f"{label} có trong CAST.md nhưng không thấy trong lời dẫn")
            elif codes and len(where) == 1 and len(order) > 6 and where[0] not in order[-2:]:
                # Một cá thể được cho MÃ là vì nó quay lại. Có mã mà chỉ xuất hiện một beat là
                # tuyến bỏ dở — hoặc cho nó quay lại, hoặc bỏ mã, gọi nó bằng tên loài.
                W(f"tuyến bỏ dở: {label} chỉ xuất hiện ở beat {where[0]} — cho quay lại, hoặc bỏ mã")
        K(f"đã đối chiếu {checked} tên trong CAST.md")
    else:
        W("chưa có docs/CAST.md")

    # ---- 5. chữ trên màn hình ----------------------------------------------
    long_txt, big = [], []
    def check_el(o):
        el = o.get("el")
        if el in CAP:
            v = str(o.get("value") or o.get("text") or "")
            plain = re.sub(r"\[(accent|good|warn|bad|muted|purple):|\[br\]|\]", "", v)
            if len(plain) > CAP[el]:
                long_txt.append(f"{el} {len(plain)} ký tự (cap {CAP[el]}): “{plain[:46]}…”")
        if el in SIZE_CAP and isinstance(o.get("size"), (int, float)) and o["size"] > SIZE_CAP[el]:
            big.append(f"{el} size {o['size']} > {SIZE_CAP[el]}")
    walk(scenes, check_el)
    for b, s in scenes.items():
        if isinstance(s, dict) and len(str(s.get("bg", ""))) > CAP["bg"]:
            long_txt.append(f"bg beat {b}: “{s['bg']}”")
    for m in long_txt:
        W("chữ dài, dễ tràn ở bản dọc — " + m)
    for m in big:
        E("chữ quá cỡ lower-third — " + m)
    if not long_txt and not big:
        K("chữ trên màn hình trong giới hạn")

    # ---- 6. file hình / tiếng có thật --------------------------------------
    srcs, sfx = set(), set()
    def collect(o):
        if o.get("el") == "sfx" and o.get("name"):
            sfx.add(str(o["name"]))
        s = o.get("src")
        if isinstance(s, str):
            srcs.add(s)
        for L in o.get("layers", []) or []:
            if isinstance(L, dict) and isinstance(L.get("src"), str):
                srcs.add(L["src"])
    walk(scenes, collect)

    miss = [s for s in sorted(srcs) if not (ROOT / "public" / s).exists()]
    if miss:
        for s in miss:
            E(f"thiếu file: public/{s}")
    else:
        K(f"{len(srcs)} file hình/clip đều có")

    cfg = json.loads((ROOT / "video.config.json").read_text(encoding="utf-8"))
    sfxdir = cfg.get("audio", {}).get("sfxDir", "audio/sfx")
    for n in sorted(sfx):
        f = n if "." in n else n + ".wav"
        if not (ROOT / "public" / sfxdir / f).exists():
            E(f"thiếu tiếng: public/{sfxdir}/{f}")
    if sfx and not any(not (ROOT / "public" / sfxdir / (n if "." in n else n + ".wav")).exists() for n in sfx):
        K(f"{len(sfx)} cue tiếng đều có")
    if not sfx:
        W("chưa có cue tiếng nào trong scenes.json (xem docs/SOUND.md)")

    # ---- 7. ảnh mồ côi ------------------------------------------------------
    ep = slug.rsplit("-", 1)[0] if (ROOT / "bible" / "shots" / f"{slug.rsplit('-', 1)[0]}.json").exists() else None
    for cand in (slug, "-".join(slug.split("-")[:2])):
        p = ROOT / "bible" / "shots" / f"{cand}.json"
        if p.exists():
            shots = json.loads(p.read_text(encoding="utf-8"))
            ids = {s["id"] for s in shots["shots"]}
            outdir = Path(shots["outDir"])
            nofile = [i for i in sorted(ids) if not (ROOT / outdir / f"{i}.jpg").exists()]
            if nofile:
                W(f"shot chưa có ảnh: {nofile}")
            used = {Path(s).stem for s in srcs}
            orphan = sorted(ids - used)
            if orphan:
                W(f"ảnh đã sinh nhưng scenes.json không dùng: {orphan}")
            K(f"bible {cand}: {len(ids)} shot")
            break

    # ---- 8. timing, phụ đề, thumbnail --------------------------------------
    t = d / "timings.json"
    if not t.exists():
        E("chưa có timings.json — chạy: npm run scaffold -- " + slug)
    else:
        if t.stat().st_mtime < (d / "content.py").stat().st_mtime:
            W("timings.json cũ hơn content.py — chạy lại scaffold")
        tim = json.loads(t.read_text(encoding="utf-8"))
        total = tim.get("total") or tim.get("totalFrames")
        if not total:
            per = tim.get("beats") or {}
            total = sum(v.get("frames", 0) for v in per.values()) if isinstance(per, dict) else 0
        mins = total / FPS / 60 if total else 0
        if mins and not (MIN_MIN <= mins <= MAX_MIN):
            W(f"thời lượng {mins:.1f} phút, ngoài khoảng {MIN_MIN}–{MAX_MIN} phút")
        elif mins:
            K(f"thời lượng {mins:.0f} phút {int(mins % 1 * 60):02d} giây")

    srt = ROOT / "out" / slug / "long.srt"
    if not srt.exists():
        W("chưa xuất phụ đề — chạy: python tools/export-subs.py " + slug)
    elif t.exists() and srt.stat().st_mtime < t.stat().st_mtime:
        W("phụ đề cũ hơn timing — xuất lại")
    else:
        K("phụ đề khớp timing hiện tại")

    th = d / "thumb.json"
    if not th.exists():
        E("thiếu thumb.json")
    else:
        tj = json.loads(th.read_text(encoding="utf-8"))
        need = [k for k in ("layout", "category", "catLabel", "kicker") if k not in tj]
        if need:
            E(f"thumb.json thiếu field: {need}")
        else:
            K("thumb.json đủ field bắt buộc")

        # Thumbnail là lời hứa, và là đòn bẩy lượt xem lớn nhất. Hứa một câu hỏi mà tập không trả
        # lời thì người bấm vào sẽ bỏ đi ở giây thứ ba mươi — và số liệu sẽ đổ lỗi cho cái hook.
        hook = f"{tj.get('pre', '')} {tj.get('em', '')}".strip()
        if hook:
            STOP = {"vì", "sao", "cứ", "thì", "là", "của", "một", "cái", "con", "nó", "có", "không",
                    "này", "kia", "và", "mà", "ở", "cho", "khi", "được", "bao", "nhiêu", "làm"}
            toks = [w for w in re.findall(r"[0-9]+|[^\W\d_]{3,}", hook.lower()) if w not in STOP]
            low = body.lower()
            # khớp theo BIÊN TỪ trên văn bản gốc: mã thực địa K7 không được tính là đã trả lời
            # con số 7 của hook. Tách token thường sẽ cắt K7 thành k + 7 và bỏ lọt đúng chỗ này.
            def said(w):
                return re.search(rf"(?<![\w]){re.escape(w)}(?![\w])", low) is not None
            miss = [w for w in toks if not said(w)]
            if toks and len(miss) / len(toks) >= 0.5:
                E(f"thumbnail hứa một câu hỏi lời dẫn không trả lời: “{hook}” — "
                  f"không tìm thấy trong lời: {miss}")
            elif miss:
                W(f"thumbnail có từ không xuất hiện trong lời dẫn: {miss} (hook: “{hook}”)")
            else:
                K("hook của thumbnail có trong lời dẫn")

    # ---- 9. phiên âm cho TTS ------------------------------------------------
    pron = getattr(c, "PRON", {})
    body = "\n".join(beats.values())
    unused = [k for k in pron if k not in body]
    if unused:
        W(f"PRON có mục không còn trong lời dẫn: {unused}")
    for foreign in set(re.findall(r"\b[A-Z][a-z]{3,}(?:saur|chu|mander|tle)\b", body)):
        if foreign not in pron:
            W(f"“{foreign}” chưa có phiên âm trong PRON — VBee sẽ đọc sai")

    # ---- cảnh ngắn quá ------------------------------------------------------
    beats_f = d / "beats.json"
    timings_f = d / "timings.json"
    if not beats_f.exists():
        W("chưa có beats.json — chưa soát được cảnh nào bị ngắt sớm (chạy npm run scaffold)")
    else:
        dur = {b["id"]: b["durationInFrames"] for b in json.loads(beats_f.read_text(encoding="utf-8"))}
        tim = json.loads(timings_f.read_text(encoding="utf-8")) if timings_f.exists() else {}
        short_bad, short_thin, spans = [], [], []
        for bid in order:
            sc = scenes.get(bid)
            if not isinstance(sc, dict) or not sc.get("moments") or bid not in dur:
                continue
            total = dur[bid] + round(float(sc.get("holdSec") or 0) * FPS)
            words = [w for ln in tim.get(bid, []) for w in ln.get("words", [])]
            for i, (a, b) in enumerate(anchored_steps(sc["moments"], total, words)):
                secs = (b - a) / FPS
                where = f"{bid}/moment {i}"
                spans.append((secs, where))
                if secs < MOMENT_BAD:
                    short_bad.append(f"{where} chỉ {secs:.2f}s")
                elif secs < MOMENT_THIN:
                    short_thin.append(f"{where} {secs:.2f}s")
                # callout của specimen chia tiếp đoạn của moment
                for e in sc["moments"][i].get("stack", []):
                    calls = e.get("callouts") if isinstance(e, dict) else None
                    if e.get("el") != "specimen" or not calls:
                        continue
                    ws = ([e.get("introW", 0.8)] + [c.get("w", 1) for c in calls]
                          + ([e.get("outroW", 0.8)] if (e.get("outro", "overview") == "overview") else []))
                    parts = split_weights(b - a, ws)
                    for ci, c in enumerate(calls):
                        cs = parts[ci + 1] / FPS
                        lbl = c.get("label") or f"#{ci}"
                        if cs < CALLOUT_BAD:
                            short_bad.append(f"{bid}/moment {i} callout “{lbl}” chỉ {cs:.2f}s")
                        elif cs < CALLOUT_THIN:
                            short_thin.append(f"{bid}/moment {i} callout “{lbl}” {cs:.2f}s")
        # lệch nhịp: ngắn hơn hẳn so với chính tập này, dù con số tuyệt đối nghe không ngắn
        off = []
        if len(spans) >= 6:
            med = statistics.median(s for s, _ in spans)
            floor = med * MOMENT_REL
            seen = {w for w in short_bad + short_thin}
            off = [f"{w} {s:.2f}s (trung vị tập là {med:.1f}s)"
                   for s, w in sorted(spans) if s < floor and not any(w in m for m in seen)]
        for m in short_bad:
            E(f"cảnh bị ngắt sớm: {m} — tăng w, hoặc bỏ bớt một moment trong beat")
        for m in short_thin:
            W(f"cảnh mỏng: {m} — xem lại có kịp nhìn không")
        for m in off:
            W(f"cảnh lệch nhịp: {m} — không ngắn tuyệt đối, nhưng hẫng so với các cảnh quanh nó")
        if not short_bad and not short_thin and not off:
            K(f"không cảnh nào dưới {MOMENT_THIN}s hay lệch nhịp")

    # ---- nhịp hình ----------------------------------------------------------
    sig, bleed_count = {}, Counter()
    for bid in order:
        s = scenes.get(bid)
        if not isinstance(s, dict):
            continue
        kinds = [e.get("el") for m in s.get("moments", []) for e in m.get("stack", [])
                 if e.get("el") in BLEED]
        if kinds:
            sig[bid] = tuple(kinds)
            bleed_count.update(kinds)

    total_bleed = sum(bleed_count.values())
    if total_bleed:
        top, n = bleed_count.most_common(1)[0]
        if n / total_bleed > DOMINANT:
            W(f"nhịp hình đơn điệu: “{top}” chiếm {n}/{total_bleed} cảnh "
              f"({n / total_bleed:.0%}) — xen clip, specimen hay trang sổ vào cho đổi nhịp")
        for kind in ("clip", "notepage", "anatomy"):
            if bleed_count[kind] == 0:
                W(f"cả tập không có cảnh “{kind}” nào")

        # chuỗi beat liên tiếp cùng một công thức hình
        ids = [b for b in order if b in sig]
        run_start = 0
        for i in range(1, len(ids) + 1):
            same = i < len(ids) and sig[ids[i]] == sig[ids[run_start]]
            if not same:
                length = i - run_start
                if length >= SAME_RUN:
                    formula = ", ".join(sig[ids[run_start]])
                    W(f"beat {ids[run_start]}–{ids[i - 1]} ({length} beat liền) cùng một công thức "
                      f"hình [{formula}] — khán giả thấy y hệt nhau")
                run_start = i
        if len(sig) and not any("nhịp hình" in m or "công thức" in m for m in warn):
            K("nhịp hình có đổi giữa các beat")

    # ---- giọng văn (docs/VOICE.md) ------------------------------------------
    sys.path.insert(0, str(ROOT / "tools"))
    from voice_lint import lint_beat
    vmsgs = []
    for bid in order + (["short-outro"] if "short-outro" in beats else []):
        vmsgs += lint_beat(bid, beats.get(bid, ""), "vi")
        en_beats = getattr(c, "BEATS_EN", {})
        if bid in en_beats:
            vmsgs += lint_beat(bid, en_beats[bid], "en")
    for m in vmsgs:
        W("giọng văn — " + m)
    if not vmsgs:
        K("giọng văn: không câu cụt liền nhau, đại từ có chủ, không từ trơ (docs/VOICE.md)")

    # ---- dừng hình và ảnh quê nhà --------------------------------------------
    # Luật cường độ (docs/SCENE-TYPES.md mục B2): dừng hình là lúc người kể ngừng lại để nghĩ —
    # nhiều quá thì thành giờ giảng. Ảnh loài Trái Đất phải có nguồn sạch ghi trong earth.json.
    freezes, earth = [], []
    for bid in order:
        s = scenes.get(bid)
        if not isinstance(s, dict):
            continue
        for m in s.get("moments", []):
            for e in m.get("stack", []):
                if e.get("el") == "specimen" and e.get("video"):
                    freezes.append(bid)
                for c in e.get("callouts", []) if e.get("el") == "specimen" else []:
                    if c.get("media"):
                        earth.append((bid, c["media"].get("src", "")))
    if len(freezes) > 3:
        E(f"{len(freezes)} cú dừng hình (beat {', '.join(freezes)}) — tối đa 3 mỗi tập")
    if len(earth) > 2:
        E(f"{len(earth)} ảnh quê nhà (beat {', '.join(b for b, _ in earth)}) — tối đa 2 mỗi tập")
    ledger_f = ROOT / "videos" / slug / "earth.json"
    ledger = {x.get("file"): x for x in json.loads(ledger_f.read_text(encoding="utf-8"))} if ledger_f.exists() else {}
    for bid, src in earth:
        row = ledger.get(Path(src).name)
        if not row:
            E(f"beat {bid}: ảnh quê nhà “{src}” chưa ghi nguồn trong videos/{slug}/earth.json")
        elif not row.get("source") or not row.get("license"):
            E(f"beat {bid}: “{src}” thiếu link gốc hoặc giấy phép trong earth.json")
    if freezes or earth:
        K(f"{len(freezes)} cú dừng hình · {len(earth)} ảnh quê nhà — trong hạn mức")

    # ---- góc máy -----------------------------------------------------------
    # Một tập chụp mãi ngang tầm mắt, cỡ trung, thì beat nào cũng giống beat nào — y như bệnh
    # "88% world" nhưng ở tầng ảnh. Soát trên shot bible vì góc máy được quyết từ lúc viết prompt.
    ep = "-".join(slug.split("-")[:2])
    shot_files = sorted((ROOT / "bible" / "shots").glob(f"{ep}*.json"))
    shots = [s for f in shot_files for s in json.loads(f.read_text(encoding="utf-8")).get("shots", [])
             if s.get("kind") not in ("plate", "fieldnote")]
    declared = [s for s in shots if s.get("size") or s.get("angle")]
    if shots and not declared:
        W(f"shot bible chưa khai size/angle cho shot nào ({len(shots)} shot) — không soát được góc máy")
    elif declared:
        sizes = Counter(s.get("size") for s in declared if s.get("size"))
        angles = Counter(s.get("angle") for s in declared if s.get("angle"))
        n = len(declared)
        if len(sizes) < 3:
            W(f"cỡ cảnh nghèo: chỉ {len(sizes)} loại {dict(sizes)} — cần ít nhất toàn · trung · cận")
        if len(angles) < 3:
            W(f"góc máy nghèo: chỉ {len(angles)} loại {dict(angles)} — thêm từ trên xuống, từ sau, góc thấp")
        for label, c in (("cỡ cảnh", sizes), ("góc máy", angles)):
            if c:
                top, k = c.most_common(1)[0]
                if k / n > 0.6:
                    W(f"{label} “{top}” chiếm {k}/{n} shot ({k / n:.0%}) — đơn điệu")
        if not any(s.get("size") in ("wide", "extreme-wide") for s in declared):
            W("không có cảnh toàn nào — khán giả không biết con vật đang ở đâu")
        if len(declared) < len(shots):
            W(f"{len(shots) - len(declared)}/{len(shots)} shot chưa khai size/angle")
        if len(sizes) >= 3 and len(angles) >= 3:
            K(f"góc máy đa dạng: {len(sizes)} cỡ cảnh · {len(angles)} góc")

    # ---- bible: cảnh nghiên cứu · ảnh mẫu · địa điểm · ảnh tham chiếu ------
    all_shots = [s for f in shot_files for s in json.loads(f.read_text(encoding="utf-8")).get("shots", [])]
    kinds = Counter(s.get("kind") for s in all_shots)
    reals = [s["id"] for s in all_shots if s.get("kind") == "real" and not s.get("_legacy")]
    if reals:
        W(f"{len(reals)} ảnh kind “real” — loài Trái Đất không sinh bằng AI nữa, lấy ảnh/video thật từ nguồn "
          f"sạch (SCENE-TYPES mục B2): {', '.join(reals[:6])}")

    # Dr. Holth là người đi tìm sự sống × năng lượng: mỗi tập bắt buộc có một cảnh nhìn XUYÊN QUA
    # (x-quang) và một trang sổ nghiên cứu kiểu Darwin / da Vinci. Xem docs/NARRATOR.md.
    if all_shots:
        for need, why in (("anatomy", "cảnh X-quang"), ("fieldnote", "trang sổ nghiên cứu")):
            if not kinds.get(need):
                E(f"tập chưa có {why} nào (kind {need}) — bắt buộc cho nghiên cứu của Dr. Holth")

    def bible_of(sp):
        f = ROOT / "bible" / "creatures" / f"{sp}.json"
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else None

    def canon_ref(r):
        sp, _, ind = r.partition(":")
        alias = ((bible_of(sp) or {}).get("individuals", {}).get(ind) or {}).get("aliasOf") if ind else None
        return f"{sp}:{alias}" if alias else r

    # Hai mẫu: con thường và con được chọn. Mỗi loại cần ảnh mẫu RIÊNG, nếu không cảnh của đàn sẽ
    # lấy con được chọn làm mẫu (và ngược lại) — dấu nhận dạng lan sang cả đàn.
    plates = set()
    for s in all_shots:
        if s.get("kind") == "plate":
            for r in s.get("creatures", []):
                full = canon_ref(r)
                plates.add(full)
                if full.split(":")[-1] in ("male", "female"):   # biến thể giới tính vẫn là mẫu loài
                    plates.add(full.split(":")[0])
    used = {canon_ref(r) for s in all_shots if s.get("kind") not in ("plate", "location")
            for r in s.get("creatures", []) if bible_of(r.split(":")[0])}
    for r in sorted(used):
        sp, _, ind = r.partition(":")
        if ind in ("male", "female"):
            continue
        if ind and r not in plates:
            W(f"cá thể “{r}” chưa có ảnh mẫu RIÊNG — mọi cảnh của nó sẽ không giữ được đặc điểm nhận dạng")
        if not ind and sp not in plates:
            W(f"loài “{sp}” chưa có ảnh mẫu con THƯỜNG — cảnh của đàn sẽ không có ref")
        if ind:
            trait = ((bible_of(sp) or {}).get("individuals", {}).get(ind) or {}).get("trait")
            if not trait:
                W(f"cá thể “{r}” chưa chốt trait trong bible/creatures/{sp}.json")

    # Cảnh có ĐÀN mà chỉ khai cá thể được chọn -> mọi con trong khung sẽ mang đặc điểm của nó (cả đàn
    # Shiny). Phải khai cả loài thường lẫn cá thể: ["bulbasaur", "bulbasaur:K-01"].
    # từ chỉ đàn; số đếm chỉ tính khi đi kèm từ chỉ con vật ("two strokes" không phải hai con)
    NUM = r"(two|three|four|five|six|seven|eight|nine|ten|a dozen|several)"
    GROUP = re.compile(r"\b(herd|group|others|dozen|ring of|among)\b|\b" + NUM +
                       r"\s+(\w+\s+){0,2}(individuals|animals|of them|bulbasaur|ivysaur|venusaur|creatures)\b", re.I)
    for s in all_shots:
        if s.get("kind") == "plate":
            continue                            # ảnh mẫu luôn chỉ một con
        crs = [canon_ref(r) for r in s.get("creatures", [])]
        for r in crs:
            sp, _, ind = r.partition(":")
            if ind and ind not in ("male", "female") and sp not in crs and GROUP.search(s.get("scene", "")):
                W(f"shot {s['id']}: cảnh có nhiều con nhưng chỉ khai “{r}” — cả đàn sẽ mang đặc điểm của "
                  f"nó. Khai thêm “{sp}” cho các con thường")

    # Địa điểm là tài sản dùng lại được: phải có bible, có canon, có ảnh mẫu địa điểm trống.
    loc_plates = {s.get("location", "").split(":")[0] for s in all_shots if s.get("kind") == "location"}
    for loc in sorted({s["location"].split(":")[0] for s in all_shots if s.get("location")}):
        f = ROOT / "bible" / "locations" / f"{loc}.json"
        if not f.exists():
            E(f"địa điểm “{loc}” dùng trong shot nhưng chưa có bible/locations/{loc}.json")
            continue
        if not json.loads(f.read_text(encoding="utf-8")).get("canon"):
            E(f"địa điểm “{loc}” chưa có dẫn chứng canon")
        if loc not in loc_plates:
            W(f"địa điểm “{loc}” chưa có ảnh mẫu địa điểm (kind location) — các cảnh sẽ không giống nhau")
    if all_shots and not any(s.get("location") for s in all_shots):
        W("chưa shot nào khai location — địa điểm chưa được chốt thành tài sản dùng lại")

    # Ảnh tham chiếu tải về: tiểu tiết AI không biết chắc (kích thước, dấu chân, Shiny).
    for sp in sorted({r.split(":")[0] for s in all_shots for r in s.get("creatures", [])}):
        mf = ROOT / "bible" / "refs" / sp / "refs.json"
        if not mf.exists():
            continue
        for x in json.loads(mf.read_text(encoding="utf-8")).get("refs", []):
            if not (mf.parent / x["file"]).exists():
                W(f"ảnh tham chiếu chưa tải: {sp}/{x['file']} — {x['what']}")

    # ---- tên người dẫn và tác giả ------------------------------------------
    # docs/NARRATOR.md. "Gilbert D. Holth" là đảo chữ tròn 13/13 của "Blight Lord" — cú lật của game
    # Blightfall. Chữ "Gilbert" hiện ở BẤT CỨ đâu trên kênh công khai là lộ bí mật của game.
    spoken = chr(10).join(beats.values())
    shown = [("scenes.json", json.dumps(scenes, ensure_ascii=False))]
    for extra in ("thumb.json", "PUBLISH.md"):
        f = d / extra
        if f.exists():
            shown.append((extra, f.read_text(encoding="utf-8")))
    leak = [where for where, txt in [("lời đọc", spoken)] + shown
            if re.search(r"gilbert", txt, re.I)]
    if leak:
        E(f"chữ “Gilbert” xuất hiện ở: {', '.join(leak)} — đảo chữ của “Blight Lord”, lộ cú lật "
          f"của Blightfall. Chỉ được dùng “Dr. Holth” (xem docs/NARRATOR.md)")
    if re.search(r"\bholth\b", spoken, re.I):
        E("người dẫn nói tên mình trong lời đọc (“Holth”) — tên chỉ được hiện bằng chữ")
    in_video = [("lời đọc", spoken)] + [s for s in shown if s[0] != "PUBLISH.md"]
    author = [where for where, txt in in_video if re.search(r"tu[aấ]n\s*la\b", txt, re.I)]
    if author:
        E(f"tên tác giả “Tuấn La” xuất hiện trong video ({', '.join(author)}) — chỉ được ở mô tả YouTube")
    if not leak and not author:
        K("tên người dẫn và tác giả đúng luật")

    # ---- in kết quả ---------------------------------------------------------
    for m in ok:
        print("  ✓", m)
    for m in warn:
        print("  ⚠", m)
    for m in err:
        print("  ✗", m)
    print(f"\n{len(ok)} qua · {len(warn)} cần xem · {len(err)} phải sửa")
    return 1 if err else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
