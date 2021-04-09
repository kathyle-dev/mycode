import speech_recognition as sr
import pyttsx3
import os

listener = sr.Recognizer()


def speakText(prompt):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(prompt)
    engine.runAndWait()


def getCommands():
    try:
        with sr.Microphone() as source:
            speakText("I am listening.")
            print("listening....")
            speech = ""
            command_list = []
            while True:
                voice = listener.listen(source)
                speech = listener.recognize_google(voice).lower()
                if speech == "stop":
                    break
                speakText(f"Entering {speech}")
                command_list.append(speech)
                print(speech)
            return command_list
    except:
        pass


def runCommands(command_list):
    os.system(command_list)


def main():
    commands = getCommands()
    print(commands)
    ##runCommands(commands)


if __name__ == "__main__":
    main()
