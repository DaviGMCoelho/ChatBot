from data.database.database import Database

class BaseRepository:
    def __init__(self, tables_db = r'data\database\database.py'):
        self.database = Database()
        self.tables_db = tables_db

    def _connection(self):
        connection, cursor = self.database.connection()
        return connection, cursor
    
    def _load_query(self, query_path):
        query = self.database.load_query(query_path)
        return query
