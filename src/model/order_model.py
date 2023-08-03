class OrderModel:
    """Class to store and manage an Order object from database"""
    next_order_id = 0
    def __init__(self, order_id, date, customer_id, total, is_complete, sales_items):
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
        if isinstance(sales_items, str):
            self.sales_items = {}
            for pair in sales_items.split(','):
                item, amount = pair.split('=')
                self.sales_items[item] = amount
        else:
            self.sales_items = dict(sales_items)

    def to_sql(self) -> list:
        """Return SQL table compatible list of values"""
        item_dict = ','.join([f'{k}={v}' for k,v in self.sales_items.items()])
        return f'{self.order_id!r}, {self.date!r}, {self.customer_id!r}, {self.total!r}, ' \
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
