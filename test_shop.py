"""
Протестируйте классы из модуля homework/models.py
"""
import pytest


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(1000) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(1001) is False
        assert product.check_quantity(1) is True

    def test_product_buy(self, product):
        product.buy(2)
        assert product.quantity == 998

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError, match="Нет продукта book в наличии"):
            product.buy(1001)
            assert product.check_quantity(1000)


class TestCart:
    def test_add_product(self, cart, product):
        cart.add_product(product, 2)
        assert cart.products[product] == 2

    def test_add_few_products(self, cart, product):
        cart.add_product(product, 4)
        assert cart.products[product] == 4

    def test_remove_one_product(self, cart, product):
        cart.remove_product(product, 4)
        assert product not in cart.products

    def test_clear_cart(self, cart, product):
        cart.add_product(product, 1)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 2)
        assert cart.get_total_price() == 200

    def test_buy_products(self, cart, product):
        cart.add_product(product, 2)
        cart.buy()
        assert product.quantity == 998
