import os
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()


def talk(words):
    print(words)
    engine.say(words)
    engine.runAndWait()


talk("Привет")

def command():
    r = sr.Recognizer()

command()