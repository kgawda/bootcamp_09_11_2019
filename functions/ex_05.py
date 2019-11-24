def silnia(n):
    print("Jesteśmy na", n)
    if n <= 1:
        return 1
    result = n * silnia(n-1)
    print("Kończymy z", n)
    return result

print(silnia(5))