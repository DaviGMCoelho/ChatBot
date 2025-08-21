from src.repository.base_repository import BaseRepository

class ChatRepository (BaseRepository):
    def __init__(self):
        super().__init__()

    def insert_message(self, message, cod_profile):
        sql_message = self._load_query(r'data\database\queries\chatbot\insert\insert_message.sql')
        sql_profile = self._load_query(r'data\database\queries\user\select\select_profile_id.sql')

        connection, cursor = self._connection()
        with connection:
            cursor.execute(sql_profile, (cod_profile,))
            profile_id = cursor.fetchone()[0]

            data = (message.origin, message.content, profile_id)
            cursor.execute(sql_message, data)
