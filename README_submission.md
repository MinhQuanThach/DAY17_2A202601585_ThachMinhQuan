# Lab 17 — Multi-Memory Agent với Zep

**Kết quả:** `--impl student --reuse-seeded` → **11/11 PASS (100%)**; baseline no-memory **2/11 (18.2%)**. Chi tiết: `reports/benchmark.md`, `reports/comparison.md`, `submission/*.png`.

## 3 câu bắt buộc

**1. Layer quan trọng nhất trong bộ test này:** long-term (Zep Context Block). Nó quyết định E02, E03, E08, E09 (20/56 điểm) và là một nửa evidence của E07 — nhiều hơn mọi layer khác.

**2. Trade-off Context Block/Zep vs Redis+Qdrant:** Zep cho sẵn trích xuất fact, `valid_at/invalid_at`, cross-session và user-scope; đổi lại là ingestion bất đồng bộ (phải poll) và latency 1.5–4 s. Redis+Qdrant nhanh mili-giây và tự chủ, nhưng `src/local_baseline.py` cho thấy nó chỉ là KV + TF-IDF: không suy luận fact, không recency/conflict, không provenance — phải tự xây.

**3. Guardrail chống memory poisoning:** (a) `privacy_guard` bắt buộc opt-in và redact email/phone trước khi ghi durable; (b) `prime_eval_thread` dùng `ignore_roles=["user"]` nên query đánh giá không ghi ngược thành fact; (c) heartbeat chỉ dedupe/đánh dấu stale, không tự thêm instruction hay quyền; (d) fact có provenance + validity nên bị supersede thay vì ghi đè; (e) namespace theo `user_id` — E09 xác nhận Lan không nhận `ORCHID-27`.

## 4 câu phân tích benchmark

1. **Hit rate thấp nhất:** không layer nào dưới 100%. Ở baseline no-memory, long_term/episodic/semantic/mixed đều 0%, chỉ short_term 2/2 — evidence của chúng nằm ngoài thread hiện tại.
2. **Nhiều token nhất:** E08 (1484 token), rồi E02 (1477) và E03 (1468) — Context Block luôn kèm USER_SUMMARY + FACTS + ENTITIES.
3. **E07 (mixed):** cần long-term + semantic; evidence bắt buộc là `Python` (preference cá nhân) và `Idempotency-Key` (KB dùng chung). Budget cắt long-term 1486→324 token (trần 320), semantic giữ 148/240.
4. **Token reduction:** memory 14.2% còn no-memory 81.8% nhưng chỉ 18.2% hit rate — không retrieve gì thì reduction gần tuyệt đối. Reduction chỉ có nghĩa khi đọc cùng hit rate.

## E08 recency và E10 compaction

**E08:** fact mới có scope dự án nên `BLUEBIRD-42 → TypeScript/NestJS` thắng preference Python cũ, còn Python vẫn đúng cho `ORCHID-27`. Zep giữ cả hai kèm `valid_at`: recency + scope, không xoá lịch sử.

**E10:** hạ `max_recent_messages` 6→4 làm sliding compaction chạy 12 lần, evict hết turn thô, nhưng `extract_durable_notes` vẫn giữ `REVIEW-DEADLINE-1600 / Friday / 16:00` trong `DURABLE_NOTES`. Buffer giữ mọi thứ nên token tăng tuyến tính và constraint rơi ngay khi cửa sổ tràn.
