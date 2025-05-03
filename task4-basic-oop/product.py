from random import randint
import collections

class product:
    """"
    here we gona look our invetory management
    """
    def __init__(self,id:int, name:str,price:int,quantity:int):
        """"
        amoung the properties we have ther is :
        name,price,quantity
        while attributes ther is :
        addd,remove,total value,display
        """
        self.name=name
        self.id = id
        self.price=price
        self.quantity=quantity
        if not isinstance(name,str):
            raise TypeError("name should be a string")
        if not isinstance(price,int):
            raise ValueError("price should be interger")
    def __str__(self):
        return (f"Id: {self.id} \n name: {self.name}\n price: {self.price}\n Qty: {self.quantity} \n Total Value: {self.total_value()}")
    # def add(self,amount:int):
    #     """
    #     add stock to the inventory
    #     """
    #     if amount<0:
    #         raise ValueError("amount shoulbe greater than zero") 
    #     self.quantity+=amount
    # def remove(self,amount:int):
    #     """"
    #     remove stock from invetory 
    #     """
    #     if amount <0:
    #         raise ValueError("amount should be greater than zero")
    #     if amount>self.quantity:
    #         raise ValueError("not enough money to remove from")
    #     self.quantity-=amount
    def total_value(self)->float:
        """"
        calculate the total value of current stock
        """
        return self.price*self.quantity
    def display(self):
        """"
        prints out my product details
        """
        print(f"product name:{self.name}")
        print(f"price:{self.price}")
        print(f"quantity:{self.quantity}")
        print(f"total invetory value:{self.total_value():.2f}") 
        
        
        
class inventory:
    def __init__(self):
        # self.name = name
        self.inventory = []
        # self.price = price
        # self.quantity = quantity
    def add_product(self,product:product):
        self.inventory.append(product)
    def remove_product(self, id):
        ind =  0
        for i in self.inventory:
            if(i.id == id):
                del self.inventory[ind]
                print(i, "Deleted successfully!")
                break
            ind += 1
    def show_products(self):
        for product in self.inventory:
            print(product)
    
invent = inventory()

id = randint(0, 2000)
# id = int(input("Enter product id: "))
name = input("Please enter the name of the product: ")
price = int(input("enter the price: "))
qty = int(input("enter the quantity: "))
products = [
    product(id, name, price, qty),
    product(1, "pants", 5000, 3),
    product(2, "shirt", 532, 3),
    product(3, "phone", 788, 3),
    product(4, "vehicle", 5000, 3),
    ]

# product = input("Enter product with spaces: ")
# product = product.split(' ')
for i in products:
    invent.add_product(i)
invent.show_products()
invent.remove_product(4)
invent.show_products()