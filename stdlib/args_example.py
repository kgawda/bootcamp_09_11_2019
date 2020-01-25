import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("imie", help="your name")
    parser.add_argument("nazwisko", help="your surname")
    parser.add_argument("--pozdrowienie", help="how to greet", default="Witaj")
    args = parser.parse_args()

    print(f"{args.pozdrowienie} {args.imie} {args.nazwisko}")


if __name__ == '__main__':
    main()