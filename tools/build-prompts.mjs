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

const creature = (ref, drop = []) => {
  const [id, state] = ref.split(":");
  const f = path.join(root, "bible/creatures", `${id}.json`);
  if (!fs.existsSync(f)) return {text: shots.extraCreatures?.[id] || id, forbidden: []};
  const b = JSON.parse(fs.readFileSync(f, "utf-8"));
  const sex = state && b.sexDifferences?.[state]?.length ? b.sexDifferences[state] : [];
  // individuals: dấu riêng của MỘT cá thể có tên trong tập (vd bulbasaur:K7 -> củ mọc nghẹo)
  const mark = state && b.individuals?.[state]?.marks ? b.individuals[state].marks : [];
  return {
    // dropAppearance: bỏ dòng mô tả chung chọi với cảnh (vd con non chưa có củ)
    text: [b.anchor, ...b.appearance.filter((a) => !drop.some((d) => a.includes(d))), ...sex, ...mark].join(", "),
    forbidden: b.forbidden || [],
  };
};

const lines = [], jsonl = [], md = [`# Prompt — ${shots.episode}`, "", "| # | id | beat | file |", "|---|---|---|---|"];
shots.shots.forEach((s, i) => {
  // cùng loài xuất hiện nhiều lần (vd đực + cái) -> mô tả loài một lần, khác biệt giới do s.scene nói
  const seen = new Set();
  const cs = s.creatures.map((r) => {
    const id = r.split(":")[0];
    if (seen.has(id)) return null;
    seen.add(id);
    return creature(s.creatures.filter((x) => x.split(":")[0] === id).length > 1 ? id : r, s.dropAppearance);
  }).filter(Boolean);
  // mỗi kind có khối style riêng; không khai thì rơi về style chung
  const LOOK = {plate: style.plateStyle, anatomy: style.anatomyStyle, fieldnote: style.fieldNoteStyle};
  const look = LOOK[s.kind] || (s.kind === "scene" && !cs.length ? style.sceneStyle : style.style);
  // anatomy và fieldnote không phải "con vật thật đang sống" nên cần cách xử lý sinh vật riêng
  const TREAT = {anatomy: style.anatomyTreatment, fieldnote: style.fieldNoteTreatment};
  const treatment = s.kind === "real" ? "real living animal, scientifically accurate"
    : cs.length ? (TREAT[s.kind] || style.creatureTreatment) : "";
  // kindForbidden: thêm/bớt so với danh sách cấm chung, theo từng kind
  const kf = style.kindForbidden?.[s.kind] || {};
  const drop = new Set([...(s.allow || []), ...(kf.drop || [])]);
  const parts = [
    look,
    treatment,
    ...cs.map((c) => c.text),
    s.scene,
    s.framing,
    style.output,
    // shot.allow: bỏ vài mục khỏi danh sách cấm chung (vd cảnh trận đấu cần bóng người xem)
    "avoid: " + [...new Set([...style.forbidden, ...(kf.add || []), ...cs.flatMap((c) => c.forbidden)])]
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
const plateOf = {};
shots.shots.forEach((s) => s.kind === "plate" && s.creatures.forEach((r) => (plateOf[r.split(":")[0]] ??= s.id)));
const blocks = shots.shots.map((s, i) => {
  // plate không tự tham chiếu. anatomy/fieldnote cũng không: lấy một ảnh CHỤP làm ref sẽ kéo bản
  // x-quang và bản vẽ tay ngược về thành ảnh chụp, đúng thứ ta không muốn.
  const noRef = s.kind === "plate" || s.kind === "anatomy" || s.kind === "fieldnote";
  const refs = noRef ? [] : [...new Set(s.creatures.map((r) => plateOf[r.split(":")[0]]).filter(Boolean))];
  return [`[id: ${s.id}]`, refs.length ? `[ref: ${refs.join(", ")}]` : null, lines[i]].filter(Boolean).join("\n");
});
fs.writeFileSync(path.join(root, `prompts/${ep}.flow.txt`), blocks.join("\n\n") + "\n");
fs.writeFileSync(path.join(root, `prompts/${ep}.jsonl`), jsonl.join("\n") + "\n");
fs.writeFileSync(path.join(root, `prompts/${ep}.md`), md.join("\n"));
console.log(`${lines.length} prompt -> prompts/${ep}.{txt,flow.txt,jsonl,md}`);
