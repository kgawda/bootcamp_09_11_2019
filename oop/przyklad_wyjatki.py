class IncorrectUserAction(Exception):
    pass

def obsluga_kantoru():
    operacja = input("Chcesz kupić czy sprzedać? [s/k]: ")
    if operacja == 'k':
        ...
    elif operacja == 's':
        ...
    else:
        raise IncorrectUserAction("Podana niepoprawna operacja")

    ...
    return 100

print("Początek programu")
try:
    kwota = obsluga_kantoru()
    print("Kolejna linijka w try")
finally:
    ...

print("Koniec programu, pożegnanie użytkownika")