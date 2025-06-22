import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.Validation.UserValidation import UserValidation
from src.Model.Entities.User import User
from src.Utils.Utilities import Utilities
from src.Model.Entities.Database import Database
from src.Model.Entities.CurrentUser import CurrentUser

class UserService:
    @staticmethod
    def get_profile_data():
        user = CurrentUser()
        data = user.get_current_user()
        return data

    @staticmethod
    def _set_current_user(cod_profile):
        user = CurrentUser()
        data = Database.get_user_data(cod_profile)
        user.cod_profile = cod_profile
        user.text_model = data['text_model']

    @staticmethod
    def create_new_user(username, password, conf_password):
        cod_profile = ''
        validate_username =  UserValidation.username_validation(username)
        if not validate_username['status']:
            return validate_username, cod_profile
        validate_password =  UserValidation.password_validation(password, conf_password)
        if not validate_password['status']:
            return validate_password, cod_profile

        while True:
            cod_profile = User.generate_cod_profile(username)
            validate_cod_profile = UserValidation.cod_profile_validation(cod_profile)
            if validate_cod_profile['status']:
                break

        user = User(username, password, cod_profile)
        Database.insert_profile(user)
        UserService._set_current_user(cod_profile)
        status_message = Utilities.generate_status_message(True, 'Cadastro realizado')
        return status_message, cod_profile

    @staticmethod
    def user_auth(cod_profile, password):
        auth = Database.authentication_user(cod_profile, password)
        if auth:
            UserService._set_current_user(cod_profile)
            message = Utilities.generate_status_message(True, 'Login realizado')
            return message
        message = Utilities.generate_status_message(False, 'identificador ou senha incorretos')
        return message
    @staticmethod
    
    def save_text_model(text_model):
        user = CurrentUser()
        user.text_model = text_model
        cod_profile = user.get_current_user()['cod_profile']
        Database.set_text_model(text_model, cod_profile)

if __name__ == '__main__':
    print(UserService.get_profile_data())
    UserService.set_current_user('oudrikanda', 'mistral')
    print(UserService.get_profile_data())
