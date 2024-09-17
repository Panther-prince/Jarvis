import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import requests
from googlesearch import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
voice = engine.setProperty('voice',voices[0].id)

def calculator(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        return "Invalid operator"
    
    return result

def sendEmail(to, contant):
    pass

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():

    hours = int(datetime.datetime.now().hour)
    if hours >0 and hours<12:
        speak("Good Morning")
    elif hours >12 and  hours <18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak('I am Jarvis,How can i help you sir?')
    

def takeCommand():    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        speak("recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f'you said : {query}\n')
    
    except Exception as e:
        #print(e)
        print("Srrory, Say Again...")
        speak("Srrory, Say Again...")

        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            l1 =[0,1]
            ran = random.choice(l1)
            print(ran)
            music = 'C:\\Users\\PRINCE\\OneDrive\\Desktop\\project\\music_a'
            song = os.listdir(music)
            print(song)
            os.startfile(os.path.join(music,song[ran]))
        
        elif 'the time' in query:
            time =  datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(f"sir the time is {time}")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\PRINCE\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to' in query:
            try:
                speak("What you want to said?")
                to = 'ravalprince50@gmail.com'
                contant =  takeCommand()
                print(contant)
                sendEmail(to,contant)
                speak("Email has been sent!")
            except Exception as e:
                print("Sorry Please Email is Not Sent")
                speak("Sorry Please Email is Not Sent")

        elif 'exit' in query:
            exit()
        
        # elif 'what'or 'who'in query:
        #     speak('Searching on Google.....')
        #     query = query.replace('google','')
        #     for url in query.range(0,2):
        #         print(url)
            
        elif 'thank you' in query:
            print('welcome sir')
            speak('welcome sir')

        elif 'ok jarvis' in query:
            print('yes sir')
            speak('yes sir')

        elif 'calculate' or 'calculator' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak a mathematical expression:")
                audio = r.listen(source)
            try:
                # Recognize speech using Google Speech Recognition
                expression = r.recognize_google(audio)
                print("You said:", expression)

                # Evaluate the expression
                result = eval(expression)
                print("Result:", result)
                speak('Answer'+str(result))

            except sr.UnknownValueError:
                print("Speech recognition could not understand audio")
                speak("Speech recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service:", e)
                speak("Could not request results from Google Speech Recognition service:", e)
            except Exception as e:
                print("Error:", e)
                speak("Invailid expression try again")
            
        elif 'how are you jarvis' in query:
            print("i am nice")
            speak("i am nice")

        elif 'hello' in query:
            print("hello sir")
            speak("hello sir")


