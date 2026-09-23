"""Xem bản dựng và ghi chú ngay tại chỗ — chặng 10 của PIPELINE.

    PYTHONUTF8=1 python tools/review.py <slug> [--port 8777] [--video <đường dẫn mp4>]

Mở một trang cục bộ có hai mặt:

  TRÁI  · bản render, có phụ đề bật/tắt được. Tạm dừng ở chỗ sai, gõ ghi chú → lưu kèm mốc thời
          gian và beat đoán được.
  PHẢI  · ảnh gốc. Bấm lên ảnh → ra toạ độ callout đã chuẩn hoá, dán thẳng vào scenes.json.

Hai mặt tách nhau là cố ý: khung video đã bị `camera` zoom/pan nên bấm lên đó không suy ngược ra
được toạ độ trên ảnh gốc. Video cho biết *chỗ nào sai*; ảnh cho biết *toạ độ bao nhiêu*.

Phụ đề lấy từ out/<slug>/*.srt (chạy tools/export-subs.py trước). Trình duyệt không đọc .srt nên
server đổi sang .vtt lúc gửi đi — file trên đĩa không bị đụng tới.

Xem trước khi thu giọng: `npm run build -- <slug> --skip-audio` ra mp4 câm, rồi mở trang này. Đọc
hết một lượt bằng mắt còn rẻ; sai một câu sau khi đã trả tiền giọng thì đắt.

Ghi ra videos/<slug>/review-notes.json. Không sửa gì khác.
"""
import json, sys, webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
args = [a for a in sys.argv[1:] if not a.startswith("--")]
if not args:
    sys.exit(__doc__)
SLUG = args[0]
EP = "-".join(SLUG.split("-")[:2])
PORT = int(sys.argv[sys.argv.index("--port") + 1]) if "--port" in sys.argv else 8777

VID_DIR = ROOT / "videos" / SLUG
IMG_DIR = ROOT / "public" / "img" / EP
NOTES = VID_DIR / "review-notes.json"

if not VID_DIR.is_dir():
    sys.exit(f"không có {VID_DIR.relative_to(ROOT)}")


def find_video():
    if "--video" in sys.argv:
        return Path(sys.argv[sys.argv.index("--video") + 1]).resolve()
    for pat in (f"out/{SLUG}/*.mp4", f"out/{SLUG}/**/*.mp4"):
        hits = sorted(ROOT.glob(pat), key=lambda p: p.stat().st_size, reverse=True)
        if hits:
            return hits[0]
    return None


def beat_offsets():
    """Mốc bắt đầu từng beat, cộng dồn — đủ chính xác để đoán beat, không phải để cắt."""
    timings = json.loads((VID_DIR / "timings.json").read_text(encoding="utf-8")) \
        if (VID_DIR / "timings.json").exists() else {}
    scenes = json.loads((VID_DIR / "scenes.json").read_text(encoding="utf-8")) \
        if (VID_DIR / "scenes.json").exists() else {}
    out, t = [], 0.0
    for beat in sorted(k for k in timings if not k.startswith("_")):
        hold = 0.0
        if isinstance(scenes.get(beat), dict):
            hold = float(scenes[beat].get("holdSec") or 0)
        dur = max((ln.get("end", 0) for ln in timings[beat]), default=0.0)
        out.append({"beat": beat, "start": round(t, 2), "end": round(t + dur, 2)})
        t += dur + hold
    return out


VIDEO = find_video()
OFFSETS = beat_offsets()
IMAGES = sorted(p.name for p in IMG_DIR.glob("*.jpg")) if IMG_DIR.is_dir() else []
OUT_DIR = ROOT / "out" / SLUG
SUBS = sorted(p.name for p in OUT_DIR.glob("*.srt")) if OUT_DIR.is_dir() else []


NL = chr(10)


def srt_to_vtt(text: str) -> str:
    """WebVTT = SRT nhưng có header và dùng dấu chấm cho phần nghìn giây.

    splitlines() nuốt luôn CRLF nên không phải lo xuống dòng kiểu Windows.
    """
    out = [ln.replace(",", ".") if "-->" in ln else ln for ln in text.splitlines()]
    return "WEBVTT" + NL + NL + NL.join(out) + NL

