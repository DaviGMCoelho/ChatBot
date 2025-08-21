from src.repository.base_repository import BaseRepository

class UserRepository (BaseRepository):
    def __init__(self):
        super().__init__()

    def verify_cod_profile(self, cod_profile: str):
        sql_query = self._load_query(r'data\database\queries\user\verify\verify_cod_profile.sql')
        data = (cod_profile,)
        connection, cursor = self._connection()
        with connection:
            cursor.execute(sql_query, data)
        search = cursor.fetchone()
        return search is None

    def get_user_data(self, cod_profile: str):
        sql_query = self._load_query(r'data\database\queries\user\select\select_user_data.sql')
        data = (cod_profile,)
        connection, cursor = self._connection()
        with connection:
            cursor.execute(sql_query, data)
        search = cursor.fetchone()
        return {'username':search[0], 'text_model':search[1]}

    def insert_profile(self, user):
        sql_query_profile = self._load_query(r'data\database\queries\user\insert\insert_profile_data.sql')
        sql_query_credentials = self._load_query(r'data\database\queries\user\insert\insert_profile_credentials.sql')
        profile_data = (user.cod_profile, user.username)
        connection, cursor = self._connection()
        with connection:
            cursor.execute(sql_query_profile, profile_data)
            last_id = cursor.lastrowid

            profile_credentials = (last_id, user.password)
            cursor.execute(sql_query_credentials, profile_credentials)

    def authentication_user(self, cod_profile: str, password: str):
        sql_query = self._load_query(r'data\database\queries\user\auth\auth_login.sql')
        auth_data = (cod_profile, password)
        connection, cursor = self._connection()
        with connection:
            cursor.execute(sql_query, auth_data)
        search = cursor.fetchone()
        return search is not None

    def message_history(self, cod_profile: str):
        sql_messages = self._load_query(r'data\database\queries\chatbot\select\select_messages.sql')
        sql_profile_id = self._load_query(r'data\database\queries\user\select\select_profile_id.sql')
        connection, cursor = self._connection()
        with connection:
            cursor.execute(sql_profile_id, (cod_profile,))
            profile_id = cursor.fetchone()
            cursor.execute(sql_messages, profile_id)
        messages = cursor.fetchall()
        new_messages = [{'role': role, 'content': content} for role, content in messages]
        return new_messages

    def set_text_model(self, model: str, cod_profile: str):
        sql_query = self._load_query(r'data\database\queries\user\modify\update_text_model.sql')
        data = (model, cod_profile)
        connection, cursor = self._connection()

        with connection:
            cursor.execute(sql_query, data)
