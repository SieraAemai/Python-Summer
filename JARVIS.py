import os
import sys
import webbrowser
import openai
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv as ld
import os.path


engine = pyttsx3.init()

def ai_response(my_task):
    copletion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo"
        , messages=[{"role": "user", "content": my_task}]
    )
    return copletion

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    ld(dotenv_path)
openai.api_key = os.getenv("api_key")

def talk(words):
    print(words)
    engine.say(words)
    engine.runAndWait()


talk("Привет")

r = sr.Recognizer()
def command():
    global r
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
    global r
    if ("открой" and "сайт") in ar_task:
        talk("Хорошо")
        url = "https://ituniver.com"
        webbrowser.open(url)
    elif "пока" in ar_task:
        talk("До встречи.")
        sys.exit()
    elif "имя" in ar_task:
        talk("Меня зовут Джарвис")
    else:
        try:
            ai_res = ai_response("Отвечай на русском. "+ar_task).choices[0].message.content
            talk(ai_res)
        except openai.error.ServiceUnavailableError:
            talk("Появилась ошибка. Пробую обработать запрос еще раз.")
            try:
                ai_res = ai_response(ar_task).choices[0].message.content
                talk(ai_res)
            except openai.error.ServiceUnavailableError:
                talk("Не получается обработать запрос. Спроси еще раз.")
        except openai.error.RateLimitError:
                talk("Попробуй еще раз через 20 секунд.")
                r.pause_threshold = 20
        except:
                talk("Упс. Что-то пошло не так. Попробуй еще раз")



while True:
    make_something(command())