liczba_min = None
liczba_max = None

while True:
    dane = input("Wpisz liczbę lub 'koniec': ")
    if dane.lower() == "koniec":  # zmienić, żeby przyjmowało też KONIEC, Koniec i koNiec
        break
    if dane == "" or not dane.replace('-', '').isdigit():
        print("Nic nie wpisałeś!")
        continue
    # użytkownik podał liczbę
    liczba = int(dane)
    if liczba_min == None or liczba < liczba_min:
        liczba_min = liczba
    if liczba_max == None or liczba > liczba_max:
        liczba_max = liczba

if liczba_min != None:  # do zmiany!
    print(f"Liczba maksymalna to {liczba_max}, a minimalna to {liczba_min}.")
else:
    print("Nie podałeś żadnych liczb!")
