# V4 · giao cho Gemini

**Cách dùng:** mở Gemini, dán **toàn bộ phần dưới vạch `DÁN TỪ ĐÂY`**, đính kèm
`docs/EPISODE-001-V3-MASTER.md` (chỉ để Gemini bắt giọng văn — bản ấy còn tên cũ, bộ soát sẽ bắt nếu
lọt). Prompt đã tự dặn Gemini chỗ lưu:

- Gemini ghi được file (Gemini CLI…) → nó tự lưu vào `videos/kanto-001-bulbasaur/drafts/v4-gemini.md`.
- Gemini trên web → nó trả **một khối code duy nhất**, bấm nút copy của khối rồi dán vào file ấy.
- Bị cắt giữa chừng → dòng cuối là `<!-- CONTINUE FROM BEAT xx -->`. Gõ "continue", dán khối mới
  **nối tiếp** vào cùng file.

Xong thì nhắn Claude: **`xong gemini`**.

Gemini được **tự sửa nhẹ** (thứ tự câu, co giãn thời lượng, chọn so sánh và chỗ dừng hình). Muốn
**sửa khung** (thêm/bớt/gộp beat, đổi sự kiện, đổi nhãn) thì chỉ được đề xuất ở mục
`SKELETON-CHANGES` — Claude soát rồi bạn chốt.

Phần 1, 2, 6 là **lõi dùng lại cho mọi tập**. Phần 3–5 là riêng tập này.

---

===== DÁN TỪ ĐÂY =====

You are the writer for a nature-documentary channel. I need the full narration for one episode,
rewritten so it sounds like a great wildlife film: calm, exact, curious and a little haunting. Below
is a skeleton: the facts, the order and the evidence. Your main job is the **voice**: rhythm,
tension, images, the sentence that makes someone stay.

**Where your answer goes.** Your answer is saved as the file
`videos/kanto-001-bulbasaur/drafts/v4-gemini.md` in the project folder
`D:\Users\tuanla2\creature-field-guide`, and a script reads it.
- If you can write files, write your whole answer to that path and reply only "saved".
- Otherwise, put your **entire** answer inside **one** code block that opens with ````markdown (four
  backticks) and whose first line is `<!-- save as videos/kanto-001-bulbasaur/drafts/v4-gemini.md -->`,
  so it can be copied in one click. Nothing outside the block.
- If you run out of space, stop at the end of a whole beat and write `<!-- CONTINUE FROM BEAT xx -->`
  as the last line. When I say "continue", start a new block with the next beat.

**What you may change, and how:**
- **Change freely** (just do it): the order of sentences inside a beat · which details you dwell on
  and which you cut · moving one fact to the neighbouring beat when the rhythm is better · shifting time
  between beats (each beat within ±15% of its target, the whole episode within ±5%) · which optional
  comparisons you use · where the freeze moments go (among the candidates, or a better place you find).
- **Propose, don't apply** (write them in `## SKELETON-CHANGES`, and keep the narration on the current
  skeleton): adding, removing, merging, splitting or reordering beats · changing, adding or dropping a
  fact · changing an evidence label · changing the spine question or the ending · new catalogue or
  anime material (goes in `## PROPOSED` with its source). For each proposal, say what it improves and
  which rule or beat it might break.
- **Never change**: the hard rules in section 2 · "shiny" said once in beat 02, after the colour is
  seen · the spine question stays unanswered.

## 1 · The world and the narrator (all episodes)

- The narrator is a field biologist from *our* Earth, now working in a world where these creatures
  are ordinary wildlife. He speaks in the first person ("I"). **He never says his own name**, and nobody
  names him. He compares everything to animals and plants "back home" (real Earth species).
- He is a patient observer: he watches, he does not interfere, and he does not give animals pet
  names.
- Tone: Attenborough's calm crossed with a private field diary. Short sentences next to long ones.
  Concrete images. No hype, no "incredible", no "amazing", no rhetorical questions stacked in a row,
  no "little did I know", no "nature is truly remarkable".

