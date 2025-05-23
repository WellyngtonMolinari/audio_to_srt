def format_timestamp(seconds: float) -> str:
    """
    Converts seconds to SRT timestamp format: HH:MM:SS,mmm

    Args:
        seconds (float): Time in seconds.

    Returns:
        str: Formatted timestamp.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


def write_srt(segments: list, output_path: str):
    """
    Writes a list of transcription segments to a .srt file.

    Args:
        segments (list): List of dicts with 'start', 'end', 'text'.
        output_path (str): Path to save the .srt file.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        for index, segment in enumerate(segments, start=1):
            start_time = format_timestamp(segment["start"])
            end_time = format_timestamp(segment["end"])
            text = segment["text"].strip()

            f.write(f"{index}\n")
            f.write(f"{start_time} --> {end_time}\n")
            f.write(f"{text}\n\n")

    print(f"[INFO] SRT file saved to: {output_path}")
