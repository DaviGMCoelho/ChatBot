'''
This module is responsible for validating chatbot messages.

Classes: 
    MessageValidation: Contains logic for verifying message content.
'''
from src.validation.validation import BaseValidation
from src.utils.utilities import Utilities

class MessageValidation(BaseValidation):
    '''
    Provides validation logic for chatbot messages.

    This class checks whether a message meets validation criteria.

    Methods:
        __init__(): 
            Initializes the class and sets validation parameters.
        message_content(message):
            Validates the content of a message.
    '''
    def __init__(self):
        '''
        Initializes the MessageValidation class.

        Attributes:
            length (int): The minimal allowed message lenght.
        '''
        self.length = 1

    def message_content(self, message):
        '''
        Validates the content of a message.

        Parameters:
            message (str): The message content to validate.

        Returns:
            dict: A dictionary containing:
                - status (bool):
                   True if the message is valid, False otherwise.
                - description (str):
                    A description about of the validation result.
        '''
        utils = Utilities()

        exist = self.exists(message)
        if exist:
            have_min_length = self.min_lenght(message, self.length)
            error_message = utils.generate_message(have_min_length, 'Campo validado')
            return error_message
        error_message = utils.generate_message(exist, 'Preencha o campo necessário')
        return error_message
