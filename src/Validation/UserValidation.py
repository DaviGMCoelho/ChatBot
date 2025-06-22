from src.Model.Entities.Database import Database
from src.Utils.Utilities import Utilities

class UserValidation:
    @staticmethod
    def username_validation(username):
        if username:
            if len(username) >= 3:
                message = 'Usuário cadastrado com sucesso!'
                status = True
                return Utilities.generate_status_message(status, message)
            message = ValueError('Username precisa conter pelo menos 3 caracteres')
            status = False
            return Utilities.generate_status_message(status, message)
        message = ValueError('Digite seu username')
        status = False
        return Utilities.generate_status_message(status, message)

    @staticmethod
    def password_validation(password, confirmation_password):
        if password:
            if password == confirmation_password:
                if len(password) >= 8:
                    message = 'Cadastro realizado com sucesso!'
                    status = True
                    return Utilities.generate_status_message(status, message)
                message = ValueError('Senha precisa ser no mínimo 8 caracteres!')
                status = False
                return Utilities.generate_status_message(status, message)
            message = ValueError('Senha e confirmação de senha precisam estar iguais!')
            status = False
            return Utilities.generate_status_message(status, message)
        message = ValueError('Digite uma senha')
        status = False
        return Utilities.generate_status_message(status, message)


    @staticmethod
    def cod_profile_validation(cod_profile):
        if not Database.verify_cod_profile(cod_profile):
            message = 'Success'
            status = True
            return Utilities.generate_status_message(status, message)
        message = ValueError('Identificador já existe')
        status = False
        return Utilities.generate_status_message(status, message)



if __name__ == '__main__':
    ...
