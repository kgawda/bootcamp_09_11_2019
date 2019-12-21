def splaszcz(lista):
    result = []
    for element in lista:
        if isinstance(element, list):
            # wiemy, że element jest listą
            for subelement in splaszcz(element):
                result.append(subelement)
        else:
            result.append(element)
    return result

def test_flat_list():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]

def test_one_embedded_list():
    assert splaszcz([1, [2, 3]]) == [1, 2, 3]

def test_one_embedded_level2():
    assert splaszcz([1, [2, [3, 4]]]) == [1, 2, 3, 4]

def test_from_exercise():
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7])  == [1, 2, 3, 4, 5, 6, 7]