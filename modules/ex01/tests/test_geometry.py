from mathematica.geometry import figures

def test_square_area():
    assert figures.square_area(3) == 9

def test_triangle_area():
    assert figures.triangle_area(10, 3) == 15