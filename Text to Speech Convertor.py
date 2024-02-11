# TEXT TO SPEACH CONVERTOR:

import tkinter as tk
from gtts import gTTS
import os

def generate_speech():
    text = text_box.get("1.0", "end-1c")
    obj = gTTS(text=text, lang = "en")
    obj.save("output.mp3")
    os.system("start output.mp3")

root = tk.Tk()
root.title("Text to Speech Converter")
root.configure(bg="Aqua")
root.geometry("2000x2000")

labl = tk.Label(root, text="Enter the text you want to convert to speech", font=("Arial", 20, "bold"), height=2, width=50, bg="black",fg="white")
labl.pack(padx=5, pady=5)
text_box = tk.Text(root, width=95, height=20,bg="white",font= ("Arial",12,"bold"))
text_box.pack(padx=5, pady=10)

convert_button = tk.Button(root, text="Convert to Speech", command=generate_speech, width=16, height=1, bg="black", fg="white",font =("Arial",14,"bold"))
convert_button.pack(padx=5, pady=10)

root.mainloop()