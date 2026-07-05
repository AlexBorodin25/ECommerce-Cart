import json

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class Cart:
    def __init__(self):
        self.items = []
        self.discount = 0

    def add_item(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart.")

    def remove_item(self, product_id):
        for product in self.items:
            if product.product.id == product_id:
                self.items.remove(product)
                print(f"Removed {product.name} from cart.")
                return
