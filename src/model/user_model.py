import re


def validate_email(email):
    """Validate email, only validates lowercase"""
    return bool(re.match(r'[a-z0-9]+@[a-z0-9]+\.[a-z0-9]', email.lower()))


class UserModel:
    """Class to store and manage a User object from database"""
    next_user_id = 0
    def __init__(self, user_id, email, first_name, last_name, orders):
        self.user_id = user_id
        if not validate_email(email):
            raise ValueError('Email is not valid: '+str(email))
        self.email = email
        self.first_name = first_name.strip().capitalize()
        self.last_name = last_name.strip().capitalize()
        self.orders = orders if isinstance(orders, list) else \
                         [int(oid.strip()) for oid in orders.split(',')]

    def to_sql(self) -> list:
        """Convert python object into SQL row of values"""
        order_ids = ','.join([str(o) for o in self.orders])
        return f'{self.user_id!r}, {self.email!r}, {self.first_name!r}, {self.last_name!r}, ' \
               f'{order_ids!r}'

    @classmethod
    def from_sql(cls, sql_row):
        """Return python object from SQL row"""
        return cls(*sql_row)

    @staticmethod
    def next_id():
        """Return the next available User ID"""
        next_id = UserModel.next_user_id
        UserModel.next_user_id += 1
        return next_id
