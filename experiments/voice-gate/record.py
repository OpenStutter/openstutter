"""Record a reference voice clip from the default input device.

Usage:
    python record.py [output.wav]

Press Enter to start, Enter again to stop. macOS will prompt for mic
permission the first time — allow it for your terminal app.
"""
import sys
import threading

import numpy as np
import sounddevice as sd
import soundfile as sf

SR = 24000
out = sys.argv[1] if len(sys.argv) > 1 else "reference.wav"

dev = sd.query_devices(kind="input")
print(f"Input device: {dev['name']}")
input("Press Enter to START recording...")
print("Recording... press Enter to STOP.")

frames = []


def cb(indata, _frames, _time, status):
    if status:
        print(status, file=sys.stderr)
    frames.append(indata.copy())


stop = threading.Event()
threading.Thread(target=lambda: (input(), stop.set()), daemon=True).start()

with sd.InputStream(samplerate=SR, channels=1, dtype="float32", callback=cb):
    while not stop.is_set():
        sd.sleep(100)

audio = np.concatenate(frames, axis=0) if frames else np.zeros((1, 1), dtype="float32")
sf.write(out, audio, SR, subtype="PCM_16")
dur = len(audio) / SR
peak = float(np.max(np.abs(audio))) if len(audio) else 0.0
print(f"Saved {out}: {dur:.1f}s, peak amplitude {peak:.3f}")
if peak < 0.02:
    print("WARNING: very low level — mic may not be capturing. Check input/permissions.")
