import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.Services.UserServices import UserServices

class UserController:
    @staticmethod
    def signup (username, password, conf_password):
        return UserServices.create_new_user(username, password, conf_password)
    
    @staticmethod
    def signin (cod_profile, password):
        return UserServices.user_auth(cod_profile, password)

    