## 2 · Hard rules. Breaking one means the draft is thrown out

1. **No game, no franchise.** Never say: Pokémon, Pokédex, trainer, gym, level, HP, stats, type,
   move, attack names (Vine Whip, Solar Beam, Sleep Powder, Razor Leaf, Leech Seed, Tackle…), ability
   names (Chlorophyll, Overgrow), Poké Ball, "evolve"/"evolution". The Pokédex is called **"the
   catalogue"** (VI: "cuốn danh lục"). Changing form is "changing form" or "the change", never
   "evolving". Describe what an organ *does*, never the name of an attack.
2. **No film crew, no screen, no AI.** Never mention a camera, crew, footage, video, viewers, screen,
   subscribing, or how the images were made. There is only "I" and a notebook.
3. **Three kinds of evidence, never mixed.** Every factual sentence belongs to exactly one:
   - 📖 **catalogue**: it comes from the catalogue, and must match a source in the skeleton;
   - 👁 **observation**: the narrator saw or measured it himself;
   - 🔬 **hypothesis**: the narrator's own reasoning, **always tied to one real Earth species**.
   - 🎬 **locals' story**: comes from the anime. Tell it as "people here say…", never as fact.
4. **No invented numbers.** No percentages, degrees, kilograms or calories. Numbers the narrator
   counted himself (seven animals, day twenty-two, three hours) are fine, and they must agree with
   the TIMELINE you write.
5. **Every ability has a cost.** When the animal uses something, say what it pays.
6. **No shedding skin, no moulting, no transformation on camera.** The change of form is told only
   through swelling, weight, light, silhouette and traces left behind.
7. **No personal names for animals.** The central animal is **K-01**, a field code from his
   notebook. Other animals are called by their species or by what they look like ("a larger one",
   "an old female"). A minor animal that keeps coming back gets a code (K-04), never a name.
8. **Anatomy is research-style only**: an x-ray-like view of bones and energy channels. No blood, no
   organs, no cutting. Mating stops at display, nest and care of young.

## 3 · This episode

- **Species:** Bulbasaur → Ivysaur (the Venusaur is a different, old animal).
- **Central animal:** `Shiny Bulbasaur · K-01`. Its whole body is a warm pale yellow-green, and the
  bulb on its back is a darker, deeper green. Every other Bulbasaur is blue-green with darker blotches.
  After the change of form it is still recognisable: a **Shiny Ivysaur has a golden-yellow bud**, while
  every ordinary Ivysaur has a **pink** one.
- **The word "shiny"** is what people in this world call such animals. It appears **exactly once in
  VO_EN and once in VO_VI**, in beat 02, *after* the audience has already seen the colour. Keep it as
  "shiny" in the Vietnamese too. Never use "shiny" as an ordinary adjective anywhere else. After beat 02
  the narrator says "K-01" or "it".
