class Pies:
    rasa = "mieszaniec"
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return f"Pies rasy {self.rasa}, x={self.x}, y={self.y}"

    def biegnij(self):
        self.x += 1
        self.y += 1

    def zjedz_karme(self, karma):
        pass

    def daj_glos(self):
        print("Hau hau!")

class Lagotto(Pies):  # to jest ta rasa psów, która znajduje trufle
    rasa = "Lagotto"
    def znajdz_trufle(self):
        return "Trufla"

class Haski(Pies):
    rasa = "Haski"
    def daj_glos(self):
        print("Uuuola!")

class Hart(Pies):
    rasa = "Hart"
    def biegnij(self):
        super().biegnij()
        super().biegnij()
        super().biegnij()

azor = Pies()
print(azor)
azor.biegnij()
print(azor)
azor.daj_glos()

dzuseppe = Lagotto()
print(dzuseppe)
dzuseppe.daj_glos()
print(dzuseppe.znajdz_trufle())

tajga = Haski()
print(tajga)
tajga.daj_glos()

szybki = Hart()
print(szybki)
szybki.biegnij()
print(szybki)