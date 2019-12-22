class SwietyMikolaj:
    kolejny_numer = 1
    miejsce_zamieszkania = "Laponia"

    def __init__(self, imie="Mikołaj"):
        self.imie = imie

    def przywitaj_sie(self):
        print(f"Hohoho! Jestem {self.imie}")

    def daj_prezent(self, dla_kogo):
        return f"Prezent dla {dla_kogo}"

    def __str__(self):
        return f"Mikołaj {self.imie}"

    @classmethod
    def zaloga_4_mikolajow(cls):
        return [cls("Albert"), cls("Baltazar"), cls("Cezary"), cls("Daniel")]
        #return [cls(imie) for imie in ("Albert", "Baltazar", "Cezary", "Daniel")]

    @classmethod
    def mikolaj_o_kolejnym_imieniu(cls):
        mikolaj = cls(f"Mikołaj{cls.kolejny_numer}")
        cls.kolejny_numer += 1
        return mikolaj

    @staticmethod
    def czy_w_ziemie_jest_zimno():
        return True

print("Czy w zimie jest zmino?", SwietyMikolaj.czy_w_ziemie_jest_zimno())

mikolaj1 = SwietyMikolaj()
#mikolaj1 = SwietyMikolaj.mikolaj_o_dlugim_imieniu()

print(SwietyMikolaj.mikolaj_o_kolejnym_imieniu())
print(SwietyMikolaj.mikolaj_o_kolejnym_imieniu())
print(SwietyMikolaj.mikolaj_o_kolejnym_imieniu())
print("Kolejny numer Mikołaja to", SwietyMikolaj.kolejny_numer)

print(str(mikolaj1)+" :)")
print("Ten SwietyMikolaj nazywa się", mikolaj1.imie)

inni_mikolajowie = SwietyMikolaj.zaloga_4_mikolajow()

mikolaj1.przywitaj_sie()
for mikolaj in inni_mikolajowie:
    mikolaj.przywitaj_sie()

print(mikolaj1.daj_prezent("Agaty"))
