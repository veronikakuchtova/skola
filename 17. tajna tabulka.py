a = str(input('Zadaj vetu na zasifrovanie (iba velke pismena): '))
pocet_policka = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
vysledok = ''
naj_pocet = 0
for i in a:
    if i == ' ':
        vysledok += '0 '
    else:
        vysledok += str((ord(i) - 65) // 3 + 1) * ((ord(i) - 65) % 3 + 1) + ' '

for i in vysledok:
    if i != ' ':
        pocet_policka[i] += 1
print(vysledok)

for i in pocet_policka:
    if pocet_policka[i] > naj_pocet:
        naj_pocet = pocet_policka[i]

for i in pocet_policka:
    if pocet_policka[i] == naj_pocet:
        print('Najčastejšie zvolené políčka: ', i)