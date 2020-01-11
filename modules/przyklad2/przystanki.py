def zbuduj_rozklad(linie):
    s = ""
    for linia in linie:
        s += f"Linia {linia.nr_linii}: odjeżdża co 5 minut\n"
    return s