import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty("voices")

for voice in voices:
    print("------")
    print(f"Name: {voice.name}")
    print(f"ID: {voice.id}")
    print(f"Language: {voice.languages}")
    print(f"Gender: {voice.gender}")
    print(f"Age: {voice.age}")
