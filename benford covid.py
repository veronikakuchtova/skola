# ci su tie cisla prve cifry ako 23.9
pocty = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
pocty_percenta = {}
subor = open("data.csv", "r")
subor.readline()
pocet = 0

for riadok in subor:
    if "China" in riadok:
        udaje = riadok.split(",")
        cislo = udaje[5]
        if cislo[0] in "123456789":
            prva_cislica = cislo[0]
            pocty[prva_cislica] += 1
            pocet += 1
subor.close()

for cislica in pocty:
    pocty_percenta[cislica] = round(pocty[cislica] / pocet * 100, 2)

print(pocty)
print(pocty_percenta)
