lista = [3, 6, 7, 4, 0, 2, 12, 54, 10, 11]
liczba_min = None
liczba_max = None
index_max = None
index_min = None

print("Przed:", lista)

#for i in range(len(lista)):
# zamiast x byłby lista[x]
for x in lista:
    if liczba_min == None or x < liczba_min:
        liczba_min = x
    if liczba_max == None or x > liczba_max:
        liczba_max = x

lista[index_max] = liczba_min
lista[index_min] = liczba_max

print("max to", liczba_max, "min to", liczba_min)

print("Po:", lista)
# [3, 6, 7, 4, 54, 2, 12, 0, 10, 11]