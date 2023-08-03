
import string
import random

class DiscountModel:
    """Class to store and manage a Discountphrase object from database"""
    def __init__(self, phrase: str, amount: float):
        self.phrase = phrase
        self.amount = amount

    def to_sql(self):
        """Convert python object into SQL row of values"""
        return f'{self.phrase!r}, {self.amount!r}'

    @classmethod
    def from_sql(cls, sql_row):
        """Return python object from SQL row"""
        return cls(*sql_row)

    @classmethod
    def generate_phrase(cls, amount, length=5):
        """Generate a discount phrase with a random phrase"""
        phrase = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        return cls(phrase, amount)
