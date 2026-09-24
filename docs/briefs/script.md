Bước 3 · Gemini dựng lại khung và viết lời. Ghép sau core.md + 2-skeleton.md bằng
`tools/handoff.py <slug> --brief script` (vòng sau: `--round 2`). Biến: {{SLUG}} · {{SAVE}}.
Luật quyền: bố cục thả, sự kiện khoá. Claude soát bằng `--draft` rồi chuẩn hoá ở bước 4.
---8<---
## Your task: shape the episode and write it

Above is the skeleton for this episode: the facts, their sources, a proposed order of beats and a
target length. Make it a great wildlife film: calm, exact, curious and a little haunting. Rhythm,
tension, images, the sentence that makes someone stay.

**What you may change freely (just do it, then list it under `## CHANGES`):**
- the structure: add, remove, merge, split or reorder beats; renumber them 00, 01, 02… in the new
  order; the `short-outro` stays last;
- time between beats: any beat may grow or shrink, but **the whole episode stays within ±5% of the
  skeleton's total**;
- the order of sentences, which details you dwell on and which you cut;
- which optional Earth comparisons you use, and where the freeze moments go;
- small sensory details (light, sound, smell, weather) and **new small observations** of the narrator,
  as long as they are plausible and contradict nothing. Mark each new one `👁 (new)` in EVIDENCE.

**What stays locked:**
- **Catalogue facts come only from the skeleton's source table.** A fact you want but cannot find
  there goes in `## PROPOSED` with its source, never in the narration.
- The hard rules above, the rules for the central animal's trait, the spine question stays
  unanswered, and the ending hook to the next episode.

## Where your answer goes

Your answer is saved as `{{SAVE}}` in the project folder `D:\Users\tuanla2\creature-field-guide`,
and a script reads it.
- If you can write files, write your whole answer to that path and reply only "saved".
- Otherwise, put your **entire** answer inside **one** code block that opens with ````markdown (four
  backticks) and whose first line is `<!-- save as {{SAVE}} -->`, so it can be copied in one click.
  Nothing outside the block.
- If you run out of space, stop at the end of a whole beat and write `<!-- CONTINUE FROM BEAT xx -->`
  as the last line. When I say "continue", start a new block with the next beat.

## Output format (strict, because a script will parse it)

Use exactly these headings and field names.

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

EN words ≈ seconds × 2.3. VO_VI must take **about the same time to read** as VO_EN, because both
voice tracks share one timeline. VO_VI is natural Vietnamese narration of the same content, not a
word-for-word translation: the narrator says "tôi", the animal is "nó", "back home" is "ở quê tôi".

Allowed values in SHOTS (anything else is rejected):

- `el`: `world` (still image, slow camera) · `clip` (moving) · `specimen` (still image with
  1–3 pointers on details) · `notepage` (a notebook page; add `notes="<short EN note>; <note>"`) ·
  `freeze` (moving, then **freezes** on the word in `at`, a pointer examines one part; add
  `part="<the body part>"`, and optionally `earth="<Latin name> · <part>"` for the photo from home).
  Mix them: no beat should be only `world`, and no four beats in a row the same.
  **At most 3 `freeze` in the episode, at most 2 of them with `earth=`.**
- `who` and `loc`: only the values listed in the skeleton. Join several with `+`
  (`bulbasaur+bulbasaur:K-01` = an ordinary group with K-01 among them).
- `size`: `extreme-wide` · `wide` · `medium` · `close` · `macro`
- `angle`: `eye` · `low` · `high` · `overhead` · `rear` · `profile` · `pov`
- Across the episode: at least 3 sizes, 3 angles, at least one `wide`, at least one x-ray
  `anatomy:*`, at least one `notepage`. The central animal's trait must be clearly visible in a
  `close` or `medium` shot **before** the narration names it.

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

## CHANGES
<one line per change you made to the skeleton's structure: what — why. "none" if none.>

## TITLES
- EN: <3 options>
- VI: <3 options>

## THUMB
<3 thumbnail hooks, ≤ 5 words each, each one a question the episode really asks>

## PROPOSED
<catalogue facts you wanted but could not find in the table: claim — source. Not used in VO.>

## SELF-CHECK
<one line per hard rule: "ok" or what you broke and why>
<one line: how many Earth comparisons (spoken), how many freezes, how many photos from home>
```
