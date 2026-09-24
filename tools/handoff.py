"""Bàn giao giữa người và máy: bạn làm xong một việc tay, nói "xong", máy tự biết cái gì vừa tới.

    PYTHONUTF8=1 python tools/handoff.py <slug>              # tập đang ở đâu, thiếu gì, bước tiếp
    PYTHONUTF8=1 python tools/handoff.py <slug> --take       # nạp file mới từ inbox/ và Downloads
    PYTHONUTF8=1 python tools/handoff.py <slug> --take --dry-run
    PYTHONUTF8=1 python tools/handoff.py <slug> --draft v4   # soát bản nháp Gemini

Mọi thứ đều suy từ **tên file**, nên luật đặt tên là cả cái tool này — bảng đầy đủ ở docs/HANDOFF.md:

    ZIP của Batch Studio          tên gì cũng được — ảnh bên trong đã mang id
    một ảnh lẻ                    <shot-id>.jpg|png         -> public/img/<ep>/<shot-id>.jpg
    ảnh tham chiếu                <ref-id>.png|jpg|webp     -> bible/refs/<loài>/<file trong refs.json>
    clip Veo / Seedance           <shot-id>.mp4             -> public/video/<ep>/<shot-id>.mp4
    loài Trái Đất (nguồn sạch)    earth-<loài>-<bộ phận>.mp4|jpg -> public/video|img/<ep>/  + dòng trong earth.json
    giọng VI (VBee)               beat-<id>.mp3 · short-outro.mp3 -> public/audio/<slug>/
    bản nháp Gemini               dán thẳng vào videos/<slug>/drafts/<vN>-gemini.md

**Chuyển chứ không chép** (cùng luật với tools/intake.py): nạp xong thì file rời inbox/Downloads.
ZIP đã giải nén được cất vào inbox/done/ — xoá hay giữ là việc của bạn, tool không xoá gì.
Âm thanh nhạc và tiếng động không đi qua đây — đó là việc của tools/intake.py (/nap-am).
"""

import importlib.util
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"
DOWNLOADS = Path.home() / "Downloads"

# Nhận file bằng ruột chứ không bằng đuôi: trình duyệt trong app lưu thành .tmp tên ngẫu nhiên.
MAGIC = [(b"\xff\xd8\xff", "jpg"), (b"\x89PNG", "png"), (b"PK\x03\x04", "zip"),
         (b"ID3", "mp3"), (b"\xff\xfb", "mp3"), (b"\xff\xf3", "mp3")]


def sniff(p):
    try:
        head = p.open("rb").read(12)
    except OSError:
        return None
    for m, kind in MAGIC:
        if head.startswith(m):
            return kind
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        return "webp"
    if head[4:8] == b"ftyp":
        return "mp4"
    return None


def ep_of(slug):
    return "-".join(slug.split("-")[:2])


def rel(p):
    try:
        return p.relative_to(ROOT).as_posix()
    except ValueError:
        return str(p)


