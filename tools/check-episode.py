"""Soát một tập trước khi thu giọng / render.

    python tools/check-episode.py kanto-001-bulbasaur

Chỉ kiểm thứ máy kiểm được. Những thứ thuộc về thẩm mỹ và nội dung
(nhịp, giọng, câu chuyện) nằm ở docs/PIPELINE.md và bộ skill.

✗ = phải sửa, ⚠ = nên xem lại, ✓ = qua. Có ✗ thì thoát mã 1.
"""

import importlib.util
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

err, warn, ok = [], [], []
def E(m): err.append(m)
def W(m): warn.append(m)
def K(m): ok.append(m)


def load_content(d: Path):
    spec = importlib.util.spec_from_file_location("content", d / "content.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


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
        # chỉ đọc cột VI của bảng (dòng bắt đầu bằng |), bỏ phần văn xuôi
        body = "\n".join(beats.values())
        rows = [L for L in cast.read_text(encoding="utf-8").splitlines() if L.startswith("|")]
        checked = 0
        for L in rows:
            cols = [c.strip() for c in L.strip("|").split("|")]
            if len(cols) < 3:
                continue
            if "credit" in cols[0].lower():   # tên chỉ hiện dưới dạng chữ, không ai đọc lên
                continue
            m = re.match(r"\*\*(.+?)\*\*", cols[1])
            if not m:
                continue
            n = m.group(1).strip()
            checked += 1
            if n not in body:
                W(f"tên “{n}” có trong bảng CAST.md nhưng không thấy trong lời dẫn")
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

    # ---- 9. phiên âm cho TTS ------------------------------------------------
    pron = getattr(c, "PRON", {})
    body = "\n".join(beats.values())
    unused = [k for k in pron if k not in body]
    if unused:
        W(f"PRON có mục không còn trong lời dẫn: {unused}")
    for foreign in set(re.findall(r"\b[A-Z][a-z]{3,}(?:saur|chu|mander|tle)\b", body)):
        if foreign not in pron:
            W(f"“{foreign}” chưa có phiên âm trong PRON — VBee sẽ đọc sai")

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
