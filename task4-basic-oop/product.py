
import collections
class inventory:
    def __init__(self):
        # self.name = name
        self.inventory = collections.defaultdict(list)
        # self.price = price
        # self.quantity = quantity
    def add_product(self, name, price, quantity):
        self.inventory[name] = [name, price, quantity]
    def remove_product(self, name):
        del self.inventory[name]
    def show_products(self):
        for product in self.inventory.items():
            print(product)
    
p = inventory()
product = input("Enter product with spaces: ")
product = product.split(' ')
p.add_product(product[0], product[1], product[2])
p.show_products()
 