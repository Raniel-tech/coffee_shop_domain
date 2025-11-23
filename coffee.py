class Coffee:    
    all = []

    def __init__(self, name: str):
        self._name = None
        self.name = name
        Coffee.all.append(self) 

    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be string")
        
        value = value.strip()
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long") 
        
        self._name = value  

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        unique = []
        for order in self.orders():
            if order.customer not in unique:
                unique.append(order.customer)
        return unique
    
    def num_orders(self):
        orders = self.orders()
        if not orders:
            return 0
        total = sum(order.price for order in orders)
        return total / len(orders)