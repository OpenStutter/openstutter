"""Generate test sentences in your cloned voice with Qwen3-TTS (MLX).

Usage:
    python try_qwen.py REF_WAV "exact transcript of REF_WAV" [--model ID] [--outdir out]

Then listen to the files in ./out and judge: does it sound like you, and is
it natural enough to put in front of a listener?
"""
import argparse
import pathlib
import time

import numpy as np
import soundfile as sf
from mlx_audio.tts.utils import load_model

# Phonetically varied + realistic work-call sentences, including "feared"
# words (Twitter/Cloudflare) so we hear how the clone handles them.
TEST_SENTENCES = {
    "01_greeting": "Hi, this is my OpenStutter voice. How does it sound to you?",
    "02_work": "Yesterday I completed the payment integration ticket and noticed a performance regression.",
    "03_question": "Could you walk me through how the deployment pipeline works right now?",
    "04_emphatic": "This is exactly the result we wanted. Great work, everyone.",
    "05_names": "I was on a call with Cloudflare and someone from the Twitter team about the outage.",
    "06_pangram": "The quick brown fox jumps over the lazy dog while five boxing wizards jump.",
}


def to_numpy(audio):
    return np.asarray(audio, dtype=np.float32)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ref_wav")
    ap.add_argument("ref_text")
    ap.add_argument("--model", default="mlx-community/Qwen3-TTS-12Hz-0.6B-Base-bf16")
    ap.add_argument("--outdir", default="out")
    args = ap.parse_args()

    out = pathlib.Path(args.outdir)
    out.mkdir(exist_ok=True)

    print(f"Loading model: {args.model}")
    t0 = time.time()
    model = load_model(args.model)
    print(f"Model loaded in {time.time() - t0:.1f}s")

    for name, text in TEST_SENTENCES.items():
        t0 = time.time()
        results = list(
            model.generate(text=text, ref_audio=args.ref_wav, ref_text=args.ref_text)
        )
        seg = results[0]
        audio = to_numpy(seg.audio)
        sr = getattr(seg, "sample_rate", None) or 24000
        path = out / f"{name}.wav"
        sf.write(str(path), audio, sr)
        gen = time.time() - t0
        dur = len(audio) / sr
        rtf = gen / dur if dur else float("inf")
        print(f"{name}: {dur:4.1f}s audio in {gen:5.1f}s (RTF {rtf:.2f}) -> {path}")

    print(f"\nDone. Open the files in {out}/ and judge clone quality.")


if __name__ == "__main__":
    main()
