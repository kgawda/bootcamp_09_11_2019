liczby = []

while len(liczby) < 10:
    dana = input("Wpisz liczbe lub 'koniec': ")
    dana = dana.strip()
    if not dana:
        print("Nic nie podałeś")
        continue
    if dana.lower() == 'koniec':
        break
    if not dana.replace('-', '').isdigit():  # to nie jest idealne
        print("Obsługuję tylko liczby całkowite i 'koniec'")
    dana = int(dana)
    liczby.append(dana)

if liczby:
    print("Średnia to", sum(liczby)/len(liczby))
else:
    print("Nie podałeś żadnej liczby")
