lista = [1, 3, 0, -83, 35, -234, 23]

ilosc_dodatnich = 0
ilosc_ujemnych = 0

for element in lista:
    if element > 0:
        ilosc_dodatnich += 1
    elif element < 0:
        ilosc_ujemnych += 1

print(f"Jest {ilosc_dodatnich} dodatnich i {ilosc_ujemnych} ujemnych")