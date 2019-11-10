liczba_min = 0  # czy na pewno?
liczba_max = 0  # czy na pewno?
CZY_PODANO_LICZBE = False

while True:
    dane = input("Wpisz liczbę lub 'koniec': ")
    if dane == "koniec":
        break
    if dane == "":
        print("Nic nie wpisałeś!")
        continue
    # użytkownik podał liczbę
    liczba = int(dane)
    if liczba < liczba_min or not CZY_PODANO_LICZBE:
        liczba_min = liczba
    if liczba > liczba_max or not CZY_PODANO_LICZBE:
        liczba_max = liczba
    CZY_PODANO_LICZBE = True

if CZY_PODANO_LICZBE:  # do zmiany!
    print(f"Liczba maksymalna to {liczba_max}, a minimalna to {liczba_min}.")
else:
    print("Nie podałeś żadnych liczb!")
