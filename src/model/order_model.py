from src.model.user_model import validate_email

class OrderModel:
    """Class to store and manage an Order object from database"""
    next_order_id = 0
    def __init__(self, date, customer_email: str, total: float, sales_items: dict):
        self.order_id = OrderModel.next_order_id
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
    
    def to_list(self) -> list:
        """Return SQL table compatible list of values"""
        return [self.order_id, self.date, self.total, self.items]