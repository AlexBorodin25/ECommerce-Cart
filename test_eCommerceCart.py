import json

from eCommerceCart import Product, Cart, load_products, show_products

def test_product():
    product = Product(1, "Jacket", 99.99)

    assert product.product_id == 1
    assert product.name == "Jacket"
    assert product.price == 99.99