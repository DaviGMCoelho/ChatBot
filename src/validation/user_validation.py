'''
This module is responsible for validating user input.

Classes: 
    UserValidation: Provides logic for validating user-relatedata.
'''
from src.repository.user_repository import UserRepository
from src.utils.utilities import Utilities
from src.validation.validation import BaseValidation


class UserValidation(BaseValidation):
    '''
    Provides validation logic for user-related data.

    This class checks whether the user data meets validation criteria.

    Methods:
        __init__():
            Initializes the class and sets validation parameters.
        username_validation(username):
            Validates that the input is not empty and meets the minimum length.
        password_validation(password, confirmation_password):
            Validates that the password meets criteria and matches the confirmation password.
        cod_profile_validation(cod_profile):
            Checks if the profile code already exists.
    '''
    def __init__(self):
        '''
        Initializes the UserValidation class.

        Attributes:
            length (int): The minimal allowed content lenght.
        '''
        super().__init__()
        self.length = 3
        self.length_password = 8

    def username_validation(self, username: str):
        '''
        Verify if the provided username meets the validation criteria.

        Parameters:
            username (str): The user's chosen username.

        Returns:
            dict: A dictionary containing:
                - status (bool): True if validation is successful, False otherwise.
                - description (str): A message describing the validation result.
        '''
        utils = Utilities()

        confirm = self.exists(username)
        if not confirm:
            return utils.generate_message(confirm, 'Digite seu username')

        has_min_length = self.min_length(username, self.length)
        if not has_min_length:
            return utils.generate_message(has_min_length, 'Username minímo de 3 caracteres')

        return utils.generate_message(has_min_length, 'Usuário cadastrado com sucesso!')

    def password_validation(self, password: str, confirmation_password: str):
        '''
        Verifies if the provided password meets the validation criteria.

        Parameters:
            password: The user's chosen password.
            confirmation_passowrd: The confirmation of the password, retyped by the user.

        Returns:
            dict: A dictionary containing:
                - status (bool): True if validation is successful, False otherwise.
                - description (str): A message describing the validation result.
        '''
        utils = Utilities()

        if not self.exists(password, confirmation_password):
            return utils.generate_message(False, 'Digite uma senha')

        if not self.equals(password, to_compare=[confirmation_password]):
            return utils.generate_message(False, 'Senha e confirmação de senha não são iguais!')

        if not self.min_length(password, self.length_password):
            return utils.generate_message(False,
                f'Sua senha precisa ter no mínimo {self.length_password} caracteres!')

        return utils.generate_message(True, 'Cadastro realizado com sucesso!')

    def cod_profile_validation(self, cod_profile: str):
        '''
        Validate whether the provided profile code already exists in the system.

        Parameters:
            cod_profile (str): The user's unique profile identifier.

        Returns:
            dict: A dictionary containing:
                - status (bool): True if validation is successful, False otherwise.
                - description (str): A message describing the validation result.
        '''
        utils = Utilities()
        user_repository = UserRepository()

        if user_repository.verify_cod_profile(cod_profile):
            return utils.generate_message(False, 'Identificador já existe')

        return utils.generate_message(True, 'Sucesso')

if __name__ == '__main__':
    ...
