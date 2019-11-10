# zamiast takiej linijki:
#  a = float(input("Wprowadź wysokość [cm]: "))
# mogą być dwie takie:
a = input("Wprowadź wysokość [cm]: ")
a = float(a)

b = float(input("Wprowadź szerokość [cm]: "))
c = float(input("Wprowadź głębokość [cm]: "))

objetosc = a * b * c

print(f"Objętość to {objetosc} cm³. Czy to więcej niż litr? {objetosc > 1000}")

nadmiar = 0
if objetosc > 1000:
    print("Niestety za dużo")
    nadmiar = objetosc - 1000
    print("Za dużo o", nadmiar)

print("Nadmiar był", nadmiar)