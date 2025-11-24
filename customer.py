class Customer:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name my be string")
        
        value = value.strip()
        if len(value) == 0 or len(value) > 15:
            raise ValueError("Customer name must be 1 to 15 characters long")
        
        self._nmae = value
    
    def orders(self):
        from order import Order
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        unique = []
        for order in self.orders():
            if order.coffee not in unique:
                unique.append(order.coffee)
        return unique
    
    def create_order(self, coffee, price: float):
        from order import Order
        return Order(self, coffee, price)   
    

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order     
        totals = {}
        for order in Order.all:
            if order.coffee is coffee:
                totals.setdefault(order.customer, 0)
                totals[order.customer] += order.price 
        
        if not totals:
            return None
        
        return max(totals.items(), key=lambda pair: pair[1])[0]