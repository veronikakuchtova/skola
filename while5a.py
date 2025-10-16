cislo = int(input("cislo: "))
vysledok_p = ""
vysledok_n = ""
while cislo != 0:
    cifra = cislo % 10
    if cifra % 2 == 0:
        vysledok_p = str(cifra) + vysledok_p
    else:
        vysledok_n = str(cifra) + vysledok_n
    cislo //= 10
print(vysledok_p, vysledok_n)