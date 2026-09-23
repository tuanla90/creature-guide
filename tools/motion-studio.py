"""Khoanh vùng và vẽ hướng chuyển động ngay trên ảnh, rồi render thử tại chỗ.

    PYTHONUTF8=1 python tools/motion-studio.py <đường dẫn ảnh> [--spec <file.json>] [--port 8778]

Vì sao có công cụ này: đặt toạ độ chuyển động bằng cách đoán số trong JSON rồi render lại để xem
là vòng lặp rất chậm — và người nhìn ảnh thì biết ngay chỗ nào phải thở, chỗ nào phải đứng yên,
còn máy thì không. Ở đây bạn kéo chuột khoanh vùng, kéo một mũi tên chỉ hướng, bấm Render, xem
ngay. Spec ghi ra đúng định dạng skill creature-motion.

Cách dùng:
  1. Bấm "Vùng mới" rồi KÉO trên ảnh  -> một hình elip: tâm và sigma của vùng.
  2. KÉO từ tâm vùng ra ngoài         -> mũi tên: hướng và biên độ.
  3. Chọn kiểu: breath | sway | drift | blink | jaw.
  4. Kéo bốn thanh cắt (trên/dưới/trái/phải) nếu chuyển động lan sang chỗ không nên lan.
  5. Bấm Render. Xem mp4 ngay dưới. Chưa ưng thì sửa rồi render lại.

Mũi tên dịch sang tham số thế nào:
  breath  -> drop_px = |thành phần dọc|, height_scale/width_scale suy theo
  sway    -> shift_px = mũi tên, angle_degrees theo độ dài, pivot = đáy elip
  drift   -> amplitude_px = mũi tên (quỹ đạo elip khép kín)
  blink   -> strength theo độ dài dọc
  jaw     -> drop_px = |thành phần dọc|
"""
import json, os, shutil, subprocess, sys, tempfile, webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
RENDER = ROOT / ".claude/skills/creature-motion/scripts/render.py"

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if not args:
    sys.exit(__doc__)
IMG = Path(args[0]).resolve()
if not IMG.is_file():
    sys.exit(f"không có ảnh: {IMG}")


