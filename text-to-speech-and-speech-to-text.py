# coded by Sanketh J

import pyttsx3
import argparse
import speech_recognition as sr

def text_to_speech(options):

    engine = pyttsx3.init()     # initializing
    engine.setProperty("rate", 100)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    if options.text or options.output:
        engine.say(options.text)  # speech
        if options.output:
            engine.save_to_file(options.text, options.output)

    if options.file or options.output:
        with options.file as file:
            engine.say(file.read())
        if options.output:
            engine.save_to_file(options.file, options.output)

    engine.runAndWait()  # waiting till it speaks completely
    engine.stop()

def speech_to_text(options):
    r = sr.Recognizer()

    if options.module or options.output:

        with sr.Microphone() as source:
            print("Listening.....")
            audio_text = r.listen(source)

            try:
                print(r.recognize_google(audio_text))
                if options.output:
                    file1 = open(options.output, "w")
                    file1.write(r.recognize_google(audio_text))
                    file1.close()
            except:
                print("I cant hear you. Please, speak again....")

    if options.speech or options.output:

        with sr.AudioFile(options.speech) as source:
            print("Reading.....")
            audio_text = r.listen(source)

            try:
                text = r.recognize_google(audio_text)
                print(text)
                if options.output:
                    file1 = open(options.output, "w")
                    file1.write(r.recognize_google(audio_text))
                    file1.close()
            except:
                print('Sorry.. run again...')

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("module", help='"stt" = speech to text, "tts" = text to speech')
    parser.add_argument("-t", "--text",  help='Enter the text to convert. Example: python text-to-speech-and-speech-to-text.py -t "i am groot"')
    parser.add_argument("-o", "--output", help='Output file name. Example: python text-to-speech-and-speech-to-text.py -t "i am groot" -o speech.mp3')
    parser.add_argument("-f","--file", type=argparse.FileType('r'), help='Enter the file path to convert to speech. Example: python text-to-speech-and-speech-to-text.py -f "trial.txt"')
    parser.add_argument("-s","--speech", help='audio file')
    options = parser.parse_args()

    if not options.text and not options.output and not options.file and not options.module:
        print("[-] Conversion from Text to Speech unsuccessful!")
        parser.error("[-] Use --help for more details")


    if options.text or options.output or options.file or options.module:
        if options.module == "tts":
            text_to_speech(options)
            print("[+] Conversion from Text to Speech successful!")
        if options.module == "stt":
            speech_to_text(options)
            print("[+] Conversion from Speech to Text successful!")


