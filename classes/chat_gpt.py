from classes.mic_recognizer import MicRecognizer
from transformers import Conversation, pipeline

class ChatGPT(MicRecognizer):
    def __init__(self):
        super().__init__()
        self.chatbot = pipeline("conversational")
        self.conversation = None

    def execute(self):
        print('GPT Ouvindo...')
        audio = self.listen(placeholder='Fale alguma coisa...')
        text = self.recognize(audio, with_unidecode=True)
        if not self.conversation:
            self.conversation = Conversation("Hello, how are you?", "I'm doing great. What can I do for you today?")
        else:
            self.conversation.add_user_input(text)
        self.speech(self.chatbot([self.conversation])[-1]['generated_text'])
        self.execute()