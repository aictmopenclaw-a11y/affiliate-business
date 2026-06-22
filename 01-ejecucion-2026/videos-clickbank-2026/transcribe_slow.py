#!/usr/bin/env python3
"""Transcribe TODOS los pendientes, 1 worker, lento pero seguro. Para correr con nohup."""
import glob
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
        if not (TRANS_DIR / f"{stem}.txt").exists():
            pend.append((m4a, str(TRANS_DIR / f"{stem}.txt"), stem))
    return pend


def main():
    pend = find_pending()
    print(f"=== {len(pend)} pendientes | 1 worker (lento/seguro) ===", flush=True)
    done = fail = 0
    for m4a, out, name in pend:
        start = time.time()
        try:
            r = subprocess.run(
                [sys.executable, str(WORKER), m4a, out],
                capture_output=True, text=True, timeout=9000,
            )
            el = int(time.time() - start)
            if r.returncode == 0 and Path(out).exists():
                print(f"  [OK ] {name} ({el}s)", flush=True)
                done += 1
            else:
                print(f"  [FAIL] {name} ({el}s) | {(r.stderr or r.stdout)[-200:]}", flush=True)
                fail += 1
        except subprocess.TimeoutExpired:
            print(f"  [FAIL] {name} (timeout 150min)", flush=True)
            fail += 1
        except Exception as e:
            print(f"  [FAIL] {name} | {str(e)[:120]}", flush=True)
            fail += 1
    print(f"\n=== Completo. OK={done} FAIL={fail} ===", flush=True)


if __name__ == "__main__":
    main()
