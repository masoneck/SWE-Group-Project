import unittest

from src.model.database import Database
from data.database_setup import setup_db

class DatabaseUnitTest(unittest.TestCase):
    """Example testing class"""

    @classmethod
    def setUpClass(cls):
        setup_db('data/unittest.db')
        cls.db = Database('data/unittest.db')

    @classmethod
    def tearDownClass(cls):
        # TODO: close connection, delete db

    def test_select_user(self):
        """Test that a user can be created"""
        users = self.db.select_user({'user_id': 1})
        self.assertTrue(len(users) == 0)
