def otworz_walizke(szyfr):
    """
    Funkcja mówiąca czy udało się otworzyć walizkę podanym szyfrem.
    Oczywiście w kodzie funkcji widać jakie jest hasło, ale możemy sobie wyobrazić, że
    ta funkcja steruje robotem, który próbuje otworzyć prawdziwą walizkę...
    Przyjmowany argument:
    :param szyfr: sprawdzany szyfr - str
    Zwracana wartość:
    :return: czy szyfra pasuje - bool
    """
    return szyfr == "dudda68"

def kolejna_literka(lista_podejrzen, czesc_hasla, krok):
    """
    Funkcja pomocnicza, wywoływana rekurencyjnie. Argumenty:
    :param lista_podejrzen: lista podana przez użytkownika - nie zmieniamy jej - list
    :param czesc_hasla: początkowa część hasła, której należy użyć (sprawdzić wszystkie możliwości, które od niej się zaczynają) - str
    :param krok: od której literki hasła zaczynamy (indeks) - in
    :return: poprawne hasło jeśli znalezione - str, lub None
    """
    print("Funkcja wywołana z", czesc_hasla)

    # czy mamy już wszystkie literki hasła do sprawdzenia?
    if krok == len(lista_podejrzen):
        print("Próbuje otworzyc walizkę hasłem", czesc_hasla)
        if otworz_walizke(czesc_hasla):
            return czesc_hasla
        else:
            return None

    # nie mamy jeszcze wszystkich literek hasła do sprawdzenia
    # spróbujmy więc wszystkich możliwych wartości kolejnej literki (tej na którą wskazuje krok)
    for literka in lista_podejrzen[krok]:
        # dla każdej możliwej literki na pozycji "krok" tworzymy nowy początek hasła (dotychczasowa część hasła plus nowa literka)
        # i uruchamiamy `kolejna_literka` (taką samą funkcję w jakiej jesteśmy), żeby ona wybrała wszytstkie opcja kolejnej literki...
        # ... i znowu uruchomiał `kolejna_literka` i tak dalej aż krok==len(lista_podejrzen)
        temp = kolejna_literka(lista_podejrzen, czesc_hasla+literka, krok+1)
        if temp:
            # uwaga! mamy poprawne hasło! przerwać pętle for i w ogóle całe wywołanie funkcji
            # Jeśli znajdujemy się w funkcji `kolejna_literka` wywołanej przez funkcję `kolejna_literka`, to
            # ona też postąpi tak samo i finalnie poprawne hasło zostanie zwrócone do funkcji `otwieracz`
            return temp

def otwieracz(lista_podejrzen):
    """
    Funkcja znajdująca jakie jest hasło do walizki.
    Do sprawdzania czy hasło pasuje używana jest funkcja otworz_walizke, która musi być dostępna
    Funkcja przyjmuje argument:
    :param lista_podejrzen: listę stringów - każdy string to możliwe wartości kolejnej litery z hasła.
    Zwracana wartość:
    :return: hasło (str) lub None jeśli żadne nie zadziałało
    """

    # wywołujemy funkcję, która dalej ma już sama siebie wywoływać (rekurencja)
    # podajemy jej na razie pusty string jako aktualnie sprawdzaną cześć hasła i każemy zacząć od pierwszego znaku
    return kolejna_literka(lista_podejrzen, "", 0)

# w liście umieszczamy podejrzenia jakie klawisze były wciśnięte dla każdej kolejnej litery
podejrzenia = ['sdf', 'yui8j', 'sdfe', 'dscf', 'aq', '6', '89']
# wywołujemy naszą funkcję, podając jej tą listę podejrzeń
print("Hasło to", otwieracz(podejrzenia))