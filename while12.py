cislo = int(input("cislo: "))
delitel = 1
while delitel <= cislo:
    if cislo % delitel == 0:
        print(delitel)
    delitel += 1
