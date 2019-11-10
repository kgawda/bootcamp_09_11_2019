suma_temperatur = 0
dzien = 1

while dzien < 8:
    suma_temperatur += float(input(f"Podaj temperature dla dnia {dzien}: "))  # np. Podaj temperature dla dnia 1:
    dzien += 1

print(f"Średnia temperatur to { suma_temperatur / 7 :.2f}")
# print("Średnia temperatur to",  round(suma_temperatur / 7, 2))

