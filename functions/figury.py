def polne_trapezu(wysokosc, podstawa1, podstawa2):
    """Funkcja licząca pole trapezu"""
    return wysokosc * (podstawa1 + podstawa2)/2

def pole_elipsy(promien, rozciagniecie=1):
    return (3.14 * kwadrat(promien)) * rozciagniecie

def kwadrat(n):
    return n ** 2



def test_pole_elipsy_z_rozciagnieciem():
    assert pole_elipsy(1, 2) == 3.14 * 2
    assert pole_elipsy(promien=1, rozciagniecie=2) == 3.14 * 2
    assert pole_elipsy(rozciagniecie=2, promien=1) == 3.14 * 2

def test_pole_elipsy_bez_rozciagnia():
    assert pole_elipsy(1) == pole_elipsy(1, 1) == 3.14
    assert pole_elipsy(promien=1) == pole_elipsy(1, 1) == 3.14
    # assert pole_elipsy(rozciagniecie=1) -- błąd

def test_argumenty_pozycyjne():
    assert polne_trapezu(10, 3, 6) == 45

def test_argumenty_nazwane():
    assert polne_trapezu(wysokosc=10, podstawa1=3, podstawa2=6) == 45

def test_argumenty_nazwane_nie_w_kolejnosci():
    assert polne_trapezu(podstawa2=6, wysokosc=10, podstawa1=3) == 45

def test_argumenty_nazwane_i_nie_nazwane():
    assert polne_trapezu(10, 3, podstawa2=6) == 45
    assert polne_trapezu(10, podstawa2=6, podstawa1=3) == 45
