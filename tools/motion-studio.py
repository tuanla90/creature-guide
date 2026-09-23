"""Khoanh vùng, vẽ hướng, render thử ngay — công cụ chỉnh ảnh thở.

    PYTHONUTF8=1 python tools/motion-studio.py <ảnh> [--spec <file.json>] [--port 8778]
    cmd.exe:  set PYTHONUTF8=1 && python tools\\motion-studio.py <ảnh>

Vì sao có: đặt toạ độ chuyển động bằng cách đoán số trong JSON rồi render lại để xem là vòng lặp
rất chậm. Người nhìn ảnh thì biết ngay chỗ nào phải thở, chỗ nào phải đứng yên; máy thì không.

Ba thứ làm vòng lặp nhanh lại:
  · NHÁP — dựng ở 520px / 2 giây / 15fps, nhanh hơn bản chuẩn khoảng mười lần. Space để chạy.
  · LỚP NHIỆT — sau khi render, phủ lên ảnh đúng chỗ đã động và mạnh bao nhiêu. Thấy ngay
    "cái đầu cũng động theo" mà không phải đo bằng script riêng.
  · SOLO — tắt mọi vùng khác, xem một vùng làm gì.

Phím tắt: Space nháp · Enter chuẩn · S bám biên · Delete xoá vùng · Ctrl+Z hoàn tác
"""
import json, os, shutil, subprocess, sys, tempfile, webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
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
NL = chr(10)


