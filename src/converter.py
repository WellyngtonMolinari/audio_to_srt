import os
import shutil
import time
from pydub import AudioSegment

def convert_to_wav(input_path, output_folder="audio"):
    ext = os.path.splitext(input_path)[1].lower()
    
    # Garante que a pasta existe
    os.makedirs(output_folder, exist_ok=True)

    # Timestamp para evitar sobrescrever
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_folder, f"{base_name}_{timestamp}.wav")

    # Se já for .wav, apenas copia
    if ext == ".wav":
        shutil.copy(input_path, output_path)
        print(f"[INFO] Copied WAV file to: {output_path}")
        return output_path

    print(f"[INFO] Converting '{input_path}' to WAV at '{output_path}'")
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format="wav")
    return output_path
