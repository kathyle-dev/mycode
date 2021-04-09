import speech_recognition as sr

listener = sr.Recognizer()


def main():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            speech = listener.recognize_google(voice)
            if speech == "hello":
                print("What's up?")
    except:
        pass

if __name__ == "__main__":
    main()