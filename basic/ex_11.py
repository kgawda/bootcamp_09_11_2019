x = int(input("Podaj pozycje gracza X: "))
y = int(input("Podaj pozycje gracza Y: "))

if x > 100 or x < 0 or y > 100 or y < 0:
    print("Gracz znajduje sie poza planszą.")
elif x <= 10:
    if y >= 90:
        print("Gracz znajduje sie w lewym górnym rogu.")
    elif y <= 10:
        print("Gracz znajduje sie w lewym dolnym rogu.")
    else:
        print("Gracz znajduje sie na lewej krawędzi.")
elif x >= 90:
    if y >= 90:
        print("Gracz znajduje sie w prawym górnym rogu.")
    elif y <= 10:
        print("Gracz znajduje sie w prawym dolnym rogu.")
    else:
        print("Gracz znajduje sie na prawej krawędzi.")
else:
    if y >= 90:
        print("Gracz znajduje sie na górnej krawędzi.")
    elif y <= 10:
        print("Gracz znajduje sie na dolnej krawędzi.")
    else:
        print("Gracz znajduje sie na środku planszy.")
