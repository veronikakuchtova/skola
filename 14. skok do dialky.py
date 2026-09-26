subor = open('skok_do_dialky.txt', 'r')
krajiny = {}
maxdlzka = 0
vitazi = []
for riadok in subor:
    udaje = riadok.split()
    krajina = udaje[1]
    if krajina in krajiny:
        krajiny[krajina] += 1
    else:
        krajiny[krajina] = 1
    dlzka = int(udaje[2])
    for i in range(3,7):
        if int(udaje[i]) > dlzka:
            dlzka = int(udaje[i])
    if dlzka > maxdlzka:
        maxdlzka = dlzka
        vitazi = [udaje[0]]
    elif dlzka == maxdlzka:
        vitazi.append(udaje[0])
print('Krajiny zucastnenych: ')
for krajina in krajiny:
    print(krajina, end=', ')
print()
print('pocty krajin zucastnenych: ')
for krajina in krajiny:
    print(krajina, ':', krajiny[krajina])
print(f'Najdlhsi skok {maxdlzka}m skocil/i: ')
for vitaz in vitazi:
    print(vitaz)