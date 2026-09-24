// Ghép prompt hàng loạt cho Google Flow từ bible/: style chung + bible sinh vật + mô tả từng shot.
//
//   node tools/build-prompts.mjs kanto-001
//
// Ra 3 file trong prompts/:
//   <ep>.txt    — MỖI DÒNG MỘT PROMPT, đúng thứ tự shot
//   <ep>.flow.txt — prompt cách nhau bằng DÒNG TRỐNG: định dạng của "Batch Image Studio" trong Flow
//   <ep>.jsonl  — {id, file, prompt} từng dòng, để đối chiếu tên file khi tải ảnh về
//   <ep>.md     — bảng đọc được cho người duyệt
import fs from "node:fs";
import path from "node:path";

const ep = process.argv[2] || "kanto-001";
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/(\w:)/, "$1")), "..");
const read = (p) => JSON.parse(fs.readFileSync(path.join(root, p), "utf-8"));
const style = read("bible/style.json");
const shots = read(`bible/shots/${ep}.json`);

// "bulbasaur:K7" -> "bulbasaur:K-01" nếu K7 là alias. Dùng chung cho mô tả và cho việc chọn ảnh mẫu.
const bibleOf = (id) => {
  const f = path.join(root, "bible/creatures", `${id}.json`);
  return fs.existsSync(f) ? JSON.parse(fs.readFileSync(f, "utf-8")) : null;
};
const canonRef = (ref) => {
  const [id, state] = ref.split(":");
  const alias = state && bibleOf(id)?.individuals?.[state]?.aliasOf;
  return alias ? `${id}:${alias}` : ref;
};

const creature = (ref, drop = []) => {
  const [id, state] = canonRef(ref).split(":");
  const b = bibleOf(id);
  if (!b) return {text: shots.extraCreatures?.[id] || id, forbidden: [], footprint: ""};
  const sex = state && b.sexDifferences?.[state]?.length ? b.sexDifferences[state] : [];
  // individuals: đặc điểm ĐÃ CHỐT của cá thể trung tâm. Cá thể có thể THAY một dòng của loài
  // (vd Shiny thay dòng màu da) qua dropAppearance — cộng thêm thôi thì prompt tự mâu thuẫn.
  const ind = state ? b.individuals?.[state] : null;
  const mark = ind?.marks || [];
  const dropAll = [...drop, ...(ind?.dropAppearance || [])];
  return {
    text: [b.anchor, ...b.appearance.filter((a) => !dropAll.some((d) => a.includes(d))), ...sex, ...mark].join(", "),
    forbidden: [...(b.forbidden || []), ...(ind?.forbidden || [])],
    footprint: b.footprint?.look || "",
  };
};

// địa điểm: bible/locations/<id>.json. "viridian-forest" hoặc "viridian-forest:clearing"
const place = (ref) => {
  if (!ref) return null;
  const [id, area] = ref.split(":");
  const f = path.join(root, "bible/locations", `${id}.json`);
  if (!fs.existsSync(f)) throw new Error(`location "${id}" chưa có trong bible/locations/`);
  const L = JSON.parse(fs.readFileSync(f, "utf-8"));
  const A = area ? L.areas?.[area] : null;
  if (area && !A) throw new Error(`location "${id}" không có khu "${area}"`);
  return {id, text: [L.look, A?.look, L.light, L.season].filter(Boolean).join(", ")};
};

