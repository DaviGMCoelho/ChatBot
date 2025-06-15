import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.Model.Entities.Database import Database

from ollama import chat

class ChatbotService:
    def generate_response(user_message, user_model):
        messages_history = ChatbotService.catch_history()
        resposta = chat(
            model= user_model,
            messages=[*messages_history, {'role':'user', 'content': user_message}],
        )
        return resposta.message.content
    
    @staticmethod
    def save_message (user_message, assistant_message):
        Database.insert_message('user', user_message)
        Database.insert_message('assistant', assistant_message)

    @staticmethod
    def catch_history():
        message_history = Database.message_history()
        return message_history
    
    

if __name__ == '__main__':
    ...