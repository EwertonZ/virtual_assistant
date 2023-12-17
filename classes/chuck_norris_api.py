from classes.mic_recognizer import MicRecognizer
import requests

METHODS = {
    'categorias': 'get_categories',
    'piada aleatoria': 'get_random_joke',
    'piada com categoria': 'get_joke_by_category'
}

class ChuckNorrisApi(MicRecognizer):
    def __init__(self):
        super().__init__()
        self.base_url = "https://api.chucknorris.io/"
    
    def execute(self):
        audio = self.listen(placeholder='Que tipo de piada que ouvir sobre Chuck Norris?')
        text = self.recognize(audio, with_unidecode=True)
        if text and text in METHODS:
            response = getattr(self, METHODS[text])()
            print(response)
            self.speech(self.translate(response))
        else:
            print('Não entendi o que você disse')
        self.execute()

    def get_random_joke(self):
        url = self.base_url + "jokes/random"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["value"]
        else:
            return None
    
    def get_joke_by_category(self):
        audio = self.listen(placeholder='Diga uma categoria')
        text = self.recognize(audio, with_unidecode=True)
        if text:
            url = self.base_url + "jokes/random?category={}".format(text)
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()["value"]
        return None
    
    def get_categories(self):
        url = self.base_url + "jokes/categories"
        response = requests.get(url)
        if response.status_code == 200:
            return ', '.join(response.json())
        else:
            return None
