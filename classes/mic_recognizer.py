import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from googletrans import Translator
from unidecode import unidecode

class MicRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer().energy_threshold = 8000

    def listen(self, placeholder='Ouvindo...'):
        with sr.Microphone() as source:
            print(placeholder)
            audio = self.recognizer.listen(source)
            print("Entendendo...")
        return audio

    def recognize(self, audio, language='pt-BR', with_unidecode=False):
        try:
            text = self.recognizer.recognize_google(audio, language='pt-BR')
            print("Você disse: " + text)
            return unidecode(text) if with_unidecode else text
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio")            
        except sr.RequestError as e:
            print("Erro ao buscar resultados; {0}".format(e))
        return None
    
    def speech(self, text, language='pt-BR'):
        tts = gTTS(text, lang=language)
        tts.save('classes/audio.mp3')
        song = AudioSegment.from_mp3('classes/audio.mp3')
        play(song)
        return song
    
    def translate(self, text, src='en', dest='pt'):
        translator = Translator()
        return translator.translate(text, src=src, dest=dest).text