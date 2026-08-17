"""Render captured terminal logs (submission/*.log) into terminal-style PNGs.

Helper for the submission evidence, not part of the graded starter kit.

    python scripts/render_evidence.py            # render every submission/*.log
    python scripts/render_evidence.py a.log b.log

Each PNG is a faithful picture of the log file next to it; the logs themselves
are the real captured stdout of the lab commands.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SUBMISSION = ROOT / "submission"

BG = (14, 17, 23)
FG = (222, 226, 230)
DIM = (128, 138, 150)
GREEN = (86, 211, 100)
RED = (248, 108, 108)
CYAN = (86, 182, 224)
YELLOW = (230, 192, 96)

FONT_CANDIDATES = (
    r"C:\Windows\Fonts\consola.ttf",
    r"C:\Windows\Fonts\CascadiaMono.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/System/Library/Fonts/Menlo.ttc",
)

FONT_SIZE = 16
PAD = 24
TITLE_H = 34


def load_font() -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, FONT_SIZE)
    return ImageFont.load_default(FONT_SIZE)


def line_color(line: str) -> tuple[int, int, int]:
    low = line.casefold()
    if "pass" in low or "[ok]" in low or "absent: true" in low or "remaining: 0" in low:
        return GREEN
    if "fail" in low or "error" in low or "missing" in low:
        return RED
    if line.startswith("$"):
        return CYAN
    if low.startswith(("|", "+", "-", "=")):
        return DIM
    if "warn" in low:
        return YELLOW
    return FG


def render(log_path: Path) -> Path:
    lines = log_path.read_text(encoding="utf-8", errors="replace").splitlines() or [""]
    font = load_font()

    probe = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(probe)
    char_w = draw.textlength("M", font=font)
    line_h = FONT_SIZE + 6

    width = int(PAD * 2 + char_w * max(len(x) for x in lines)) + 8
    width = max(width, 720)
    height = PAD * 2 + TITLE_H + line_h * len(lines)

    img = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(img)

    # Title bar with the usual three dots so it reads as a terminal window.
    draw.rectangle([0, 0, width, TITLE_H], fill=(30, 35, 44))
    for i, dot in enumerate(((255, 95, 86), (255, 189, 46), (39, 201, 63))):
        cx = 18 + i * 20
        draw.ellipse([cx - 6, TITLE_H // 2 - 6, cx + 6, TITLE_H // 2 + 6], fill=dot)
    draw.text((90, TITLE_H // 2 - FONT_SIZE // 2), log_path.name, font=font, fill=DIM)

    y = TITLE_H + PAD
    for line in lines:
        draw.text((PAD, y), line, font=font, fill=line_color(line))
        y += line_h

    out = log_path.with_suffix(".png")
    img.save(out)
    return out


def main() -> None:
    args = sys.argv[1:]
    paths = [Path(a) for a in args] if args else sorted(SUBMISSION.glob("*.log"))
    if not paths:
        raise SystemExit(f"No log files found in {SUBMISSION}")
    for path in paths:
        if not path.is_absolute():
            path = ROOT / path
        print(render(path))


if __name__ == "__main__":
    main()
