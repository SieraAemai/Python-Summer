import os
import sys
import webbrowser

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
    with sr.Microphone() as source:
        print("Говори")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        #task = r.recognize_google(audio, language="en-US").lower() #ru-Ru
        task = r.recognize_google(audio, language="ru-RU").lower() #ru-Ru
        print("You: "+task)
    except sr.UnknownValueError:
        talk("Я тебя не понял")
        task = command()
    return task


def make_something(ar_task):
    if ("открой" and "сайт") in ar_task:
        talk("Хорошо")
        url = "https://ituniver.com"
        webbrowser.open(url)
    elif "стоп" in ar_task:
        talk("Пока")
        sys.exit()
    elif "имя" in ar_task:
        talk("Меня зовут Джарвис")
while True:
    make_something(command())