PAGE = """<!doctype html><html lang="vi"><meta charset="utf-8">
<title>Soát tập · __SLUG__</title>
<style>
:root{--bg:#14161a;--fg:#e8e6e3;--dim:#8b9199;--line:#2a2e35;--hi:#d9a441;--ok:#6fb07a}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.5 ui-sans-serif,system-ui,sans-serif}
header{padding:10px 16px;border-bottom:1px solid var(--line);display:flex;gap:16px;align-items:center}
h1{font-size:14px;margin:0;font-weight:600}
.dim{color:var(--dim)}
main{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);min-height:calc(100vh - 47px)}
section{background:var(--bg);padding:14px;min-width:0}
h2{font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--dim);margin:0 0 10px}
video{width:100%;background:#000;border-radius:4px}
select,textarea,button,input{font:inherit;background:#1d2026;color:var(--fg);border:1px solid var(--line);border-radius:4px;padding:6px 8px}
button{cursor:pointer}
button.go{background:var(--hi);color:#14161a;border-color:var(--hi);font-weight:600}
.row{display:flex;gap:8px;align-items:center;margin:8px 0;flex-wrap:wrap}
textarea{width:100%;min-height:62px;resize:vertical}
#wrap{position:relative;display:inline-block;max-width:100%}
#shot{max-width:100%;display:block;border-radius:4px;cursor:crosshair}
.pin{position:absolute;width:12px;height:12px;margin:-6px 0 0 -6px;border:2px solid var(--hi);border-radius:50%;pointer-events:none}
ul{list-style:none;padding:0;margin:10px 0 0;max-height:34vh;overflow:auto}
li{border-bottom:1px solid var(--line);padding:7px 0;display:flex;gap:8px;align-items:flex-start}
li code{color:var(--hi);cursor:pointer;white-space:nowrap}
li .x{margin-left:auto;color:var(--dim);cursor:pointer}
#saved{color:var(--ok)}
.empty{color:var(--dim);font-style:italic}
.subline{border-left:3px solid var(--hi);padding:8px 12px;margin:8px 0;background:#1a1d23;
  border-radius:0 4px 4px 0;min-height:2.6em;font-size:15px;line-height:1.45}
.subline.none{color:var(--dim);font-style:italic;border-left-color:var(--line)}
</style>
<header>
  <h1>Soát tập · __SLUG__</h1>
  <span class="dim" id="vidname"></span>
  <button class="go" id="save" style="margin-left:auto">Lưu</button>
  <span id="saved"></span>
</header>
<main>
<section>
  <h2>Bản dựng — ghi chú theo mốc thời gian</h2>
  <div id="noVid" class="empty" hidden>Chưa có bản render trong out/__SLUG__/. Truyền --video &lt;đường dẫn&gt;.</div>
  <video id="v" controls crossorigin="anonymous"></video>
  <div class="row">
    <span class="dim">phụ đề</span><select id="subpick"></select>
    <span class="dim" id="subnote"></span>
  </div>
  <div id="subline" class="subline">—</div>
  <div class="row">
    <span class="dim">tại</span><code id="t">0.00s</code>
    <span class="dim">beat</span><select id="beat"></select>
  </div>
  <textarea id="note" placeholder="Sai cái gì ở đây? (Enter để lưu, Shift+Enter xuống dòng)"></textarea>
  <div class="row"><button id="addNote">Thêm ghi chú</button>
    <span class="dim">phím tắt: <b>N</b> tạm dừng và nhảy vào ô ghi chú</span></div>
  <ul id="notes"></ul>
</section>
<section>
  <h2>Ảnh gốc — bấm để lấy toạ độ callout</h2>
  <div class="row">
    <select id="pick"></select>
    <span class="dim" id="dim"></span>
  </div>
  <div id="wrap"><img id="shot" alt=""></div>
  <div class="row">
    <span class="dim">toạ độ</span><code id="xy">—</code>
    <input id="label" placeholder="callout ghi gì?" style="flex:1;min-width:140px">
    <button id="addXY">Thêm toạ độ</button>
  </div>
  <ul id="coords"></ul>
</section>
</main>
<script>
const DATA = __DATA__;
const $ = s => document.querySelector(s);
let state = DATA.notes || {notes: [], coords: []};
if (!state.notes) state.notes = [];
if (!state.coords) state.coords = [];

// ---- video ----
const v = $("#v");
if (DATA.video) { v.src = "/video"; $("#vidname").textContent = DATA.video; }
else { v.hidden = true; $("#noVid").hidden = false; }

// ---- phụ đề ----
// <track> cho phụ đề nằm TRÊN khung hình như lúc xem thật; đồng thời in ra một dòng to
// bên dưới để đọc chữ cho kỹ — đó mới là việc đang làm ở đây.
const subpick = $("#subpick");
subpick.innerHTML = DATA.subs.length
  ? '<option value="">(tắt)</option>' + DATA.subs.map(s => `<option>${s}</option>`).join("")
  : '<option value="">(chưa có .srt — chạy tools/export-subs.py)</option>';
let cues = [];
function loadSubs(){
  [...v.querySelectorAll("track")].forEach(t => t.remove());
  cues = []; $("#subline").textContent = "—"; $("#subline").className = "subline none";
  if (!subpick.value) { $("#subnote").textContent = ""; return; }
  const tr = document.createElement("track");
  tr.kind = "subtitles"; tr.label = subpick.value; tr.default = true;
  tr.src = "/subs/" + encodeURIComponent(subpick.value);
  v.appendChild(tr);
  tr.addEventListener("load", () => {
    const t0 = tr.track; t0.mode = "showing";
    cues = [...(t0.cues || [])].map(c => ({s: c.startTime, e: c.endTime, t: c.text}));
    $("#subnote").textContent = cues.length + " dòng";
  });
}
subpick.onchange = loadSubs;
if (DATA.subs.length) { subpick.value = DATA.subs.includes("long.srt") ? "long.srt" : DATA.subs[0]; }
loadSubs();

const beatSel = $("#beat");
beatSel.innerHTML = '<option value="">—</option>' +
  DATA.offsets.map(o => `<option value="${o.beat}">${o.beat} · ${o.start}s</option>`).join("");

function beatAt(t){
  const hit = DATA.offsets.filter(o => t >= o.start).pop();
  return hit ? hit.beat : "";
}
v.addEventListener("timeupdate", () => {
  const now = v.currentTime;
  $("#t").textContent = now.toFixed(2) + "s";
  beatSel.value = beatAt(now);
  const hit = cues.find(c => now >= c.s && now < c.e);
  const el = $("#subline");
  el.textContent = hit ? hit.t : (cues.length ? "…" : "—");
  el.className = "subline" + (hit ? "" : " none");
});
document.addEventListener("keydown", e => {
  if (e.key.toLowerCase() === "n" && e.target.tagName !== "TEXTAREA" && e.target.tagName !== "INPUT") {
    v.pause(); $("#note").focus(); e.preventDefault();
  }
});
$("#note").addEventListener("keydown", e => {
  if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); addNote(); }
});
$("#addNote").onclick = addNote;
function addNote(){
  const text = $("#note").value.trim();
  if (!text) return;
  state.notes.push({t: +v.currentTime.toFixed(2), beat: beatSel.value, text});
  state.notes.sort((a,b) => a.t - b.t);
  $("#note").value = ""; render(); dirty();
}

// ---- ảnh ----
const pick = $("#pick"), shot = $("#shot"), wrap = $("#wrap");
pick.innerHTML = DATA.images.length
  ? DATA.images.map(n => `<option>${n}</option>`).join("")
  : '<option value="">(chưa có ảnh trong public/img/' + DATA.ep + '/)</option>';
let last = null;
function loadShot(){
  if (!pick.value) return;
  shot.src = "/img/" + encodeURIComponent(pick.value);
  wrap.querySelectorAll(".pin").forEach(p => p.remove());
  last = null; $("#xy").textContent = "—";
}
shot.onload = () => { $("#dim").textContent = shot.naturalWidth + "×" + shot.naturalHeight + " px"; };
pick.onchange = loadShot; loadShot();

shot.addEventListener("click", e => {
  const r = shot.getBoundingClientRect();
  const x = +((e.clientX - r.left) / r.width).toFixed(4);
  const y = +((e.clientY - r.top) / r.height).toFixed(4);
  last = {shot: pick.value, x, y};
  $("#xy").textContent = `x ${x} · y ${y}`;
  wrap.querySelectorAll(".pin").forEach(p => p.remove());
  const pin = document.createElement("div");
  pin.className = "pin";
  pin.style.left = (x * 100) + "%"; pin.style.top = (y * 100) + "%";
  wrap.appendChild(pin);
});
$("#addXY").onclick = () => {
  if (!last) return;
  state.coords.push({...last, label: $("#label").value.trim()});
  $("#label").value = ""; render(); dirty();
};

// ---- danh sách ----
function render(){
  $("#notes").innerHTML = state.notes.length ? state.notes.map((n,i) =>
    `<li><code data-seek="${n.t}">${n.t.toFixed(2)}s</code>`
    + `<span class="dim">${n.beat || "—"}</span><span>${esc(n.text)}</span>`
    + `<span class="x" data-del="n${i}">✕</span></li>`).join("")
    : '<li class="empty">chưa có ghi chú</li>';
  $("#coords").innerHTML = state.coords.length ? state.coords.map((c,i) =>
    `<li><code data-shot="${esc(c.shot)}">${esc(c.shot)}</code>`
    + `<span>x ${c.x} · y ${c.y}</span><span class="dim">${esc(c.label || "")}</span>`
    + `<span class="x" data-del="c${i}">✕</span></li>`).join("")
    : '<li class="empty">chưa có toạ độ</li>';
}
function esc(s){ return String(s).replace(/[<>&"]/g, c => ({"<":"&lt;",">":"&gt;","&":"&amp;",'"':"&quot;"}[c])); }
document.addEventListener("click", e => {
  const seek = e.target.dataset?.seek;
  if (seek) { v.currentTime = +seek; v.pause(); }
  const s = e.target.dataset?.shot;
  if (s) { pick.value = s; loadShot(); }
  const d = e.target.dataset?.del;
  if (d) {
    const i = +d.slice(1);
    (d[0] === "n" ? state.notes : state.coords).splice(i, 1);
    render(); dirty();
  }
});

// ---- lưu ----
let isDirty = false;
function dirty(){ isDirty = true; $("#saved").textContent = "chưa lưu"; }
$("#save").onclick = save;
async function save(){
  const r = await fetch("/save", {method:"POST", headers:{"content-type":"application/json"},
                                 body: JSON.stringify(state, null, 2)});
  $("#saved").textContent = r.ok ? "đã lưu " + new Date().toLocaleTimeString() : "lưu hỏng";
  if (r.ok) isDirty = false;
}
setInterval(() => { if (isDirty) save(); }, 20000);
window.addEventListener("beforeunload", e => { if (isDirty) e.preventDefault(); });
render();
</script></html>"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _file(self, path: Path, ctype):
        if not path.is_file():
            return self._send(404, "không có file", "text/plain; charset=utf-8")
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Accept-Ranges", "none")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        p = unquote(urlparse(self.path).path)
        if p == "/":
            notes = json.loads(NOTES.read_text(encoding="utf-8")) if NOTES.exists() else {}
            data = {"slug": SLUG, "ep": EP, "offsets": OFFSETS, "images": IMAGES, "subs": SUBS,
                    "video": VIDEO.name if VIDEO else None, "notes": notes}
            page = (PAGE.replace("__DATA__", json.dumps(data, ensure_ascii=False))
                        .replace("__SLUG__", SLUG))
            return self._send(200, page, "text/html; charset=utf-8")
        if p == "/video" and VIDEO:
            return self._file(VIDEO, "video/mp4")
        if p.startswith("/img/"):
            name = Path(p[5:]).name          # chặn ../
            return self._file(IMG_DIR / name, "image/jpeg")
        if p.startswith("/subs/"):
            name = Path(p[6:]).name          # chặn ../
            f = OUT_DIR / name
            if not f.is_file() or f.suffix != ".srt":
                return self._send(404, "không có phụ đề", "text/plain; charset=utf-8")
            return self._send(200, srt_to_vtt(f.read_text(encoding="utf-8")),
                              "text/vtt; charset=utf-8")
        self._send(404, "không có", "text/plain; charset=utf-8")

    def do_POST(self):
        if urlparse(self.path).path != "/save":
            return self._send(404, "{}")
        n = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(n).decode("utf-8")
        try:
            json.loads(body)
        except json.JSONDecodeError:
            return self._send(400, '{"err":"json hỏng"}')
        NOTES.write_text(body, encoding="utf-8")
        print(f"  đã lưu {NOTES.relative_to(ROOT)}")
        self._send(200, '{"ok":true}')


if __name__ == "__main__":
    print(f"tập     {SLUG}  (ep {EP})")
    print(f"render  {VIDEO.relative_to(ROOT) if VIDEO else '— chưa có, truyền --video'}")
    print(f"ảnh     {len(IMAGES)} tấm trong public/img/{EP}/")
    print(f"beat    {len(OFFSETS)} (mốc cộng dồn, dùng để đoán beat thôi)")
    print(f"ghi ra  {NOTES.relative_to(ROOT)}")
    print(f"\n  http://localhost:{PORT}   —   Ctrl+C để dừng\n")
    webbrowser.open(f"http://localhost:{PORT}")
    try:
        HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        print("dừng")
