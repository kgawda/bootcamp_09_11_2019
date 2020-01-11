# with open('example.txt') as f:
#     f.read()

with open('example.txt') as f:
    for line in f:
        if line.strip():
            print(line.strip())