const lines = [], jsonl = [], md = [`# Prompt — ${shots.episode}`, "", "| # | id | beat | file |", "|---|---|---|---|"];
shots.shots.forEach((s, i) => {
  // cùng loài xuất hiện nhiều lần (vd đực + cái) -> mô tả loài một lần, khác biệt giới do s.scene nói
  // Gom theo loài. Một loài xuất hiện nhiều lần trong một khung:
  //  · biến thể giới tính (male/female) -> tả loài một lần, khác biệt do s.scene nói (như cũ)
  //  · có CÁ THỂ ĐƯỢC CHỌN lẫn trong đàn -> tả loài một lần (màu THƯỜNG), rồi thêm "đúng một con
  //    trong số đó: <đặc điểm>". Trước đây nhánh này gộp về tả loài và BỎ MẤT đặc điểm, nên cảnh
  //    "một đàn thường + đúng một con Shiny" không sinh được. Không áp forbidden/dropAppearance của cá
  //    thể lên cả khung — các con khác vẫn mang màu thường.
  const seen = new Set();
  const cs = s.creatures.map((r) => {
    const id = r.split(":")[0];
    if (seen.has(id)) return null;
    seen.add(id);
    const group = s.creatures.filter((x) => x.split(":")[0] === id);
    if (group.length === 1) return creature(r, s.dropAppearance);
    const chosen = group.map(canonRef).filter((x) => {
      const st = x.split(":")[1];
      return st && !["male", "female"].includes(st);
    });
    const base = creature(id, s.dropAppearance);
    if (!chosen.length) return base;
    const extra = chosen.map((x) => {
      const [sp, st] = x.split(":");
      const marks = bibleOf(sp)?.individuals?.[st]?.marks || [];
      return `exactly ONE individual among them is different from all the others: ${marks.join(", ")}; ` +
             `every other individual in the frame has the ordinary colouring described above`;
    });
    return {...base, text: [base.text, ...extra].join(". ")};
  }).filter(Boolean);
  // mỗi kind có khối style riêng; không khai thì rơi về style chung
  const LOOK = {plate: style.plateStyle, anatomy: style.anatomyStyle, fieldnote: style.fieldNoteStyle,
                location: style.locationStyle};
  if (s.kind === "location" && s.creatures.length)
    throw new Error(`shot ${s.id}: kind location là ảnh địa điểm TRỐNG — không được có creatures`);
  const loc = place(s.location);
  const look = LOOK[s.kind] || (s.kind === "scene" && !cs.length ? style.sceneStyle : style.style);
  // anatomy và fieldnote không phải "con vật thật đang sống" nên cần cách xử lý sinh vật riêng
  const TREAT = {anatomy: style.anatomyTreatment, fieldnote: style.fieldNoteTreatment};
  const treatment = s.kind === "real" ? "real living animal, scientifically accurate"
    : cs.length ? (TREAT[s.kind] || style.creatureTreatment) : "";
  // kindForbidden: thêm/bớt so với danh sách cấm chung, theo từng kind
  const kf = style.kindForbidden?.[s.kind] || {};
  const drop = new Set([...(s.allow || []), ...(kf.drop || [])]);
  // size / angle / motion: ngữ pháp góc máy, chọn từ lúc viết prompt (xem docs/SCENE-TYPES.md)
  const bad = (k, m) => { throw new Error(`shot ${s.id}: ${k} "${m}" không có trong style.json`); };
  const size = s.size ? (style.sizes?.[s.size] ?? bad("size", s.size)) : "";
  const angle = s.angle ? (style.angles?.[s.angle] ?? bad("angle", s.angle)) : "";
  const studies = (s.studies || []).map((x) => (x === "footprint" ? cs.map((c) => c.footprint).filter(Boolean).join("; ") || "its footprint" : x));
  const parts = [
    look,
    treatment,
    ...cs.map((c) => c.text),
    loc ? `setting: ${loc.text}` : "",
    s.scene,
    studies.length ? `${style.studyPrefix}: ${studies.join("; ")}` : "",
    size,
    angle,
    s.framing,
    s.motion ? style.motionReady : "",
    style.output,
    // shot.allow: bỏ vài mục khỏi danh sách cấm chung (vd cảnh trận đấu cần bóng người xem)
    "avoid: " + [...new Set([...style.forbidden, ...(kf.add || []), ...(s.motion ? style.motionForbidden || [] : []),
                             ...(s.kind === "location" ? style.locationForbidden || [] : []),
                             ...cs.flatMap((c) => c.forbidden)])]
      .filter((x) => !drop.has(x)).join(", "),
  ].filter(Boolean);
  const prompt = parts.join(". ").replace(/\s+/g, " ").replace(/\.\./g, ".");
  const file = `${shots.outDir}/${s.id}.jpg`;
  lines.push(prompt);
  jsonl.push(JSON.stringify({id: s.id, file, prompt}));
  md.push(`| ${i + 1} | \`${s.id}\` | ${s.beat} | \`${file}\` |`);
});
md.push("", ...shots.shots.map((s, i) => `**${i + 1}. ${s.id}**\n\n${lines[i]}\n`));

