import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


from src.Validations.UserValidation import UserValidation
from src.Model.Entities.User import User
from Services.ServicesUtils import ServicesUtils
from src.Model.Entities.Database import Database

class UserServices:
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
        status_message = ServicesUtils.generate_status_message(True, 'Cadastro realizado')
        return status_message, cod_profile

    @staticmethod
    def user_auth(cod_profile, password):
        auth = Database.authentication_user(cod_profile, password)
        if auth:
            return ServicesUtils.generate_status_message(True, 'Login realizado')
        return ServicesUtils.generate_status_message(False, 'identificador ou senha incorretos')

    
if __name__ == '__main__':
    print(UserServices.create_new_user('Adenilson', 'espada78', 'espada78'))