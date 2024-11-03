"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from _pytest.python_api import raises


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(
            self,
            product
    ):
        assert product.check_quantity(1000) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(1001) is False
        assert product.check_quantity(1) is True

    def test_product_buy(
            self,
            product
    ):
        product.buy(2)
        assert product.quantity == 998

    def test_product_buy_more_than_available(
            self,
            product
    ):
        with pytest.raises(ValueError, match="Нет продукта book в наличии"):
            product.buy(1001)


class TestCart:
    def test_add_product(
            self,
            cart,
            product
    ):
        cart.add_product(product, 2)
        assert cart.products[product] == 2

    def test_add_same_product_multiple_times(self,
            cart,
            product):
        cart.add_product(product, 2)
        cart.add_product(product, 3)
        assert cart.products[product] == 5

    def test_add_multiple_different_products(self,
            cart,
            product,
            another_product):
        cart.add_product(product, 2)
        cart.add_product(another_product, 1)
        assert cart.products[product] == 2
        assert cart.products[another_product] == 1

    def test_remove_product_no_count(self,
            cart,
            product):
        cart.add_product(product, 4)
        cart.remove_product(product)
        assert product not in cart.products

    def test_remove_product_less_than_in_cart(self,
            cart,
            product):
        cart.add_product(product, 5)
        cart.remove_product(product, 3)
        assert cart.products[product] == 2

    def test_remove_product_equal_to_in_cart(self,
            cart,
            product):
        cart.add_product(product, 5)
        cart.remove_product(product, 5)
        assert product not in cart.products

    def test_remove_product_more_than_in_cart(self,
            cart,
            product):
        cart.add_product(product, 2)
        cart.remove_product(product, 5)
        assert product not in cart.products

    def test_remove_one_of_multiple_products(self,
            cart,
            product,
            another_product):
        cart.add_product(product, 4)
        cart.add_product(another_product, 3)
        cart.remove_product(product, 4)
        assert product not in cart.products
        assert another_product in cart.products

    def test_clear_cart(
            self,
            cart,
            product
    ):
        cart.add_product(product, 1)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self,
            cart,
            product,
            another_product):
        product.price = 123
        another_product.price = 456
        cart.add_product(product, 2)
        cart.add_product(another_product, 3)
        assert cart.get_total_price() == 123 * 2 + 456 * 3

    def test_get_total_price_(self,
            cart,
            product,
            another_product):
        product.price = 99.99
        cart.add_product(product, 3)

        another_product.price = 149.49
        cart.add_product(another_product, 2)

        expected_total_price = (99.99 * 3) + (149.49 * 2)
        assert abs(cart.get_total_price() - expected_total_price) < 0.01

    def test_buy_products(self,
            cart,
            product,
            another_product):
        product.quantity = 1000
        another_product.quantity = 500
        cart.add_product(product, 2)
        cart.add_product(another_product, 3)
        cart.buy()
        assert product.quantity == 998
        assert another_product.quantity == 497
        assert len(cart.products) == 0

    def test_buy_insufficient_quantity(self,
            cart,
            product,
            another_product):
        product.quantity = 1
        another_product.quantity = 2
        cart.add_product(product, 2)
        cart.add_product(another_product, 1)
        with raises(ValueError, match="Недостаточно товара в наличии"):
            cart.buy()

        assert cart.products[product] == 2
        assert cart.products[another_product] == 1
