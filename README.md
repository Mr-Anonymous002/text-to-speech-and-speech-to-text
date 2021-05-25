# text-to-speech-and-speech-to-text
Text to Speech and Speech to Text in Python.
AI based project, coded by Sanketh J.

# Installation
* `pip install argparse`
* `pip install pyttsx3`
* `pip install speech_recognition`
* `pip install pyaudio`

if you cant install `pyaudio` properly on Windows, then follow this:
* `pip insall pipwin`
* `pipwin install pyaudio`

# Usage
To see how to use this script, use "-h" or "--help"
`python text-to-speech-and-speech-to-text.py -h` 


If you want to use "speech to text", use module argument "sst".
In the same way, if you wanted use "text to speech", use module argument "tts".

## Speech to Text (tts)
* To convert from text to speech, use module "tts" and "-t" to mention text.
* `python text-to-speech-and-speech-to-text.py tts -t "i am groot"`

* To save this in a output file, just use "-o" argument.
* `python text-to-speech-and-speech-to-text.py tts -t "i am groot" -o new.mp3`

* To convert from text to speech, from a file, use "-f" argument to mention the file
* `python text-to-speech-and-speech-to-text.py tts -f myfile.txt` 

* To ouput the file, use "-o" argument
* `python text-to-speech-and-speech-to-text.py tts -f myfile.txt -o new1.mp3`

## Text to Speech (stt)
#### You need internet connection for this
* To convert from speech to text, use module "stt".
* `python text-to-speech-and-speech-to-text.py stt`

* To save this in a output file, just use "-o" argument.
* `python text-to-speech-and-speech-to-text.py stt -o new2.txt`

* To convert from speech to text, from a file, use "-n" argument to mention the file (you can use any other formats too).
* `python text-to-speech-and-speech-to-text.py stt -n myfile2.mp3` 

* To ouput the file, use "-o" argument
* `python text-to-speech-and-speech-to-text.py stt -n myfile2.mp3 -o new4.txt`

