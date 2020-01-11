from mathematica.algebra import matrices

def test_add_matrices():
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    m2 = [
        [6, 5, 0],
        [1, 3, 9],
        [0, 2, 1]
    ]
    expected = [
        [1+6, 2+5, 3+0],
        [4+1, 5+3, 6+9],
        [7+0, 8+2, 9+1]
    ]
    assert matrices.add_matrices(m1, m2) == expected