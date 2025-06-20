import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.Validation.UserValidation import UserValidation
from src.Model.Entities.User import User
from src.Utils.Utilities import Utilities
from src.Model.Entities.Database import Database
from src.current_user import current_user

class UserService:
    @staticmethod
    def _get_current_user():
        print(current_user)
        ...

    @staticmethod
    def _load_profile_data():
        user = UserService._get_current_user.get_user()
        return user

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
            if validate_cod_profile['status'] == True:
                break

        user = User(username, password, cod_profile)
        Database.insert_profile(user)
        status_message = Utilities.generate_status_message(True, 'Cadastro realizado')
        #current_user.cod_profile = cod_profile
        return status_message, cod_profile


    @staticmethod
    def user_auth(cod_profile, password):
        auth = Database.authentication_user(cod_profile, password)
        if auth:
            UserService._load_profile_data(cod_profile)
            status_message = Utilities.generate_status_message(True, 'Login realizado')
            return status_message
        status_message = Utilities.generate_status_message(False, 'identificador ou senha incorretos')
        return status_message
    
    @staticmethod
    def save_text_model(model):
        cod_profile = UserService._load_profile_data()['cod_profile']
        main_model = model
        UserService._set_profile_data()['main_text_model'] = model
        Database.set_text_model(main_model, cod_profile)

    


    
if __name__ == '__main__':
    print(UserService._get_current_user())
