ilosc_liczb_podzielnych = 0

print("Liczby podzielne przez 3 lub 5:")

for x in range(101):
    if x % 3 == 0 or x % 5 == 0:
        print(x)
        ilosc_liczb_podzielnych += 1

print(f"W przedziale 0-100 jest {ilosc_liczb_podzielnych} liczb podzielnych przez 3 lub 5")