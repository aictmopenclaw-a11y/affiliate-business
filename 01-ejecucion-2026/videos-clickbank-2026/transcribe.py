#!/usr/bin/env python3
"""
Transcripción paralela de los videos ClickBank 2026.
faster-whisper · modelo small · inglés · subprocess fan-out.
"""
import concurrent.futures as cf
import glob
import os
import subprocess
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent
AUDIO_DIR = BASE / "audio"
TRANS_DIR = BASE / "transcripciones"
TRANS_DIR.mkdir(exist_ok=True)
WORKER = BASE / "_one.py"


def find_pending():
    pend = []
    for m4a in sorted(glob.glob(str(AUDIO_DIR / "*.m4a"))):
        stem = Path(m4a).stem
        out = TRANS_DIR / f"{stem}.txt"
        if not out.exists():
            pend.append((m4a, str(out), stem))
    return pend


def run_one(m4a, out, name):
    start = time.time()
    try:
        r = subprocess.run(
            [sys.executable, str(WORKER), m4a, out],
            capture_output=True, text=True, timeout=2400,
        )
        el = int(time.time() - start)
        if r.returncode == 0 and Path(out).exists():
            return ("ok", name, f"{el}s", "")
        return ("fail", name, f"{el}s", (r.stderr or r.stdout)[-200:])
    except subprocess.TimeoutExpired:
        return ("fail", name, "timeout", "40min exceeded")
    except Exception as e:
        return ("fail", name, "err", str(e)[:120])


def main():
    pend = find_pending()
    print(f"=== {len(pend)} audios a transcribir | workers=3 ===", flush=True)
    done = fail = 0
    with cf.ThreadPoolExecutor(max_workers=3) as ex:
        futs = {ex.submit(run_one, *p): p[2] for p in pend}
        for f in cf.as_completed(futs):
            st, name, t, err = f.result()
            icon = "OK " if st == "ok" else "FAIL"
            msg = f"  [{icon}] {name} ({t})"
            if err:
                msg += f" | {err}"
            print(msg, flush=True)
            if st == "ok":
                done += 1
            else:
                fail += 1
    print(f"\n=== Completo. OK={done} FAIL={fail} ===", flush=True)


if __name__ == "__main__":
    main()
