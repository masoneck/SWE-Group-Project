import unittest

from src.model.database import Database
from src.model.user_model import UserModel
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
        """Test that a user can be created"""
        self.db.add_user('johndoe@gmail.com', 'John', 'Doe', 'customer', 'password', [])
        users = self.db.select_user({'first_name': 'John'})
        self.assertTrue(len(users) == 1)
        self.assertTrue(users[0].first_name == 'John')
        users = self.db.select_user({'first_name': 'Notjohn'})
        self.assertTrue(len(users) == 0)

    def test_invalid_email_for_user(self):
        """Test invalid email being entered for user"""
        with self.assertRaises(ValueError):
            self.db.add_user('invalid?@b@de_ail.39', 'John', 'Doe', 'customer', 'password', [])
        with self.assertRaises(ValueError):
            self.db.add_user('almost@agood_email', 'John', 'Doe', 'customer', 'password', [])

    def test_users_orders_are_formatted(self):
        """Test the formatting for a user's order_ids"""
        self.db.add_user('johndoe2@gmail.com', 'John', 'Doe', 'customer', 'password', [1, 2])
        user = self.db.select_user({'email': 'johndoe2@gmail.com'})
        raise Exception(user[0].orders)
        self.assertTrue(user[0].orders == '1,2')