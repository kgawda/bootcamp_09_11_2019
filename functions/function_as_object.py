def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

liczba1 = int(input("Liczba1 "))
liczba2 = int(input("Liczba2 "))
operacja = input("+ czy -? ")

if operacja == "+":
    funkcja = dodaj
else:
    funkcja = odejmij

print(  funkcja(liczba1, liczba2)  )