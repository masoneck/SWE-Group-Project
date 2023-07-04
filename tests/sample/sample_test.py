import unittest

class SampleUnitTest(unittest.TestCase):
    """Example testing class"""

    def test_example_run(self):
        """An example run of a test"""
        self.assertTrue(2 + 2 == 4)
        sentence = 'hello'+'world'
        self.assertFalse(sentence == 'somethingelse')
        with self.assertRaises(ValueError):
            raise ValueError('This is just a fake error.')
