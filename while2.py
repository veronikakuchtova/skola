cislo = int(input("cislo: "))
pocet = 0
while cislo != 0:
    cifra = cislo % 10
    if  cifra % 2 == 0:
        pocet += 1
    cislo //= 10
print(pocet)