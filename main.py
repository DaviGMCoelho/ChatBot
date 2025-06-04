# Código principal
import os

from src.Model.Entities.Database import Database
from src.View.Desktop.AuthenticationInterface import AuthenticationInterface

class Main():
    @staticmethod
    def start_program():
        if not os.path.exists(r'data\database\chatbot.db'):
            Database.init_database
        window = AuthenticationInterface()
        window.mainloop()


Main.start_program()
