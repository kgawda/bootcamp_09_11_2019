def vowels(s):
    for c in s:
        if c.lower() in 'aeiouy':
            yield c

for char in vowels('ala ma kota a kot ma ale'):
    print(char)

print("".join(vowels('ala ma kota a kot ma ale')))