fs.mkdirSync(path.join(root, "prompts"), {recursive: true});
fs.writeFileSync(path.join(root, `prompts/${ep}.txt`), lines.join("\n") + "\n");
// Batch Image Studio: mỗi block mở bằng [id: …] (tên ảnh/tên file) và [ref: …] — cảnh có sinh vật
// đã có ảnh mẫu (plate) thì lấy ảnh mẫu ấy làm tham chiếu, để con vật giống nhau giữa các cảnh.
// Ảnh mẫu khoá theo CÁ THỂ trước ("bulbasaur:K-01"), rồi mới theo loài ("bulbasaur"). Trước đây chỉ
// khoá theo loài, nên mọi cảnh của cá thể trung tâm lấy ảnh mẫu của một con THƯỜNG làm ref — dấu nhận
// dạng không bao giờ được giữ. Ảnh mẫu địa điểm khoá bằng "loc:<id>".
const plateOf = {};
shots.shots.forEach((s) => {
  if (s.kind === "plate") s.creatures.forEach((r) => {
    const full = canonRef(r), [sp, ind] = full.split(":");
    // male/female là BIẾN THỂ của loài, không phải cá thể được chọn -> vẫn làm ảnh mẫu loài được
    if (ind && !["male", "female"].includes(ind)) plateOf[full] ??= s.id;
    else { plateOf[sp] ??= s.id; if (ind) plateOf[full] ??= s.id; }
  });
  if (s.kind === "location" && s.location) plateOf["loc:" + s.location.split(":")[0]] ??= s.id;
});
const plateFor = (r) => { const full = canonRef(r); return plateOf[full] || plateOf[full.split(":")[0]]; };
// Ảnh tham chiếu tải về (bible/refs/<loài>/refs.json): tiểu tiết AI không biết chắc — kích thước so
// với người, dấu chân, màu Shiny. Chúng nuôi ẢNH MẪU; ảnh mẫu nuôi mọi cảnh. Nên chỉ gắn vào plate,
// và vào trang sổ có nghiên cứu dấu chân. Id trong [ref] là tên ảnh phải nạp lên Flow trước.
const refImages = (s) => {
  const out = [];
  for (const r of s.creatures) {
    const [sp, ind] = canonRef(r).split(":");
    const f = path.join(root, "bible/refs", sp, "refs.json");
    if (!fs.existsSync(f)) continue;
    for (const x of JSON.parse(fs.readFileSync(f, "utf-8")).refs || []) {
      const want = x.feeds || [];
      const plate = s.kind === "plate" && (want.includes("plate") || (ind && want.includes(`plate:${ind}`)));
      const foot = s.kind === "fieldnote" && (s.studies || []).includes("footprint") && want.includes("fieldnote:footprint");
      if (plate || foot) out.push(x.id);
    }
  }
  return out;
};
const blocks = shots.shots.map((s, i) => {
  // plate không tự tham chiếu. anatomy/fieldnote cũng không: lấy một ảnh CHỤP làm ref sẽ kéo bản
  // x-quang và bản vẽ tay ngược về thành ảnh chụp, đúng thứ ta không muốn.
  const noRef = s.kind === "plate" || s.kind === "anatomy" || s.kind === "fieldnote" || s.kind === "location";
  const locRef = s.location ? plateOf["loc:" + s.location.split(":")[0]] : null;
  const refs = [...new Set([...(noRef ? [] : [...s.creatures.map(plateFor), locRef]), ...refImages(s)].filter(Boolean))];
  return [`[id: ${s.id}]`, refs.length ? `[ref: ${refs.join(", ")}]` : null, lines[i]].filter(Boolean).join("\n");
});
fs.writeFileSync(path.join(root, `prompts/${ep}.flow.txt`), blocks.join("\n\n") + "\n");
fs.writeFileSync(path.join(root, `prompts/${ep}.jsonl`), jsonl.join("\n") + "\n");
fs.writeFileSync(path.join(root, `prompts/${ep}.md`), md.join("\n"));
console.log(`${lines.length} prompt -> prompts/${ep}.{txt,flow.txt,jsonl,md}`);
