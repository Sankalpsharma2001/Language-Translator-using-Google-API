import pyaudio as pyaudio
import googletrans
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

# print all available languages
print("List of all available languages:")
print(googletrans.LANGUAGES)

# create recognizer() class objects
recog1 = spr.Recognizer()
recog2 = spr.Recognizer()

# create microphone instance with device microphone
micro = spr.Microphone(device_index=0)

# taking language as input
from_lang = input("Enter the code of the language to be translated:")
to_lang = input("Enter the code of the your preferred language:")

# capture voice
with micro as source:
    print("Speak 'hello' to initiate the translation!")
    print("-------------------->")
    audio = recog1.listen(source)

# translate the sentence based on speech
if 'hello' in recog1.recognize_google(audio):
    recog1 = spr.Recognizer()
    translator = Translator()
    with micro as source:
        print('Speak a sentence...')
        audio = recog2.listen(source)
        get_sentence = recog2.recognize_google(audio)
        try:
            get_sentence = recog2.recognize_google(audio)
            default_text = (translator.translate(
                get_sentence, src='en', dest=from_lang)).text
            print("Phrase to be translated: "+default_text)
            text_to_translate = translator.translate(
                get_sentence, src=from_lang, dest=to_lang)
            # print(type(text_to_translate))
            text = text_to_translate.text
            print("The translated sentence is:"+text)
            speak = gTTS(text=text, lang=to_lang, slow=False)
            speak.save("captured_voice.mp3")
            os.system("start captured_voice.mp3")
        except spr.UnknownValueError:
            print("Unable to understand input")
        except spr.RequestError as e:
            print("Unable to provide required output".format(e))