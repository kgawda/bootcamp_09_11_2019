import sys

def main(args):
    adresy = set()

    if len(args) < 2:
        print("Podaj nazwy plików")
        return

    with open(args[0]) as f:
        for line in f:
            adres = line.strip()
            adres = adres.lower()
            # if adres.count('@') != 1:
            #     continue
            # adresy.add(adres)
            if adres.count('@') == 1:
                adresy.add(adres)

    with open(args[1], 'w') as f:
        for adres in sorted(adresy):
            f.write(adres + "\n")

    # # wersja bez sortowania
    # with open(args[0]) as f:
    #     with open(args[1], 'w') as f2:
    #         for line in f:
    #             adres = line.strip()
    #             adres = adres.lower()
    #             # if adres.count('@') != 1:
    #             #     continue
    #             # adresy.add(adres)
    #             if adres.count('@') == 1:
    #                 if adres not in adresy:
    #                     f2.write(adres + "\n")
    #                     adresy.add(adres)

if __name__ == "__main__":
    main(sys.argv[1:])