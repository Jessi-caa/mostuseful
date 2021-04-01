# importing speech recognition package from google api
import string

import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import wolframalpha  # to calculate strings into formula
from selenium import webdriver  # to control browser operation
import wikipedia
import webbrowser
import datetime


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)




def takeCommand():
    def query():

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening...')
            audio = r.listen(source)
            query = " "

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}")

    except sr.UnknownValueError:
        print("say that again please.")
    except sr.RequestError:
        print('Sorry,my speech services is down')

        return "None"
    return query


query = takeCommand().lower()

if "hello" in query:
    speak("hello how are you?")
elif "what is your name" in query:
    speak("My name is Jessica")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good  morning!")

    elif hour >= 12 and hour <= 18:
        speak("Good  afternoon!")

    else:
        speak("Good  evening!")


if __name__ == '__main__':
    speak("Hello i am Jessica how may i help you")
    wishMe()

    query = takeCommand().lower()

    while True:

        if "in wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("what should i search in google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
