'''
This module contains methods related to user interactions within the system.

It handles the logic for calling User Service methods.

Classes:
    UserController: Contains all methods that call the User Service.

Methods:
    signup:
        Register a new user.
    signin: 
        uthentication user.
    edit_model:
        Alterate the model used to generate text.
    get_profile_data:
        Retrieves the user data.
'''

from src.service.user_service import UserService

class UserController:
    '''
    Manages all user-related methods for interacting with the program.

    This class is responsible for managing calls to User Service methods.

    Methods:
        signup(username, password, conf_password): 
            Creates a new user in the system.
        signin(cod_profile, password):
            Authenticates the user with profile code and chosen password.
        edit_model(model):
            Updates the text model used for text generation.
        get_profile_data():
            Retrieves profile data related for the current user.
    '''
    def signup (self, username, password, conf_password):
        '''
        Creates a new user, call the user-related service method.

        Parameters:
            username: The user's chosen username.
            password: The user's chosen password.
            conf_password: The confirmation of the password for validation.

        Returns:
            tuple: Always return a tuple with values:
                - message (dict): A status message describing the registration process.
                - cod_profile (str): The user's profile code.
        '''
        service = UserService()
        message, cod_profile = service.create_new_user(username, password, conf_password)
        return message, cod_profile

    def signin (self, cod_profile, password):
        '''
        Authenticate user using profile code and password, call the user-related service method.

        Paramaeters:
            cod_profile (str): The unique identifier of the user's profile.
            password (str): The password related to am existent user.

        Returns:
            message (str): A status message indicating the result of the authentication.
        '''
        service = UserService()
        message = service.user_auth(cod_profile, password)
        return message

    def edit_model(self, model):
        '''
        Updates the main model used for text generation.

        Parameters:
            model (str): The name of the model to be used.
        '''
        service = UserService()
        service.save_text_model(model)

    def get_profile_data(self):
        '''
        Retrieves the data related to the currently authenticated user.

        Returns:
            data (dict): A dictionary containing user profile information.
        '''
        service = UserService()
        data = service.get_profile_data()
        return data
