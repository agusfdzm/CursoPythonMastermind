import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

engine.setProperty("voice", "spanish")

engine.say("Hola")
engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Puedes hablar")
    audio = r.listen(source)
    text = r.recognize_google(audio, language="es-ES")
    print(text)