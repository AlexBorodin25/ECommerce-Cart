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
            if product.product_id == product_id:
                self.items.remove(product)
                print(f"Removed {product.name} from cart.")
                return

        print("Not found in cart.")

    def add_discount(self, discount_code):
        discounts = {
            "SAVE10": 0.10,
            "SAVE20": 0.20,
            "SAVE30": 0.30,
        }

        if discount_code in discounts:
            self.discount = discounts[discount_code]
            print(f"Discount code {discount_code} applied.")
        else:
            print(f"Discount code {discount_code} not found.")

    def calculate_total(self):
        total = sum([product.price for product in self.items])

        if self.discount > 0:
            total -= total * self.discount

        return total

    def show_cart(self):
        if not self.items:
            print("No items in cart.")
            return

        print("Your Cart:")
        for product in self.items:
            print(product)

        print(f"Total price: ${self.calculate_total():.2f}")

def load_products(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    products = []

    for item in data:
        product = Product(item["id"], item["name"], item["price"])
        products.append(product)

    return products

def show_products(products):
    print("Available products:")
    for product in products:
        print(f"{product.product_id}. {product}")

def main():
   products = load_products("products.json")
   cart = Cart()

   while True:
       print("E-Commerce Cart Simulation")
       print("1. View products")
       print("2. Add products to cart")
       print("3. Remove products from cart")
       print("4. Apply discount")
       print("5. Show cart")
       print("6. Exit")

       choice = int(input("Enter your choice: "))

       if choice == 1:
           show_products(products)

       elif choice == 2:
           show_products(products)
           product_id = int(input("Enter product id to add: "))

           product_found = None
           for product in products:
               if product.product_id == product_id:
                   product_found = product
                   break

           if product_found:
               cart.add_item(product_found)
           else:
               print("Product not found.")

       elif choice == 3:
           product_id = int(input("Enter product id to remove: "))
           cart.remove_item(product_id)

       elif choice == 4:
           discount_code = input("Enter discount code: ")
           cart.add_discount(discount_code)

       elif choice == 5:
           cart.show_cart()

       elif choice == 6:
           print("Exiting...")
           break

       else:
           print("Invalid choice.")

if __name__ == "__main__":
    main()