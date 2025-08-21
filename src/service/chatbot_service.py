'''
This module contains all methods related to chatbot operations.

It includes functionalities such as retrieving the currently selected model, 
generating responses using the model, and saving message history to the database

Classes:
    ChatbotService: Provides all chatbot-related functionalities.
'''
from ollama import chat

from src.repository.user_repository import UserRepository
from src.repository.chat_repository import ChatRepository
from src.Model.Entities.Message import Message
from src.Model.Entities.CurrentUser import CurrentUser

class ChatbotService:
    '''
    Handles all chatbot-related operations within the system.

    This class is responsible by managing all chatbot operations such as 
    generating responses, and saving and retrieving messages from the database.

    Methods:
        generate_response(user_message): 
            Use the text model to generate a response.
        get_models(): 
            Retrieves the user's selected text model.
        save_message(user_message, assistant_message):
            Saves the messages to the database.
        catch_history():
            Retrieves the current user's message history.
    '''
    def generate_response(self, user_message: str):
        '''
        Generates the model's response.

        Parameters:
            user_message (str): The user's message.

        Returns:
            str : The assistant's message.
        '''
        model = self.get_models()
        messages_history = self.catch_history()
        response = chat(
            model = model,
            messages=[*messages_history, {'role':'user', 'content': user_message}],
        )
        #message = response.message.content
        message = response['message']['content']
        return message

    def get_models(self):
        '''
        Returns the current user's selected text model.

        Returns:
            str: The name of the model currently selected for text generation.
        '''
        user = CurrentUser()
        text_model = user.get_current_user()['text_model']
        return text_model

    def save_message (self, user_message: str, assistant_message: str):
        '''
        Saves both user's and the assistant's messages to the database.

        Parameters:
            user_message (str): The user's message.
            assistant_message (str): The assistant's message.

        Returns:
            None
        '''
        user = CurrentUser()
        chatbot_repository = ChatRepository()

        cod_profile = user.get_current_user()['cod_profile']
        message_user = Message('user', user_message)
        message_assistant = Message('assistant', assistant_message)
        chatbot_repository.insert_message(message_user, cod_profile)
        chatbot_repository.insert_message(message_assistant, cod_profile)

    def catch_history(self):
        '''
        Retrieves the user's message history from the database.

        Returns:
            list[dict]: List of dictionaries, each containing the role and content of a message
        '''
        user = CurrentUser()
        user_repository = UserRepository()
        cod_profile = user.get_current_user()['cod_profile']
        message_history = user_repository.message_history(cod_profile)
        return message_history
