with open('potegi.txt', 'w') as f:
    for i in range(100):
        f.write(f"{2 ** i}\n")