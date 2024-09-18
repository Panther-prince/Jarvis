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

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Text-to-speech output"""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Greets the user based on the current time"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak('I am Jarvis. How can I assist you, sir?')

def takeCommand():
    """Listens to the user's voice command and converts it to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'You said: {query}\n')
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please repeat.")
        speak("Sorry, I didn't catch that. Please repeat.")
        return "None"
    except sr.RequestError:
        print("Could not request results. Check your network connection.")
        speak("Could not request results. Check your network connection.")
        return "None"

def sendEmail(to, content):
    """Placeholder function to send emails"""
    # You can implement sending emails using smtplib here
    try:
        # Example code to send email using SMTP
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.starttls()
        # server.login('your-email@gmail.com', 'your-password')
        # server.sendmail('your-email@gmail.com', to, content)
        # server.close()
        speak("Email has been sent!")
    except Exception as e:
        print("Sorry, email could not be sent.", e)
        speak("Sorry, I could not send the email.")

def performCalculation():
    """Takes a mathematical expression as voice input and evaluates it"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak a mathematical expression:")
        speak("Speak a mathematical expression:")
        audio = r.listen(source)
    
    try:
        expression = r.recognize_google(audio)
        print(f"You said: {expression}")
        result = eval(expression)  # Use eval safely in limited contexts
        print(f"Result: {result}")
        speak(f"The result is {result}")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        speak("Sorry, I didn't understand that.")
    except sr.RequestError:
        print("Could not process the request.")
        speak("Could not process the request.")
    except Exception as e:
        print("Error in calculation:", e)
        speak("There was an error. Please try again.")

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
            music_dir = 'C:\\Users\\PRINCE\\OneDrive\\Desktop\\project\\music_a'
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            print(f"Playing: {random_song}")
            os.startfile(os.path.join(music_dir, random_song))

        elif 'the time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Current time: {current_time}")
            speak(f"Sir, the time is {current_time}")

        elif 'open code' in query:
            code_path = "C:\\Users\\PRINCE\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'ravalprince50@gmail.com'  # Receiver email address
                sendEmail(to, content)
            except Exception as e:
                print("Sorry, I could not send the email.", e)
                speak("Sorry, I could not send the email.")

        elif 'exit' in query:
            speak("Goodbye, sir!")
            exit()

        elif 'thank you' in query:
            speak("You're welcome, sir!")

        elif 'ok jarvis' in query:
            speak("Yes, sir!")

        elif 'calculate' in query or 'calculator' in query:
            performCalculation()

        elif 'how are you jarvis' in query:
            speak("I'm doing well, sir. Thank you for asking.")

        elif 'hello' in query:
            speak("Hello, sir!")
