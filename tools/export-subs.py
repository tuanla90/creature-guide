"""Xuất phụ đề .srt (bản Long + Short) và lời thoại cho TTS từ một slug đã scaffold/thu giọng.

    python tools/export-subs.py kanto-001-bulbasaur

Mốc thời gian tính y hệt Root.tsx của engine (introPad, sectionGap, holdSec, leadIn, shortGap),
nên .srt khớp khung hình Remotion. Khi mới scaffold thì timing là ƯỚC LƯỢNG — thu giọng thật
(VBee) rồi căn lại timings.json thì chạy lại lệnh này.

Ra trong out/<slug>/:
  long.srt, short.srt      — phụ đề theo từng dòng caption
  script.txt               — lời thoại từng beat, chính tả gốc (đọc duyệt)
  script-tts.txt           — cùng nội dung nhưng đã thay PRON (dán vào VBee)
"""
import importlib.util, json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
slug = sys.argv[1]
vdir = ROOT / "videos" / slug
cfg = json.loads((ROOT / "video.config.json").read_text(encoding="utf-8"))
fps, P = cfg["fps"], cfg["pacing"]
sec = lambda s: round(s * fps)
beats = json.loads((vdir / "beats.json").read_text(encoding="utf-8"))
outro = json.loads((vdir / "outro.json").read_text(encoding="utf-8"))
timings = json.loads((vdir / "timings.json").read_text(encoding="utf-8"))
scenes = json.loads((vdir / "scenes.json").read_text(encoding="utf-8"))
spec = importlib.util.spec_from_file_location("content", vdir / "content.py")
content = importlib.util.module_from_spec(spec); spec.loader.exec_module(content)

def ts(frames):
    ms = round(frames / fps * 1000)
    h, ms = divmod(ms, 3600_000); m, ms = divmod(ms, 60_000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def cues(beat_id, start_frame):
    lead = sec(P["leadIn"])
    for L in timings.get(beat_id, []):
        yield start_frame + lead + round(L["start"] * fps), start_frame + lead + round(L["end"] * fps), L["text"]

def write_srt(path, items):
    out = [f"{i}\n{ts(a)} --> {ts(b)}\n{t}\n" for i, (a, b, t) in enumerate(items, 1)]
    path.write_text("\n".join(out), encoding="utf-8")

out = ROOT / "out" / slug
out.mkdir(parents=True, exist_ok=True)

# Long — như layout() trong Root.tsx
items, off = [], sec(P["introPad"])
for i, b in enumerate(beats):
    items += cues(b["id"], off)
    hold = sec(scenes.get(b["id"], {}).get("holdSec", 0))
    off += b["durationInFrames"] + hold + (sec(P["sectionGap"]) if i < len(beats) - 1 else 0)
write_srt(out / "long.srt", items)

# Short — beat "00" + "short-outro", như shortLayout()
b00 = next(b for b in beats if b["id"] == "00")
short = list(cues("00", 0)) + list(cues("short-outro", b00["durationInFrames"] + sec(P["shortGap"])))
write_srt(out / "short.srt", short)

# lời thoại cho TTS
ids = list(content.ORDER) + (["short-outro"] if "short-outro" in content.BEATS else [])
pron = getattr(content, "PRON", {})
def tts(t):
    for k, v in pron.items(): t = t.replace(k, v)
    return t
(out / "script.txt").write_text("\n\n".join(f"[{i}]\n{content.BEATS[i]}" for i in ids), encoding="utf-8")
(out / "script-tts.txt").write_text("\n\n".join(f"[{i}]\n{tts(content.BEATS[i])}" for i in ids), encoding="utf-8")
print(f"long.srt {len(items)} dòng · short.srt {len(short)} dòng · script.txt · script-tts.txt -> {out}")
