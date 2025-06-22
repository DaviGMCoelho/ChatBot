import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Service.UserService import UserService

class UserController:
    @staticmethod
    def signup (username, password, conf_password):
        message, cod_profile = UserService.create_new_user(username, password, conf_password)
        return message, cod_profile
    
    @staticmethod
    def signin (cod_profile, password):
        return UserService.user_auth(cod_profile, password)
    
    @staticmethod
    def edit_model(model):
        return UserService.save_text_model(model)
    
    @staticmethod
    def get_profile_data(cod_profile):
        return UserService.load_profile_data(cod_profile)
    

if __name__ == '__main__':
    print(UserController.signin('ivad@421033', 'ariuepa7'))

    