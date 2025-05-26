import sqlite3

class Database:
    DATABASE = r'data\database\chatbot.db'
    TABLES = r'data\database\db_setup\create_tables.sql'
    #INSERTS = r'database\db_setup\inserts.sql'

    @staticmethod # Deixa como uma função normal mas protegida pelo escopo da classe, sem acesso aos dados da classe
    def connect_database():
        connection = sqlite3.connect(Database.DATABASE)
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;') # Habilita chaves estrangeiras
        return connection, cursor
    
    @staticmethod
    def init_database():
        connection, cursor = Database.connect_database()
        with connection:
            with open(Database.TABLES, 'r', encoding='utf-8') as tables:
                sql_tables = tables.read()
                cursor.executescript(sql_tables) # Insere um script sql
            #with open(Database.INSERTS, 'r', encoding='utf-8') as inserts:
                #sql_inserts = inserts.sql
                #cursor.executescript(sql_inserts)
            connection.commit()
    

if __name__ == '__main__':
    Database.init_database()
    