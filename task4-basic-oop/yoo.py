class product:
    """"
    here we gona look our invetory management
    """
    def __init__(self,name:str,price:int,quantity:int):
        """"
        amoung the properties we have ther is :
        name,price,quantity
        while attributes ther is :
        addd,remove,total value,display
        """
        self.name=name
        self.price=price
        self.quantity=quantity
        if not isinstance(name,str):
            raise TypeError("name should be a string")
        if not isinstance(price,int):
            raise ValueError("price should be interger")
    def add(self,amount:int):
        """
        add stock to the inventory
        """
        if amount<0:
            raise ValueError("amount shoulbe greater than zero") 
        self.quantity+=amount
    def remove(self,amount:int):
        """"
        remove stock from invetory 
        """
        if amount <0:
            raise ValueError("amount should be greater than zero")
        if amount>self.quantity:
            raise ValueError("not enough money to remove from")
        self.quantity-=amount
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
a=product(p1,p2,p3,p4,p5)
a.add(5)
a.remove(3)
a.total_value()
a.display()
