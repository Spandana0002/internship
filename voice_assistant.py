import speech_recognition as sr
from gtts import gTTS
import datetime
import webbrowser
import os

# Function to convert text to speech using gTTS
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")  # For macOS, on Windows use 'start' or 'wmplayer'

# Function to listen to the user's voice and recognize the command
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that. Could you please repeat?")
            return None
        except sr.RequestError:
            speak("Sorry, I am unable to connect to the service.")
            return None

        return command.lower()

# Main function to handle commands
def run_voice_assistant():
    speak("Hello, how can I assist you today?")
    
    while True:
        command = listen()

        if command is None:
            continue

        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "play music" in command:
            speak("Playing music")
            music_dir = "/path/to/your/music/folder"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

        else:
            speak("I am sorry, I don't understand that command.")

if __name__ == "__main__":
    run_voice_assistant()