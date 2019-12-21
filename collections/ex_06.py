lista = [3, 6, 7, 4, 0, 2, 12, 54, 10, 11]
liczba_min = None
liczba_max = None
index_max = None
index_min = None

print("Przed:", lista)

# Opcja 1:
for index in range(len(lista)):
    if liczba_min == None or lista[index] < liczba_min:
        liczba_min = lista[index]
        index_min = index
    if liczba_max == None or lista[index] > liczba_max:
        liczba_max = lista[index]
        index_max = index

# Opcja 2:
#index = 0
#for x in lista:
#    if liczba_min == None or x < liczba_min:
#        liczba_min = x
#        index_min = index
#    if liczba_max == None or x > liczba_max:
#        liczba_max = x
#        index_max = index
#    index += 1

if liczba_min is not None:
  lista[index_max] = liczba_min
  lista[index_min] = liczba_max

  print("max to", liczba_max, "min to", liczba_min)
  print("Po:   ", lista)
  # [3, 6, 7, 4, 54, 2, 12, 0, 10, 11]
