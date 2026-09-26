import random

pocty = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
pocty_percenta = {}

for i in range(1, 10001):
    c1 = random.randint(1, 100)
    c2 = random.randint(1, 100)
    nas = str(c1**c2)
    dig = int(nas[0])
    pocty[str(dig)] += 1

for pocet in pocty:
    pocty_percenta[pocet] = pocty[pocet] / 100

print(pocty)
print(pocty_percenta)
# pandas = datagrip vyrtualna tabulka dat v pocitaci, ma vela prikazov, vsetky funkcie co ma excel su tu
