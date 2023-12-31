import unittest

from src.model.database import Database
from data.database_setup import setup_db, delete_db

DATABASE_FILE_NAME = 'data/unittest.db'

class DatabaseUnitTest(unittest.TestCase):
    """Test cases for model and database"""

    @classmethod
    def setUpClass(cls):
        setup_db(DATABASE_FILE_NAME)
        cls.db = Database(DATABASE_FILE_NAME)

    @classmethod
    def tearDownClass(cls):
        cls.db.close()
        delete_db(DATABASE_FILE_NAME)

    def test_user_database(self):
        """Test interacting with users in database"""
        self.db.add_user('johndoe@gmail.com', 'John', 'Doe', [1,7])
        users = self.db.select_user({'first_name': 'John', 'last_name': 'Doe'})
        self.assertTrue(len(users) == 1)
        self.assertTrue(users[0].first_name == 'John' and users[0].email == 'johndoe@gmail.com' \
                        and users[0].orders == [1,7])
        self.db.delete_user({'email': 'johndoe@gmail.com'})
        users = self.db.select_all_users()
        self.assertTrue(len(users) == 0)

    def test_invalid_email_for_user(self):
        """Test invalid email being entered for user"""
        with self.assertRaises(ValueError):
            self.db.add_user('invalid?@b@de_ail.39', 'John', 'Doe', [])
        with self.assertRaises(ValueError):
            self.db.add_user('almost@agood_email', 'John', 'Doe', [])

    def test_sales_item_database(self):
        """Test interacting with sales items in database"""
        self.db.add_sales_item('Apple', 7, 12.34, 1)
        items = self.db.select_sales_item({'name': 'Apple', 'stock': 7})
        self.assertTrue(len(items) == 1)
        self.assertTrue(items[0].department_id == 1 and items[0].price == 12.34)
        self.db.delete_sales_item({'name': 'Apple'})
        items = self.db.select_all_sales_items()
        self.assertTrue(len(items) == 0)

    def test_invalid_parameters_for_sales_items(self):
        """Test that an error is raised for invalid inputs"""
        with self.assertRaises(ValueError):
            self.db.add_sales_item('Oranges', -11, 4.20, 2)
        with self.assertRaises(ValueError):
            self.db.add_sales_item('Oranges', 11, -4.20, 2)

    def test_order_database(self):
        """Test interacting with orders in database"""
        self.db.add_order('2023-01-29 12:34:59', 1, 16.04, True, {1:10,2:20,3:30})
        previous_orders = self.db.select_order({'is_complete': True})
        self.assertTrue(len(previous_orders) == 1)
        current_orders = self.db.select_order({'is_complete': False})
        self.assertTrue(len(current_orders) == 0)
        self.db.add_order('2024-11-19 01:02:30', 2, 90.01, False, {1:4})
        older_order = self.db.select_order({'order_id': 0})
        newer_order = self.db.select_order({'order_id': 1})
        self.assertTrue(older_order[0].date < newer_order[0].date)
        self.db.delete_order({'is_complete': True})
        all_orders = self.db.select_all_orders()
        self.assertTrue(len(all_orders) == 1)

    def test_discount_database(self):
        """Test interacting with discounts in database"""
        self.db.add_discount('FREEMONEY', 0.10)
        discounts = self.db.select_discount({'phrase': 'FREEMONEY'})
        self.assertTrue(len(discounts) == 1)
        self.assertTrue(discounts[0].amount == 0.10)
        self.db.delete_discount({'phrase': 'FREEMONEY'})
        all_discounts = self.db.select_all_discounts()
        self.assertTrue(len(all_discounts) == 0)

    def test_update_users_in_database(self):
        """Test updating a user's value"""
        self.db.add_user('wrong@email.com', 'Alice', 'Bob', [])
        self.db.update_user({'email': 'wrong@email.com'}, {'email': 'right@email.com'})
        user = self.db.select_user({'email':'right@email.com'})
        self.assertTrue(len(user) == 1)
        self.db.delete_user({'first_name': 'Alice', 'last_name': 'Bob'})
        all_users = self.db.select_all_users()
        self.assertTrue(len(all_users) == 0)

    def test_update_sales_items_in_database(self):
        """Test updating a sales item's value"""
        self.db.add_sales_item('Toothpaste', 3, 2.10, 3)
        self.db.update_sales_item({'name': 'Toothpaste'}, {'stock': 25})
        sales_item = self.db.select_sales_item({'name':'Toothpaste', 'price': 2.10})
        self.assertTrue(len(sales_item) == 1)
        self.db.delete_sales_item({'name': 'Toothpaste', 'stock': 25})
        all_sales_items = self.db.select_all_sales_items()
        self.assertTrue(len(all_sales_items) == 0)