def snap_mask(cx, cy, sx, sy, idx):
    """Vẽ đại một elip, để máy bắt lấy biên vật thể bên trong (GrabCut).

    Trả mask xám cùng cỡ ảnh gốc. KHÔNG nhân lại Gaussian ở đây — render.py đã nhân rồi,
    nhân hai lần thì chuyển động teo mất.
    """
    import cv2
    import numpy as np
    img = cv2.imread(str(IMG), cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError(f"không đọc được ảnh: {IMG}")
    h, w = img.shape[:2]
    pad = 1.35
    x0 = max(1, int((cx - sx * pad) * w)); x1 = min(w - 1, int((cx + sx * pad) * w))
    y0 = max(1, int((cy - sy * pad) * h)); y1 = min(h - 1, int((cy + sy * pad) * h))
    if x1 - x0 < 8 or y1 - y0 < 8:
        raise ValueError("vùng quá nhỏ để bắt biên")
    m = np.zeros((h, w), np.uint8)
    cv2.grabCut(img, m, (x0, y0, x1 - x0, y1 - y0),
                np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64),
                4, cv2.GC_INIT_WITH_RECT)
    out = np.where((m == cv2.GC_FGD) | (m == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    out = cv2.GaussianBlur(out, (0, 0), max(2.0, min(w, h) * 0.004))
    png = WORK / f"mask-{idx}.png"
    cv2.imwrite(str(png), out)
    rgba = np.zeros((h, w, 4), np.uint8)          # bản xem: phần bắt được tô vàng, nền trong suốt
    rgba[..., 0], rgba[..., 1], rgba[..., 2] = 65, 164, 217      # BGRA
    rgba[..., 3] = (out * 0.5).astype(np.uint8)
    cv2.imwrite(str(WORK / f"maskview-{idx}.png"), rgba)
    return png, float((out > 40).mean())


def heat_map(gif: Path):
    """Chỗ nào động và mạnh bao nhiêu — phủ lên ảnh cho mắt thấy, khỏi phải chạy script đo."""
    import numpy as np
    from PIL import Image, ImageSequence
    fr = [np.asarray(f.convert("RGB"), dtype=np.int16)
          for f in ImageSequence.Iterator(Image.open(gif))]
    base = fr[0]
    dev = np.zeros(base.shape[:2], np.float32)
    for f in fr[1:]:
        np.maximum(dev, np.abs(f - base).mean(axis=2), out=dev)
    norm = np.clip(dev / 24.0, 0, 1)                      # 24 mức xám = đỏ hết cỡ
    h, w = norm.shape
    rgba = np.zeros((h, w, 4), np.uint8)
    rgba[..., 0] = (norm * 255).astype(np.uint8)          # càng động càng đỏ
    rgba[..., 2] = ((1 - norm) * 170 * (norm > 0.02)).astype(np.uint8)
    rgba[..., 3] = (np.clip(norm * 1.7, 0, 1) * 205).astype(np.uint8)
    Image.fromarray(rgba, "RGBA").save(WORK / "heat.png")
    return dev, (w, h)


def region_stats(dev, size, regions):
    """Lệch trung bình bên trong từng elip — con số đi kèm lớp nhiệt."""
    import numpy as np
    w, h = size
    yy, xx = np.mgrid[0:h, 0:w]
    out = []
    for r in regions:
        inside = (((xx - r["cx"] * w) / max(r["sx"] * w, 1)) ** 2 +
                  ((yy - r["cy"] * h) / max(r["sy"] * h, 1)) ** 2) <= 1
        out.append(round(float(dev[inside].mean()) if inside.any() else 0.0, 2))
    return out


PAGE = r"""<!doctype html><html lang="vi"><meta charset="utf-8">
<title>Motion Studio · __NAME__</title>
<style>
:root{--bg:#14161a;--fg:#e8e6e3;--dim:#8b9199;--line:#2a2e35;--hi:#d9a441;--ok:#6fb07a;--bad:#c96a5a}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:13px/1.5 ui-sans-serif,system-ui,sans-serif;overflow:hidden}
header{padding:8px 13px;border-bottom:1px solid var(--line);display:flex;gap:7px;align-items:center}
h1{font-size:13px;margin:0;font-weight:600;white-space:nowrap}
main{display:grid;grid-template-columns:1fr 330px;gap:1px;background:var(--line);height:calc(100vh - 41px)}
section{background:var(--bg);padding:11px;overflow:auto;min-width:0}
button,select,input{font:inherit;background:#1d2026;color:var(--fg);border:1px solid var(--line);border-radius:4px;padding:5px 8px}
button{cursor:pointer}button:disabled{opacity:.45;cursor:default}
button.go{background:var(--hi);color:#14161a;border-color:var(--hi);font-weight:600}
button.on{background:#2c3442;border-color:var(--hi)}
button.del{color:var(--bad)}
#stage{position:relative;display:inline-block;max-width:100%;user-select:none}
#img{max-width:100%;display:block;border-radius:4px}
#heat,#maskv{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;border-radius:4px}
#ov{position:absolute;inset:0;width:100%;height:100%;cursor:crosshair}
.row{display:flex;gap:6px;align-items:center;margin:6px 0;flex-wrap:wrap}
.dim{color:var(--dim)}.sm{font-size:11px}
ul{list-style:none;padding:0;margin:6px 0 0}
li{border:1px solid var(--line);border-radius:4px;padding:5px 7px;margin-bottom:4px;cursor:pointer;display:flex;gap:6px;align-items:center}
li.sel{border-color:var(--hi);background:#1d2026}
li.mute{opacity:.38}
li .k{font-weight:600}
li .n{margin-left:auto;font-variant-numeric:tabular-nums}
video{width:100%;background:#000;border-radius:4px;margin-top:7px}
label{display:flex;gap:6px;align-items:center;font-size:12px;margin:4px 0}
input[type=range]{flex:1;padding:0}
kbd{background:#1d2026;border:1px solid var(--line);border-radius:3px;padding:0 4px;font-size:10px}
#msg{margin-left:auto;white-space:nowrap}
.warn{color:var(--bad)}.good{color:var(--ok)}
pre{background:#1a1d23;border-radius:4px;padding:7px;max-height:19vh;overflow:auto;margin:7px 0 0}
</style>
<header>
  <h1>Motion Studio</h1><span class="dim sm">__NAME__</span>
  <button id="add">+ Vùng</button>
  <button class="go" id="draft">Nháp <kbd>space</kbd></button>
  <button id="full">Chuẩn <kbd>enter</kbd></button>
  <button id="heatb">Lớp nhiệt</button>
  <button id="maskb">Mask</button>
  <button id="save">Lưu</button>
  <span id="msg" class="dim sm"></span>
</header>
<main>
<section>
  <div id="stage">
    <img id="img" src="/img">
    <img id="maskv" hidden alt=""><img id="heat" hidden alt="">
    <canvas id="ov"></canvas>
  </div>
  <div class="row dim sm">kéo = khoanh vùng · kéo từ trong vùng ra = hướng · <kbd>S</kbd> bám biên · <kbd>del</kbd> xoá · <kbd>ctrl+Z</kbd> hoàn tác</div>
  <video id="vid" controls loop hidden></video>
</section>
<section>
  <div class="row">
    <span class="dim sm">dài</span><input id="dur" type="number" step="0.5" min="1" max="12" value="5" style="width:62px">
    <span class="dim sm">giây</span>
    <select id="preset" style="margin-left:auto"><option value="">+ mẫu sẵn</option>
      <option value="breath">thở · bụng, sườn</option><option value="sway">lắc · lá, củ</option>
      <option value="drift">trôi · đốm nắng</option><option value="blink">chớp mắt</option></select>
  </div>
  <ul id="list"></ul>
  <div id="editor" hidden>
    <div class="row">
      <select id="kind">
        <option value="breath">breath · thở</option><option value="sway">sway · lắc lư</option>
        <option value="drift">drift · trôi</option><option value="blink">blink · chớp mắt</option>
        <option value="jaw">jaw · hàm</option>
      </select>
      <button id="snap">Bám biên <kbd>S</kbd></button>
      <button class="del" id="del">Xoá</button>
    </div>
    <label>biên độ <input id="amp" type="range" min="0.2" max="5" step="0.1"><span id="ampv" class="dim sm"></span></label>
    <label>cổng màu <select id="gate">
      <option value="">không · an toàn nhất</option><option value="green">green</option>
      <option value="pink">pink</option><option value="bright">bright · chỉ vùng sáng</option></select></label>
    <div class="row sm dim">thanh cắt — chặn lan sang chỗ không nên lan</div>
    <div class="row">
      <label><input type="checkbox" id="fT">trên</label><label><input type="checkbox" id="fB">dưới</label>
      <label><input type="checkbox" id="fL">trái</label><label><input type="checkbox" id="fR">phải</label>
    </div>
  </div>
  <pre id="out" class="sm"></pre>
</section>
</main>
<script>
const D = __DATA__;
const $ = s => document.querySelector(s);
const img = $("#img"), ov = $("#ov"), ctx = ov.getContext("2d");
let R = D.regions || [], sel = -1, drag = null, mode = null, undoStack = [], preset = null;
const COL = {breath:"#6fb07a", sway:"#d9a441", drift:"#7aa7d9", blink:"#c07ad9", jaw:"#d97a7a"};
const DEF = {
  breath:{kind:"breath", amp:1.6, gate:"", ax:0,     ay:0.040},
  sway:  {kind:"sway",   amp:1.4, gate:"", ax:0.014, ay:-0.010},
  drift: {kind:"drift",  amp:2.0, gate:"bright", ax:0.009, ay:0.006},
  blink: {kind:"blink",  amp:1.0, gate:"", ax:0,     ay:0.014},
  jaw:   {kind:"jaw",    amp:1.0, gate:"", ax:0,     ay:0.010},
};

function fit(){ ov.width=img.clientWidth; ov.height=img.clientHeight; draw(); }
img.onload=fit; window.onresize=fit; if(img.complete) fit();
function snapshot(){ undoStack.push(JSON.stringify(R)); if(undoStack.length>40) undoStack.shift(); }
function hint(s,cls){ const m=$("#msg"); m.textContent=s; m.className="sm "+(cls||"dim"); }

function draw(){
  const W=ov.width,H=ov.height; ctx.clearRect(0,0,W,H);
  R.forEach((r,i)=>{
    const c = r.mute ? "#555" : (COL[r.kind]||"#999");
    ctx.strokeStyle=c; ctx.lineWidth=i===sel?2.5:1.3; ctx.setLineDash(i===sel?[]:[5,4]);
    ctx.beginPath(); ctx.ellipse(r.cx*W,r.cy*H,Math.max(r.sx,0.005)*W,Math.max(r.sy,0.005)*H,0,0,6.2832); ctx.stroke();
    ctx.setLineDash([]);
    if(r.ax||r.ay){
      const x0=r.cx*W,y0=r.cy*H,x1=x0+r.ax*W,y1=y0+r.ay*H,a=Math.atan2(y1-y0,x1-x0);
      ctx.beginPath(); ctx.moveTo(x0,y0); ctx.lineTo(x1,y1); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(x1,y1);
      ctx.lineTo(x1-11*Math.cos(a-0.4),y1-11*Math.sin(a-0.4));
      ctx.lineTo(x1-11*Math.cos(a+0.4),y1-11*Math.sin(a+0.4));
      ctx.closePath(); ctx.fillStyle=c; ctx.fill();
    }
    ctx.fillStyle=c; ctx.font="11px system-ui";
    ctx.fillText((r.mask?"◆ ":"")+r.kind, r.cx*W-r.sx*W, r.cy*H-r.sy*H-4);
    ctx.strokeStyle=c+"66"; ctx.lineWidth=1;
    const ln=(a,b,c2,d)=>{ctx.beginPath();ctx.moveTo(a,b);ctx.lineTo(c2,d);ctx.stroke();};
    if(r.fT!=null) ln(0,r.fT*H,W,r.fT*H);
    if(r.fB!=null) ln(0,r.fB*H,W,r.fB*H);
    if(r.fL!=null) ln(r.fL*W,0,r.fL*W,H);
    if(r.fR!=null) ln(r.fR*W,0,r.fR*W,H);
  });
  renderList(); dumpSpec();
}
function pos(e){ const b=ov.getBoundingClientRect(); return [(e.clientX-b.left)/b.width,(e.clientY-b.top)/b.height]; }

$("#add").onclick=()=>{ mode="new"; preset=null; hint("kéo chuột trên ảnh để khoanh vùng"); };
$("#preset").onchange=e=>{ if(!e.target.value) return; mode="new"; preset=e.target.value;
  hint("kéo để khoanh vùng · mẫu "+preset); e.target.value=""; };

ov.onmousedown=e=>{
  const [x,y]=pos(e);
  if(mode==="new"){
    snapshot();
    R.push(Object.assign({cx:x,cy:y,sx:0.012,sy:0.012,mute:false},
                         JSON.parse(JSON.stringify(DEF[preset||"drift"]))));
    sel=R.length-1; drag={t:"ellipse",x0:x,y0:y,i:sel}; mode=null; preset=null; draw(); return;
  }
  for(let i=R.length-1;i>=0;i--){
    const r=R[i],dx=(x-r.cx)/Math.max(r.sx,0.01),dy=(y-r.cy)/Math.max(r.sy,0.01);
    if(dx*dx+dy*dy<=1.3){ snapshot(); sel=i; drag={t:"arrow",i}; hint("kéo ra ngoài để đặt hướng"); draw(); return; }
  }
  sel=-1; draw();
};
ov.onmousemove=e=>{
  if(!drag) return; const [x,y]=pos(e), r=R[drag.i];
  if(drag.t==="ellipse"){ r.cx=(drag.x0+x)/2; r.cy=(drag.y0+y)/2;
    r.sx=Math.max(Math.abs(x-drag.x0)/2,0.008); r.sy=Math.max(Math.abs(y-drag.y0)/2,0.008); }
  else { r.ax=x-r.cx; r.ay=y-r.cy; }
  draw();
};
ov.onmouseup=()=>{ if(drag&&drag.t==="ellipse") hint("bấm S để bám biên, rồi kéo từ trong vùng ra"); drag=null; draw(); };

function renderList(){
  $("#list").innerHTML=R.map((r,i)=>{
    const s=(D.stats&&D.stats[i]!=null)?D.stats[i]:null;
    const cls=s==null?"dim":(s>=1.5?"good":"warn");
    return '<li class="'+(i===sel?"sel ":"")+(r.mute?"mute":"")+'" data-i="'+i+'">'
      +'<span class="k" style="color:'+COL[r.kind]+'">'+(r.mask?"◆":"○")+' '+r.kind+'</span>'
      +'<span class="dim sm">'+r.cx.toFixed(2)+','+r.cy.toFixed(2)+'</span>'
      +'<span class="n sm '+cls+'">'+(s==null?"":s.toFixed(1))+'</span>'
      +'<button class="sm" data-solo="'+i+'">solo</button></li>';}).join("");
  $("#editor").hidden=sel<0;
  if(sel>=0){ const r=R[sel];
    $("#kind").value=r.kind; $("#amp").value=r.amp; $("#ampv").textContent=(+r.amp).toFixed(1)+"×";
    $("#gate").value=r.gate||"";
    for(const k of ["T","B","L","R"]) $("#f"+k).checked=r["f"+k]!=null;
  }
}
$("#list").onclick=e=>{
  const s=e.target.dataset.solo;
  if(s!=null){ const i=+s, others=R.some((r,j)=>j!==i&&!r.mute);
    R.forEach((r,j)=>{ r.mute = others ? j!==i : false; }); draw(); return; }
  const li=e.target.closest("li"); if(li){ sel=+li.dataset.i; draw(); }
};
$("#kind").onchange=e=>{snapshot();R[sel].kind=e.target.value;draw();};
$("#gate").onchange=e=>{snapshot();R[sel].gate=e.target.value;draw();};
$("#amp").oninput=e=>{R[sel].amp=+e.target.value;draw();};
$("#del").onclick=()=>{snapshot();R.splice(sel,1);sel=-1;draw();};
for(const kv of [["T",0.15],["B",0.55],["L",0.20],["R",0.80]])
  $("#f"+kv[0]).onchange=e=>{snapshot();R[sel]["f"+kv[0]]=e.target.checked?kv[1]:null;draw();};
$("#heatb").onclick=()=>{ const h=$("#heat"); h.hidden=!h.hidden; $("#heatb").classList.toggle("on",!h.hidden); };
$("#maskb").onclick=()=>{ const m=$("#maskv"); m.hidden=!m.hidden; $("#maskb").classList.toggle("on",!m.hidden);
  if(!m.hidden&&sel>=0&&R[sel].mask) m.src="/maskview?i="+sel+"&t="+Date.now(); };

function spec(draft){
  const on=R.filter(r=>!r.mute);
  return {duration_seconds: draft?2.0:+$("#dur").value, fps: draft?15:25,
    output_width: draft?520:D.width, loop_mode:"cyclic", composite_mode:"warp_only", breath_skew:0.38,
    motions: on.map(function(r,i){
      const m={kind:r.kind,name:r.kind+"-"+(i+1),center:[+r.cx.toFixed(3),+r.cy.toFixed(3)],
               sigma:[+Math.max(r.sx,0.01).toFixed(3),+Math.max(r.sy,0.01).toFixed(3)]};
      const px=(r.ax||0)*D.width, py=(r.ay||0)*D.height, len=Math.hypot(px,py), a=r.amp||1;
      if(r.kind==="breath"){ m.drop_px=+(Math.abs(py)*a).toFixed(2);
        m.height_scale=+(Math.abs(py)/D.height*3*a).toFixed(4);
        m.width_scale=+(Math.abs(px)/D.width*3*a).toFixed(4);
        m.anchors={top_fade:[0.03,0.10],bottom_fade:[0.90,0.97],face_fade:[0.97,1.0],face_side:"right",face_min:0}; }
      if(r.kind==="sway"){ m.pivot=[+r.cx.toFixed(3),+(r.cy+r.sy).toFixed(3)];
        m.angle_degrees=+(len/D.width*40*a).toFixed(2);
        m.shift_px=[+(px*a).toFixed(2),+(py*a).toFixed(2)]; m.phase=0.1*i; }
      if(r.kind==="drift"){ m.amplitude_px=[+(px*a).toFixed(2),+(py*a).toFixed(2)]; m.phase=2.1*i; }
      if(r.kind==="blink"){ m.strength=+(Math.abs(py)/D.height*6*a).toFixed(3); m.peak=0.65; m.width=0.06; }
      if(r.kind==="jaw"){ m.drop_px=+(Math.abs(py)*a).toFixed(2); }
      if(r.gate) m.color_gate=r.gate;
      if(r.mask) m.region_mask=r.mask;
      const f={};
      if(r.fT!=null) f.top=[+r.fT.toFixed(3),+(r.fT+0.08).toFixed(3)];
      if(r.fB!=null) f.bottom=[+(r.fB-0.08).toFixed(3),+r.fB.toFixed(3)];
      if(r.fL!=null) f.left=[+r.fL.toFixed(3),+(r.fL+0.08).toFixed(3)];
      if(r.fR!=null) f.right=[+(r.fR-0.08).toFixed(3),+r.fR.toFixed(3)];
      if(Object.keys(f).length) m.fade=f;
      return m;
    })};
}
function dumpSpec(){ $("#out").textContent=JSON.stringify(spec(false),null,1); }
$("#dur").oninput=dumpSpec;

async function post(p,b){
  const r=await fetch(p,{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify(b)});
  return r.json();
}
let busy=false;
async function run(draft){
  if(busy) return;
  if(!R.filter(r=>!r.mute).length){ hint("chưa có vùng nào","warn"); return; }
  busy=true; const t0=Date.now();
  $("#draft").disabled=$("#full").disabled=true;
  hint(draft?"nháp…":"chuẩn…");
  const j=await post("/render",{spec:spec(draft),regions:R,draft:!!draft});
  $("#draft").disabled=$("#full").disabled=false; busy=false;
  if(!j.ok){ hint("lỗi: "+(j.err||"").slice(0,90),"warn"); return; }
  const v=$("#vid"); v.hidden=false; v.src="/mp4?t="+Date.now(); v.play().catch(function(){});
  const h=$("#heat"); h.src="/heat?t="+Date.now(); h.hidden=false; $("#heatb").classList.add("on");
  D.stats=j.stats;
  hint(((Date.now()-t0)/1000).toFixed(1)+"s · đỏ = động mạnh","good");
  draw();
}
$("#draft").onclick=function(){run(true);};
$("#full").onclick=function(){run(false);};
$("#snap").onclick=async function(){
  const r=R[sel]; hint("đang bám biên…");
  const j=await post("/mask",{index:sel,region:{cx:r.cx,cy:r.cy,sx:r.sx,sy:r.sy}});
  if(j.ok){ r.mask=j.path; hint("bám xong · phủ "+(j.cover*100).toFixed(1)+"% khung","good");
    const m=$("#maskv"); m.src="/maskview?i="+sel+"&t="+Date.now(); m.hidden=false; $("#maskb").classList.add("on"); }
  else hint("hỏng: "+j.err,"warn");
  draw();
};
$("#save").onclick=async function(){
  const j=await post("/save",{spec:spec(false),regions:R});
  hint(j.ok?("đã lưu "+j.path):"lưu hỏng", j.ok?"good":"warn");
};
document.addEventListener("keydown",function(e){
  if(/input|select|textarea/i.test(e.target.tagName)) return;
  if(e.key===" "){ e.preventDefault(); run(true); }
  else if(e.key==="Enter"){ e.preventDefault(); run(false); }
  else if(e.key==="Delete"&&sel>=0){ snapshot(); R.splice(sel,1); sel=-1; draw(); }
  else if((e.key==="s"||e.key==="S")&&sel>=0){ $("#snap").click(); }
  else if(e.ctrlKey&&e.key==="z"&&undoStack.length){ R=JSON.parse(undoStack.pop()); sel=-1; draw(); }
});
draw();
</script></html>"""


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

    def _file(self, path: Path, ctype):
        if not path.is_file():
            return self._send(404, b"", "text/plain")
        self._send(200, path.read_bytes(), ctype)

    def do_GET(self):
        u = urlparse(self.path)
        p = unquote(u.path)
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
            data = {"width": w, "height": h, "regions": regions, "stats": None}
            page = PAGE.replace("__DATA__", json.dumps(data)).replace("__NAME__", IMG.name)
            return self._send(200, page, "text/html; charset=utf-8")
        if p == "/img":
            return self._file(IMG, "image/jpeg")
        if p == "/mp4":
            return self._file(WORK / "preview.mp4", "video/mp4")
        if p == "/heat":
            return self._file(WORK / "heat.png", "image/png")
        if p == "/maskview":
            i = u.query.split("i=")[-1].split("&")[0] if "i=" in u.query else "0"
            i = "".join(ch for ch in i if ch.isdigit()) or "0"
            return self._file(WORK / f"maskview-{i}.png", "image/png")
        self._send(404, "{}")

    def do_POST(self):
        p = urlparse(self.path).path
        n = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(n).decode("utf-8"))

        if p == "/mask":
            r = body["region"]
            try:
                png, cover = snap_mask(r["cx"], r["cy"], r["sx"], r["sy"], int(body["index"]))
            except Exception as e:                       # noqa: BLE001 — báo thẳng ra giao diện
                return self._send(200, json.dumps({"ok": False, "err": str(e)[:200]}))
            print(f"  bám biên vùng {body['index']}: phủ {cover:.1%}")
            return self._send(200, json.dumps({"ok": True, "path": str(png), "cover": cover}))

        spec = body.get("spec") or {}
        spec["_studio"] = body.get("regions", [])

        if p == "/save":
            SPEC.parent.mkdir(parents=True, exist_ok=True)
            SPEC.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + NL, encoding="utf-8")
            print(f"  đã lưu {SPEC}")
            return self._send(200, json.dumps({"ok": True, "path": SPEC.name}))

        if p == "/render":
            draft = bool(body.get("draft"))
            tmp = WORK / "spec.json"
            tmp.write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")
            gif = WORK / "preview.gif"
            r = subprocess.run([sys.executable, str(RENDER), "--input", str(IMG),
                                "--spec", str(tmp), "--output", str(gif)],
                               capture_output=True, text=True, errors="ignore",
                               env={**os.environ, "PYTHONUTF8": "1"})
            if r.returncode:
                return self._send(200, json.dumps({"ok": False, "err": (r.stderr or r.stdout)[-400:]}))
            dev, size = heat_map(gif)
            stats = region_stats(dev, size, body.get("regions", []))
            ff = shutil.which("ffmpeg")
            cmd = ([ff] if ff else ["npx", "remotion", "ffmpeg"]) + [
                "-y", "-i", str(gif), "-c:v", "libx264", "-crf", "22" if draft else "19",
                "-pix_fmt", "yuv420p", str(WORK / "preview.mp4")]
            r2 = subprocess.run(cmd, capture_output=True, text=True, errors="ignore",
                                shell=(ff is None and os.name == "nt"))
            if r2.returncode:
                return self._send(200, json.dumps({"ok": False, "err": (r2.stderr or "")[-400:]}))
            print(f"  {'nháp' if draft else 'chuẩn'} xong · lệch theo vùng {stats}")
            return self._send(200, json.dumps({"ok": True, "stats": stats}))
        self._send(404, "{}")


if __name__ == "__main__":
    print(f"ảnh   {IMG.name}")
    print(f"spec  {SPEC}")
    print(f"\n  http://localhost:{PORT}    space=nháp · enter=chuẩn · S=bám biên\n")
    webbrowser.open(f"http://localhost:{PORT}")
    try:
        ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
    except KeyboardInterrupt:
        print("dừng")
