import random

class Pionek:
    def __init__(self):
        self.x = 0
        self.y = 0

    def umiesc_w_losowym_miejscu(self, plansza_wymiar_x, plansza_wymiar_y):
        self.x = random.randrange(0, plansza_wymiar_x)
        self.y = random.randrange(0, plansza_wymiar_y)

    def przesun(self, kierunek, plansza_wymiar_x=None, plansza_wymiar_y=None):
        if kierunek == 'w':
            if plansza_wymiar_y and self.y + 1 >= plansza_wymiar_y:
                return
            self.y += 1
        elif kierunek == 's':
            if self.y - 1 < 0:
                return
            self.y -= 1
        elif kierunek == 'a':
            if self.x - 1 < 0:
                return
            self.x -= 1
        elif kierunek == 'd':
            if plansza_wymiar_x and self.x + 1 >= plansza_wymiar_x:
                return
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
    s = ""
    for y in range(plansza_wymiar_y - 1, -1, -1):
        for x in range(plansza_wymiar_x):
            for pionek in pionki:
                if pionek.x == x and pionek.y == y:
                    s += pionek.imie[0]
                    break
            else: # nie znaleziono pionka na tym polu
                s += '.'
        s += "\n"
    return s
    
    # s = ""
    # for pionek in pionki:
    #     s += f"{pionek.imie}:\t\t{pionek.x}, {pionek.y}\n"
    # return s

if __name__ == "__main__":
    wojownicy = [Wojownik("Janusz"), Wojownik("Grażyna"), Wojownik("Brajan"), Boss("Seba")]
    skarby = []
    apteczki = []
    pionki =  wojownicy + skarby + apteczki
    print(plansza_jako_string(pionki, 20, 20))
    print()
    for pionek in pionki:
        pionek.umiesc_w_losowym_miejscu(20, 20)
    print(plansza_jako_string(pionki, 20, 20))
    while True:
        ruch = input("Podaj ruch [w/s/a/d] lub q by wyjść: ")
        if ruch == 'q':
            break
        wojownicy[0].przesun(ruch, 20, 20)
        #for pionek in wojownicy[1:]:
        #   ... przesun losowo
        #   ... sprawdz czy kolizja
        print(plansza_jako_string(pionki, 20, 20))

