fr = open('mena_zamestnancov.txt', 'r', encoding='utf-8')
fw = open('vystup.txt', 'w', encoding='utf-8')
pocet_mien = 0
zoz = fr.readlines()
zoz_pol = zoz[:len(zoz)//2]
zoz_pol2 = zoz[len(zoz)//2:]
max_meno = zoz_pol[0]
max_priezvisko = zoz_pol2[0]

for i in range(1,len(zoz_pol)):
    if len(zoz_pol[i]) > len(max_meno):
        max_meno = zoz_pol[i]
for i in range(len(zoz_pol2)):
    if len(zoz_pol2[i]) > len(max_priezvisko):
        max_priezvisko = zoz_pol2[i]

for i in range(len(zoz_pol)):
    fw.write(zoz_pol[i][:-1:]+ ' '*(len(max_meno)-len(zoz_pol[i])+1)+zoz_pol2[i])
    pocet_mien += 1

print('Pocet mien je: ',pocet_mien)
print('Najdlhsie meno ma',len(max_meno), 'znakov')
print('Najdlhsie priezvisko ma',len(max_priezvisko), 'znakov')
fw.close()
fr.close()


