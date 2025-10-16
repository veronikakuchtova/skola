cislo = int(input("cislo: "))
print(cislo)
while cislo != 1:
    if cislo % 2 == 0:
        cislo = cislo // 2
        print(cislo)
    else:
        cislo = 3*cislo + 1
        print(cislo)