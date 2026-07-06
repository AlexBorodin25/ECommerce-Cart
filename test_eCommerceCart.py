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
