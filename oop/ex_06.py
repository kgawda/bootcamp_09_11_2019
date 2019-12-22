class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        else:
            return Vector(self.x * other, self.y * other)

    def __eq__(self, other):
        # porównanie po x i y
        return (self.x == other.x) and (self.y == other.y)
        # porównanie po długości
        # return (self.x ** 2 + self.y ** 2) == (other.x ** 2 + other.y ** 2)

def test_vector_init():
    v1 = Vector(1, 2)
    assert v1.x == 1
    assert v1.y == 2

def test_vector_str():
    v1 = Vector(1, 2)
    assert str(v1) == "Vector(1, 2)"

def test_vector_add():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    assert v3.x == 1 + 3
    assert v3.y == 2 + 4

def test_vector_mul_int():
    v1 = Vector(1, 2)
    v2 = v1 * 3
    assert v2.x == 1 * 3
    assert v2.y == 2 * 3

def test_vector_mul_vector():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 * v2
    assert v3.x == 1 * 3
    assert v3.y == 2 * 4

def test_vector_eq():
    v1 = Vector(1, 2)
    v2 = Vector(1, 2)
    v3 = Vector(3, 4)
    assert v1 == v1
    assert v1 == v2
    assert not (v1 == v3)

# print("Dodwawanie:", Vector(1, 2) + Vector(3, 4))