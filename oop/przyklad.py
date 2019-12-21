class SwietyMikolaj:
    def __init__(self, imie="Mikołaj"):
        self.imie = imie

    def przywitaj_sie(self):
        print(f"Hohoho! Jestem {self.imie}")

    def daj_prezent(self, dla_kogo):
        return f"Prezent dla {dla_kogo}"

    def __str__(self):
        return f"Mikołaj {self.imie}"

mikolaj1 = SwietyMikolaj("Mikołajek")
print(str(mikolaj1)+" :)")
print("Ten SwietyMikolaj nazywa się", mikolaj1.imie)

inni_mikolajowie = [SwietyMikolaj("Andrzej"), SwietyMikolaj("Bltazar"), SwietyMikolaj()]

mikolaj1.przywitaj_sie()
for mikolaj in inni_mikolajowie:
    mikolaj.przywitaj_sie()

print(mikolaj1.daj_prezent("Agaty"))