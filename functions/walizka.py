def otworz_walizke(szyfr):
    return szyfr == "dudda68"

def kolejna_literka(lista_podejrzen, czesc_hasla, krok):
    print("Funkcja wywolana z", czesc_hasla)
    if krok == len(lista_podejrzen):
        print("Proboje otworzyc walizke z haslem", czesc_hasla)
        if otworz_walizke(czesc_hasla):
            return czesc_hasla
        else:
            return None

    for literka in lista_podejrzen[krok]:
        temp = kolejna_literka(lista_podejrzen, czesc_hasla+literka, krok+1)
        if temp:
            return temp

def otwieracz(lista_podejrzen):
    return kolejna_literka(lista_podejrzen, "", 0)


podejrzenia = ['sdf', 'yui8j', 'sdfe', 'dscf', 'aq', '6', '89']
print("Hasło to", otwieracz(podejrzenia))