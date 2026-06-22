#!/usr/bin/env python3
"""Worker: transcribe 1 audio -> txt. Uso: _one.py <audio> <out.txt>"""
import sys
from faster_whisper import WhisperModel

audio, out = sys.argv[1], sys.argv[2]

model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=2)
segments, info = model.transcribe(audio, language="en", beam_size=5, vad_filter=True)

lines = []
for seg in segments:
    ts = f"[{int(seg.start//60):02d}:{int(seg.start%60):02d}]"
    lines.append(f"{ts} {seg.text.strip()}")

with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
