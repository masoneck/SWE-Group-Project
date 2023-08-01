class SalesItemModel:
    """Class to store and manage a Sales Item object from database"""
    def __init__(self, name, stock, price, department_id):
        self.name = name
        if stock < 0:
            raise ValueError('Cannot have negative stock: '+str(stock))
        self.stock = stock
        if price < 0.00:
            raise ValueError('Cannot have negative price: '+str(price))
        self.price = price
        self.department_id = department_id

    def to_list(self) -> list:
        """Return SQL table compatible list of values"""
        return [self.name, self.stock, self.price, self.department_id]
