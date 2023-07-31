import sqlite3

class Database:
    """Class to execute queries and statements."""

    def __init__(self, db_file_name):
        conn = sqlite3.connect(db_file_name)
        self._cursor = conn.cursor()

    def _select_query(self, table: str, query: dict, is_cursor=False):
        rows = self._cursor.execute(f"""
        SELECT * FROM {table.capitalize()} WHERE {', '.join([f'{k}={v}' for k,v in query.items()])}
        """)
        return rows if is_cursor else rows.fetchall()

    def select_user(self, query: dict):
        """Select a user from the database"""
        return self._select_query('Users', query)


    def select_sales_item(self, query: dict):
        """Select a sales item from the database"""
        return self._select_query('Items', query)

    def select_order(self, query: dict):
        """Select an order from the database"""
        return self._select_query('Orders', query)

    def close(self):
        """Close connection to database"""
        return self._cursor.connection.close() and self._cursor.close()
