def write_srt(segments, original_audio_path, output_folder="output"):
    import os
    os.makedirs(output_folder, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(original_audio_path))[0]
    srt_path = os.path.join(output_folder, f"{base_name}.srt")

    def format_timestamp(seconds):
        hrs, rem = divmod(int(seconds), 3600)
        mins, secs = divmod(rem, 60)
        millis = int((seconds - int(seconds)) * 1000)
        return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"

    with open(srt_path, "w", encoding="utf-8") as srt_file:
        for i, segment in enumerate(segments, start=1):
            start = format_timestamp(segment["start"])
            end = format_timestamp(segment["end"])
            text = segment["text"].strip()
            srt_file.write(f"{i}\n{start} --> {end}\n{text}\n\n")

    print(f"[INFO] SRT file saved to: {srt_path}")
    return srt_path  # ✅ ESTA LINHA É ESSENCIAL!
