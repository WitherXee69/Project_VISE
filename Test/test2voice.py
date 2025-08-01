import speech_recognition as sr
import os
import whisper

r = sr.Recognizer()
with sr.Microphone() as source:
    # ding()
    print("Listening...")
    # r.pause_threshold = 1
    r.energy_threshold = 350
    r.dynamic_energy_threshold = True
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source=source, timeout=20, phrase_time_limit=50000)  # timeout=20 phrase_time_limit=5
    options = {"download_root": "Data/SR_Model/"}
    query = r.recognize_whisper(audio, model="base", load_options=options, language="en")
print(query)
