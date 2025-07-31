'''
This module contains methods related to chatbot operations within the system.

It handles the logic for calling methods from the ChatbotService class.

Classes:
    ChatbotController: Handles interactions between the user and the chatbot service.
'''
from src.service.chatbot_service import ChatbotService
from src.Manager.model_manager import ModelManager

class ChatbotController:
    '''
    Manages all chatbot-related interactions with the program.

    This class is responsible for calling and coordinates methods
    from the ChatbotService class.

    Methods:
        send_response(user_message): 
            Retrieves a response to the user's input.
        get_message_history():
            Returns the user's message history.
        get_ia_models():
            Display all available models installed in the system.
        get_main_models():
            Retrieves the currently selected main models.
    '''
    def send_response(self, user_message: str):
        '''
        Generates the assistant's response to the user's message.

        Parameters:
            user_message (str): The user's input message.

        Returns:
            str: The assistant's generated response.
        '''
        chatbot = ChatbotService()
        response = chatbot.generate_response(user_message)
        chatbot.save_message(user_message, response)
        return response

    def get_message_history(self):
        '''
        Returns the message history between the user and the assistant.

        Returns:
            list[dict]: A list of dictionaries, each containing:
                - role (str): 'user' or 'assistant'.
                - content (str): The message content.
        '''
        chatbot = ChatbotService()
        messages = chatbot.catch_history()
        return messages

    def get_ia_models(self):
        '''
        Retrieves all models currently installed in the user's system.

        Returns:
            dict: A message containing:
                - status (bool): Whether the request was successful.
                - models (list[str]): A list of installed model names.
        '''
        model_manager = ModelManager()
        models = model_manager.get_installed_models()
        return models

    def get_main_models(self):
        '''
        Retrieves the models currently selected for use by the user.

        Returns:
            dict: A dictionary containing
                - text_model (str): The name of the selected text model.
        '''
        chatbot = ChatbotService()
        text_model = chatbot.get_models()
        models = {
            'text_model': text_model
        }
        return models
