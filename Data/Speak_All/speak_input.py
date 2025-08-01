from Data.Imports.global_imports import *

engine = pyttsx3.init('sapi5')

rate = engine.getProperty('rate')
engine.setProperty('rate', 140)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speakIN(audio):
    input('Vise: ' + audio)
    engine.say(audio)
    engine.runAndWait()
