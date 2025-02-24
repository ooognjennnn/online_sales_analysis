#product_manager.py
from product import Product # Uvozimo klasu Product iz product.py

class ProductManager:
    def __init__(self):
        self.products = [] # Lista proizvoda

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added to the inventory")

    def display_all_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                product.display_info()


    def total_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        return total