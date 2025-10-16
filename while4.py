cislo = int(input("cislo: "))
vysledok = 0
while cislo != 0:
    cifra = cislo % 10
    vysledok = vysledok * 10 + cifra
    cislo //= 10
print(vysledok)