"""Xưởng duyệt một tập: cảnh dự kiến (ảnh hoặc mô tả) + prompt + lời EN cạnh VI + ô duyệt từng beat.

    PYTHONUTF8=1 python tools/review-page.py <slug> [--img-root <thư mục ảnh>] [--assets <map.json>] [--out <file>]

Đọc videos/<slug>/content.py (BEATS = VI, BEATS_EN = EN), drafts/4-scene-plan.json (cảnh dự kiến),
drafts/2-skeleton.md (thời lượng đích), prompts/<ep>*.flow.txt (prompt thật từ build-prompts.mjs, file
sau đè file trước), ghép vào tools/templates/review-page.html, ghi ra out/<slug>/review.html.

--img-root  nơi có ảnh thật (mặc định public/img/<ep> của repo này). Chạy từ worktree thì trỏ về thư
            mục chính, vì ảnh không nằm trong git.
--assets    JSON {id: url} — link các ảnh thu nhỏ đã tải lên asset store của Artifact (mặc định lấy từ
            videos/<slug>/drafts/review-page.json). Ảnh có trên máy mà chưa có link thì trang vẫn biết
            là "đã có", chỉ không hiện được hình.

Claude đăng file ra thành Artifact với capabilities {db: {}, assets: {}}. Trang ghi vào db:
  review/b<beat>   {status: ok|fix|"", note}      — Duyệt / Cần sửa từng beat
  edits/<key>      {text}                          — sc-<beat>-<i> (mô tả cảnh) · en-<beat>-<i> · vi-<beat>-<i>
  picks/state      {ids: [...]}                    — ảnh đang chọn cho batch
Khi người dùng nói "xong duyệt", Claude đọc ba collection ấy và đưa vào repo. Chi tiết: docs/HANDOFF.md.
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
EN_WPS, VI_SPS = 2.3, 3.0          # nhịp ước lượng, như tools/handoff.py


def arg(flag, default=None):
    a = sys.argv
    return a[a.index(flag) + 1] if flag in a and a.index(flag) + 1 < len(a) else default


def flow_blocks(ep):
    """id -> khối prompt nguyên văn ([id] + [ref] + prompt), đúng thứ Batch Studio nhận."""
    out = {}
    for f in sorted((ROOT / "prompts").glob(f"{ep}*.flow.txt")):
        for blk in re.split(r"\n\s*\n", f.read_text(encoding="utf-8")):
            m = re.match(r"\[id:\s*([^\]]+)\]", blk.strip())
            if m:
                out[m.group(1).strip()] = blk.strip()
    return out


def steps(slug, vid, plan, has):
    d = vid / "drafts"
    rv = d / "4-review.md"
    approved = rv.exists() and "Đã duyệt:" in rv.read_text(encoding="utf-8")
    refs_total = refs_have = 0
    for f in (ROOT / "bible" / "refs").glob("*/refs.json"):
        for r in json.loads(f.read_text(encoding="utf-8"))["refs"]:
            refs_total += 1
            refs_have += (f.parent / r["file"]).exists()
    plates = [p for p in plan["plates"]]
    scenes = {s["src"]["id"] for b in plan["beats"].values() for s in b["scenes"]
              if s["src"]["kind"] in ("regen", "new")}
    p_have = sum(has(p["id"]) for p in plates)
    s_have = sum(has(i) for i in scenes)
    rows = [
        ("Ý tưởng", (d / "1-ideas-gemini.md").exists() or (d / "2-skeleton.md").exists(),
         "" if (d / "1-ideas-gemini.md").exists() else "bỏ qua"),
        ("Khung", (d / "2-skeleton.md").exists(), ""),
        ("Gemini viết", bool(list(d.glob("3-script-gemini*.md"))), ""),
        ("Chuẩn hoá", rv.exists(), ""),
        ("Duyệt", approved, ""),
        ("Ảnh tham chiếu", refs_total and refs_have == refs_total, f"{refs_have}/{refs_total}"),
        ("Ảnh mẫu", p_have == len(plates), f"{p_have}/{len(plates)}"),
        ("Ảnh cảnh", s_have == len(scenes), f"{s_have}/{len(scenes)}"),
        ("Clip · dừng hình", False, ""),
        ("Giọng", False, ""),
        ("Dựng · soát", False, ""),
        ("Đăng", False, ""),
    ]
    out, now = [], False
    for name, done, note in rows:
        state = "done" if done else ("todo" if now else "now")
        now = now or not done
        out.append({"name": name, "state": state, "note": note})
    return out


def main(slug):
    ep = "-".join(slug.split("-")[:2])
    vid = ROOT / "videos" / slug
    spec = importlib.util.spec_from_file_location("c", vid / "content.py")
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)
    if not hasattr(c, "BEATS_EN"):
        raise SystemExit("content.py chưa có BEATS_EN — bước 4 chưa chuẩn hoá bản EN")
    plan = json.loads((vid / "drafts" / "4-scene-plan.json").read_text(encoding="utf-8"))
    sk = vid / "drafts" / "2-skeleton.md"
    tg = {m.group(1).lower(): int(m.group(2)) for m in
          re.finditer(r"^\|\s*(\d\d|short-outro)\s*\|\s*(\d+)s\s*\|", sk.read_text(encoding="utf-8"), re.M)} \
        if sk.exists() else {}
    img_root = Path(arg("--img-root", ROOT / "public" / "img" / ep))
    rp = vid / "drafts" / "review-page.json"          # link trang + ảnh đã tải lên, nếu tập đã có trang
    if arg("--assets"):
        assets = json.loads(Path(arg("--assets")).read_text(encoding="utf-8"))
    else:
        assets = json.loads(rp.read_text(encoding="utf-8")).get("assets", {}) if rp.exists() else {}
    blocks = flow_blocks(ep)
    has = lambda i: bool(i) and any((img_root / f"{i}.{x}").exists() for x in ("jpg", "png", "webp"))

    def enrich(s_src, extra):
        i, old = s_src.get("id"), s_src.get("replaces")
        extra["has"] = has(i)
        extra["img"] = assets.get(i) if has(i) or s_src["kind"] == "reuse" else None
        extra["oldImg"] = assets.get(old) if old else None
        if s_src["kind"] in ("regen", "new") and i in blocks:
            extra["prompt"] = blocks[i]
        return extra

    warn = []
    plates = []
    for p in plan.get("plates", []):
        src = {"kind": p["src"]["kind"], "id": p["id"], "replaces": p.get("replaces")}
        plates.append(enrich(src, {**p}))
        if src["kind"] in ("regen", "new") and p["id"] not in blocks:
            warn.append(f"ảnh mẫu {p['id']}: chưa có prompt (chạy build-prompts)")
    beats = []
    for b in list(c.ORDER) + (["short-outro"] if "short-outro" in c.BEATS else []):
        p = plan["beats"].get(b)
        if not p:
            warn.append(f"{b}: chưa có trong 4-scene-plan.json")
            continue
        en = [x.strip() for x in c.BEATS_EN.get(b, "").split("\n") if x.strip()]
        vi = [x.strip() for x in c.BEATS[b].split("\n") if x.strip()]
        if len(en) != len(vi):
            warn.append(f"{b}: EN {len(en)} đoạn, VI {len(vi)} đoạn — bảng hai cột sẽ lệch dòng")
        scenes = []
        for sc in p["scenes"]:
            if sc["at"].lower() not in c.BEATS_EN.get(b, "").lower():
                warn.append(f"{b}: chữ neo “{sc['at']}” không có trong lời EN")
            if sc["src"]["kind"] in ("regen", "new") and sc["src"]["id"] not in blocks:
                warn.append(f"{b}: {sc['src']['id']} chưa có prompt")
            scenes.append(enrich(sc["src"], {**sc}))
        beats.append({"id": b, **{k: p[k] for k in ("act", "title", "chip", "caption")}, "scenes": scenes,
                      "en": en, "vi": vi, "target": tg.get(b, 0),
                      "enSec": round(len(re.findall(r"[A-Za-z0-9'’-]+", c.BEATS_EN.get(b, ""))) / EN_WPS),
                      "viSec": round(len(c.BEATS[b].split()) / VI_SPS)})
    data = {"beats": beats, "plates": plates, "steps": steps(slug, vid, plan, has)}
    html = (ROOT / "tools" / "templates" / "review-page.html").read_text(encoding="utf-8")
    html = (html.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
                .replace("__PAGETITLE__", plan.get("pageTitle", f"{slug} · xưởng duyệt"))
                .replace("__SLUG__", slug).replace("__TITLE__", plan.get("episode", slug)))
    out = Path(arg("--out", ROOT / "out" / slug / "review.html"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    n_img = sum(1 for b in beats for s in b["scenes"] if s.get("img") or s.get("oldImg"))
    print(f"{out}  ({len(beats)} beat · {sum(len(b['scenes']) for b in beats)} cảnh · {n_img} cảnh có hình · "
          f"{len(blocks)} prompt)")
    for w in warn:
        print("  ⚠", w)


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1].startswith("-"):
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1])
