import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.Service.ChatbotService import ChatbotService

class ChatbotController:
    def __init__(self, model: str):
        self.model =  model

    # Realiza pergunta ao modelo e recebe a resposta
    def send_response(self, user_message: str):
        user_message = user_message
        model = self.model

        # Gera a resposta
        response = ChatbotService.generate_response(user_message, model)
        ChatbotService.save_message(user_message, response)

        return response
    
    
    def get_message_history(self):
        messages = ChatbotService.catch_history()
        return messages

if __name__ == '__main__':
    ...