# uppgift 4 webbshop test
import pytest
from my_app.uppg4_webbshop import *


def test_webbshop_create_product():
    # arrange
    expected_name = "Artikel"
    expected_price = 999
    expected_id = 1
    expected_result = expected_name + str(expected_price)+ str(expected_id)
    # act
    artikel = Product(expected_name, expected_price)
    actual_result = artikel.get_item_info_for_test()
    # assert
    assert expected_result == actual_result

def test_webbshop_cart_add_and_remove_items():
    # arrange
    product_name = "Artikel"
    product_price = 999
    artikel = Product(product_name, product_price)
    expected_result = product_name + str(product_price)
    # act
    cart = Shopping_cart()
    cart.add_product_to_cart(artikel)
    cart.add_product_to_cart(artikel)
    cart.remove_product_from_cart(artikel)
    actual_result = cart.get_cart_info_for_test()
    # assert
    assert actual_result == expected_result


def test_webbshop_create_order():
    product_name = "Artikel"

