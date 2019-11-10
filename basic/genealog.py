rok = int(input("Podaj rok urodzenia postaci (przed 1960 r.): "))
aktualny_rok = 2019
wiek = aktualny_rok - rok

print("Ta osoba urodziła się przed", wiek, "laty.")

if wiek < 60:
    print("Postać zbyt młoda")
else:
    # print("To mogła być Twoja", "pra" * (wiek // 30 - 2) + "babka.")
    print(f"To mogła być Twoja {'pra' * (wiek // 30 - 2)}babka.")

# 'to jest "ładny" obraz'
# "to jest \"ładny\" obraz"
# """to jest "ładny" obraz"""

# Postać urodzona 60-89 lat temu: babka
# Postać urodzona 90-119 lat temu: prababka
# Postać urodzona 120-149 lat temu: praprababka

# Podaj rok urodzenia postaci (przed 1960 r.): 1926
# Ta osoba urodziła się przed 93 laty.
# To mogła być Twoja prababka.