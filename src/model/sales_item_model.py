class SalesItemModel:
    """Class to store and manage a Sales Item object from database"""
    next_item_id = 0
    def __init__(self, item_id, name, stock, price, department_id):
        self.item_id = item_id
        self.name = name
        if stock < 0:
            raise ValueError('Cannot have negative stock: '+str(stock))
        self.stock = stock
        if price < 0.00:
            raise ValueError('Cannot have negative price: '+str(price))
        self.price = price
        self.department_id = department_id

    def to_sql(self) -> list:
        """Convert python object into SQL row of values"""
        return f'{self.item_id!r}, {self.name!r}, {self.stock!r}, ' \
               f'{self.price!r}, {self.department_id!r}'

    @classmethod
    def from_sql(cls, sql_row):
        """Return python object from SQL row"""
        return cls(*sql_row)

    @staticmethod
    def next_id():
        """Return the next available Order ID"""
        next_id = SalesItemModel.next_item_id
        SalesItemModel.next_item_id += 1
        return next_id