- **Place:** Viridian Forest (📖 *Pokémon: Let's Go, Pikachu!/Eevee!*). The hollow where they gather is
  **The Mysterious Garden** (🎬 anime, episode 51). Do not invent other place names.
- **The spine question**, asked in beat 00/01, asked again in beat 05, **never answered** (not even in
  beat 15):
  > *Is the animal feeding the seed, or is the seed feeding the animal?*
- **Research purpose** (said once, beat 01): the narrator came because he believes there are creatures
  in which life and energy cannot be pulled apart. Say it plainly, without saying where he comes from.

### Sources you may use (📖 and 🎬). Nothing else counts as catalogue.

| Claim | Source |
|---|---|
| a seed was planted on its back at birth | Pokédex Red/Blue |
| sleeps in the sun; the seed grows by absorbing sunlight | Pokédex Ruby/Sapphire/Emerald |
| can go for days without eating; stores energy in the bulb | Pokédex Yellow |
| two temperaments: faster in harsh sun; hits harder when badly hurt | Chlorophyll; Overgrow (Bulbapedia). **Never name them.** |
| the bud draws energy from the body | Pokédex Yellow (Ivysaur) |
| can no longer stand on hind legs; legs and trunk thicken | Pokédex Red/LeafGreen/Sword; Ruby/Emerald |
| basks more than usual before blooming; gives off scent when about to bloom | Pokédex Ruby; Blue/Silver (Ivysaur) |
| the female has a pistil at the centre of the flower | Bulbapedia, Venusaur gender differences |
| the scent is stronger after rain and calms those who are fighting | Pokédex Venusaur (Ruby/Sapphire; FireRed) |
| once a year they gather in a hidden place and change form together | 🎬 anime ep. 51, via Bulbapedia (Biology) |
| releases a fine powder that makes attackers sleepy | 📖 its known behaviour (Sleep Powder, Gen I). **Never name it.** |
| charges light in the bulb, holds still, then releases a beam | 📖 known behaviour (Solar Beam's charging turn). **Never name it.** |
| the Shiny colours, and that they persist after changing form | Bulbapedia: Shiny Pokémon |

### Earth comparisons: fewer, and only the ones that carry the argument

V3 had eleven comparisons and it started to sound like a lecture. The creature is the star. Every
comparison below is already fact-checked (🔬), but they are not equal:

- **Core** (keep; each one pushes the spine question): algae inside coral tissue recycle the host's
  waste (04) · lichen vs mistletoe (05) · an elephant's trunk grasps, caresses and strikes with one
  organ (10) · **peppered moths: pale moths on soot-darkened bark were eaten by birds far more often**
  (08) · young sunflowers track the sun, mature ones stay fixed facing east (12).
- **Optional** (use **at most two** in the whole episode, and only if the beat still breathes): frogs
  drink through belly skin (04) · a horse's tail swatting flies (07) · lizards basking before they can
  run (11) · agave spending its whole life on one flowering (11) · elephants and giant tortoises: carrying
  weight turns legs into pillars (15).
- **At most one comparison per beat.** A comparison is one or two sentences, never a paragraph.

### Freeze moments: the narrator stops to think

Up to **three times** in the episode the picture **freezes** on a word of the narration: the animal
is caught mid-action, the frame darkens, and a pointer examines the one body part that matters. In
**at most two** of those, a small **photograph from home** (a real Earth animal, like a print he
carries in his notebook) appears next to the pointer. Write the narration so it has room for that
pause: a short sentence that lands on the frozen moment, then the thought. Candidates (pick; don't
use all):

- beat 10: the vine frozen mid-lash → photo: an elephant's trunk
- beat 08: K-01 pressed flat under the fern, still pale in the shade → photo: a pale peppered moth
  on dark bark
- beat 12: head still, bulb turned toward the sun → photo: a young sunflower

## 4 · The skeleton: 16 beats + short outro

EN words ≈ seconds × 2.3. Stay within ±15%. VO_VI must take **about the same time to read** as VO_EN,
because both voice tracks share one timeline.

| Beat | Target | EN words | Must happen (in this order) |
|---|---|---|---|
| 00 | 13s | ~30 | Day one: it lies motionless on the trail at noon. He thinks it is dead. The seed on its back contracts. It is breathing, and not only with its lungs. |
| 01 | 20s | ~46 | Research purpose (see above). Method: pick one animal and follow it long enough to see what changes, as people do with wolves and elephants back home. The catalogue calls this species Bulbasaur; his notebook calls it K-01. For weeks that is all it is: a word and a number. |
| 02 | 45s | ~103 | Viridian: where old forest meets grassland; a trail of flattened grass that *they* made. 👁 Seven animals in this clearing. K-01 is the smallest and always walks last, and it is the one you notice first: pale yellow-green where the others are blue-green, with a bulb darker than theirs. 👁 For a week he maps where each one lies at noon: K-01 is in the brightest patch every day, all seven days. Then, **only now**: *people here call ones like this "shiny". In my notebook it's still just K-01.* |
| 03 | 36s | ~84 | At noon K-01 stops eating and lies still (once he even lost track of it and crawled around a fern clump to find it). After hours the seed is swollen and the belly still flat. It isn't fasting; it is eating something else. 📖 Two separate catalogue lines (sunlight grows the seed · days without food, energy stored in the bulb). It took him nearly a month to put them together. The thing on its back is a second stomach. (Label the line "a second stomach" as his own way of putting it.) |
| 04 | 41s | ~94 | Sunlight is not enough: a plant also needs water and minerals. Three more weeks to see where they come from. 👁 Late afternoon: it stands at the pond edge with both front feet sunk in mud, a long time, and never drinks (optional 🔬: frogs drink through belly skin). 🔬 Minerals may come from inside: coral algae recycle the host's waste. If so, the bulb is fed by what K-01's own body throws away: a closed loop. |
| 05 | 39s | ~89 | His notebook changes. First he wrote "parasite" (clings, sucks, grows on what the host finds), **crossed out on the page**. But parasites don't leave the host well fed, and K-01 is strongest on the harshest sunny days. **Spine question asked again.** 🔬 Lichen (fungus + alga so fused they were taken for one species) vs mistletoe (drains the host until it dies standing). The two ways of living together are a hair apart. |
| 06 | 45s | ~102 | 👁 The seven never lie close: each keeps enough space for sun to reach its back. At dusk the sun patches shrink fast and there is shoving: shoulders, no biting; the loser leaves. K-01 sleeps about two body-lengths from a larger animal, the same distance every night; they never touch. The day that larger one's flank is torn open (a small wound, no gore), **he gives it a code, K-04**: an animal gets a code once he can tell it apart. That night the clearing rearranges: four animals lie around K-04, and K-01 is at its usual distance. |
| 07 | 38s | ~87 | They do touch, just not lying down. 👁 Two vines come out from under the bulbs, meet in the air, curl around each other for a few seconds, let go. He watched for twenty minutes and wrote nothing. Not a whip: an organ to hold, to touch, to greet. (Save the elephant for beat 10.) And to scratch: the back is a blind spot for a short-necked, four-legged animal. 👁 K-01 flicks a vine over its back and knocks off a caterpillar (optional 🔬: like a horse's tail at a horsefly). |
| 08 | 52s | ~121 | **The colour has a price.** 👁 Day twenty-two: a large, long-beaked bird circling high (the catalogue lists it as Fearow; one eye clouded ash-grey from an old wound). It doesn't hunt the clearing. It follows only K-01. 👁 Why: the ordinary ones' blue-green skin with dark blotches disappears into dappled shade under the leaves, and K-01's pale colour doesn't. 🔬 Peppered moths: pale moths on soot-dark bark were eaten by birds far more often. First dive: K-01 does not run; it presses flat under a fern and freezes, and **the fern hides it, not its skin**. The bird misses by an arm's length and circles back. Second dive: the top of the bulb opens and a fine powder bursts out (📖); the bird rolls, loses its line, leaves. |
| 09 | 27s | ~61 | 👁 The part he underlined: afterwards K-01 lies still almost all afternoon (no eating, no moving, no reaction when he comes close). The bulb is **visibly smaller**. What saved it came out of the store it had spent a month filling in the sun. From then on he stops writing these under "abilities" and files them under **income and expenses**. **No numbers.** |
| 10 | 50s | ~114 | This land has something home doesn't: people make these animals fight each other. He goes down to a town, stands at the outer ring of a dirt yard, watches one match. 👁 The vines no longer greet; they lash. Same organ: picking fruit and swatting pests in the forest, fighting in the yard. He doesn't condemn it: 🔬 the elephant's trunk also caresses a calf and can break a man's bones. 👁 One move keeps him writing till dawn: the animal **holds still for a beat, the bulb glows, then the beam** (📖). The crowd calls that pause a weakness; he sees the noon store drained in one breath. Back in the forest at dawn, K-01 is already lying in the first patch of sun. |
| 11 | 52s | ~119 | People who have raised them for years say every species has its own nature, and this one has two. 👁/📖 First, which he measured before anyone told him: at harsh noon K-01 covers the same stretch **almost twice as fast** as in shade (he timed it); a sun-driven body runs harder the harsher the sun (optional 🔬: lizards bask before they can run). 📖 Second, seen only in the yard, and it bothers him more than it impresses him: a badly hurt animal suddenly hits harder. His reading: it isn't stronger, it is spending the last of the reserve, once (optional 🔬: agave, decades stored for one flowering, then death). |
| 12 | 54s | ~125 | **The climax of the middle.** Month four: K-01 changes its habits: basks far longer, skips the midday shade, eats more (📖 basks more before blooming), walks slower; the vines thicken and droop as if it can't steer them. 👁 One morning he sits three hours to record one detail: the **head faces south and stays still; the bulb turns slowly east, following the sun.** Two parts of one body, facing two ways, the same morning. **That is the strongest evidence yet for "two lives in one body"**, so let the spine question press here without answering it. 🔬 Young sunflowers track the sun; once in full bloom they stop and face one way for good. (Nothing about a crooked bulb or a name. That idea is gone.) |
| 13 | 32s | ~74 | End of that month K-01 leaves the herd, heads into the old forest; he loses it for four days. 👁 K-04 stays; every morning it lies in the same place, **with the same two-body-length gap beside it, and nobody takes that spot.** Night five: he finds K-01 in a hollow behind a ring of trees with more than ten others, standing in a circle, not touching, silent. **K-01 is the only pale one among them.** 🎬 People here say they gather there once a year; they call it The Mysterious Garden. He thought it was about to die, and wrote a whole page about it. |
| 14 | 52s | ~119 | He didn't see the moment: he fell asleep after two sleepless nights, and at dawn the hollow was empty. 👁 It left enough for someone who reads traces: soil ploughed into short furrows where four feet braced under a new weight · grass flattened in a ring · around the base of the bulb, old dry bracts come loose and curled like onion skin (on the ground, not on the body) · a smell of flowers he had never smelled on this species (📖 scent before blooming). In the mist across the grass: large shapes. **The others carry pink buds. One carries a yellow bud.** Its skin is green now, not pale yellow, but the bud is gold, and he knows. Deeper footprints with a drag mark. What stands there is no longer the animal he recorded, but when he opens his notebook it still tilts its head toward the sound of the pen. |
| 15 | 86s | ~198 | 📖 The bud is now so heavy it can't rise onto its hind legs; legs and trunk have thickened (optional 🔬: elephants and giant tortoises, carry weight and legs become pillars). Last rainy season in this notebook: an **old female Venusaur** at the forest edge (trunk gone woody, moss and small ferns on her back, flower large and a little faded; people say she was there before they were born). 📖 A pistil at the centre of her flower (others he met had none): female, the first time he could tell sex by eye. K-01's bud hasn't opened, so he still doesn't know whether he followed a male or a female. 📖 After rain her scent grows stronger; he watched two animals that had been snarling sit down a few steps apart inside it. **The spine question one last time, unanswered**, then: perhaps a body can begin as two lives and still become one individual. Last line, handing over to the next episode: on the next page of the catalogue is a species that carries a flame at the tip of its tail. If that flame goes out in the rain, how does it survive? |
| short-outro | 10s | ~23 | For the vertical Short: the spine question in its plainest form, plus "after fourteen months in the field, I still can't answer it" (the number must match your TIMELINE). |

## 5 · What to improve

- **Voice and tension.** Each beat should end on something that pulls into the next one: an image, a
  doubt, a small reversal.
- **Show, then say.** The audience must *see* a thing before the narrator names or explains it.
- **Timeline.** V3 contradicted itself (the change of form in month four, "followed it for a year",
  "fourteen months"). Write one consistent TIMELINE and make every number in VO agree with it.
- **Vietnamese.** VO_VI is a natural Vietnamese narration of the same content, not a word-for-word
  translation. Pronoun for the animal: "nó". The narrator says "tôi". "Back home" = "ở quê tôi".
  Species names stay in English (Bulbasaur, Ivysaur, Venusaur, Fearow). K-01 is read "ca không một".

## 6 · Output format (strict, because a script will parse it)

Use exactly these headings and field names. No other prose before or after.

```
## BEAT 00
TARGET: 13s
VO_EN:
<narration, one paragraph per breath/pause>
VO_VI:
<narration>
SCREEN:
- caption: <EN, ≤ 68 characters>
- text: <EN, ≤ 52 characters, optional>
- chip: <one of 📖 CATALOGUE · 👁 OBSERVATION · 🔬 HYPOTHESIS · 🎬 LOCAL ACCOUNT>
SHOTS:
- <el> | who=<…> | size=<…> | angle=<…> | loc=<…> | motion=<yes|no> | at="<an EARLY word in VO_EN where it appears>" | <one sentence: what we see>
EVIDENCE:
- 📖 <claim> — <source from the table>
- 👁 <claim> — observation
- 🔬 <claim> — <Earth species>: <what it shows>
```

Allowed values in SHOTS (anything else is rejected):

- `el`: `world` (still image, slow camera) · `clip` (moving) · `specimen` (still image with
  1–3 pointers on details) · `notepage` (a notebook page; add `notes="<short EN note>; <note>"`) ·
  `freeze` (moving, then **freezes** on the word in `at`, a pointer examines one part; add
  `part="<the body part>"`, and optionally `earth="<Latin name> · <part>"` for the photo from home).
  Mix them: no beat should be only `world`, and no four beats in a row the same.
  **At most 3 `freeze` in the episode, at most 2 of them with `earth=`.** No other shot shows an
  Earth animal.
- `who`: `none` · `bulbasaur` · `bulbasaur:K-01` · `bulbasaur:K-04` · `ivysaur` · `ivysaur:K-01` ·
  `venusaur:female` · `fearow` · `anatomy:<species>` (x-ray style) — join with
  `+` for several (`bulbasaur+bulbasaur:K-01` = an ordinary herd with K-01 among them).
- `size`: `extreme-wide` · `wide` · `medium` · `close` · `macro`
- `angle`: `eye` · `low` · `high` · `overhead` · `rear` · `profile` · `pov`
- `loc`: `viridian-forest:trail` · `viridian-forest:clearing` · `viridian-forest:garden` · `town:yard` ·
  `none`
- Across the episode: at least 3 sizes, 3 angles, at least one `wide`, at least one x-ray
  `anatomy:*`, at least one `notepage`. K-01's colour must be clearly visible in a `close` or
  `medium` shot **before** beat 02 says "shiny".

After the last beat:

```
## SHORT-OUTRO
TARGET: 10s
VO_EN:
VO_VI:
SCREEN:
- caption: …

## TIMELINE
<one line per event: day/week/month → what happens>

## TITLES
- EN: <3 options>
- VI: <3 options>

## THUMB
<3 thumbnail hooks, ≤ 5 words each, each one a question the episode really asks>

## SKELETON-CHANGES
<one per line: what you would change in the skeleton — why — what it might break. "none" if none.>

## PROPOSED
<new facts you would like to add: claim — source. Do NOT use these in VO.>

## SELF-CHECK
<one line per rule 1–8 in section 2: "ok" or what you broke and why>
<one line: how many Earth comparisons you kept (spoken), how many freezes, how many photos from home>
```

===== HẾT PHẦN DÁN =====
