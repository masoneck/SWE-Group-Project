import unittest

from src.model.database import Database
from data.database_setup import setup_db, delete_db

class DatabaseUnitTest(unittest.TestCase):
    """Example testing class"""

    @classmethod
    def setUpClass(cls):
        # TODO: setup DB in :memory:
        setup_db('data/unittest.db')
        cls.db = Database('data/unittest.db')

    @classmethod
    def tearDownClass(cls):
        cls.db.close()
        delete_db('data/unittest.db')

    def test_user_database(self):
        """Test interacting with users in database"""
        self.db.add_user('johndoe@gmail.com', 'John', 'Doe', [1,7])
        users = self.db.select_user({'first_name': 'John', 'last_name': 'Doe'})
        self.assertTrue(len(users) == 1)
        self.assertTrue(users[0].first_name == 'John' and users[0].email == 'johndoe@gmail.com' \
                        and users[0].orders == [1,7])
        # TODO: add update test
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
        # TODO: add update test
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
        # TODO: add update test
        self.db.delete_order({'is_complete': True})
        all_orders = self.db.select_all_orders()
        self.assertTrue(len(all_orders) == 1)
