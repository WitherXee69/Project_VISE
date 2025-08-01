from Data.Imports.local_imports import *
from Data.Imports.global_imports import *
from Data.Speak_All.speak_print_only import speak

sorry_quatus = ["I'm so sorry sir!", "Next time I will do my best", "i am sorry sir", "", ""]


def sorry():
    sorry_phase = random.choice(sorry_quatus)
    speak(sorry_phase)
