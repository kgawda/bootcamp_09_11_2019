import przystanki
#import pojazdy.szynowe
#import pojazdy.kolowe
from pojazdy import szynowe, kolowe

def main():
    linie = [
        szynowe.Tramwaj(1),
        szynowe.Tramwaj(2),
        kolowe.Autobus(105),
        kolowe.Autobus(501),
    ]
    print(przystanki.zbuduj_rozklad(linie))

if __name__ == "__main__":
    main()