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


def transcribe_audio(model, audio_path: str) -> dict:
    """
    Transcribes audio using Whisper and returns the full result.

    Args:
        model: Whisper model instance.
        audio_path (str): Path to the .wav audio file.

    Returns:
        dict: Transcription result including 'segments' and 'language'.
    """
    print(f"[INFO] Transcribing audio: {audio_path}")
    result = model.transcribe(audio_path)
    return result


def transcribe_audio_with_progress(model, audio_path: str, progress_callback=None) -> dict:
    """
    Transcribes audio with simulated progress feedback.

    Args:
        model: Whisper model instance.
        audio_path (str): Path to the .wav audio file.
        progress_callback (callable): Optional callback for progress updates: (current_step, total_steps).

    Returns:
        dict: Transcription result including 'segments' and 'language'.
    """
    print(f"[INFO] Transcribing audio with progress: {audio_path}")
    result = model.transcribe(audio_path, verbose=False)

    segments = result.get("segments", [])
    total = len(segments)

    if progress_callback:
        for i, _ in enumerate(segments):
            progress_callback(i + 1, total)

    result["segments"] = segments
    return result

