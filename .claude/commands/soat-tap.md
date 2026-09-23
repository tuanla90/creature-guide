---
description: Soát một tập trước khi thu giọng hoặc render — máy soát trước, rồi soát tay phần máy không thấy
argument-hint: <slug, vd kanto-001-bulbasaur>
---

Soát tập **$ARGUMENTS** trước khi thu giọng / render.

**Bước 1 — máy soát.** Chạy:

```bash
PYTHONUTF8=1 python tools/check-episode.py $ARGUMENTS
```

Sửa hết ✗. Với mỗi ⚠, nói rõ là sửa hay cố ý bỏ qua và vì sao — không được lướt.

**Bước 2 — soát tay.** Đọc `content.py` và `scenes.json` của tập, đối chiếu
`.claude/skills/creature-field-guide-scriptwriter/references/episode-checklist.md`. Tập trung vào
những thứ máy không thấy được:

- Câu chuyện có sức ép và hạn chót thật không, hay chỉ là một chuỗi sự thật xếp cạnh nhau.
- Mỗi cái tên có **đến sau** quan sát không, và cái dấu tích ấy có shot riêng không.
- Cảnh tiến hoá có đúng luật không: không lột da, chỉ sưng nở, sức nặng, ánh sáng, dấu vết.
- Mỗi khả năng có nêu **cái giá** không.
- Có chỗ nào giả thuyết bị kể như sự thật, hay canon bị kể thiếu nguồn.
- Nhịp: có đoạn nào ba bốn moment liên tiếp dưới hai giây không.
- Bản 9:16: chữ có tràn, cảnh rộng có chết không.

**Bước 3 — báo cáo.** Một bảng ngắn: chặng nào của `docs/PIPELINE.md` đã qua cổng, chặng nào chưa,
và việc kế tiếp là gì. Đừng render nếu còn ✗.
