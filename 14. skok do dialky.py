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

#list = neheterogenne = moze byt znak, cislo, zoznam....
#   = mutable = menitelne ( imutable = string, tuple )
#   = najdeme podla indexu [i]... 0,1,2,3,4 alebo -1,-2,-3, index alebo kľúča
#   = daco.count() bodka a funkcia = čo robia s listom
#   = das si vypisat list = [#,10.5,hello]
#   = miso.append() podľa indexu na ďalší index
#dictionary = viacero hodnôt ale ja si vyberám indexi a kľúče- indexi musia byť rozdielne
#           = pristupit k prvej polozke = miso[10], miso[a]
#           = keď chcem vypísať = {10:7, 'a':'p'} po dvojiciach inak mnozina, dic oddelene dvojbodkou
#           = keď chcem pridať do dic miso[135] = 'ahoj'
#           = for chodi cez kluce
# oba iterovatelne = da sa prechadzat pomocou cyklu
#tuple = debilnejsi brat listu
#      = mozem si predstavit ako vektor
#      = imutable = nemenne
#      = pouziva sa ako vektor = (4.5,5,6,7) dlzka 4
#komprehencia = syntax sugar
#A1C577 odtien farby =  a1 = 1.16na0 + 10.16na1
#                       c5 = 5.16na0 + 12.16na1
# dic = {10:a, 11:b, 12:c..}
# premenna ktora vznikne vo vnutriš sa vola lokalna premenna