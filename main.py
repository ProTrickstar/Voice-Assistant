import json
import sys
from time import time
from types import new_class
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from requests import get
import sys
from pywikihow import search_wikihow
import pywhatkit as kit
import pyjokes
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('swastiksinghwhitehat@gmail.com', 'soham_07')
    server.sendmail('swastiksinghwhitehat@gmail.com', to, content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis sir, Please Tell me how may i help you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1.2)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

    def search_wikihow(query, max_results=10, lang='en'):
        return list(WikiHow.search(query, max_results, lang))

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            speak("Opening Stack Overflow...")
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            speak("Opening Instagram...")
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            speak("Playing Music...")
            music_dir = 'G:\\song\\kick'
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            print(strTime)

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shut down' in query:
            speak("Computer Shut Down Initiated")
            os.system("shutdown /s /t 5")

        elif 'restart' in query:
            speak("Restarting Computer")
            os.system("shutdown /r /t 5")

        elif 'sleep' in query:
            speak("As you say sir")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'very bad joke' in query:
            speak("Ok, Here's another one")
            speak(joke)

        elif 'open code' in query:
            speak("Opening VS CODE")
            codePath = "C:\\Users\\admin\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            # time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'open notepad' in query:
            speak("Opening Notepad")
            codePath1 = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(codePath1)

        elif 'close notepad' in query:
            speak("Ok sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'close code' in query:
            speak("Ok sir, closing VS CODE")
            os.system("taskkill /f /im code.exe")

        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn==14:
                music_dir = 'C:\\Users\\admin\\Downloads\\Music\\Alarm'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "codingbashbusiness@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am unable to send this mail")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP adress is {ip}")
            print(ip)

        elif 'where am i' in query:
            speak("Wait sir let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = "https://www.geojs.io/v1/ip/geo" +ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Sir i am not sure, but i think we are in {city}, {country}")
            except Exception as e:
                speak("Sorry sir, due to network issue i am unable to find where we are")
                pass

        elif 'send message to swayam' in query:
            kit.sendwhatmsg("+918219415958", "Hello Rabbit!",12,24)

        elif 'activate how to do mode' in query:
                speak("How to do mode has been activated, please tell me what do you want to know")
                how = takeCommand()
                max_resuls = 1
                how_to = search_wikihow(how, max_resuls)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)

                speak("How to do mode has been deactivated")
            
        elif 'quit' in query:
            speak("Thanks for using me sir, have a good day")
            sys.exit()    