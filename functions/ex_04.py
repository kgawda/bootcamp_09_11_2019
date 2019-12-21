def formatuj(*args, **kwargs):
    result = "\n".join(args)
    for nazwa, wartosc in kwargs.items():
        result = result.replace("$"+nazwa, str(wartosc))
    return result

def test_formatuj_no_kwargs():
    expected = """aa
bb
cc"""
    assert formatuj("aa", "bb", "cc") == expected

def test_formatuj_single_line_with_kwargs():
    expected = 'Podróż z Los Angeles do Yorktown zajmuje 5 h'
    assert formatuj('Podróż z $miasto1 do $miasto2 zajmuje $czas h',
        miasto1="Los Angeles", miasto2="Yorktown", czas=5) == expected

def test_formatuj_multiple_lines_multiple_kwargs():
    expected = 'Hej!\nMam niebieski samochód\nMam też niebieski rower\nA nawet mam niebieski dom, bo niebieski to mój ulubiony kolor.'
    got = formatuj('$powitanie', 'Mam $kolor samochód', 'Mam też $kolor rower',
        'A nawet mam $kolor dom, bo $kolor to mój ulubiony kolor.',
        powitanie="Hej!", kolor='niebieski')
    assert got == expected

def test_formatuj_empty():
    assert formatuj() == ""

def test_formatuj_empty_string():
    assert formatuj("") == ""