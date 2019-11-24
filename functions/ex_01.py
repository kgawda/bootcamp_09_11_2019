def czy_jest_pierwsza(liczba):
    if liczba <= 1:
        return False

    for x in range(2, liczba):
        if liczba % x == 0:
            return False

    return True

def test_mniejsza_od_2():
    assert czy_jest_pierwsza(1) == False

def test_nie_pierwsza_nieparzysta():
    assert czy_jest_pierwsza(9) == False

def test_nie_pierwsza_parzysta():
    assert czy_jest_pierwsza(10) == False

def test_pierwsza_2():
    assert czy_jest_pierwsza(2) == True

def test_pierwsza_wieksza_od_2():
    assert czy_jest_pierwsza(17) == True
