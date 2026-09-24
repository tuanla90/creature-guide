"""Trang duyệt kịch bản (bước 5 của luồng kịch bản): cảnh dự kiến + lời EN cạnh VI + ô duyệt từng beat.

    PYTHONUTF8=1 python tools/review-page.py <slug>

Đọc videos/<slug>/content.py (BEATS = VI, BEATS_EN = EN), drafts/4-scene-plan.json (cảnh dự kiến,
Claude soạn ở bước 4) và drafts/2-skeleton.md (thời lượng đích từng beat), ghép vào
tools/templates/review-page.html, ghi ra out/<slug>/review.html. Claude đăng file ấy thành Artifact có
capability db: người duyệt bấm Duyệt / Cần sửa và ghi chú ngay dưới từng beat, Claude đọc lại bằng
collection "review" (doc b00…b15, bshort-outro). Chi tiết: docs/HANDOFF.md.
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
EN_WPS, VI_SPS = 2.3, 3.0          # nhịp ước lượng, như tools/handoff.py


def main(slug):
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
    beats, warn = [], []
    for b in list(c.ORDER) + (["short-outro"] if "short-outro" in c.BEATS else []):
        p = plan["beats"].get(b)
        if not p:
            warn.append(f"{b}: chưa có trong 4-scene-plan.json")
            continue
        en = [x.strip() for x in c.BEATS_EN.get(b, "").split("\n") if x.strip()]
        vi = [x.strip() for x in c.BEATS[b].split("\n") if x.strip()]
        if len(en) != len(vi):
            warn.append(f"{b}: EN {len(en)} đoạn, VI {len(vi)} đoạn — bảng hai cột sẽ lệch dòng")
        for sc in p["scenes"]:
            if sc["at"].lower() not in c.BEATS_EN.get(b, "").lower():
                warn.append(f"{b}: chữ neo “{sc['at']}” không có trong lời EN")
        beats.append({"id": b, **{k: p[k] for k in ("act", "title", "chip", "caption", "scenes")},
                      "en": en, "vi": vi, "target": tg.get(b, 0),
                      "enSec": round(len(re.findall(r"[A-Za-z0-9'’-]+", c.BEATS_EN.get(b, ""))) / EN_WPS),
                      "viSec": round(len(c.BEATS[b].split()) / VI_SPS)})
    html = (ROOT / "tools" / "templates" / "review-page.html").read_text(encoding="utf-8")
    html = html.replace("/*__DATA__*/null", json.dumps({"beats": beats, "plates": plan.get("plates", [])},
                                                         ensure_ascii=False))
    html = html.replace("__SLUG__", slug).replace("__TITLE__", plan.get("episode", slug + " — bản duyệt"))
    out = ROOT / "out" / slug / "review.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"{out.relative_to(ROOT).as_posix()}  ({len(beats)} beat, {sum(len(b['scenes']) for b in beats)} cảnh)")
    for w in warn:
        print("  ⚠", w)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1])
