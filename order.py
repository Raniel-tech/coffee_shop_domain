class Order:
    all = []

    def __init__(self, customer, coffee, price: float):
        self._customer = None
        self._coffee = None
        self._price = None

        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.all.append(self)

    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise TypeError("Order customer must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee     
    
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise TypeError("Order coffee must be a Coffee instance")
        self._coffee = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        
        if not (50.0 <= float(value) <= 1000.0):
            raise ValueError("Price must be between 50 and 1000")
        
        self._price = float(value)