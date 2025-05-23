import os
import tkinter as tk
from tkinter import filedialog, messagebox

from converter import convert_to_wav
from transcriber import load_model, transcribe_audio
from srt_writer import write_srt

class AudioToSRTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio to SRT Converter")
        self.root.geometry("400x200")

        self.model_size = "base"
        self.input_file = ""

        self.build_interface()

    def build_interface(self):
        self.label = tk.Label(self.root, text="Select an audio file:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.select_button.pack()

        self.convert_button = tk.Button(self.root, text="Convert to SRT", command=self.process_file, state=tk.DISABLED)
        self.convert_button.pack(pady=20)

    def browse_file(self):
        filetypes = [("Audio files", "*.mp3 *.wav *.mp4"), ("All files", "*.*")]
        file = filedialog.askopenfilename(title="Select Audio File", filetypes=filetypes)
        if file:
            self.input_file = file
            self.convert_button.config(state=tk.NORMAL)
            self.label.config(text=f"Selected: {os.path.basename(file)}")

    def process_file(self):
        try:
            wav_path = convert_to_wav(self.input_file)
            model = load_model(self.model_size)
            segments = transcribe_audio(model, wav_path)

            output_dir = "output"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            filename = os.path.splitext(os.path.basename(self.input_file))[0]
            srt_path = os.path.join(output_dir, f"{filename}.srt")
            write_srt(segments, srt_path)

            messagebox.showinfo("Success", f"SRT file created: {srt_path}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

def run_gui():
    root = tk.Tk()
    app = AudioToSRTApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
