import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.Model.Entities.Database import Database
from src.Model.Entities.Message import Message
from src.Model.Entities.CurrentUser import CurrentUser

from ollama import chat

class ChatbotService:
    @staticmethod
    def generate_response(user_message):
        model = ChatbotService.get_models()
        messages_history = ChatbotService.catch_history()
        resposta = chat(
            model = model,
            messages=[*messages_history, {'role':'user', 'content': user_message}],
        )
        return resposta.message.content
    
    @staticmethod
    def get_models():
        user = CurrentUser()
        text_model = user.get_current_user()['text_model']
        return text_model
    
    @staticmethod
    def save_message (user_message, assistant_message):
        message_user = Message('user', user_message)
        message_assistant = Message('assistant', assistant_message)
        Database.insert_message(message_user)
        Database.insert_message(message_assistant)

    @staticmethod
    def catch_history():
        message_history = Database.message_history()
        return message_history
    

if __name__ == '__main__':
    chatbot = ChatbotService()
    user = 'Como você está?'
    print('gerando resposta')
    resposta = chatbot.generate_response(user)
    print(resposta)
