#import dzialania.b
from dzialania import b

def powitanie():
    print("Cześć!")

x = input("Podaj X ")
y = input("Podaj Y ")
dzialanie = input("Podaj dzialanie ")

if x == 'pi':
    x = b.pi
else:
    x = float(x)

if y == 'pi':
    y = b.pi
else:
    y = float(y)

if dzialanie == '+':
    wynik = b.dodawanie(x, y)
elif dzialanie == '-':
    wynik = b.odejmowanie(x, y)

print(wynik)

