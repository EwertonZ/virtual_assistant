from classes.mic_recognizer import MicRecognizer
from config import LISTNERS

if __name__ == '__main__':
    mic = MicRecognizer()
    audio = mic.listen()
    text = mic.recognize(audio, with_unidecode=True)   
    print(text.lower())
    
    if text and text in LISTNERS:
        LISTNERS[text.lower()]().execute()

