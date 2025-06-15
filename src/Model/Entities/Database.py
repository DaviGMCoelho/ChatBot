import sqlite3

class Database:
    DATABASE = r'data\database\chatbot.db'
    TABLES = r'data\database\db_setup\create_tables.sql'
    #INSERTS = r'database\db_setup\inserts.sql'

    @staticmethod # Deixa como uma função normal mas protegida pelo escopo da classe, sem acesso aos dados da classe
    def _connect_database():
        connection = sqlite3.connect(Database.DATABASE)
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;') # Habilita chaves estrangeiras
        return connection, cursor
    
    @staticmethod
    def _load_query(path):
        with open(path, 'r') as archive:
            return archive.read()
        
    
    @staticmethod
    def init_database():
        connection, cursor = Database._connect_database()
        with connection:
            with open(Database.TABLES, 'r', encoding='utf-8') as tables:
                sql_tables = tables.read()
                cursor.executescript(sql_tables) # Insere um script sql
            #with open(Database.INSERTS, 'r', encoding='utf-8') as inserts:
                #sql_inserts = inserts.sql
                #cursor.executescript(sql_inserts)
            connection.commit()

    @staticmethod
    def verify_cod_profile(cod_profile):
        sql_query = Database._load_query(r'data\database\sql_queries\verify\verify_cod_profile.sql')
        connection, cursor = Database._connect_database()
        with connection:
            cursor.execute(sql_query, (cod_profile,))
        search = cursor.fetchone()
        return search is not None
    

    @staticmethod
    def insert_profile(user):
        sql_query_profile = Database._load_query(r'data\database\sql_queries\insert\insert_profile_data.sql')
        sql_query_credentials = Database._load_query(r'data\database\sql_queries\insert\insert_profile_credentials.sql')
        profile_data = (user.cod_profile, user.username)

        connection, cursor = Database._connect_database()
        with connection:
            cursor.execute(sql_query_profile, profile_data)
            last_id = cursor.lastrowid

            profile_credentials = (last_id, user._password)
            cursor.execute(sql_query_credentials, profile_credentials,)


    @staticmethod
    def authentication_user(cod_profile, password):
        sql_query = Database._load_query(r'data\database\sql_queries\auth\auth_login.sql')
        auth_datas = (cod_profile, password)

        connection, cursor = Database._connect_database()
        with connection:
            cursor.execute(sql_query, auth_datas)
        search = cursor.fetchone()
        return search is not None
    

    @staticmethod
    def insert_message(origin, content):
        sql_query = Database._load_query(r'data\database\sql_queries\insert\insert_message.sql')
        message = (origin, content)

        connection, cursor = Database._connect_database()
        with connection:
            cursor.execute(sql_query, message)

    @staticmethod
    def message_history():
        sql_query = Database._load_query(r'data\database\sql_queries\select\select_messages.sql')
        connection, cursor = Database._connect_database()

        with connection:
            cursor.execute(sql_query)
        messages = cursor.fetchall()
        new_messages = [{'role': role, 'content': content} for role, content in messages]
        return new_messages


if __name__ == '__main__':
   Database.init_database()