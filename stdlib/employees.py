import json
import os

def main():
    #if os.path.exists('employees.json'):
    try:
        with open('employees.json') as f:
            pracownicy = json.load(f)
    except json.decoder.JSONDecodeError:
        pracownicy = []
    except FileNotFoundError:
        pracownicy = []

    akcja = input("Co chcesz zrobic? [d - dodaj, w - wypisz] ")
    if akcja == 'd':
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        rok_ur = input("Rok urodzenia: ")
        pensja = float(input("Pensja: "))

        pracownik = {
            'imie': imie,
            'nazwisko': nazwisko,
            'rok_ur': rok_ur,
            'pensja': pensja,
        }
        pracownicy.append(pracownik)

        with open('employees.json', 'w') as f:
            json.dump(pracownicy, f, indent=4)

    elif akcja == 'w':
        for numer, pracownik in enumerate(pracownicy):
            print(f" - [{numer+1}] {pracownik['imie']} {pracownik['nazwisko']}"
                  f" - rok: {pracownik['rok_ur']}, "
                  f"pensja: {pracownik['pensja']:.2f} PLN"
                  )

if __name__ == '__main__':
    main()