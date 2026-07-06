import json

from eCommerceCart import Product, Cart, load_products, show_products

def test_product():
    product = Product(1, "Jacket", 99.99)

    assert product.product_id == 1
    assert product.name == "Jacket"
    assert product.price == 99.99

def test_add_item():
    cart = Cart()
    product = Product(1, "Jacket", 99.99)

    cart.add_item(product)

    assert len(cart.items) == 1
    assert cart.items[0] == product

def test_remove_item():
    cart = Cart()
    product = Product(1, "Jacket", 99.99)

    cart.add_item(product)
    cart.remove_item(1)

    assert len(cart.items) == 0

def test_add_discount():
    cart = Cart()

    cart.add_discount("SAVE10")

    assert cart.discount == 0.10

def test_calculate_total():
    cart = Cart()
    cart.add_item(Product(1, "Jacket", 99.99))
    cart.add_discount("SAVE10")

    assert cart.calculate_total() == 89.991

def test_show_empty_cart(capsys):
    cart = Cart()

    cart.show_cart()

    captured = capsys.readouterr()
    assert "No items in cart." in captured.out

def test_show_cart(capsys):
    cart = Cart()
    cart.add_item(Product(1, "Jacket", 99.99))

    cart.show_cart()

    captured = capsys.readouterr()
    assert "Your Cart:" in captured.out
    assert "Jacket - $99.99" in captured.out
    assert "Total price: $99.99" in captured.out

def test_load_products(tmp_path):
    product_data = [
        {"id": 1, "name": "Jacket", "price": 99.99},
        {"id": 2, "name": "Pants", "price": 39.99},
    ]

    file_path = tmp_path / "products.json"

    with open(file_path, "w") as f:
        json.dump(product_data, f)

    products = load_products(file_path)

    assert len(products) == 2
    assert products[0].product_id == 1
    assert products[0].name == "Jacket"
    assert products[0].price == 99.99
    assert products[1].product_id == 2
    assert products[1].name == "Pants"
    assert products[1].price == 39.99

def test_show_products(capsys):
    products = [
        Product(1, "Jacket", 99.99),
        Product(2, "Pants", 39.99),
    ]

    show_products(products)
    captured = capsys.readouterr()
    assert "Available products:" in captured.out
    assert "1. Jacket - $99.99" in captured.out
    assert "2. Pants - $39.99" in captured.out

def test_product_format():
    product = Product(1, "Jacket", 99.99)

    assert str(product) == "Jacket - $99.99"

def test_invalid_discount(capsys):
    cart = Cart()

    cart.add_discount("WRONG")

    captured = capsys.readouterr()
    assert cart.discount == 0
    assert "Discount code WRONG not found." in captured.out