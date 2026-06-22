#!/usr/bin/env python3
"""Transcribe los 6 videos prioritarios de alto valor. 4 workers (8 cores)."""
import concurrent.futures as cf
import subprocess
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent
AUDIO_DIR = BASE / "audio"
TRANS_DIR = BASE / "transcripciones"
TRANS_DIR.mkdir(exist_ok=True)
WORKER = BASE / "_one.py"

PRIORITY = [
    "N3-L2mO5trX3io",   # Blanchard - 5 Mistakes 2026
    "N3-K0fHu6FivH4",   # Blanchard - Find Winning Offers
    "N3-HSZGl6JNoa8",   # Joel - $20K/20 dias
    "N3-SH71IXrbp-A",   # Param - $100/day build en vivo
    "N2-26x8v-Lmzq0",   # Thomas Owen - $7500/11 dias caso
    "N2-_-OnRxjaWMM",   # Thomas Owen - Scale $10K/day Meta
]


def run_one(stem):
    m4a = str(AUDIO_DIR / f"{stem}.m4a")
    out = str(TRANS_DIR / f"{stem}.txt")
    if Path(out).exists():
        return ("skip", stem, "0s", "")
    start = time.time()
    try:
        r = subprocess.run(
            [sys.executable, str(WORKER), m4a, out],
            capture_output=True, text=True, timeout=3000,
        )
        el = int(time.time() - start)
        if r.returncode == 0 and Path(out).exists():
            return ("ok", stem, f"{el}s", "")
        return ("fail", stem, f"{el}s", (r.stderr or r.stdout)[-200:])
    except subprocess.TimeoutExpired:
        return ("fail", stem, "timeout", "50min exceeded")
    except Exception as e:
        return ("fail", stem, "err", str(e)[:120])


def main():
    print(f"=== {len(PRIORITY)} videos prioritarios | workers=2 ===", flush=True)
    done = fail = 0
    with cf.ThreadPoolExecutor(max_workers=2) as ex:
        futs = {ex.submit(run_one, s): s for s in PRIORITY}
        for f in cf.as_completed(futs):
            st, name, t, err = f.result()
            icon = {"ok": "OK ", "skip": "SKIP", "fail": "FAIL"}[st]
            msg = f"  [{icon}] {name} ({t})"
            if err:
                msg += f" | {err}"
            print(msg, flush=True)
            if st in ("ok", "skip"):
                done += 1
            else:
                fail += 1
    print(f"\n=== Completo. OK/SKIP={done} FAIL={fail} ===", flush=True)


if __name__ == "__main__":
    main()
