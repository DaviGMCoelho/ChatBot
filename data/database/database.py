'''
This module handles the connection to the SQLite database using a singleton pattern.

Classes: 
    DatabaseConnection: A singleton metaclass that ensure only one instance of a class is created.
    Database: Manages the connection to the database using the difined path.
'''

import sqlite3

class DatabaseConnection(type):
    '''
    Singleton metaclass to ensure only one instance of a class is created.

    This metaclass is used to implement the Singleton design pattern by ensuring
    only one instance of a class throught the application's lifetime.

    Methods:
        __call__(*args, **kwds): Returns the existing instance if it exists, otherwise 
                                 creates and stores a new one.
    '''
    _instances = {}
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass = DatabaseConnection):
    '''
    Manages the connection to the SQLite database using a singleton pattern.

    Attributes:
        db_path (str): Path to the SQLite database file.

    Methods:
        __init__(db_path): Initializes database path.
        _connection(): Opens a new connection to the database and enabels foreign key constraints.
    '''

    def __init__(self, db_path=r'data\database\chatbot.db', tables_path=r'data\database\db_setup\create_tables.sql'):
        '''
        Initializes the database path.

        Parameters:
            db_path: The file path to the SQLite databse.
        '''
        self.db_path = db_path
        self.tables_path = tables_path


    def load_query(self, query_path: str):
        with open(query_path, 'r', encoding='utf-8') as query:
            return query.read()


    def init_database(self):
        '''
        Initialize the database and execute the setup scripts.
        '''
        sql_query = self.load_query(self.tables_path)
        connection, cursor = self.connection()

        with connection:
            cursor.executescript(sql_query)
        connection.commit()


    def connection(self):
        '''
        Opens a new SQLite connection and cursor, enabling foreign key constraints.

        Returns:
            tuple: A tuple containing the SQLite connection and cursor.
        '''
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')
        return connection, cursor
