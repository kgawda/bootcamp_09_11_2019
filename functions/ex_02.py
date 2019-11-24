def wiecej_niz(napis, liczba):
    ilosc_wystapien = {}
    for litera in napis:
        ilosc_wystapien[litera] = ilosc_wystapien.get(litera, 0) + 1

    wybrane = set()
    for litera, wystapienia in ilosc_wystapien.items():
        if wystapienia > liczba:
            wybrane.add(litera)
    return wybrane

def test_pusty_string():
    assert wiecej_niz('', 0) == set()
    assert wiecej_niz('', 3) == set()

def test_brak_powtorzen():
    assert wiecej_niz('abcdefghij', 1) == set()

def test_powtorzenia_dla_wiecej_niz_0():
    assert wiecej_niz('ala ma kota a kot ma ale', 0) == {'m', 'o', 'e', 'a', 'l', ' ', 'k', 't'}

def test_powtorzenia_dla_wiecej_niz_3():
    assert wiecej_niz('ala ma kota a kot ma ale', 3) == {'a', ' '}


if __name__ == "__main__":
    napis = input("Podaj tekst: ")
    ilosc = int(input("Podaj ilosc: "))
    print(wiecej_niz(napis, ilosc))