# ---------------------------------------------------------------- các bảng hẹn trước
def wanted_images(ep):
    """id ảnh -> đường đích, gom từ mọi prompts/<ep>*.jsonl (tập chính, v3, motion...)."""
    want = {}
    for f in sorted((ROOT / "prompts").glob(f"{ep}*.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.strip():
                d = json.loads(line)
                want[d["id"]] = ROOT / d["file"]
    return want


def shot_kinds(ep):
    kinds = {}
    for f in sorted((ROOT / "bible" / "shots").glob(f"{ep}*.json")):
        for s in json.loads(f.read_text(encoding="utf-8")).get("shots", []):
            kinds[s["id"]] = s.get("kind", "scene")
    return kinds


def wanted_refs(ep):
    """id tham chiếu -> đường đích, chỉ cho những loài có mặt trong shot của tập."""
    species = set()
    for f in sorted((ROOT / "bible" / "shots").glob(f"{ep}*.json")):
        for s in json.loads(f.read_text(encoding="utf-8")).get("shots", []):
            species |= {r.split(":")[0] for r in s.get("creatures", [])}
    out = {}
    for sp in sorted(species):
        f = ROOT / "bible" / "refs" / sp / "refs.json"
        if f.exists():
            for r in json.loads(f.read_text(encoding="utf-8"))["refs"]:
                out[r["id"]] = (f.parent / r["file"], r)
    return out


def load_content(slug):
    f = ROOT / "videos" / slug / "content.py"
    if not f.exists():
        return None
    spec = importlib.util.spec_from_file_location("content", f)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ---------------------------------------------------------------- trạng thái
def status(slug):
    ep = ep_of(slug)
    vid = ROOT / "videos" / slug
    print(f"TẬP {slug}  (ảnh: {ep})\n")
    nxt = []

    # 1 · kịch bản
    drafts = sorted((vid / "drafts").glob("v*-*.md")) if (vid / "drafts").exists() else []
    briefs = {re.match(r"(v\d+)", p.name).group(1) for p in drafts if p.name.endswith("-brief.md")}
    backs = {re.match(r"(v\d+)", p.name).group(1) for p in drafts if p.name.endswith("-gemini.md")}
    print("1 · KỊCH BẢN")
    for v in sorted(briefs | backs, key=lambda x: int(x[1:])):
        b = "✓ brief" if v in briefs else "· không brief"
        g = "✓ Gemini đã trả" if v in backs else "… chờ Gemini"
        print(f"   {v}: {b} · {g}")
        if v in briefs and v not in backs:
            nxt.append(f"dán {rel(vid / 'drafts' / (v + '-brief.md'))} vào Gemini, lưu câu trả lời vào "
                       f"{rel(vid / 'drafts' / (v + '-gemini.md'))}, rồi nói “xong gemini”")
    if not drafts:
        print("   chưa có bản nháp nào trong drafts/")

    # 2 · ảnh tham chiếu
    refs = wanted_refs(ep)
    miss_refs = [(i, p, r) for i, (p, r) in refs.items() if not p.exists()]
    print(f"\n2 · ẢNH THAM CHIẾU  {len(refs) - len(miss_refs)}/{len(refs)}")
    for i, p, r in miss_refs:
        print(f"   · {i:26} -> {rel(p)}   ({r.get('source', '?')})")
    if miss_refs:
        nxt.append(f"tải {len(miss_refs)} ảnh tham chiếu, đặt tên <ref-id>.png vào inbox/, rồi nói “xong refs”")

    # 3 · ảnh (mẫu trước, cảnh sau)
    want, kinds = wanted_images(ep), shot_kinds(ep)
    base = {"plate", "location"}
    groups = {"ảnh mẫu / địa điểm": [i for i in want if kinds.get(i) in base],
              "cảnh": [i for i in want if kinds.get(i) not in base]}
    print("\n3 · ẢNH")
    for name, ids in groups.items():
        have = [i for i in ids if want[i].exists()]
        print(f"   {name}: {len(have)}/{len(ids)}")
        miss = [i for i in ids if not want[i].exists()]
        if miss:
            print("      thiếu: " + ", ".join(miss[:12]) + (f" … (+{len(miss) - 12})" if len(miss) > 12 else ""))
    fix = []
    for f in sorted((ROOT / "bible" / "shots").glob(f"{ep}*.json")):
        fix += [s["id"] for s in json.loads(f.read_text(encoding="utf-8")).get("shots", [])
                if "PHẢI SINH LẠI" in s.get("_fix", "")]
    if fix:
        print("   đánh dấu PHẢI SINH LẠI: " + ", ".join(fix))
    miss_base = [i for i in groups["ảnh mẫu / địa điểm"] if not want[i].exists()]
    if miss_base and not miss_refs:
        nxt.append("sinh ảnh mẫu trước (" + ", ".join(miss_base) + "), rồi nói “xong ảnh mẫu”")

    # 4 · clip
    scenes = vid / "scenes.json"
    clips = []
    if scenes.exists():
        clips = sorted(set(re.findall(r'"src"\s*:\s*"(video/[^"]+)"', scenes.read_text(encoding="utf-8"))))
    miss_clips = [c for c in clips if not (ROOT / "public" / c).exists()]
    print(f"\n4 · CLIP  {len(clips) - len(miss_clips)}/{len(clips)} (theo scenes.json)")
    for c in miss_clips:
        print(f"   · thiếu public/{c}")

    # 4b · loài Trái Đất: file có mặt và đã ghi nguồn chưa
    led_f = vid / "earth.json"
    ledger = {x.get("file") for x in json.loads(led_f.read_text(encoding="utf-8"))} if led_f.exists() else set()
    earth = sorted(q.name for d in ("img", "video") for q in (ROOT / "public" / d / ep).glob("earth-*"))
    if earth or ledger:
        print(f"\n4b · LOÀI TRÁI ĐẤT  {len(earth)} file · {len(ledger)} dòng nguồn")
        for n in earth:
            if n not in ledger:
                print(f"   ✗ {n}: chưa ghi nguồn/giấy phép trong videos/{slug}/earth.json")
                nxt.append(f"ghi nguồn cho {n} vào earth.json (link gốc + giấy phép)")

    # 5 · giọng
    c = load_content(slug)
    order = list(getattr(c, "ORDER", [])) if c else []
    adir = ROOT / "public" / "audio" / slug
    names = [("short-outro" if b == "short-outro" else f"beat-{b}") + ".mp3" for b in order]
    have = [n for n in names if (adir / n).exists()]
    print(f"\n5 · GIỌNG VI  {len(have)}/{len(names)}  (public/audio/{slug}/beat-<id>.mp3)")
    print("   EN: nhà cung cấp chưa chốt — chưa có chỗ đặt")

    # 6 · duyệt
    notes = vid / "review-notes.json"
    if notes.exists():
        n = json.loads(notes.read_text(encoding="utf-8"))
        print(f"\n6 · GHI CHÚ DUYỆT  {len(n.get('notes', []))} ghi chú · {len(n.get('coords', []))} toạ độ")

    # bước tiếp
    stray = [x for x in pending_files(slug) if x[1]]
    if stray:
        nxt.insert(0, f"có {len(stray)} file khớp tập này đang chờ nạp — chạy lại với --take")
    print("\nBƯỚC TIẾP")
    for s in nxt[:3] or ["không có gì chờ bạn — việc đang ở phía máy"]:
        print("   →", s)


# ---------------------------------------------------------------- nạp file
def targets(slug):
    ep = ep_of(slug)
    order = list(getattr(load_content(slug), "ORDER", []) or [])
    voice = {("short-outro" if b == "short-outro" else f"beat-{b}") for b in order}
    return ep, wanted_images(ep), wanted_refs(ep), voice


def classify(p, ep, want, refs, voice):
    """File này là gì của tập này — hoặc None nếu không phải."""
    kind, stem = sniff(p), p.stem
    if kind == "zip":
        return ("zip", None) if zip_ids(p, want) else None
    if kind in ("jpg", "png", "webp") and stem in want:
        return ("img", want[stem])
    if kind in ("jpg", "png", "webp") and stem in refs:
        return ("ref", refs[stem][0])
    if kind == "mp4" and (stem in want or stem.rsplit("-", 1)[0] in want):
        return ("clip", ROOT / "public" / "video" / ep / f"{stem}.mp4")
    if stem.startswith("earth-") and kind in ("jpg", "png", "webp"):   # loài Trái Đất: SCENE-TYPES mục B2
        return ("earth", ROOT / "public" / "img" / ep / f"{stem}.{kind}")
    if stem.startswith("earth-") and kind == "mp4":
        return ("earth", ROOT / "public" / "video" / ep / f"{stem}.mp4")
    if kind == "mp3" and stem in voice:
        return ("voice", ROOT / "public" / "audio" / "{slug}" / f"{stem}.mp3")
    return None


def pending_files(slug):
    """(file, loại, đích) cho mọi file khớp tập này; inbox/ thì trả cả file lạ (loại None)."""
    ep, want, refs, voice = targets(slug)
    out = []
    for d in (INBOX, DOWNLOADS):
        if not d.exists():
            continue
        for p in d.iterdir():
            if not p.is_file():
                continue
            c = classify(p, ep, want, refs, voice)
            if c or d == INBOX:
                out.append((p, *(c or (None, None))))
    return out


def zip_ids(p, want):
    try:
        with zipfile.ZipFile(p) as z:
            return [n for n in z.namelist() if re.sub(r"_\d+$", "", Path(n).stem) in want]
    except zipfile.BadZipFile:
        return []


def keep_old(dst):
    """Không ghi đè: bản cũ đổi tên thành <tên>.prevN, người dùng tự quyết xoá hay giữ."""
    n = 1
    while (old := dst.with_name(f"{dst.stem}.prev{n}{dst.suffix}")).exists():
        n += 1
    dst.replace(old)
    print(f"      (bản cũ giữ ở {old.name} — toạ độ callout đo trên bản cũ phải đo lại)")


def move(src, dst, dry, note=""):
    print(f"   {src.name}  ->  {rel(dst)}{note}")
    if dry:
        return
    if dst.exists():
        keep_old(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))


def take(slug, dry):
    ep, want, refs, _ = targets(slug)
    done, zips, unknown = 0, 0, []
    print(("XEM TRƯỚC — chưa đụng file nào" + chr(10) if dry else "") + f"Nạp cho {slug}:")
    for p, kind, dst in pending_files(slug):
        if kind is None:
            unknown.append(p)
        elif kind == "zip":
            names = zip_ids(p, want)
            print(f"   {p.name}: {len(names)} ảnh")
            if not dry:
                with zipfile.ZipFile(p) as z:
                    for n in names:
                        out, data = want[re.sub(r"_\d+$", "", Path(n).stem)], z.read(n)
                        if out.exists() and out.read_bytes() == data:
                            continue                      # ZIP cũ nạp lại: ảnh y hệt, bỏ qua
                        if out.exists():
                            keep_old(out)
                        out.parent.mkdir(parents=True, exist_ok=True)
                        out.write_bytes(data)
                        print(f"      {n} -> {rel(out)}")
                (INBOX / "done").mkdir(parents=True, exist_ok=True)
                shutil.move(str(p), str(INBOX / "done" / p.name))
            done, zips = done + 1, zips + 1
        else:
            if kind == "voice":
                dst = Path(str(dst).replace("{slug}", slug))
            note = f"   [{refs[p.stem][1]['what']}]" if kind == "ref" else ""
            move(p, dst, dry, note)
            if kind == "earth":
                note = "   [nhớ ghi link gốc + giấy phép vào earth.json]"
            if kind == "ref" and not dry:
                mark_ref(dst.parent / "refs.json", p.stem)
            zips += kind == "img"
            done += 1
    for p in unknown:
        print(f"   ? {p.name}: tên không khớp shot, ref hay beat nào — đổi tên theo docs/HANDOFF.md rồi chạy lại")
    print(f"\n{done} món {'sẽ nạp' if dry else 'đã nạp'}" + (f" · {len(unknown)} không rõ" if unknown else ""))
    if zips and not dry:
        print(f"   ảnh Flow còn watermark: PYTHONUTF8=1 python tools/unwatermark.py {ep}")


def mark_ref(f, rid):
    d = json.loads(f.read_text(encoding="utf-8"))
    for r in d["refs"]:
        if r["id"] == rid:
            r["status"] = "đã tải"
    f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- soát bản nháp Gemini
EN_BANNED = [
    (r"pok[eé]", "tên thương hiệu"), (r"\btrainers?\b", "thuật ngữ game"), (r"\bgym\b", "thuật ngữ game"),
    (r"\blevels?\b", "thuật ngữ game"), (r"\bHP\b", "thuật ngữ game"), (r"\bstats?\b", "thuật ngữ game"),
    (r"\bevol(ve|ved|ves|ving|ution)", "gọi là 'the change' / 'changing form'"),
    (r"solar ?beam|vine whip|sleep powder|razor leaf|leech seed|\btackle\b|chlorophyll|overgrow",
     "tên đòn / tên nết của game"),
    (r"\bcamera|\bcrew\b|\bfootage\b|\bvideo\b|\bviewers?\b|\bscreen\b|\bsubscrib", "lộ đoàn phim / màn hình"),
    (r"\bAI\b|\bprompt", "lộ công cụ"),
    (r"\bmolt|\bmoult|\bshed(s|ding)? (its |the )?skin|\bslough", "cảnh đổi hình không có lột da"),
]
OLD_NAMES = r"crookedbud|scar-?shoulder|ash-?eye|moss-?back|\bsaur\b|búp lệch|vai rách|mắt tro|lưng rêu"
NUM_WORDS = (r"\b(\d+[\d.,]*|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
             r"twenty[- ]?\w*|thirty|forty|fifty|hundred|thousand|dozen|percent|degrees?)\b")
ALLOWED = {
    "el": {"world", "clip", "specimen", "notepage", "freeze"},
    "size": {"extreme-wide", "wide", "medium", "close", "macro"},
    "angle": {"eye", "low", "high", "overhead", "rear", "profile", "pov"},
    "loc": {"viridian-forest:trail", "viridian-forest:clearing", "viridian-forest:garden", "town:yard", "none"},
}
WHO = re.compile(r"^(none|bulbasaur(:K-0[14])?|ivysaur(:K-01)?|venusaur:female|fearow|anatomy:.+)$")
EN_WPS, VI_SPS = 2.3, 3.0        # nhịp ƯỚC LƯỢNG (VI lấy theo scaffold) — có giọng thật thì đo lại


def vi_forbidden():
    spec = importlib.util.spec_from_file_location("ce", ROOT / "tools" / "check-episode.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.FORBIDDEN


def parse_draft(text):
    blocks = re.split(r"^##\s+", text, flags=re.M)
    out = {}
    for b in blocks[1:]:
        head, _, body = b.partition("\n")
        key = head.strip().upper()
        m = re.match(r"BEAT\s+(\S+)", key)
        key = m.group(1).lower() if m else key.lower()
        fields, cur = {}, None
        for line in body.splitlines():
            fm = re.match(r"^(TARGET|VO_EN|VO_VI|SCREEN|SHOTS|EVIDENCE):\s*(.*)$", line)
            if fm:
                cur = fm.group(1)
                fields[cur] = fm.group(2).strip()
            elif cur:
                fields[cur] = (fields[cur] + "\n" + line).strip()
        out[key] = fields if fields else body.strip()
    return out


def check_draft(slug, ver):
    vid = ROOT / "videos" / slug / "drafts"
    f = vid / f"{ver}-gemini.md"
    if not f.exists():
        raise SystemExit(f"chưa có {rel(f)}")
    brief = (vid / f"{ver}-brief.md").read_text(encoding="utf-8") if (vid / f"{ver}-brief.md").exists() else ""
    targets = {m.group(1).lower(): int(m.group(2))
               for m in re.finditer(r"^\|\s*(\d\d|short-outro)\s*\|\s*(\d+)s\s*\|", brief, re.M)}
    d = parse_draft(f.read_text(encoding="utf-8"))
    beats = {k: v for k, v in d.items() if isinstance(v, dict)}
    err, warn, ok = [], [], []
    VI_BAN = vi_forbidden()

    miss = [b for b in targets if b not in beats]
    if miss:
        err.append("thiếu beat: " + ", ".join(miss))
    for sec in ("timeline", "titles", "thumb", "self-check"):
        if sec not in d:
            warn.append(f"thiếu mục {sec.upper()}")

    en_all, vi_all, shots, total = "", "", [], 0.0
    for b, fl in beats.items():
        for need in ("VO_EN", "VO_VI", "SHOTS", "EVIDENCE"):
            if not fl.get(need):
                err.append(f"beat {b}: thiếu {need}")
        en, vi = fl.get("VO_EN", ""), fl.get("VO_VI", "")
        en_all += f"\n[{b}] " + en
        vi_all += f"\n[{b}] " + vi
        en_s = len(re.findall(r"[A-Za-z0-9'’-]+", en)) / EN_WPS
        vi_s = len(vi.split()) / VI_SPS
        total += en_s
        t = targets.get(b)
        if t and not (0.85 * t <= en_s <= 1.15 * t):
            warn.append(f"beat {b}: EN đọc ~{en_s:.0f}s, đích {t}s")
        if en_s and abs(vi_s - en_s) / en_s > 0.15:
            warn.append(f"beat {b}: VI ~{vi_s:.0f}s lệch EN ~{en_s:.0f}s quá 15% — hai track giọng lệch nhau")
        for pat, why in EN_BANNED:
            for m in re.finditer(pat, en, re.I if pat != r"\bAI\b|\bprompt" else 0):
                err.append(f"beat {b} EN: “{m.group(0)}” — {why}")
        for pat, flags, why in VI_BAN:
            for m in re.finditer(pat, vi, flags):
                err.append(f"beat {b} VI: “{m.group(0)}” — {why}")
        nums = sorted({m.group(0).lower() for m in re.finditer(NUM_WORDS, re.sub(r"K-\d+", "", en), re.I)})
        if nums:
            warn.append(f"beat {b}: số trong lời — soát với TIMELINE: {', '.join(nums)}")
        for line in fl.get("SCREEN", "").splitlines():
            m = re.match(r"-\s*(caption|text|chip):\s*(.*)", line.strip())
            if m and m.group(1) in ("caption", "text"):
                cap = {"caption": 68, "text": 52}[m.group(1)]
                s = m.group(2).split("||")[0].strip()
                if len(s) > cap:
                    err.append(f"beat {b}: {m.group(1)} {len(s)} ký tự > {cap}: “{s}”")
        for line in fl.get("SHOTS", "").splitlines():
            line = line.strip().lstrip("-").strip()
            if not line:
                continue
            parts = [x.strip() for x in line.split("|")]
            sh = {"beat": b, "el": parts[0]}
            for x in parts[1:]:
                if "=" in x:
                    k, v = x.split("=", 1)
                    sh[k.strip()] = v.strip().strip('"')
            shots.append(sh)
        for line in fl.get("EVIDENCE", "").splitlines():
            line = line.strip().lstrip("-").strip()
            if line.startswith("📖") and "—" not in line:
                warn.append(f"beat {b}: dòng 📖 không có nguồn: {line[:60]}")
            if line.startswith("🔬") and ":" not in line:
                warn.append(f"beat {b}: dòng 🔬 không nêu loài Trái Đất: {line[:60]}")

    blob = f.read_text(encoding="utf-8")
    if re.search(r"gilbert", blob, re.I):
        err.append("“Gilbert” xuất hiện trong bản nháp — tuyệt đối không")
    if re.search(r"\bholth\b", en_all + vi_all, re.I):
        err.append("người dẫn nói tên mình (“Holth”) trong lời")
    for m in set(re.findall(OLD_NAMES, en_all + vi_all, re.I)):
        err.append(f"tên riêng cũ còn sót: “{m}”")
    for lang, txt in (("EN", en_all), ("VI", vi_all)):
        hits = re.findall(r"\[(\S+)\][^\[]*?\bshiny\b", txt, re.I | re.S)
        n = len(re.findall(r"\bshiny\b", txt, re.I))
        if n != 1:
            err.append(f"“shiny” xuất hiện {n} lần trong lời {lang} — phải đúng 1, ở beat 02")
        elif hits and hits[0] != "02":
            err.append(f"“shiny” ({lang}) nằm ở beat {hits[0]}, phải ở beat 02")

    for sh in shots:
        where = f"beat {sh['beat']}"
        for k, allowed in ALLOWED.items():
            if k in sh and sh[k] not in allowed:
                err.append(f"{where}: {k}={sh[k]} không có trong danh sách cho phép")
        for w in sh.get("who", "none").split("+"):
            if not WHO.match(w.strip()):
                err.append(f"{where}: who={w} không hợp lệ")
    freezes = [s for s in shots if s["el"] == "freeze"]
    earth = [s for s in shots if s.get("earth")]
    if len(freezes) > 3:
        err.append(f"{len(freezes)} cú dừng hình — tối đa 3 (beat {', '.join(s['beat'] for s in freezes)})")
    if len(earth) > 2:
        err.append(f"{len(earth)} ảnh quê nhà — tối đa 2 (beat {', '.join(s['beat'] for s in earth)})")
    for s in earth:
        if s["el"] != "freeze":
            err.append(f"beat {s['beat']}: earth= chỉ đi kèm el=freeze (ảnh quê nhà nằm trong thẻ của cú dừng)")
    sizes = {s.get("size") for s in shots} - {None}
    angles = {s.get("angle") for s in shots} - {None}
    if len(sizes) < 3 or len(angles) < 3 or "wide" not in sizes:
        warn.append(f"góc máy nghèo: {len(sizes)} cỡ, {len(angles)} góc" + ("" if "wide" in sizes else ", không có wide"))
    if not any("anatomy:" in s.get("who", "") for s in shots):
        err.append("không có cảnh X-quang (who=anatomy:<loài>)")
    if not any(s["el"] == "notepage" for s in shots):
        err.append("không có trang sổ (el=notepage)")
    early = [s for s in shots if s["beat"] in ("00", "01", "02") and "K-01" in s.get("who", "")
             and s.get("size") in ("close", "medium")]
    if not early:
        err.append("chưa có cảnh close/medium thấy rõ màu K-01 trước khi beat 02 nói “shiny”")

    ok.append(f"{len(beats)} beat · {len(shots)} shot · EN ước ~{total / 60:.1f} phút")
    print(f"SOÁT {rel(f)}\n")
    for m in ok:
        print("  ✓", m)
    for m in warn:
        print("  ⚠", m)
    for m in dict.fromkeys(err):
        print("  ✗", m)
    print(f"\n{len(warn)} cần xem · {len(set(err))} phải sửa")
    print("Máy chỉ soát được phần có luật. Nhãn bằng chứng có đúng không, câu có hay không — Claude đọc tiếp.")
    return 1 if err else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        print(__doc__)
        sys.exit(2)
    slug = args[0]
    if "--take" in args:
        take(slug, "--dry-run" in args)
    elif "--draft" in args:
        sys.exit(check_draft(slug, args[args.index("--draft") + 1]))
    else:
        status(slug)
