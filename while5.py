cislo = int(input("cislo: "))
vysledok_p = 0
vysledok_n = 0
while cislo != 0:
    cifra = cislo % 10
    if cifra % 2 == 0:
        vysledok_p = vysledok_p * 10 + cifra
    if cifra % 2 == 1:
        vysledok_n = vysledok_n * 10 + cifra
    cislo //= 10
print(vysledok_p, vysledok_n)