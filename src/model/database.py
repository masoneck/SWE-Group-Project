import sqlite3

from src.model.discount_model import DiscountModel
from src.model.order_model import OrderModel
from src.model.sales_item_model import SalesItemModel
from src.model.user_model import UserModel

class Database:
    """Class to execute queries and statements."""

    def __init__(self, db_file_name):
        conn = sqlite3.connect(db_file_name)
        self._cursor = conn.cursor()

    # --[ database statements ]-- #
    def _select_all_query(self, table: str):
        rows = self._cursor.execute(f"""SELECT * FROM {table.capitalize()}""")
        return rows.fetchall()

    def _select_query(self, table: str, query: dict):
        rows = self._cursor.execute(f"""
        SELECT * FROM {table.capitalize()} WHERE {' AND '.join([f'{k}={v!r}' for k,v in query.items()])}
        """)
        return rows.fetchall()

    def _insert_statement(self, table: str, statement: str):
        """Insert values into database table. Assumes values are in correct order"""
        rows = self._cursor.execute(f"""
        INSERT INTO {table.capitalize()} VALUES ({statement})
        """)
        return rows.fetchall()

    def _delete_statement(self, table: str, query: dict):
        """Delete row matching query from database"""
        rows = self._cursor.execute(f"""
        DELETE FROM {table} WHERE {' AND '.join([f'{k}={v!r}' for k,v in query.items()])}
        """)
        return rows.fetchall()

    # --[ read statements ]-- #
    def select_user(self, query: dict):
        """Select a user from the database"""
        rows = self._select_query('Users', query)
        return [UserModel.from_sql(row) for row in rows]

    def select_sales_item(self, query: dict):
        """Select a sales item from the database"""
        return self._select_query('Items', query)

    def select_order(self, query: dict):
        """Select an order from the database"""
        return self._select_query('Orders', query)

    def select_discount(self, query: dict):
        """Select a discount from the database"""
        return self._select_query('Discounts', query)

    def select_all_users(self):
        """Select all users from the database"""
        rows = self._select_all_query('Users')
        return [UserModel.from_sql(row) for row in rows]

    def select_all_sales_items(self):
        """Select all sales items from the database"""
        rows = self._select_all_query('Items')
        return [SalesItemModel.from_sql(row) for row in rows]

    def select_all_orders(self):
        """Select all orders from the database"""
        rows = self._select_all_query('Orders')
        return [OrderModel.from_sql(row) for row in rows]

    def select_all_discounts(self):
        """Select all discounts from the database"""
        rows = self._select_all_query('Discounts')
        return [DiscountModel.from_sql(row) for row in rows]

    # --[ create statements ]-- #
    def add_user(self, email, first_name, last_name, order_ids):
        """Add a user to database"""
        user_id = UserModel.next_id()
        user = UserModel(user_id, email, first_name, last_name, order_ids)
        return self._insert_statement('Users', user.to_sql())

    def add_sales_item(self, name, stock: int, price: float, department_id: int):
        """Add a sales item to the database"""
        item_id = SalesItemModel.next_id()
        sales_item = SalesItemModel(item_id, name, stock, price, department_id)
        return self._insert_statement('Items', sales_item.to_sql())

    def add_order(self, date, customer_id, total, is_complete, sales_items):
        """Add an order to the database"""
        order_id = OrderModel.next_id()
        order = OrderModel(order_id, date, customer_id, total, is_complete, sales_items)
        return self._insert_statement('Orders', order.to_sql())

    def add_discount(self, phrase, amount):
        """Add an order to the database"""
        discount = DiscountModel(phrase, amount)
        return self._insert_statement('Discounts', discount.to_sql())

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

    def delete_discount(self, query: dict):
        """Delete a discount from the database"""
        return self._delete_statement('Discounts', query)

    # --[ update statements ]-- #
    def update_user(self, query: dict, values: dict):
        """Update a user from the database"""
        pass

    def update_sales_item(self, query: dict, values: dict):
        """Update a sales item from the database"""
        pass

    def update_order(self, query: dict, values: dict):
        """Update an order from the database"""
        pass

    def update_discount(self, query: dict, values: dict):
        """Update a discount from the database"""
        pass

    def close(self):
        """Close connection to database"""
        return self._cursor.connection.close() and self._cursor.close()
