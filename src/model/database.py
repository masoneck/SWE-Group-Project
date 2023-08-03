import sqlite3

from src.model.user_model import UserModel
from src.model.sales_item_model import SalesItemModel
from src.model.order_model import OrderModel

class Database:
    """Class to execute queries and statements."""

    def __init__(self, db_file_name):
        conn = sqlite3.connect(db_file_name)
        self._cursor = conn.cursor()

    # --[ database statements ]-- #
    def _select_all_query(self, table: str, is_cursor=False):
        rows = self._cursor.execute(f"""SELECT * FROM {table.capitalize()}""")
        return rows if is_cursor else rows.fetchall()

    def _select_query(self, table: str, query: dict, is_cursor=False):
        rows = self._cursor.execute(f"""
        SELECT * FROM {table.capitalize()} WHERE {', '.join([f'{k}={v!r}' for k,v in query.items()])}
        """)
        return rows if is_cursor else rows.fetchall()

    def _insert_statement(self, table: str, statement: str, is_cursor=False):
        """Insert values into database table. Assumes values are in correct order"""
        rows = self._cursor.execute(f"""
        INSERT INTO {table.capitalize()} VALUES ({statement})
        """)
        return rows if is_cursor else rows.fetchall()

    def _delete_statement(self, table: str, query: dict, is_cursor=False):
        """Delete row matching query from database"""
        rows = self._cursor.execute(f"""
        DELETE FROM {table} WHERE {', '.join([f'{k}={v!r}' for k,v in query.items()])}
        """)
        return rows if is_cursor else rows.fetchall()

    # --[ read statements ]-- #
    def select_user(self, query: dict, is_raw=False):
        """Select a user from the database"""
        rows = self._select_query('Users', query, is_cursor=is_raw)
        return [UserModel.from_sql(row) for row in rows]

    def select_sales_item(self, query: dict):
        """Select a sales item from the database"""
        return self._select_query('Items', query)

    def select_order(self, query: dict):
        """Select an order from the database"""
        return self._select_query('Orders', query)

    def select_all_users(self, is_raw=False):
        """Select all users from the database"""
        rows = self._select_all_query('Users', is_cursor=is_raw)
        return [UserModel.from_sql(row) for row in rows]

    def select_all_sales_items(self, is_raw=False):
        """Select all sales items from the database"""
        rows = self._select_all_query('Items', is_cursor=is_raw)
        return [SalesItemModel.from_sql(row) for row in rows]

    def select_all_orders(self, is_raw=False):
        """Select all orders from the database"""
        rows = self._select_all_query('Orders', is_cursor=is_raw)
        return [OrderModel.from_sql(row) for row in rows]

    # --[ create statements ]-- #
    def add_user(self, email, first_name, last_name, order_ids):  # pylint: disable=too-many-arguments
        """Add a user to database"""
        user_id = UserModel.next_id()
        user = UserModel(user_id, email, first_name, last_name, order_ids)
        return self._insert_statement('Users', user.to_sql())

    def add_sales_item(self, name, stock: int, price: float, department_id: int):
        """Add a sales item to the database"""
        sales_item = SalesItemModel(name, stock, price, department_id)
        return self._insert_statement('Items', sales_item.to_sql())

    def add_order(self, date, customer_email: str, total: float, sales_items: dict):
        """Add an order to the database"""
        order = OrderModel(date, customer_email, total, sales_items)
        return self._insert_statement('Orders', order.to_sql())

    # --[ delete statements ]-- #
    def delete_user(self, query: dict):
        """Delete a user from the database"""
        return self._delete_statement('Users', query)

    def delete_sales_item(self, query: dict):
        """Delete a sales item from the database"""
        return self._delete_statement('Items', query)

    def delete_order(self, query: dict):
        """Delete an order from the database"""
        return self._delete_statement('Orders', query)
    
    # --[ update statements ]-- #
    def update_user(self, query: dict):
        """Update a user from the database"""
        pass

    def update_sales_item(self, query: dict):
        """Update a sales item from the database"""
        pass

    def update_order(self, query: dict):
        """Update an order from the database"""
        pass

    def close(self):
        """Close connection to database"""
        return self._cursor.connection.close() and self._cursor.close()
