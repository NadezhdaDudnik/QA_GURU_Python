class Product:

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        return self.quantity >= quantity

    def buy(self, quantity):
        if not self.check_quantity(quantity):
            raise ValueError(f"Нет продукта {self.name} в наличии")
        self.quantity -= quantity

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        if product in self.products:
            if remove_count is None or remove_count >= self.products[product]:
                del self.products[product]
            else:
                self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> int:
        summa = 0
        for product, count in self.products.items():
            summa += product.price * count
        return summa

    def buy(self):
        for product, count in self.products.items():
            if not product.check_quantity(count):
                raise ValueError(f"Нет продукта {self.name} в наличии")
            else:
                product.buy(count)
