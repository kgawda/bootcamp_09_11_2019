import random

class Pionek:
    def __init__(self):
        self.x = 0
        self.y = 0

    #TODO def umiesc_w_losowym_miejscu

    def przesun(self, kierunek):
        if kierunek == 'w':
            self.y += 1
        elif kierunek == 's':
            self.y -= 1
        elif kierunek == 'a':
            self.x -= 1
        elif kierunek == 'd':
            self.x += 1

class Wojownik(Pionek):
    def __init__(self, imie):
        super().__init__()
        self.imie = imie
        self.punkty_zycia = 100

class Boss(Wojownik):
    def __init__(self, imie, punkty_zycia=200):
        super().__init__(imie)
        self.punkty_zycia = punkty_zycia

pionki = [Wojownik("Janusz"), Wojownik("Grażyna"), Wojownik("Brajan"), Boss("Seba")]
for pionek in pionki:
    print(f"{pionek.imie}:\t\t{pionek.x}, {pionek.y}")
print()
for _ in range(10):
    for pionek in pionki:
        pionek.przesun(random.choice("wsad"))
for pionek in pionki:
    print(f"{pionek.imie}:\t\t{pionek.x}, {pionek.y}")