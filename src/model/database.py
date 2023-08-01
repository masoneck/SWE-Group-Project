import sqlite3

from src.model.user_model import UserModel
from src.model.sales_item_model import SalesItemModel

class Database:
    """Class to execute queries and statements."""

    def __init__(self, db_file_name):
        conn = sqlite3.connect(db_file_name)
        self._cursor = conn.cursor()

    def _select_query(self, table: str, query: dict, is_cursor=False):
        rows = self._cursor.execute(f"""
        SELECT * FROM {table.capitalize()} WHERE {', '.join([f'{k}={v!r}' for k,v in query.items()])}
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

    def _insert_statement(self, table: str, values: list, is_cursor=False):
        """Insert values into database table. Assumes values are in correct order"""
        rows = self._cursor.execute(f"""
        INSERT INTO {table.capitalize()} VALUES ({', '.join(values)})
        )""")
        return rows if is_cursor else rows.fetchall()

    def add_user(self, query: dict):
        """Add a user to database"""
        user = UserModel(**query)
        return self._insert_statement('Users', user.to_list())

    def add_sales_item(self, query: dict):
        """Add a sales item to the database"""
        sales_item = SalesItemModel(**query)
        return self._insert_statement('Items', sales_item.to_list())

    def close(self):
        """Close connection to database"""
        return self._cursor.connection.close() and self._cursor.close()
