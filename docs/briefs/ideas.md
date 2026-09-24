Bước 1 · Gemini liệt kê ý tưởng cho một tập. Ghép sau core.md bằng
`tools/handoff.py <slug> --brief ideas "<loài>"`. Biến: {{SLUG}} · {{SPECIES}} · {{CONTEXT}}.
Claude đọc 1-ideas-gemini.md, chấm, chọn một (kèm một ý dự phòng), rồi viết 2-skeleton.md.
---8<---
## Your task: pitch episode ideas

The next episode is about **{{SPECIES}}**. Pitch **six** different episode ideas. Each idea is one
question about this species that is strange enough to justify following one animal for months, and
that cannot be answered by looking once.

What the channel already knows about this episode:

{{CONTEXT}}

Look at the species from many sides, not only its most famous ability: body shape and what the odd
part is for · energy and fasting · heat and daily rhythm · movement · defence · senses and
communication · social life · reproduction · young and growing up · age and scars · neighbours and
food web · life near humans · tracks and sounds · parasites and cleaning · camouflage or warning ·
death and what it leaves behind. **The six ideas must use at least four different sides**, and at
least one must be a quiet idea that is not about a fighting ability.

Two episode frames exist:
- **A · one individual** (default): follow one animal, K-01, through one survival question.
- **B · comparison**: two or three animals set side by side on one question.

For every idea, only use catalogue facts you can source (game + version, anime + episode, manga +
chapter). If you are not sure a fact is canon, write it under RISK instead of CANON.

## Where your answer goes

Your answer is saved as `videos/{{SLUG}}/drafts/1-ideas-gemini.md` in the project folder
`D:\Users\tuanla2\creature-field-guide`, and a script reads it.
- If you can write files, write your whole answer to that path and reply only "saved".
- Otherwise, put your **entire** answer inside **one** code block that opens with ````markdown (four
  backticks) and whose first line is `<!-- save as videos/{{SLUG}}/drafts/1-ideas-gemini.md -->`.
  Nothing outside the block.

## Output format (strict)

```
## IDEA 1
FRAME: A | B
TITLE_EN: <working title>
SPINE: <the one question the whole episode keeps asking and never fully answers>
CENTRAL: <species> · <one visible canon trait of the central animal, prefer Shiny> — <why that trait carries the story>
ARC: <5–8 lines, one per act, from the first strange sight to the unanswered ending>
CANON:
- <claim> — <source>
EARTH:
- <real Earth species>: <what it shows> (at most 3)
COST: <the main ability and what it costs the animal>
FREEZE: <1–2 moments worth freezing on, and the body part to examine>
HOOK: <thumbnail line, ≤ 5 words>
RISK: <what is thin, unsure or might break a rule>
```

Then `## IDEA 2` … `## IDEA 6`, and finally:

```
## MY PICK
<which idea you would make, and why, in 3 lines>
```