def flag(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


PORT = int(flag("--port", 8778))
SPEC = Path(flag("--spec", ROOT / ".claude/skills/creature-motion/assets" / (IMG.stem + ".spec.json")))
WORK = Path(tempfile.gettempdir()) / "motion-studio"
WORK.mkdir(parents=True, exist_ok=True)
MP4 = WORK / "preview.mp4"

NL = chr(10)

PAGE = """<!doctype html><html lang="vi"><meta charset="utf-8">
<title>Motion Studio · __NAME__</title>
<style>
:root{--bg:#14161a;--fg:#e8e6e3;--dim:#8b9199;--line:#2a2e35;--hi:#d9a441;--ok:#6fb07a;--bad:#c96a5a}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:13px/1.5 ui-sans-serif,system-ui,sans-serif}
header{padding:9px 14px;border-bottom:1px solid var(--line);display:flex;gap:10px;align-items:center}
h1{font-size:13px;margin:0;font-weight:600}
main{display:grid;grid-template-columns:1fr 320px;gap:1px;background:var(--line)}
section{background:var(--bg);padding:12px;min-width:0}
button,select,input{font:inherit;background:#1d2026;color:var(--fg);border:1px solid var(--line);border-radius:4px;padding:5px 8px}
button{cursor:pointer}
button.go{background:var(--hi);color:#14161a;border-color:var(--hi);font-weight:600}
button.del{color:var(--bad)}
#stage{position:relative;display:inline-block;max-width:100%;user-select:none}
#img{max-width:100%;display:block;border-radius:4px}
#ov{position:absolute;inset:0;width:100%;height:100%;cursor:crosshair}
.row{display:flex;gap:6px;align-items:center;margin:7px 0;flex-wrap:wrap}
.dim{color:var(--dim)}
ul{list-style:none;padding:0;margin:8px 0 0}
li{border:1px solid var(--line);border-radius:4px;padding:6px 8px;margin-bottom:5px;cursor:pointer}
li.sel{border-color:var(--hi);background:#1d2026}
li .k{color:var(--hi);font-weight:600}
video{width:100%;background:#000;border-radius:4px;margin-top:8px}
label{display:flex;gap:6px;align-items:center;font-size:12px}
input[type=range]{flex:1;padding:0}
pre{background:#1a1d23;border-radius:4px;padding:8px;font-size:11px;max-height:22vh;overflow:auto;margin:6px 0 0}
#msg{margin-left:auto}
</style>
<header>
  <h1>Motion Studio</h1><span class="dim">__NAME__</span>
  <button id="add">+ Vùng mới</button>
  <button class="go" id="render">Render thử</button>
  <button id="save">Lưu spec</button>
  <span id="msg" class="dim"></span>
</header>
<main>
<section>
  <div id="stage"><img id="img" src="/img"><canvas id="ov"></canvas></div>
  <div class="row dim">Kéo trên ảnh để khoanh elip · kéo từ tâm ra để đặt mũi tên · kéo thanh cắt ở mép</div>
</section>
<section>
  <div class="row">
    <span class="dim">thời lượng</span><input id="dur" type="number" step="0.5" min="1" max="12" value="5" style="width:70px"> giây
  </div>
  <ul id="list"></ul>
  <div id="editor" hidden>
    <div class="row">
      <select id="kind">
        <option value="breath">breath · thở</option>
        <option value="sway">sway · lắc lư</option>
        <option value="drift">drift · trôi</option>
        <option value="blink">blink · chớp mắt</option>
        <option value="jaw">jaw · hàm</option>
      </select>
      <button class="del" id="del">Xoá</button>
    </div>
    <label>biên độ <input id="amp" type="range" min="0.2" max="4" step="0.1" value="1"><span id="ampv" class="dim"></span></label>
    <label>cổng màu
      <select id="gate"><option value="">không</option><option value="green">green</option>
      <option value="pink">pink</option><option value="bright">bright · chỉ vùng sáng</option></select>
    </label>
    <div class="row">
      <button id="snap">Bám biên vật thể</button>
      <span id="snapv" class="dim"></span>
    </div>
    <div class="row dim" style="margin-top:8px">Thanh cắt — kéo ở mép ảnh</div>
    <label><input type="checkbox" id="fT">cắt trên</label>
    <label><input type="checkbox" id="fB">cắt dưới</label>
    <label><input type="checkbox" id="fL">cắt trái</label>
    <label><input type="checkbox" id="fR">cắt phải</label>
  </div>
  <video id="vid" controls loop hidden></video>
  <pre id="out"></pre>
</section>
</main>
<script>
const D = __DATA__;
const $ = s => document.querySelector(s);
const img = $("#img"), ov = $("#ov"), ctx = ov.getContext("2d");
let R = D.regions || [], sel = -1, drag = null;

function fit(){ ov.width = img.clientWidth; ov.height = img.clientHeight; draw(); }
img.onload = fit; window.onresize = fit; if (img.complete) fit();

const COL = {breath:"#6fb07a", sway:"#d9a441", drift:"#7aa7d9", blink:"#c07ad9", jaw:"#d97a7a"};

function draw(){
  const W = ov.width, H = ov.height;
  ctx.clearRect(0,0,W,H);
  R.forEach((r,i) => {
    const c = COL[r.kind] || "#999";
    ctx.strokeStyle = c; ctx.lineWidth = i===sel ? 2.5 : 1.4;
    ctx.setLineDash(i===sel ? [] : [5,4]);
    ctx.beginPath();
    ctx.ellipse(r.cx*W, r.cy*H, r.sx*W, r.sy*H, 0, 0, 6.2832); ctx.stroke();
    ctx.setLineDash([]);
    if (r.ax || r.ay) {          // mũi tên
      const x0=r.cx*W, y0=r.cy*H, x1=x0+r.ax*W, y1=y0+r.ay*H;
      ctx.beginPath(); ctx.moveTo(x0,y0); ctx.lineTo(x1,y1); ctx.stroke();
      const a=Math.atan2(y1-y0,x1-x0);
      ctx.beginPath(); ctx.moveTo(x1,y1);
      ctx.lineTo(x1-10*Math.cos(a-0.4), y1-10*Math.sin(a-0.4));
      ctx.lineTo(x1-10*Math.cos(a+0.4), y1-10*Math.sin(a+0.4));
      ctx.closePath(); ctx.fillStyle=c; ctx.fill();
    }
    ctx.fillStyle = c; ctx.font = "11px system-ui";
    ctx.fillText(r.kind, r.cx*W - r.sx*W, r.cy*H - r.sy*H - 4);
    // thanh cắt
    ctx.strokeStyle = c + "88"; ctx.lineWidth = 1;
    if (r.fT!=null){ ctx.beginPath(); ctx.moveTo(0,r.fT*H); ctx.lineTo(W,r.fT*H); ctx.stroke(); }
    if (r.fB!=null){ ctx.beginPath(); ctx.moveTo(0,r.fB*H); ctx.lineTo(W,r.fB*H); ctx.stroke(); }
    if (r.fL!=null){ ctx.beginPath(); ctx.moveTo(r.fL*W,0); ctx.lineTo(r.fL*W,H); ctx.stroke(); }
    if (r.fR!=null){ ctx.beginPath(); ctx.moveTo(r.fR*W,0); ctx.lineTo(r.fR*W,H); ctx.stroke(); }
  });
  renderList(); dumpSpec();
}

function pos(e){ const b = ov.getBoundingClientRect();
  return [(e.clientX-b.left)/b.width, (e.clientY-b.top)/b.height]; }

let mode = null;
function hint(s){ $("#msg").textContent = s; }
$("#add").onclick = () => { mode = "new"; hint("Bước 1 — kéo chuột trên ảnh để khoanh một vùng"); };

ov.onmousedown = e => {
  const [x,y] = pos(e);
  if (mode === "new"){
    // tạo ĐÚNG MỘT vùng rồi sửa tại chỗ trong lúc kéo
    R.push({cx:x, cy:y, sx:0.01, sy:0.01, kind:"drift", ax:0, ay:0, amp:1, gate:"bright"});
    sel = R.length - 1;
    drag = {t:"ellipse", x0:x, y0:y, i:sel};
    mode = null;
    draw();
    return;
  }
  for (let i=R.length-1;i>=0;i--){
    const r=R[i], dx=(x-r.cx)/Math.max(r.sx,0.01), dy=(y-r.cy)/Math.max(r.sy,0.01);
    if (dx*dx+dy*dy <= 1.3){ sel=i; drag={t:"arrow", i}; hint("Bước 2 — kéo ra ngoài để đặt hướng và biên độ"); draw(); return; }
  }
  sel=-1; draw();
};

ov.onmousemove = e => {
  if (!drag) return;
  const [x,y] = pos(e);
  const r = R[drag.i];
  if (drag.t === "ellipse"){
    r.cx = (drag.x0 + x) / 2;
    r.cy = (drag.y0 + y) / 2;
    r.sx = Math.max(Math.abs(x - drag.x0) / 2, 0.01);
    r.sy = Math.max(Math.abs(y - drag.y0) / 2, 0.01);
  } else {
    r.ax = x - r.cx;
    r.ay = y - r.cy;
  }
  draw();
};

ov.onmouseup = () => {
  if (drag && drag.t === "ellipse") hint("Bước 2 — kéo TỪ TRONG vùng ra ngoài để đặt hướng");
  else if (drag) hint("Xong. Chọn kiểu bên phải rồi bấm Render thử.");
  drag = null; draw();
};

function renderList(){
  $("#list").innerHTML = R.map((r,i)=>
    `<li class="${i===sel?'sel':''}" data-i="${i}"><span class="k">${r.kind}</span>
     <span class="dim"> tâm ${r.cx.toFixed(2)},${r.cy.toFixed(2)} · σ ${r.sx.toFixed(3)},${r.sy.toFixed(3)}</span></li>`).join("");
  $("#editor").hidden = sel<0;
  if (sel>=0){ const r=R[sel];
    $("#kind").value=r.kind; $("#amp").value=r.amp||1; $("#ampv").textContent=(r.amp||1).toFixed(1)+"×";
    $("#gate").value=r.gate||"";
    for (const k of ["T","B","L","R"]) $("#f"+k).checked = r["f"+k]!=null;
  }
}
$("#list").onclick = e => { const li=e.target.closest("li"); if(li){ sel=+li.dataset.i; draw(); } };
$("#kind").onchange = e => { R[sel].kind=e.target.value; draw(); };
$("#gate").onchange = e => { R[sel].gate=e.target.value; draw(); };
$("#amp").oninput = e => { R[sel].amp=+e.target.value; draw(); };
$("#del").onclick = () => { R.splice(sel,1); sel=-1; draw(); };
$("#snap").onclick = async () => {
  const r = R[sel];
  $("#snapv").textContent = "đang bắt…";
  const j = await post("/mask", {index: sel, region: {cx:r.cx, cy:r.cy, sx:r.sx, sy:r.sy}});
  if (j.ok){ r.mask = j.path; $("#snapv").textContent = "đã bám · phủ " + (j.cover*100).toFixed(1) + "%"; }
  else $("#snapv").textContent = "hỏng: " + j.err;
  draw();
};
for (const [k,def] of [["T",0.15],["B",0.55],["L",0.2],["R",0.8]])
  $("#f"+k).onchange = e => { R[sel]["f"+k] = e.target.checked ? def : null; draw(); };

function spec(){
  return {duration_seconds:+$("#dur").value, fps:25, output_width:D.width,
    loop_mode:"cyclic", composite_mode:"warp_only", breath_skew:0.38,
    motions: R.map((r,i)=>{
      const m = {kind:r.kind, name:`${r.kind}-${i+1}`, center:[+r.cx.toFixed(3), +r.cy.toFixed(3)],
                 sigma:[+Math.max(r.sx,0.01).toFixed(3), +Math.max(r.sy,0.01).toFixed(3)]};
      const px = (r.ax||0)*D.width, py=(r.ay||0)*D.height, len=Math.hypot(px,py), a=r.amp||1;
      if (r.kind==="breath"){ m.drop_px=+(Math.abs(py)*a).toFixed(2);
        m.height_scale=+(Math.abs(py)/D.height*3*a).toFixed(4);
        m.width_scale=+(Math.abs(px)/D.width*3*a).toFixed(4);
        m.anchors={top_fade:[0.05,0.15],bottom_fade:[0.85,0.95],face_fade:[0.95,1.0],face_side:"right",face_min:0}; }
      if (r.kind==="sway"){ m.pivot=[+r.cx.toFixed(3), +(r.cy+r.sy).toFixed(3)];
        m.angle_degrees=+(len/D.width*40*a).toFixed(2);
        m.shift_px=[+(px*a).toFixed(2), +(py*a).toFixed(2)]; m.phase=0.1*i; }
      if (r.kind==="drift"){ m.amplitude_px=[+(px*a).toFixed(2), +(py*a).toFixed(2)]; m.phase=2.1*i; }
      if (r.kind==="blink"){ m.strength=+(Math.abs(py)/D.height*6*a).toFixed(3); m.peak=0.65; m.width=0.06; }
      if (r.kind==="jaw"){ m.drop_px=+(Math.abs(py)*a).toFixed(2); }
      if (r.gate) m.color_gate=r.gate;
      if (r.mask) m.region_mask=r.mask;
      const f={};
      if (r.fT!=null) f.top=[+r.fT.toFixed(3), +(r.fT+0.08).toFixed(3)];
      if (r.fB!=null) f.bottom=[+(r.fB-0.08).toFixed(3), +r.fB.toFixed(3)];
      if (r.fL!=null) f.left=[+r.fL.toFixed(3), +(r.fL+0.08).toFixed(3)];
      if (r.fR!=null) f.right=[+(r.fR-0.08).toFixed(3), +r.fR.toFixed(3)];
      if (Object.keys(f).length) m.fade=f;
      return m;
    })};
}
function dumpSpec(){ $("#out").textContent = JSON.stringify(spec(), null, 1); }
$("#dur").oninput = dumpSpec;

async function post(path, body){
  const r = await fetch(path, {method:"POST", headers:{"content-type":"application/json"},
                              body: JSON.stringify(body)});
  return r.json();
}
$("#save").onclick = async () => {
  const j = await post("/save", {spec:spec(), regions:R});
  $("#msg").textContent = j.ok ? "đã lưu " + j.path : "lưu hỏng";
};
$("#render").onclick = async () => {
  $("#msg").textContent = "đang render…"; $("#render").disabled = true;
  const j = await post("/render", {spec:spec(), regions:R});
  $("#render").disabled = false;
  $("#msg").textContent = j.ok ? "xong" : ("lỗi: " + (j.err||"").slice(0,120));
  if (j.ok){ const v=$("#vid"); v.hidden=false; v.src="/mp4?t="+Date.now(); v.play().catch(()=>{}); }
};
draw();
</script></html>"""


def snap_mask(cx, cy, sx, sy, idx):
    """Vẽ đại một elip, để máy bắt lấy biên vật thể bên trong.

    GrabCut lấy hộp bao quanh elip làm gợi ý, tự tách nền khỏi vật. Trả về ảnh xám cùng cỡ ảnh
    gốc, render.py nhân nó vào trọng số. KHÔNG nhân lại Gaussian ở đây — render.py đã làm rồi,
    nhân hai lần thì chuyển động teo mất.
    """
    import cv2
    import numpy as np
    img = cv2.imread(str(IMG), cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError(f"không đọc được ảnh: {IMG}")
    hgt, wid = img.shape[:2]
    pad = 1.35
    x0 = max(1, int((cx - sx * pad) * wid)); x1 = min(wid - 1, int((cx + sx * pad) * wid))
    y0 = max(1, int((cy - sy * pad) * hgt)); y1 = min(hgt - 1, int((cy + sy * pad) * hgt))
    if x1 - x0 < 8 or y1 - y0 < 8:
        raise ValueError("vùng quá nhỏ để bắt biên")
    mask = np.zeros((hgt, wid), np.uint8)
    cv2.grabCut(img, mask, (x0, y0, x1 - x0, y1 - y0),
                np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64),
                4, cv2.GC_INIT_WITH_RECT)
    m = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    m = cv2.GaussianBlur(m, (0, 0), max(2.0, min(wid, hgt) * 0.004))   # mép mềm, không răng cưa
    out = WORK / f"mask-{idx}.png"
    cv2.imwrite(str(out), m)
    return out, float((m > 40).mean())


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        p = unquote(urlparse(self.path).path)
        if p == "/":
            from PIL import Image
            with Image.open(IMG) as im:
                w, h = im.size
            regions = []
            if SPEC.exists():
                try:
                    regions = json.loads(SPEC.read_text(encoding="utf-8")).get("_studio", [])
                except json.JSONDecodeError:
                    pass
            data = {"width": w, "height": h, "regions": regions}
            page = PAGE.replace("__DATA__", json.dumps(data)).replace("__NAME__", IMG.name)
            return self._send(200, page, "text/html; charset=utf-8")
        if p == "/img":
            return self._send(200, IMG.read_bytes(), "image/jpeg")
        if p == "/mp4" and MP4.exists():
            return self._send(200, MP4.read_bytes(), "video/mp4")
        self._send(404, "{}")

    def do_POST(self):
        p = urlparse(self.path).path
        n = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(n).decode("utf-8"))
        if p == "/mask":
            r = body["region"]
            try:
                path, cover = snap_mask(r["cx"], r["cy"], r["sx"], r["sy"], body["index"])
            except Exception as e:                       # noqa: BLE001 — báo thẳng ra UI
                return self._send(200, json.dumps({"ok": False, "err": str(e)[:200]}))
            print(f"  bắt biên vùng {body['index']}: phủ {cover:.1%} khung")
            return self._send(200, json.dumps({"ok": True, "path": str(path), "cover": cover}))
        spec = body.get("spec") or {}
        spec["_studio"] = body.get("regions", [])   # nhớ hình vẽ để mở lại còn sửa tiếp
        if p == "/save":
            SPEC.parent.mkdir(parents=True, exist_ok=True)
            SPEC.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + NL, encoding="utf-8")
            print(f"  đã lưu {SPEC}")
            return self._send(200, json.dumps({"ok": True, "path": SPEC.name}))
        if p == "/render":
            tmp = WORK / "spec.json"
            tmp.write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")
            gif = WORK / "preview.gif"
            r = subprocess.run([sys.executable, str(RENDER), "--input", str(IMG),
                                "--spec", str(tmp), "--output", str(gif)],
                               capture_output=True, text=True, errors="ignore",
                               env={**os.environ, "PYTHONUTF8": "1"})
            if r.returncode:
                return self._send(200, json.dumps({"ok": False, "err": (r.stderr or r.stdout)[-400:]}))
            ff = shutil.which("ffmpeg")
            cmd = ([ff] if ff else ["npx", "remotion", "ffmpeg"]) + [
                "-y", "-i", str(gif), "-c:v", "libx264", "-crf", "20",
                "-pix_fmt", "yuv420p", str(MP4)]
            r2 = subprocess.run(cmd, capture_output=True, text=True, errors="ignore",
                                shell=(ff is None and os.name == "nt"))
            if r2.returncode or not MP4.exists():
                return self._send(200, json.dumps({"ok": False, "err": (r2.stderr or "")[-400:]}))
            print(f"  render xong · {MP4.stat().st_size // 1024} KB")
            return self._send(200, json.dumps({"ok": True}))
        self._send(404, "{}")


if __name__ == "__main__":
    print(f"ảnh   {IMG}")
    print(f"spec  {SPEC}")
    print(f"\n  http://localhost:{PORT}   —   Ctrl+C để dừng\n")
    webbrowser.open(f"http://localhost:{PORT}")
    try:
        HTTPServer(("127.0.0.1", PORT), H).serve_forever()
    except KeyboardInterrupt:
        print("dừng")
