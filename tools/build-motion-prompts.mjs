// Sinh danh sách Motion Prompts cho Google Flow (Image-to-Video) từ bible/shots/<ep>.json
// Chạy:
//   node tools/build-motion-prompts.mjs kanto-001

import fs from "node:fs";
import path from "node:path";

const ep = process.argv[2] || "kanto-001";
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/(\w:)/, "$1")), "..");
const shotsFile = path.join(root, `bible/shots/${ep}.json`);

if (!fs.existsSync(shotsFile)) {
  console.error(`Không tìm thấy file: ${shotsFile}`);
  process.exit(1);
}

const data = JSON.parse(fs.readFileSync(shotsFile, "utf-8"));

function generateMotionPrompt(shot) {
  const scene = shot.scene.toLowerCase();
  const framing = (shot.framing || "").toLowerCase();
  const kind = shot.kind;

  let cameraAction = "Slow subtle camera push-in, cinematic telephoto lens";
  let subjectAction = "subtle realistic breathing, slight muscle twitch, natural eye blink";
  let environmentAction = "leaves and grass gently swaying in soft wind, natural outdoor lighting";

  // Phân tích loại shot
  if (kind === "plate") {
    cameraAction = "Locked-off tripod camera, studio reference observation";
    subjectAction = "calm living specimen, slow breathing movement, subtle head turn, eyes blinking naturally";
    environmentAction = "soft ambient studio lighting, no rapid motion";
  } else if (scene.includes("aerial") || scene.includes("vista") || framing.includes("establishing")) {
    cameraAction = "Smooth cinematic drone forward drift over countryside, slow sweeping aerial pan";
    subjectAction = "";
    environmentAction = "morning mist rolling slowly through valleys, sunrise light shifting across rolling hills";
  } else if (scene.includes("macro") || framing.includes("macro")) {
    cameraAction = "Macro telephoto lens, shallow depth of field, delicate slow push-in";
    subjectAction = "tiny muscle movements, subtle breathing, glistening skin moisture";
    environmentAction = "soft dappled sunlight shifting, floating atmospheric dust motes";
  } else if (scene.includes("asleep") || scene.includes("sunbath") || scene.includes("lying flat")) {
    cameraAction = "Slow static telephoto shot, very gentle tilt down";
    subjectAction = "creature sleeping peacefully, deep rhythmic breathing movement, chest gently rising and falling";
    environmentAction = "golden sunbeams warming the ground, sparkling dust particles in the air, calm forest clearing";
  } else if (scene.includes("walking") || scene.includes("march") || scene.includes("crawling")) {
    cameraAction = "Smooth tracking shot following the slow heavy footsteps, side profile camera pan";
    subjectAction = "deliberate heavy steps, shifting body weight, muscles rippling under bumpy skin";
    environmentAction = "tall meadow grass parting around legs, faint pollen drifting in warm breeze";
  } else if (scene.includes("vine") || scene.includes("whip")) {
    cameraAction = "Dynamic cinematic camera angle, subtle tracking";
    subjectAction = "organic green vines extending fluidly, natural muscular articulation, controlled reach";
    environmentAction = "foliage reacting with gentle secondary motion, dramatic lighting";
  } else if (scene.includes("battle") || scene.includes("arena") || scene.includes("strike") || scene.includes("raptor")) {
    cameraAction = "High-speed 60fps nature documentary slow-motion, dramatic tracking pan";
    subjectAction = "tense predatory standoff, alert posture, sudden controlled defensive reaction";
    environmentAction = "dust kicking up from dirt ground, tension in the air, documentary lighting";
  } else if (scene.includes("rain") || scene.includes("wet")) {
    cameraAction = "Slow cinematic telephoto observation, soft horizontal pan";
    subjectAction = "steady calm presence, gentle water droplets beading and trickling down petals and leaves";
    environmentAction = "soft rain mist falling, low clouds breaking, damp glisten in the wet meadow";
  }

  const parts = [
    cameraAction,
    subjectAction,
    environmentAction,
    "photorealistic 4k BBC wildlife documentary footage, cinematic 24fps, highly detailed natural motion, no warping"
  ].filter(Boolean);

  return parts.join(", ");
}

const lines = [];
const jsonl = [];
const md = [`# Motion Prompts (Image-to-Video) — ${data.episode}`, "", "| # | id | file | motion prompt preview |", "|---|---|---|---|"];

data.shots.forEach((s, i) => {
  const motionPrompt = generateMotionPrompt(s);
  const file = `${data.outDir}/${s.id}.jpg`;

  lines.push(`[${s.id}]\n${motionPrompt}\n`);
  jsonl.push(JSON.stringify({
    id: s.id,
    file: file,
    motionPrompt: motionPrompt
  }));

  md.push(`| ${i + 1} | \`${s.id}\` | \`${file}\` | ${motionPrompt.slice(0, 80)}... |`);
});

fs.writeFileSync(path.join(root, `prompts/${ep}-motion.jsonl`), jsonl.join("\n") + "\n");
fs.writeFileSync(path.join(root, `prompts/${ep}-motion.txt`), lines.join("\n") + "\n");
fs.writeFileSync(path.join(root, `prompts/${ep}-motion.md`), md.join("\n"));

console.log(`[✓] Đã tạo thành công ${data.shots.length} motion prompts vào prompts/${ep}-motion.{jsonl,txt,md}`);
