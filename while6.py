cislo = int(input("cislo: "))
backup = cislo
pocet = 0
while cislo != 0:
    pocet += 1
    cislo //= 10

if pocet % 2 == 1:
    index = pocet // 2 + 1
    neparne = True
else:
    index = pocet // 2
    neparne = False

pocitadlo_pozicie = 1
while backup !=0:
    cifra = backup % 10
    if neparne:
        if pocitadlo_pozicie == index:
            print(cifra )
    else:
        if pocitadlo_pozicie == index:
            print((cifra + (backup // 10)%10)/2)
    backup //= 10
    pocitadlo_pozicie +=1