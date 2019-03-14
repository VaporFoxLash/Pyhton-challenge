import os
import pyaudio
import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 4000

print("Say something: ")

with sr.Microphone() as source:
	print("Say something: ")
	audio = r.listen(source)

try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
	print("Sorry couldn't recognize what you said")
