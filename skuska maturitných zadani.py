#2
# subor = open('hada.txt', 'r')
# subor2 = open('hada_kompresia', 'w')
# pocethier = 0
# maximum = 0
#
# def kompresia(s):
#     if s == '':
#         return ''
#     s = s + '.'
#     pismeno = s[0]
#     vystup = ''
#     pocet = 0
#     for znak in s:
#         if znak == pismeno:
#             pocet += 1
#         else:
#             vystup = vystup + '{} {} '.format(pismeno, pocet)
#             pismeno = znak
#             pocet = 1
#     return vystup
#
# for riadok in subor:
#     riadok = riadok.strip()
#     print(riadok)
#     riadok2 = kompresia(riadok)
#     subor2.write(riadok2)
#     print(riadok2)
#     if len(riadok) > maximum:
#         maximum = len(riadok)
#     pocethier += 1
# print('pocet hier:', pocethier)
# print('maximum: ', maximum)
# subor.close()
# subor2.close()

#4
# subor = open('meteo_stanice.txt', 'r')
# pocetmerani = 0
# teploty = []
# ibateploty = []
# zoz = []
#
# for riadok in subor:
#     info = riadok.strip()
#     teplota = info[21:26]
#     teplota = float(teplota.replace(',', '.'))
#     teploty.append((teplota, info[:3]))
#     ibateploty.append(teplota)
#     print(teplota)
#     pocetmerani +=1
#     zoz.append(info)
# print('pocet merani:', pocetmerani)
# print('maximum: ', max(teploty)[0])
# print('stanica maxima: ', max(teploty)[1])
# priemer = sum(ibateploty)/ len(teploty)
# print('primerna teplota: {:5.2f} stupnov'.format(priemer))
# subor.close()

# 5
# subor = open('objednane_jedla.txt', 'r')
# pocet = 0
# s = {'z':0, 'o':0, 'm':0, 'c':0}
# for riadok in subor:
#     info = riadok.split()
#     jedlo = info[1]
#     pocet += 1
#     s[jedlo] = s.get(jedlo, 0) + 1
# print( 'pocet jedal: ', pocet)
# malo = ''
# for jedlo, pocet in s.items():
#     print('kod jedla: {} pocet objednavok: {}'.format(jedlo, pocet))
#     if pocet < 20:
#         malo += str(jedlo) + ', '
# malo = malo[:-2]
# if malo != '':
#     print('tolkoto malo:', malo)
# else:
#     print('vsetky dobre')
# subor.close()

#7
# import random
# pocet_studentov = int(input('Pocet studentov: '))
# pocet_otazok = int(input('Pocet otazok: '))
#
# while pocet_otazok < pocet_studentov:
#     print('Chyba: pocet otazok je mensi ako pocet studentov')
#     pocet_otazok = int(input('pocet otazok: '))
#
# studenti = []
# otazky = []
# for i in range(pocet_studentov):
#     studenti.append(i + 1)
# for i in range(pocet_otazok):
#     otazky.append(i + 1)
#
# parne_otazky = otazky[1::2]
# neparne_otazky = otazky[::2]
# random.shuffle(parne_otazky)
# random.shuffle(neparne_otazky)
# otazky = []
# for i in range(len(parne_otazky)):
#     otazky = otazky + [parne_otazky[i], neparne_otazky[i]]
# if len(neparne_otazky) > len(parne_otazky):
#     otazky.append(neparne_otazky[-1])
#
# random.shuffle(studenti)
# print('Poradie odpovedajúcich a ich číslo otázky:')
# for i in range(pocet_studentov):
#     oznam = '{}. student: {}, otazka: {}'.format(i+1, studenti[i], otazky[i])
#     print(oznam)





























































