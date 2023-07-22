import sqlite3

class Database:

    def __init__(self, db_file_name):
        conn = sqlite3.connect(db_file_name)
        self._cursor = conn.cursor()

    def select_user(self, query: dict):
        """Select a user from the database"""
        self._cursor.execute(f"""
        SELECT * FROM Users WHERE {', '.join([f'{k}={v}' for k,v in query.items()])}
        """)

