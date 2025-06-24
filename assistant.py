#Importing Libraries
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys

#Initializing the speech engine for text-to-speech
engine = pyttsx3.init()

#Function Speak the text function
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Arrays with some common commands:
greetings = ['hi', 'hello', 'hey']
salam = ['aoa', 'assalamalaikum', 'assalam o alaikum']
byes = ['bye','exit', 'quit']

#User Input voice command Function
def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that, can you repeat please.")
            return None
        except sr.RequestError:
            print("Network Error.")
            return None
    return command.lower()

#Respond to Command Function
def respond(command):
    
    if any(greet in command for greet in greetings):
        speak(" Hello! How can i assist you today?")

    elif any(word in command for word in salam):
        speak("Walaikum Assalam! How can I assist you today?")

    elif 'search' in command:
        speak("What would you like to search for?")

        search_query = take_command()

        if search_query:
            speak(f"Searching for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
    
    elif 'open' in command:
        if 'chrome' in command:
            speak("Opening Chrome")
            os.system("start chrome")
        elif 'calculator' in command:
            speak("Opening Calculator")
            os.system("start calc")
        elif 'notepad' in command:
            speak("Opening Notepad")
            os.system("start notepad")
    
    elif any(word in command for word in byes):
        speak("Goodbye! Have a great day.")
        sys.exit()

    else:
        speak("Sorry, I do not know the command.")

#Main function to run the assistant
def run_assistant():
    speak("Hello, I am your assistant. How can i help you today?")

    while True:
        command = take_command()
        if command:
            respond(command)
            
run_assistant()