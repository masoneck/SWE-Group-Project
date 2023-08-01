class SalesItemModel:
    """Class to store and manage a Sales Item object from database"""
    next_item_id = 0
    def __init__(self, name, stock, price, department_id):
        self.item_id = SalesItemModel.next_item_id
        SalesItemModel.next_item_id += 1
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
        return [self.item_id, self.name, self.stock, self.price, self.department_id]
