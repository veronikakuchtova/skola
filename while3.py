cislo = int(input("cislo: "))
pocet = 0
while cislo != 0:
    cislo //= 10
    pocet += 1
print(pocet)