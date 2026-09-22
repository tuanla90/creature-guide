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

const creature = (ref) => {
  const [id, state] = ref.split(":");
  const f = path.join(root, "bible/creatures", `${id}.json`);
  if (!fs.existsSync(f)) return {text: shots.extraCreatures?.[id] || id, forbidden: []};
  const b = JSON.parse(fs.readFileSync(f, "utf-8"));
  const sex = state && b.sexDifferences?.[state]?.length ? b.sexDifferences[state] : [];
  return {
    text: [b.anchor, ...b.appearance, ...sex].join(", "),
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
    return creature(s.creatures.filter((x) => x.split(":")[0] === id).length > 1 ? id : r);
  }).filter(Boolean);
  const look = s.kind === "plate" ? style.plateStyle : style.style;
  const parts = [
    look,
    s.kind === "real" ? "real living animal, scientifically accurate" : cs.length ? style.creatureTreatment : "",
    ...cs.map((c) => c.text),
    s.scene,
    s.framing,
    style.output,
    "avoid: " + [...new Set([...style.forbidden, ...cs.flatMap((c) => c.forbidden)])].join(", "),
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
fs.writeFileSync(path.join(root, `prompts/${ep}.flow.txt`), lines.join("\n\n") + "\n");
fs.writeFileSync(path.join(root, `prompts/${ep}.jsonl`), jsonl.join("\n") + "\n");
fs.writeFileSync(path.join(root, `prompts/${ep}.md`), md.join("\n"));
console.log(`${lines.length} prompt -> prompts/${ep}.{txt,flow.txt,jsonl,md}`);
