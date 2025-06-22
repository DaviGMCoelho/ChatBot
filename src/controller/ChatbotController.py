import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.Service.ChatbotService import ChatbotService
from src.Manager.ModelManager import ModelManager


class ChatbotController:
    # Realiza pergunta ao modelo e recebe a resposta
    def send_response(self, user_message: str):
        print(user_message)
        response = ChatbotService.generate_response(user_message)
        ChatbotService.save_message(user_message, response)
        return response

    def get_message_history(self):
        messages = ChatbotService.catch_history()
        return messages
    
    @staticmethod
    def get_ia_models():
        models = ModelManager.show_installed_models()
        return models
    
    @staticmethod
    def get_main_models():
        text_model = ChatbotService.get_models()
        return {
            'text_model': text_model
        }


if __name__ == '__main__':
    chatbot = ChatbotController.get_main_models()
    print(chatbot)
    
    
