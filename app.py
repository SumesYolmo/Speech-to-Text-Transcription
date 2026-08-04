import speech_recognition as sr


class SpeechToText:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def microphone_to_text(self):

        with sr.Microphone() as source:

            print("=" * 50)
            print("Speech-to-Text")
            print("=" * 50)

            print("\nAdjusting for background noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            print("Speak now...\n")

            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")

            text = self.recognizer.recognize_google(audio)

            print("\nRecognized Text:")
            print("--------------------------------")
            print(text)
            print("--------------------------------")

            self.save_text(text)

        except sr.UnknownValueError:
            print("Could not understand the audio.")

        except sr.RequestError:
            print("Internet connection required.")

    def audiofile_to_text(self, filename):

        try:

            with sr.AudioFile(filename) as source:

                print("\nReading audio file...")
                audio = self.recognizer.record(source)

            print("Recognizing...")

            text = self.recognizer.recognize_google(audio)

            print("\nRecognized Text:")
            print("--------------------------------")
            print(text)
            print("--------------------------------")

            self.save_text(text)

        except FileNotFoundError:
            print("File not found.")

        except sr.UnknownValueError:
            print("Speech not recognized.")

        except sr.RequestError:
            print("Internet connection required.")

    def save_text(self, text):

        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(text)

        print("\nText saved as output.txt")


def menu():

    stt = SpeechToText()

    while True:

        print("\n")
        print("=" * 50)
        print("Speech-to-Text Menu")
        print("=" * 50)
        print("1. Microphone to Text")
        print("2. Audio File to Text")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            stt.microphone_to_text()

        elif choice == "2":

            filename = input("Enter WAV file path: ")

            stt.audiofile_to_text(filename)

        elif choice == "3":

            print("Goodbye!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()