import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


from src.Validation.UserValidation import UserValidation
from src.Model.Entities.User import User
from Utils.ServiceUtils import ServiceUtils
from src.Model.Entities.Database import Database
from src.Utils.SessionUtils import SessionUtils

class UserService:
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
        status_message = ServiceUtils.generate_status_message(True, 'Cadastro realizado')
        SessionUtils.set_user(cod_profile)
        return status_message, cod_profile

    @staticmethod
    def user_auth(cod_profile, password):
        auth = Database.authentication_user(cod_profile, password)
        if auth:
            SessionUtils.set_user(cod_profile)
            status_message = ServiceUtils.generate_status_message(True, 'Login realizado')
            return status_message
        status_message = ServiceUtils.generate_status_message(False, 'identificador ou senha incorretos')
        return status_message

    
if __name__ == '__main__':
    ...