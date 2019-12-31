import random

class Pionek:
    def __init__(self):
        self.x = 0
        self.y = 0

    def umiesc_w_losowym_miejscu(self, plansza_wymiar_x, plansza_wymiar_y):
        self.x = random.randrange(0, plansza_wymiar_x)
        self.y = random.randrange(0, plansza_wymiar_y)

    def przesun(self, kierunek):
        # TODO: nie pozwolić na wyjście poza planszę (trzeba pojakoś poznać wymiary planszy)
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

def plansza_jako_string(pionki, plansza_wymiar_x, plansza_wymiar_y):
    #s = ""
    #for x in range(plansza_wymiar_y):
    #    for y in range(plansza_wymiar_x):
    #        pass
    #        # TODO: jeśli pod tymi współrzędnymi jest pionek, dopisz do s 
    #        #  literę, która go reprezentuje. Jeśli nie ma - dopisz kropkę.
    #        #  Zakładamy, że w tym samym miejscu jest tylko jeden pionek.
    #        #  Uwaga: może być potrzebna pętla for
    #    s += "\n"
    #return s
    
    s = ""
    for pionek in pionki:
        s += f"{pionek.imie}:\t\t{pionek.x}, {pionek.y}\n"
    return s

if __name__ == "__main__":
    pionki = [Wojownik("Janusz"), Wojownik("Grażyna"), Wojownik("Brajan"), Boss("Seba")]
    print(plansza_jako_string(pionki, 20, 20))
    print()
    for pionek in pionki:
        pionek.umiesc_w_losowym_miejscu(20, 20)
    print(plansza_jako_string(pionki, 20, 20))

