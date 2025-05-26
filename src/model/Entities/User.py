class User:
    def __init__(self, name: str, password: str):
        self.name = name
        self._password = password # Indica que o atributo é "Protegido"

    def validate_password(self):
        if len(self.passoword) < 8:
            raise ValueError('Senha muito curta')