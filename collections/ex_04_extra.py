liczby_podzielne = []

print("Liczby podzielne przez 3 lub 5:")

for x in range(101):
    if x % 3 == 0 or x % 5 == 0:
        print(x)
        liczby_podzielne.append(x)

print(f"W przedziale 0-100 jest {len(liczby_podzielne)} liczb podzielnych przez 3 lub 5")
print("To są:", liczby_podzielne)