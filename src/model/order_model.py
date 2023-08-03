class OrderModel:
    """Class to store and manage an Order object from database"""
    next_order_id = 0
    def __init__(self, order_id, date, customer_id, total, is_complete, items):
        self.order_id = order_id
        self.date = date
        self.customer_id = customer_id
        if total < 0.00:
            raise ValueError('Cannot have negative total amount: '+str(total))
        self.total = total
        if isinstance(is_complete, str):
            self.is_complete = is_complete.upper() == 'TRUE'
        else:
            self.is_complete = is_complete
        if isinstance(items, str):
            self.items = {}
            for pair in items.split(','):
                item, amount = pair.split('=')
                self.items[item] = amount
        else:
            self.items = dict(items)

    def to_sql(self) -> list:
        """Return SQL table compatible list of values"""
        item_dict = ','.join([f'{k}={v}' for k,v in self.items])
        return f'{self.order_id!r}, {self.date!r}, {self.total!r}, ' \
               f'{str(self.is_complete).upper()}, {item_dict!r}'

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
