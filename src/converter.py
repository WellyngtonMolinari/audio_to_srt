import os
from pydub import AudioSegment

def convert_to_wav(input_path: str, output_dir: str = "audio") -> str:
    """
    Converts an input audio file to WAV format using pydub.
    
    Args:
        input_path (str): Path to the input audio file.
        output_dir (str): Directory to save the converted .wav file.
    
    Returns:
        str: Path to the output .wav file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_dir, f"{filename}.wav")

    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format="wav")
    print(f"[INFO] Converted '{input_path}' to WAV at '{output_path}'")
    return output_path
