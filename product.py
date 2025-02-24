#product.py
class Product:
    def __init__(self,name,price,quantity):
        self.name=name 
        self.price=price
        self.quantity=quantity

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
    
    def update_quantity(self,updated_quantity):
        self.quantity= updated_quantity
        print(f" Updated Quantity: {self.quantity}")