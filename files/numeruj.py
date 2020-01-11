import sys

def main():
    if len(sys.argv) < 2:
        print("Użycie: numeruj.py PLIK")
        return

    try:
        with open(sys.argv[1], encoding='utf-8') as f:
            for index, line in enumerate(f):
                print(f"{index+1}: {line.rstrip()}")
    except FileNotFoundError:
        print("Podano nieistniejący plik")

if __name__ == "__main__":
    main()