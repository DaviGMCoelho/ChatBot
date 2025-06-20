class CurrentUser:
    def __init__(self):
        self._cod_profile = None
        self._text_model = None

    @property # Cria um atributo como um método
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
