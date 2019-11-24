def funkcja(*args, **kwargs):
    dzien_miesiaca = kwargs.get('dzien', 1)

    print("Argumenty pozycyjne:")
    for wartosc in args:
        print(" -", wartosc)
    print("Argumenty nazwane (keyword):")
    for klucz, wartosc in kwargs.items():
        print(" -", klucz, ":", wartosc)
    print()


funkcja()
funkcja("Alfa", "Omega", dzien=24)
funkcja("Beta", dzien=24, miesiac="listopad")