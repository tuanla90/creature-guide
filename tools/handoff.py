"""Bàn giao giữa người và máy: bạn làm xong một việc tay, nói "xong", máy tự biết cái gì vừa tới.

    PYTHONUTF8=1 python tools/handoff.py <slug>              # tập đang ở đâu, thiếu gì, bước tiếp
    PYTHONUTF8=1 python tools/handoff.py <slug> --take       # nạp file mới từ inbox/ và Downloads
    PYTHONUTF8=1 python tools/handoff.py <slug> --take --dry-run
    PYTHONUTF8=1 python tools/handoff.py <slug> --brief ideas "#0004 Charmander"   # bước 1: bản dán cho Gemini
    PYTHONUTF8=1 python tools/handoff.py <slug> --brief script [--round 2]          # bước 3: bản dán cho Gemini
    PYTHONUTF8=1 python tools/handoff.py <slug> --draft [file]   # soát bản Gemini viết (mặc định vòng mới nhất)

Luồng kịch bản năm bước, file trong videos/<slug>/drafts/ (docs/HANDOFF.md):
    1-ideas-brief.md → 1-ideas-gemini.md → 2-skeleton.md → 3-script-brief.md → 3-script-gemini.md
    → content.py + 4-review.md → người duyệt

Mọi thứ đều suy từ **tên file**, nên luật đặt tên là cả cái tool này — bảng đầy đủ ở docs/HANDOFF.md:

    ZIP của Batch Studio          tên gì cũng được — ảnh bên trong đã mang id
    một ảnh lẻ                    <shot-id>.jpg|png         -> public/img/<ep>/<shot-id>.jpg
    ảnh tham chiếu                <ref-id>.png|jpg|webp     -> bible/refs/<loài>/<file trong refs.json>
    clip Veo / Seedance           <shot-id>.mp4             -> public/video/<ep>/<shot-id>.mp4
    loài Trái Đất (nguồn sạch)    earth-<loài>-<bộ phận>.mp4|jpg -> public/video|img/<ep>/  + dòng trong earth.json
    giọng VI (VBee)               beat-<id>.mp3 · short-outro.mp3 -> public/audio/<slug>/
    bản Gemini viết               dán thẳng vào videos/<slug>/drafts/1-ideas-gemini.md · 3-script-gemini.md

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
    script_status(slug, vid, nxt)

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


# ---------------------------------------------------------------- bản giao cho Gemini
# Luồng kịch bản: 1 Gemini liệt kê ý → 2 Claude chọn ý, dựng khung → 3 Gemini dựng lại khung và
# viết lời → 4 Claude chuẩn hoá → 5 người duyệt. Bản dán ghép từ docs/briefs/ (lõi dùng chung) và
# 2-skeleton.md (riêng tập) — luật kênh sửa ở một chỗ, mọi bản dán sau đều theo.
BRIEFS = ROOT / "docs" / "briefs"
CUT = "---8<---"


def body_of(p):
    """Bỏ phần ghi chú cho người bảo trì phía trên vạch cắt."""
    t = p.read_text(encoding="utf-8")
    return t.split(CUT, 1)[1].strip() if CUT in t else t.strip()


def meta_of(p):
    """`<!-- handoff: trait=shiny central=bulbasaur:K-01 -->` trong phần ghi chú của 2-skeleton.md."""
    m = re.search(r"<!--\s*handoff:(.*?)-->", p.read_text(encoding="utf-8")) if p.exists() else None
    return dict(x.split("=", 1) for x in m.group(1).split() if "=" in x) if m else {}


def context_for(species):
    """Những gì kênh đã ghi về loài này: các dòng bảng trong IDEA-BANK và SLATE."""
    name = re.sub(r"[#\d]+", " ", species).split()[0]
    rows = []
    for doc in ("IDEA-BANK.md", "SLATE.md"):
        f = ROOT / "docs" / doc
        for line in f.read_text(encoding="utf-8").splitlines() if f.exists() else []:
            if line.startswith("|") and re.search(rf"\b{re.escape(name)}\b", line, re.I):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                rows.append("- " + " · ".join(c for c in cells if c and not re.fullmatch(r"\d+", c)))
    return ("(notes in Vietnamese, from the channel's idea bank and schedule)\n" + "\n".join(rows)) if rows \
        else "- nothing yet: start fresh"


def make_brief(slug, kind, species=None, rnd=1):
    d = ROOT / "videos" / slug / "drafts"
    d.mkdir(parents=True, exist_ok=True)
    core = body_of(BRIEFS / "core.md")
    sfx = "" if rnd == 1 else f"-{rnd}"
    if kind == "ideas":
        if not species:
            raise SystemExit('cần tên loài: --brief ideas "#0004 Charmander"')
        task = body_of(BRIEFS / "ideas.md").replace("{{SPECIES}}", species).replace("{{CONTEXT}}", context_for(species))
        parts, out, save, word = [core, task], d / "1-ideas-brief.md", d / "1-ideas-gemini.md", "xong ý tưởng"
    elif kind == "script":
        sk = d / "2-skeleton.md"
        if not sk.exists():
            raise SystemExit(f"chưa có {rel(sk)} — bước 2 (Claude dựng khung) chưa xong")
        save = d / f"3-script-gemini{sfx}.md"
        task = body_of(BRIEFS / "script.md").replace("{{SAVE}}", rel(save))
        parts, out, word = [core, body_of(sk), task], d / f"3-script-brief{sfx}.md", "xong kịch bản"
    else:
        raise SystemExit("--brief ideas | script")
    text = "\n\n".join(parts).replace("{{SLUG}}", slug)
    head = (f"# Dán cho Gemini · {kind} · {slug}\n\n"
            f"Sinh bằng `PYTHONUTF8=1 python tools/handoff.py {slug} --brief {kind}` — đừng sửa tay: sửa "
            f"`docs/briefs/` hoặc `2-skeleton.md` rồi ghép lại.\n\n"
            f"1. Dán **toàn bộ phần dưới vạch** vào Gemini.\n"
            f"2. Gemini tự lưu, hoặc trả **một khối code**: bấm copy, dán vào `{rel(save)}`.\n"
            f"3. Bị cắt giữa chừng thì gõ \"continue\", dán nối vào cùng file.\n"
            f"4. Nhắn Claude: **`{word}`**.\n\n===== DÁN TỪ ĐÂY =====\n\n")
    out.write_text(head + text + "\n\n===== HẾT PHẦN DÁN =====\n", encoding="utf-8")
    print(f"{rel(out)}  (~{len(text.split())} từ)  → Gemini lưu vào {rel(save)}")


def script_drafts(d):
    """Các vòng Gemini viết, cũ trước mới sau. v*-gemini.md là tên cũ trước khi có luồng năm bước."""
    rounds = sorted(d.glob("3-script-gemini*.md"), key=lambda p: int(re.search(r"-(\d+)\.md$", p.name).group(1))
                    if re.search(r"-(\d+)\.md$", p.name) else 1)
    return rounds or sorted(d.glob("v*-gemini.md"))


def script_status(slug, vid, nxt):
    d = vid / "drafts"
    ideas, sk, rv = d / "1-ideas-gemini.md", d / "2-skeleton.md", d / "4-review.md"
    drafts = script_drafts(d) if d.exists() else []
    n_ideas = len(re.findall(r"^##\s+IDEA\b", ideas.read_text(encoding="utf-8"), re.M)) if ideas.exists() else 0
    approved = rv.exists() and re.search(r"Đã duyệt:", rv.read_text(encoding="utf-8"))
    rows = [
        ("1 ý tưởng · brief cho Gemini", (d / "1-ideas-brief.md").exists()),
        (f"1 ý tưởng · Gemini trả ({n_ideas} ý)" if n_ideas else "1 ý tưởng · Gemini trả", ideas.exists()),
        ("2 khung · Claude chọn ý, dựng khung", sk.exists()),
        ("3 kịch bản · brief cho Gemini", bool(list(d.glob("3-script-brief*.md"))) if d.exists() else False),
        (f"3 kịch bản · Gemini trả ({len(drafts)} vòng)" if drafts else "3 kịch bản · Gemini trả", bool(drafts)),
        ("4 chuẩn hoá · Claude", rv.exists()),
        ("5 duyệt · bạn", bool(approved)),
    ]
    print("1 · KỊCH BẢN")
    for name, done in rows:
        print(f"   {'✓' if done else '·'} {name}")
    if approved:
        return
    if not sk.exists() and not (d / "1-ideas-brief.md").exists():
        nxt.append(f"Claude: ghép brief ý tưởng — tools/handoff.py {slug} --brief ideas \"<loài>\"")
    elif not sk.exists() and not ideas.exists():
        nxt.append(f"dán {rel(d / '1-ideas-brief.md')} vào Gemini, lưu vào {rel(ideas)}, rồi nói “xong ý tưởng”")
    elif not sk.exists():
        nxt.append("Claude: chấm các ý, chọn một (kèm dự phòng), dựng 2-skeleton.md")
    elif not list(d.glob("3-script-brief*.md")):
        nxt.append(f"Claude: ghép brief kịch bản — tools/handoff.py {slug} --brief script")
    elif not drafts:
        nxt.append(f"dán {rel(d / '3-script-brief.md')} vào Gemini, lưu vào {rel(d / '3-script-gemini.md')}, "
                   f"rồi nói “xong kịch bản”")
    elif not rv.exists():
        nxt.append(f"Claude: soát {drafts[-1].name} (--draft), chuẩn hoá vào content.py, ghi 4-review.md")
    else:
        nxt.append(f"đọc {rel(rv)} và bản dựng, rồi nói “duyệt” hoặc ghi chú chỗ cần sửa")


# ---------------------------------------------------------------- soát bản nháp Gemini
EN_BANNED = [
    (r"pok[eé]", "tên thương hiệu"), (r"\btrainers?\b", "thuật ngữ game"), (r"\bgym\b", "thuật ngữ game"),
    (r"\blevels?\b", "thuật ngữ game"), (r"\bHP\b", "thuật ngữ game"), (r"\bstats?\b", "thuật ngữ game"),
    (r"\bevol(ve|ved|ves|ving|ution)", "gọi là 'the change' / 'changing form'"),
    (r"solar ?beam|vine whip|sleep powder|razor leaf|leech seed|\btackle\b|\bember\b|flamethrower|water gun|"
     r"thunderbolt|thunder shock|chlorophyll|overgrow|\bblaze\b|\btorrent\b", "tên đòn / tên nết của game"),
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
}
EN_WPS, VI_SPS = 2.3, 3.0        # nhịp ƯỚC LƯỢNG (VI lấy theo scaffold) — có giọng thật thì đo lại


def vi_forbidden():
    spec = importlib.util.spec_from_file_location("ce", ROOT / "tools" / "check-episode.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.FORBIDDEN


def allowed_from(skeleton, key):
    """Các giá trị `who` / `loc` khung cho phép — đọc từ dòng "- `who`: …" (có thể xuống dòng)."""
    m = re.search(rf"^- `{key}`:(.*?)(?=^- `|^#|\Z)", skeleton, re.M | re.S)
    return set(re.findall(r"`([^`]+)`", m.group(1))) if m else None


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


def check_draft(slug, which=None):
    d = ROOT / "videos" / slug / "drafts"
    f = (d / which) if which else (script_drafts(d)[-1] if script_drafts(d) else None)
    if not f or not f.exists():
        raise SystemExit(f"chưa có bản Gemini viết trong {rel(d)}")
    skp = d / "2-skeleton.md"
    skeleton = skp.read_text(encoding="utf-8") if skp.exists() else ""
    meta = meta_of(skp)
    targets = {m.group(1).lower(): int(m.group(2))
               for m in re.finditer(r"^\|\s*(\d\d|short-outro)\s*\|\s*(\d+)s\s*\|", skeleton, re.M)}
    who_ok = allowed_from(skeleton, "who")
    loc_ok = allowed_from(skeleton, "loc")
    raw = f.read_text(encoding="utf-8")
    dd = parse_draft(raw)
    beats = {k: v for k, v in dd.items() if isinstance(v, dict)}
    err, warn, ok = [], [], []
    VI_BAN = vi_forbidden()

    if re.search(r"CONTINUE FROM BEAT", raw):
        err.append("Gemini bị cắt giữa chừng (còn dòng CONTINUE FROM BEAT) — gõ “continue” rồi dán nối phần sau")
    ch = dd.get("changes") or dd.get("skeleton-changes")
    if isinstance(ch, str) and ch.strip() and ch.strip().lower() != "none":
        rows = [x.strip("- ") for x in ch.strip().splitlines() if x.strip() and not x.startswith(("`", "<!--"))]
        warn.append("Gemini đã đổi bố cục — soát từng dòng:" + "".join("\n      · " + x for x in rows))
    for sec in ("timeline", "changes", "titles", "thumb", "self-check"):
        if sec not in dd and not (sec == "changes" and "skeleton-changes" in dd):
            warn.append(f"thiếu mục {sec.upper()}")
    # bố cục được thả: chỉ báo beat đổi, không bắt lỗi — tổng thời lượng mới là thứ giữ
    same = set(targets) == set(beats)
    if targets and not same:
        gone = [b for b in targets if b not in beats]
        new = [b for b in beats if b not in targets]
        warn.append("bố cục khác khung" + (f" · bỏ/gộp: {', '.join(gone)}" if gone else "")
                    + (f" · mới: {', '.join(new)}" if new else "") + " — đối chiếu với mục CHANGES")

    en_all, vi_all, shots, total, order = "", "", [], 0.0, list(beats)
    for b, fl in beats.items():
        for need in ("VO_EN", "VO_VI") if b == "short-outro" else ("VO_EN", "VO_VI", "SHOTS", "EVIDENCE"):
            if not fl.get(need):
                err.append(f"beat {b}: thiếu {need}")
        # số đo trong ghi chú trang sổ cũng là số bịa — lần đầu chạy thật, Gemini ghi "2.1 m/s"
        for m in re.finditer(r"\d+(?:[.,]\d+)?\s*(?:m/s|km/h|km|kg|cm|mm|%|°|m\b)", fl.get("SHOTS", "")):
            err.append(f"beat {b}: số đo trong SHOTS/notes “{m.group(0)}” — số bịa, trang sổ chỉ ghi quan sát")
        en, vi = fl.get("VO_EN", ""), fl.get("VO_VI", "")
        sys.path.insert(0, str(ROOT / "tools"))
        from voice_lint import lint_beat                      # docs/VOICE.md: câu cụt, đại từ trôi, từ trơ
        warn.extend("giọng văn — " + m for m in lint_beat(b, vi, "vi") + lint_beat(b, en, "en"))
        en_all += f"\n[{b}] " + en
        vi_all += f"\n[{b}] " + vi
        en_s = len(re.findall(r"[A-Za-z0-9'’-]+", en)) / EN_WPS
        vi_s = len(vi.split()) / VI_SPS
        total += en_s
        t = targets.get(b)
        if same and t and not (0.85 * t <= en_s <= 1.15 * t):
            warn.append(f"beat {b}: EN đọc ~{en_s:.0f}s, khung gợi ý {t}s")
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
            if not line or line.startswith(("`", "<!--")):
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
            if "(new)" in line:
                warn.append(f"beat {b}: quan sát mới của Gemini — soát có hợp lý không: {line[:70]}")

    goal = sum(targets.values())
    if goal:
        off = (total - goal) / goal
        (err if abs(off) > 0.10 else warn if abs(off) > 0.05 else ok).append(
            f"tổng EN ~{total / 60:.1f} phút, khung {goal / 60:.1f} phút ({off:+.0%})")

    if re.search(r"gilbert", raw, re.I):
        err.append("“Gilbert” xuất hiện trong bản nháp — tuyệt đối không")
    if re.search(r"\bholth\b", en_all + vi_all, re.I):
        err.append("người dẫn nói tên mình (“Holth”) trong lời")
    for m in set(re.findall(OLD_NAMES, en_all + vi_all, re.I)):
        err.append(f"tên riêng cũ còn sót: “{m}”")
    tl = dd.get("timeline")
    for m in set(re.findall(OLD_NAMES, tl if isinstance(tl, str) else "", re.I)):
        warn.append(f"tên riêng cũ trong TIMELINE: “{m}” — Gemini còn nghĩ bằng tên cũ, soát lời kỹ hơn")
    # "ở quê tôi" là dấu của một lần so sánh Trái Đất: lõi (tối đa ~5) + tối đa 2 tuỳ chọn
    for lang, txt, pat in (("EN", en_all, r"back home"), ("VI", vi_all, r"ở quê tôi")):
        n = len(re.findall(pat, txt, re.I))
        if n > 7:
            warn.append(f"“{pat}” {n} lần trong lời {lang} — so sánh Trái Đất vượt hạn mức (lõi + tối đa 2 tuỳ chọn)")
    per_beat = [b for b in order if len(re.findall(r"back home", beats[b].get("VO_EN", ""), re.I)) > 1]
    if per_beat:
        warn.append(f"hơn một so sánh Trái Đất trong một beat: {', '.join(per_beat)}")

    # đặc điểm của cá thể trung tâm: gọi đúng một lần, và chỉ sau khi đã có cảnh cận thấy nó
    trait, central = meta.get("trait"), meta.get("central")
    seen_at = next((i for i, b in enumerate(order) for s in shots if s["beat"] == b and central
                    and central in s.get("who", "") and s.get("size") in ("close", "medium", "macro")), None)
    if trait:
        for lang, txt in (("EN", en_all), ("VI", vi_all)):
            n = len(re.findall(rf"\b{re.escape(trait)}\b", txt, re.I))
            at = next((b for b in order if re.search(rf"\[{re.escape(b)}\][^\[]*\b{re.escape(trait)}\b", txt, re.I)), None)
            if n != 1:
                err.append(f"“{trait}” xuất hiện {n} lần trong lời {lang} — phải đúng 1")
            elif seen_at is None or order.index(at) < seen_at:
                err.append(f"“{trait}” ({lang}) được gọi ở beat {at} trước khi có cảnh close/medium thấy {central}")

    for sh in shots:
        where = f"beat {sh['beat']}"
        for k, allowed in ALLOWED.items():
            if k in sh and sh[k] not in allowed:
                err.append(f"{where}: {k}={sh[k]} không có trong danh sách cho phép")
        if loc_ok and sh.get("loc") and sh["loc"] not in loc_ok:
            err.append(f"{where}: loc={sh['loc']} không có trong khung")
        for w in sh.get("who", "none").split("+"):
            w = w.strip()
            if who_ok and w not in who_ok:
                err.append(f"{where}: who={w} không có trong khung")
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

    ok.insert(0, f"{len(beats)} beat · {len(shots)} shot · {len(freezes)} dừng hình · {len(earth)} ảnh quê nhà")
    print(f"SOÁT {rel(f)}  (khung: {rel(skp) if skeleton else 'không có'})\n")
    for m in ok:
        print("  ✓", m)
    for m in warn:
        print("  ⚠", m)
    for m in dict.fromkeys(err):
        print("  ✗", m)
    print(f"\n{len(warn)} cần xem · {len(set(err))} phải sửa")
    print("Máy chỉ soát được phần có luật. Nhãn bằng chứng có đúng không, câu có hay không — Claude đọc tiếp.")
    return 1 if err else 0


def arg(args, flag, default=None):
    return args[args.index(flag) + 1] if flag in args and args.index(flag) + 1 < len(args) else default


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        print(__doc__)
        sys.exit(2)
    slug = args[0]
    if "--take" in args:
        take(slug, "--dry-run" in args)
    elif "--brief" in args:
        kind = arg(args, "--brief")
        rest = [a for a in args[args.index("--brief") + 2:] if not a.startswith("--")]
        make_brief(slug, kind, species=rest[0] if rest else None, rnd=int(arg(args, "--round", 1)))
    elif "--draft" in args:
        nxt_arg = arg(args, "--draft")
        sys.exit(check_draft(slug, nxt_arg if nxt_arg and not nxt_arg.startswith("--") else None))
    else:
        status(slug)
