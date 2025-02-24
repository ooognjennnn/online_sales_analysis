#main.py
from product_manager import ProductManager
from product import Product

if __name__ == "__main__":
    manager = ProductManager()

    # Dodavanje proizvoda
    manager.add_product(Product("Laptop", 999.99, 5))
    manager.add_product(Product("Smartphone", 499.99, 10))

    # Prikaz proizvoda
    print("Available Products:")
    manager.display_all_products()

    # Ukupna vrednost inventara
    total = manager.total_value()
    print(f"Total Inventory Value: ${total:.2f}")