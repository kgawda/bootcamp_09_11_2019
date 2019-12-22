class Pies:
    def __init__(self, rasa="mieszaniec"):
        self.rasa = rasa

    def __str__(self):
        return f"Pies rasy {self.rasa}"

    def __mul__(self, other):
        if self.rasa == other.rasa:
            nowa_rasa = self.rasa
        else:
            nowa_rasa = self.rasa + '-' + other.rasa
        return Pies(nowa_rasa)

p1 = Pies()
p2 = Pies("pekińczyk")
p3 = Pies("hart")

p12 = p1 * p2
print(f"Potomkiem {p1} i {p2} jest {p12}")
p23 = p3 * p2
print(f"Potomkiem {p2} i {p3} jest {p23}")