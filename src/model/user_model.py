import re


def validate_email(email):
    """Validate email, only validates lowercase"""
    return bool(re.match(r'[a-z0-9]+@[a-z0-9]+\.[a-z0-9]', email.lower()))


class UserModel:
    """Class to store and manage a User object from database"""
    next_user_id = 0
    def __init__(self, email, first_name, last_name, role, password_hash, order_id: list):   # pylint: disable=too-many-arguments
        self.user_id = UserModel.next_user_id
        UserModel.next_user_id += 1
        if not validate_email(email):
            raise ValueError('Email is not valid: '+str(email))
        self.email = email
        self.first_name = first_name.strip().capitalize()
        self.last_name = last_name.strip().capitalize()
        # TODO: Check that role is in valid range of enums
        self.role = role
        # Password should be hashed by client before being sent to server
        self.password_hash = password_hash
        self.order_id = order_id  # TODO: determine where is string and where is list

    @property
    def orders(self) -> str:
        """SQL VARCHAR version of orders"""
        return ','.join(self.order_id)

    def to_list(self) -> list:
        """Return SQL table compatible list of values"""
        return [self.user_id, self.email, self.first_name, self.last_name,
                self.role, self.password_hash, self.orders]

    #TODO: add methods for handling orders (add, search, etc.)
