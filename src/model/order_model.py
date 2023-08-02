from src.model.user_model import validate_email

class OrderModel:
    """Class to store and manage an Order object from database"""
    next_order_id = 0
    def __init__(self, date, customer_email: str, total: float, sales_items: dict):
        self.order_id = OrderModel.next_order_id
        self.date = date
        OrderModel.next_order_id += 1
        if not validate_email(customer_email):
            raise ValueError('Email is not valid: '+str(customer_email))
        self.customer_email = customer_email
        if total < 0.00:
            raise ValueError('Cannot have negative total amount: '+str(total))
        self.total = total
        self.sales_items = sales_items

    @property
    def items(self) -> str:
        """SQL VARCHAR version of sales items"""
        return ','.join([f'{k}={v}' for k,v in self.sales_items])

    def to_sql(self) -> list:
        """Return SQL table compatible list of values"""
        return f'{self.order_id!r}, {self.date!r}, {self.total!r}, {self.items!r}'

    @classmethod
    def from_sql(cls, sql_row):
        """Return python object from SQL row"""
        return cls(*sql_row)

    @staticmethod
    def next_id():
        """Return the next available Order ID"""
        next_id = OrderModel.next_order_id
        OrderModel.next_order_id += 1
        return next_id
