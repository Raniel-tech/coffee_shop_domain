from customer import Customer
from coffee import Coffee
from order import Order 

c1 = Customer("Raniel")
c2 = Customer("Daniel")
c3 = Customer("Ana")

latte = Coffee("Latte")
espresso = Coffee("Espresso")
mocha = Coffee("Mocha")

o1 = Order(c1, latte, 450.0)
o2 = Order(c1, espresso, 300.0)
o3 = Order(c2, latte, 500.0)
o4 = Order(c3, mocha, 700.0)

print("Customer c1 orders:", [o.price for o in c1.orders()])
print("Customer c1 coffees:", [c.name for c in c1.coffees()])

print("Customer c2 orders:", [o.price for o in c2.orders()])
print("Customer c2 coffees:", [c.name for c in c2.coffees()])

print("Customer c3 orders:", [o.price for o in c3.orders()])
print("Customer c3 coffees:", [c.name for c in c3.coffees()])

print("Latte orders:", [o.price for o in latte.orders()])
print("Espresso orders:", [o.price for o in espresso.orders()])
print("Mocha orders:", [o.price for o in mocha.orders()])

print("Latte customers:", [c.name for c in latte.customers()])
print("Espresso customers:", [c.name for c in espresso.customers()])
print("Mocha customers:", [c.name for c in mocha.customers()])
