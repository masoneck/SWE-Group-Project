import unittest

from src.model.database import Database
from data.database_setup import setup_db, delete_db

class DatabaseUnitTest(unittest.TestCase):
    """Example testing class"""

    @classmethod
    def setUpClass(cls):
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
        users = self.db.select_user({'first_name': 'Notjohn'})
        self.assertTrue(len(users) == 0)
