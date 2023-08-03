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
        """Test that a user can be created"""
        self.db.add_user('johndoe@gmail.com', 'John', 'Doe', [])
        users = self.db.select_user({'first_name': 'John', 'last_name': 'Doe'})
        self.assertTrue(len(users) == 1)
        self.assertTrue(users[0].first_name == 'John' and users[0].email == 'johndoe@gmail.com')
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

    def test_users_orders_are_formatted(self):
        """Test the formatting for a user's order_ids"""
        self.db.add_user('johndoe2@gmail.com', 'John', 'Doe', [1, 2])
        user = self.db.select_user({'email': 'johndoe2@gmail.com'})
        self.assertTrue(user[0].orders == [1,2])
