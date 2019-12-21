class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f"Produkt {self.name!r}, id: {self.id}, cena: {self.price} PLN")

class Basket:
    def __init__(self):
        self._products = {}
        #self._total_price = 0

    def add_product(self, produkt, quantity):
        if produkt in self._products:  # key == produtk
            self._products[produkt] += quantity
        else:
            self._products[produkt] = quantity
        # self._total_price += ...

    def count_total_price(self):
        total_price = 0
        for product, quantity in self._products.items():
            total_price += product.price * quantity
        return total_price

    #def generate_report(self):

def test_basket_empty_price():
    b = Basket()
    assert b.count_total_price() == 0

def test_basket_one_product_price():
    b = Basket()
    p = Product(1, 'Woda', 10.00)
    b.add_product(p, 3)
    assert b.count_total_price() == 3 * 10

def test_basket_multiple_products_price():
    b = Basket()
    woda = Product(1, 'Woda', 10.00)
    chleb = Product(2, 'Chleb', 20.00)
    b.add_product(woda, 3)
    b.add_product(chleb, 1)
    b.add_product(woda, 1)
    assert b.count_total_price() == 4 * 10 + 1 * 20
