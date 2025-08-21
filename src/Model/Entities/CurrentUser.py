class CurrentUserSingleton(type):
    _instances = {}
    #             v- Referencia ao objeto / classe do objeto
    def __call__(cls, *args, **kwds): # __call__ -> Método especial, executa quanado chama a classe
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds) # Cria a instância
            cls._instances[cls] = instance
        return cls._instances[cls] # Se já tiver, retorna a que já foi criada


class CurrentUser(metaclass=CurrentUserSingleton): #metaclass(?)
    def __init__(self):
        self._cod_profile = None
        self._text_model = None

    @property
    def cod_profile(self):
        return self._cod_profile
    
    @cod_profile.setter
    def cod_profile(self, cod_profile):
        self._cod_profile = cod_profile
    
    @property
    def text_model(self):
        return self._text_model
    
    @text_model.setter
    def text_model(self, text_model):
        self._text_model = text_model


    def get_current_user(self):
        self.current_user = {
            'cod_profile' : self._cod_profile,
            'text_model' : self._text_model
        }

        return self.current_user

if __name__ == '__main__':
    ...
