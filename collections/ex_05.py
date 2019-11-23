print("   ", end='')
for y in range(10):
    print(f"{y:3}", end='')
print()
print()

for x in range(10):
    print(x, end='  ')
    for y in range(10):
        print(f"{x*y:3}", end='')
    print()
