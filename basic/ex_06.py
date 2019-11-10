liczba = int(input("Podaj liczbę: "))

print(f"Większa od 10: {liczba > 10}")
print("Mniejsza równa 15:", liczba <= 15)
print("Podzielna przez 2:", liczba % 2 == 0)

# test_zadania_7 = ((liczba % 2 != 0) and (liczba % 3 == 0) and (liczba > 10)) or liczba == 7
test_zadania_7 = (liczba % 2) and not (liczba % 3) and (liczba > 10) or liczba == 7
print("Zadanie 7:", test_zadania_7)
