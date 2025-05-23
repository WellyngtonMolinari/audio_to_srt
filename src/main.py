import os
from converter import convert_to_wav
from transcriber import load_model, transcribe_audio
from srt_writer import write_srt

def main():
    # === Input configuration ===
    input_audio = "audio/exemplo.mp3"  # Change to your audio file
    model_size = "base"
    output_srt = os.path.join("output", "exemplo.srt")

    # === Step 1: Convert to WAV ===
    wav_path = convert_to_wav(input_audio)

    # === Step 2: Load Whisper Model ===
    model = load_model(model_size)

    # === Step 3: Transcribe Audio ===
    segments = transcribe_audio(model, wav_path)

    # === Step 4: Write SRT File ===
    if not os.path.exists("output"):
        os.makedirs("output")
    write_srt(segments, output_srt)

if __name__ == "__main__":
    main()
