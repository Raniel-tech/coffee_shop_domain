from customer import Customer
from coffee import Coffee
import customer
from order import Order 

c1 = Customer("Raniel, str")
c2 = Customer("Daniel, str")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

o1 = Order(c1, latte, 450)
o2 = Order(c1, espresso, 300)
o3 = Order(c2, latte, 500)

print("Customer c1 orders:", [o.price for o in c1.orders()])
print("Customer c1 coffees:", [c.name for c in c1.coffees()])

print("Customer c2 orders:", [o.price for o in c2.orders()])
print("Customer c2 coffees:", [c.name for c in c2.coffees()])

print("Latte orders:", [o.price for o in latte.orders()])
print("Espresso orders:", [o.price for o in espresso.orders()])

print("Latte customers:", [c.name for c in latte.customers()])
