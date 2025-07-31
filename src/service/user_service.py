'''
This module contains all methods related to user interactions within the system.

It includes functionalities such as user registration, authentication, and profile management.

Classes:
    UserService: Contains all user-related methods.
'''
from src.validation.user_validation import UserValidation
from src.Model.Entities.User import User
from src.utils.utilities import Utilities
from src.Model.Entities.Database import Database
from src.Model.Entities.CurrentUser import CurrentUser

class UserService:
    '''
    Handles all user-related operations within the system.

    This class is responsible for managing user interactions such as registration,
    authentication, user data retrieval, and preference updates.

    Methods:
        _set_current_user(cod_profile): Initializes the current user session.
        get_profile_data(): Retrives the current user's data.
        create_new_user(username, password, conf_password): Register a new user.
        user_auth(cod_profile, password): Authenticates a user.
        save_text_model(text_model): Saves the selected text model for the current user.
    '''
    def _set_current_user(self, cod_profile: str):
        '''
        Retrieves user data from the database using the provided profile code, 
        and initializes the current user session.

        Parameters:
            cod_profile (str): The user's profile code.

        Returns:
            None
        '''
        current = CurrentUser()

        data = Database.get_user_data(cod_profile)
        current.cod_profile = cod_profile
        current.text_model = data['text_model']

    def get_profile_data(self):
        '''
        Retrieves and returns the current user's profile data.

        Returns:
            dict: A dictionary containing the user's information.
        '''
        current = CurrentUser()
        data = current.get_current_user()
        return data

    def create_new_user(self, username: str, password: str, conf_password: str):
        '''
        Validates input data, generates a unique profile code, and creates
        a new user in the database.

        Parameters:
            username (str): The desired username.
            password (str): The chosen password.
            conf_password (str): The password confirmation.

        Returns:
            tuple:
                dict: A status message indicating the result of the operation.
                str: The generated profile code.
        '''
        validation = UserValidation()
        utils = Utilities()

        cod_profile = ''
        validate_username =  validation.username_validation(username)
        if not validate_username['status']:
            return validate_username, cod_profile

        validate_password =  validation.password_validation(password, conf_password)
        if not validate_password['status']:
            return validate_password, cod_profile

        while True:
            cod_profile = User.generate_cod_profile(username)
            validate_cod_profile = validation.cod_profile_validation(cod_profile)
            if not validate_cod_profile['status']:
                break

        user = User(username, password, cod_profile)
        Database.insert_profile(user)
        self._set_current_user(cod_profile)
        status_message = utils.generate_message(True, 'Cadastro realizado')
        return status_message, cod_profile

    def user_auth(self, cod_profile: str, password: str):
        '''
        Authenticates the user using the profile code and password.

        Parameters:
            cod_profile (str): The user's profile identifier.
            password (str): The user's password.

        Returns:
            dict: A status message indicating whether the authentication was successful.
        '''
        utils = Utilities()

        auth = Database.authentication_user(cod_profile, password)
        if auth:
            self._set_current_user(cod_profile)
            message = utils.generate_message(True, 'Login realizado')
            return message
        message = utils.generate_message(False, 'identificador ou senha incorretos')
        return message

    def save_text_model(self, text_model: str):
        '''
        Saves the specified text model to the database for the current user.

        Parameters:
            text_model (str): The name of the model to be saved.

        Returns:
            None
        '''
        current = CurrentUser()
        current.text_model = text_model
        cod_profile = current.get_current_user()['cod_profile']
        Database.set_text_model(text_model, cod_profile)
