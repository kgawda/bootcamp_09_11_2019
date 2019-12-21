class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f"Produkt {self.name!r}, id: {self.id}, cena: {self.price} PLN")

def test_product_init():
    product = Product(1, 'Woda', 10.99)
    assert product.id == 1
    assert product.name == 'Woda'
    assert product.price == 10.99

def test_print_info(capsys):
    product = Product(1, 'Woda', 10.99)
    product.print_info()
    captured = capsys.readouterr()
    assert captured.out == "Produkt 'Woda', id: 1, cena: 10.99 PLN\n"

if __name__ == "__main__":
    product = Product(1, 'Woda', 10.99)
    product.print_info()