miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")
dystans = float(input(f"Dystans {miasto_a}-{miasto_b}: "))
cena = float(input("Cena paliwa: "))
spalanie = float(input("Spalanie na 100 km: "))

koszt = dystans / 100 * cena * spalanie

print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {int(koszt)} PLN")