# Ghi chú bằng chứng

## Các file

| File | Nội dung |
| --- | --- |
| `long_term.{log,png}` | `--only-layer long_term` → E02, E03, E08, E09 PASS |
| `episodic.{log,png}` | `--only-layer episodic` → E04, E05 PASS |
| `semantic.{log,png}` | `--only-layer semantic` → E06, E11 PASS |
| `privacy.{log,png}` | `src.forget` + `--verify-only` + kiểm tra retrieval sau khi xoá |
| `benchmark_student.{log,png}` | Full run 11/11, sinh ra `reports/benchmark.*` |
| `smoke.{log,png}` | Redis / Qdrant / dataset / `ZEP_API_KEY` |
| `seed.log`, `reseed.log` | Seed trước benchmark, và seed lại sau privacy drill |

## Cách tạo ảnh

Các `.png` **không phải ảnh chụp màn hình OS**. Chúng được render 1-1 từ chính file `.log`
đặt cạnh nó bằng `scripts/render_evidence.py` (Pillow, font Consolas). Nội dung `.log` là
stdout thật của các lệnh, ghi lại bằng `tee` lúc chạy — không chỉnh sửa thủ công.
File `.log` là nguồn gốc, `.png` chỉ để dễ xem.

## Thứ tự chạy

Toàn bộ report trong `reports/` được sinh bằng đúng lệnh Docker của lab:

```bash
docker compose build
docker compose up -d redis qdrant
docker compose run --rm app pytest -q          # 11 passed, 1 skipped
docker compose run --rm app python -m src.smoke
docker compose run --rm app python -m src.seed

docker compose run --rm app python -m src.evaluate --impl student --reuse-seeded --only-layer long_term
docker compose run --rm app python -m src.evaluate --impl student --reuse-seeded --only-layer episodic
docker compose run --rm app python -m src.evaluate --impl student --reuse-seeded --only-layer semantic
docker compose run --rm app python -m src.evaluate --impl student --reuse-seeded   # ghi reports/benchmark.*
docker compose run --rm app python -m src.evaluate --impl no_memory
docker compose run --rm app python -m src.compare_reports
```

Lưu ý: `--only-layer` cũng ghi đè `reports/benchmark.json`, nên full run luôn chạy **sau**
ba lệnh per-layer.

Privacy drill chạy **sau** khi đã lưu `reports/benchmark.*`, rồi seed lại để graph sẵn sàng:

```bash
docker compose run --rm app python -m src.forget --user-id minh-lab17
docker compose run --rm app python -m src.forget --user-id minh-lab17 --verify-only
docker compose run --rm app python -m src.seed
```

Hai lệnh forget và các log `seed/reseed/privacy` được chạy bằng venv trên host (lúc đó
image `app` chưa build được do mạng đứt khi pip tải `pyarrow`), với
`REDIS_URL=redis://localhost:6379/0` và `QDRANT_URL=http://localhost:6333` vì Redis/Qdrant
expose ra localhost. Code và kết quả không khác gì chạy trong container.

Không sửa file starter kit nào ngoài `src/memory_student.py`. File mới duy nhất được thêm
là `scripts/render_evidence.py` (chỉ dùng để vẽ ảnh, không nằm trong đường chấm điểm).
