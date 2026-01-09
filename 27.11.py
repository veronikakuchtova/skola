# z.append - pridava do zoznamu
# for a in range(2,201,2):
#     z.append(a) - pridava parne
# komprehenzia - coming soon
# syntax sugar - jeden riadok ako vytvorit naplneny riadok
# ret='ahoj jozo a miso'
# zoz=ret.split() - zatvorky alebo lubovolny znak, rozdeli sa na ['ahoj','jozo','a','miso'] -  vrati v zozname
# C je pole - musia byt homogenne

# import random
# zoz=[]
# for i in range(10):
#     zoz.append(random.randint(50,101))
# # na zaciatku prehlasim prvy za najvacsi, potom v cykle budem prehladavta zvysnu cast zoznamu
# # ak najdem vacsie cislo to da maximum, este aj index
# print(zoz)

import random
# maximum = zoz[0]
# poz_max = 0
# for i in range(1,len(zoz)):
#     if zoz[i] > maximum:
#         maximum = zoz[i]
#         poz_max = i
# print(zoz)
# print(maximum, poz_max)

# ak by if zoz[i] >= maximum, bolo by to posledne cislo takze posledny index
# a) sucet parnych
# b) sucet parneho indexu

# import random
# zoz=[]
# for i in range(10):
#     zoz.append(random.randint(50,101))
# sucet_parnych = 0
# sucet_par_index = 0
# for i in range(len(zoz)):
#     if zoz[i] % 2 == 0: # ak je cislo parne
#         sucet_parnych += zoz[i]
#     if i % 2 == 0: # ak je index parny
#         sucet_par_index += zoz[i]
# print(zoz)
# print(sucet_parnych)
# print(sucet_par_index)
# konkretna hodnota zoznamu  - for prvok in zoz:
# najst ci  je cislo prvocislo
# import random
# zoz=[]
# for i in range(10):
#     zoz.append(random.randint(50,101))
# def isprime(cislo):
#     poc_del = 0
#     for i in range(1,cislo+1):
#         if cislo % i == 0:
#             poc_del += 1
#     if poc_del > 2:
#         return False
#     else:
#         return True
# sucet_prvoc = 0
# for i in range(len(zoz)):
#     if isprime(zoz[i]):
#         sucet_prvoc += zoz[i]
# print(zoz)
# print(sucet_prvoc)