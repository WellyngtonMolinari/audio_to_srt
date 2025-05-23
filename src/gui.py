import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import threading

from converter import convert_to_wav
from transcriber import load_model, transcribe_audio_with_progress
from srt_writer import write_srt

class AudioToSRTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio to SRT Converter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Model selection
        tk.Label(root, text="Choose Whisper model:").pack(pady=5)
        self.model_var = tk.StringVar(value="base")
        model_menu = tk.OptionMenu(root, self.model_var, "tiny", "base", "small", "medium", "large")
        model_menu.pack()

        # Select audio file
        self.select_button = tk.Button(root, text="Select Audio File", command=self.select_file)
        self.select_button.pack(pady=10)

        # Progress bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        # Status label
        self.status_label = tk.Label(root, text="Awaiting file selection...", fg="blue")
        self.status_label.pack(pady=5)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[
            ("Audio Files", "*.mp3 *.wav *.m4a *.flac *.ogg"),
            ("All files", "*.*")
        ])
        if file_path:
            threading.Thread(target=self.process_audio, args=(file_path,), daemon=True).start()

    def update_status(self, message, color="black"):
        self.status_label.config(text=message, fg=color)
        self.root.update_idletasks()

    def update_progress(self, current, total):
        self.progress["maximum"] = total
        self.progress["value"] = current
        percent = int((current / total) * 100)
        self.update_status(f"Transcribing... {percent}%", color="black")

    def process_audio(self, file_path):
        try:
            self.update_status("Converting to WAV (if needed)...")
            self.progress["value"] = 0
            wav_path = convert_to_wav(file_path)

            self.update_status("Loading Whisper model...")
            model = load_model(self.model_var.get())

            self.update_status("Transcribing audio...")
            result = transcribe_audio_with_progress(model, wav_path, progress_callback=self.update_progress)

            # Limita legendas a 4 segundos por trecho
            from transcriber import split_long_segments
            result["segments"] = split_long_segments(result["segments"], max_duration=4.0)

            detected_lang = result.get("language", "unknown")
            self.update_status(f"Transcription complete. Language: {detected_lang}", color="green")

            self.update_status("Writing SRT file...")
            srt_path = write_srt(result["segments"], wav_path)

            self.update_status(f"SRT saved at: {srt_path}", color="green")
            messagebox.showinfo("Success", f"Transcription completed!\n\nSRT saved at:\n{srt_path}")

        except Exception as e:
            self.update_status("Error during transcription", color="red")
            messagebox.showerror("Error", str(e))
    

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioToSRTApp(root)
    root.mainloop()
