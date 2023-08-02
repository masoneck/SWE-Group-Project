import re


def validate_email(email):
    """Validate email, only validates lowercase"""
    return bool(re.match(r'[a-z0-9]+@[a-z0-9]+\.[a-z0-9]', email.lower()))


class UserModel:
    """Class to store and manage a User object from database"""
    next_user_id = 0
    def __init__(self, user_id, email, first_name, last_name, role, password_hash, order_ids: list):   # pylint: disable=too-many-arguments
        self.user_id = user_id
        if not validate_email(email):
            raise ValueError('Email is not valid: '+str(email))
        self.email = email
        self.first_name = first_name.strip().capitalize()
        self.last_name = last_name.strip().capitalize()
        # TODO: Check that role is in valid range of enums
        self.role = role
        # Password should be hashed by client before being sent to server
        self.password_hash = password_hash
        self.order_ids = order_ids  # TODO: determine where is string and where is list

    @property
    def orders(self) -> str:
        """SQL VARCHAR version of orders"""
        return ','.join([str(oid) for oid in self.order_ids]) \
            if isinstance(self.order_ids, list) else self.order_ids

    def to_sql(self) -> list:
        """Convert python object into SQL row of values"""
        print(f'debug::orders::{self.orders!r}')
        return f'{self.user_id!r}, {self.email!r}, {self.first_name!r}, {self.last_name!r}, ' \
                f'{self.role!r}, {self.password_hash!r}, {self.orders!r}'

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

    #TODO: add methods for handling orders (add, search, etc.)
