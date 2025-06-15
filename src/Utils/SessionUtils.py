class SessionUtils:
    _current_user = None

    @classmethod
    def set_user(cls, user_data):
        cls._current_user = user_data

    @classmethod
    def get_user(cls):
        return cls._current_user
    
    @classmethod
    def logout(cls):
        cls._current_user = None