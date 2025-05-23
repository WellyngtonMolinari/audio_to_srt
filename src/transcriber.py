import whisper

def load_model(model_size: str = "base"):
    """
    Loads a Whisper model.

    Args:
        model_size (str): Model size to load. Options: tiny, base, small, medium, large.

    Returns:
        whisper.model.Whisper: The loaded model.
    """
    print(f"[INFO] Loading Whisper model: {model_size}")
    model = whisper.load_model(model_size)
    return model


def transcribe_audio(model, audio_path: str) -> list:
    """
    Transcribes audio using Whisper and returns segments with timestamps.

    Args:
        model: Whisper model instance.
        audio_path (str): Path to the .wav audio file.

    Returns:
        list: List of segments containing 'start', 'end', and 'text'.
    """
    print(f"[INFO] Transcribing audio: {audio_path}")
    result = model.transcribe(audio_path, verbose=False)
    segments = result.get("segments", [])
    return segments
