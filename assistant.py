import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import pyautogui

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio).lower()
        except:
            speak("Sorry, I didn't catch that.")
            return ""

def execute_command(command):
    if "open" in command and "notepad" in command:
        os.system("notepad.exe")
        speak("Opening Notepad")
    elif "open" in command and "chrome" in command:
        os.system("start chrome")
        speak("Opening Chrome")
    elif "open" in command and "documents" in command:
        os.startfile("C:\\Users\\YourUsername\\Documents")
        speak("Opening Documents folder")
    elif "search" in command:
        query = command.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}")
    elif "type" in command:
        text = command.replace("type", "")
        pyautogui.typewrite(text)
        speak(f"Typed {text}")
    elif "screenshot" in command:
        pyautogui.screenshot("screenshot.png")
        speak("Screenshot taken and saved.")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't understand that command yet.")

# Main loop
try:
    # your main logic
    if __name__ == "__main__":
        while True:
            command = listen()
            execute_command(command)
except Exception as e:
    print(f"Error: {e}")
