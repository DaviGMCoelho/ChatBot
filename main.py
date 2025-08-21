'''
Initializes the program by creating the local database and open the authentication interface.

Classes:
    Main

Methods:
    start_program: Verifies if a database file exists and opens the authentication window.
'''
import os

from data.database.database import Database
from src.view.desktop.authentication_interface import AuthenticationInterface

class Main():
    '''
    Manages all initialization-related methods for starting the program.

    Methods:
        start_program(): 
            Creates the database file if it does not exist and opens the authentication window. 
    '''
    def start_program(self):
        '''
        Create the database file and opens the authentication window.
        '''
        if not os.path.exists(r'data\database\chatbot.db'):
            db = Database()
            db.init_database()

        window = AuthenticationInterface()
        window.mainloop()

main = Main()
main.start_program()
