class DiscountModel:
    """Class to store and manage a DiscountCode object from database"""
    def __init__(self, code: str, amount: float):
        self.code = code
        self.amount = amount

    def to_sql(self):
        """Convert python object into SQL row of values"""
        return f'{self.code!r}, {self.amount!r}'

    @classmethod
    def from_sql(cls, sql_row):
        """Return python object from SQL row"""
        return cls(*sql_row)
