produkty = {
    "ziemniaki": 2.20,
    "kukurydza": 3.40,
    "pomidory": 7.00,
    "kapusta": 3.00,
    "złoto": 10000.00,
}

print("Dostępne produkty:")
for produkt in produkty:
    print(f" - {produkt}")

produkt = input("Co kupujesz: ")
ilosc = float(input("Ile kg: "))

if produkt in produkty:
    print("Należy się", produkty[produkt] * ilosc)
else:
    print(f"Niestety, {produkt} - brak na stanie")

"""PRZYKŁADOWY WYDRUK
Dostępne produkty:
- ziemniaki
- kukurydza
- pomidory
- kapusta

Co kupujesz: kukurydza
Ile kg: 4.5

Należy się 14.80
"""