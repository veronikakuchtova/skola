import random
# def generuj(dlzka:int)->list:
#     zoz=[]
#     for i in range(dlzka):
#         zoz.append(random.randint(5,10))
#     return zoz
# print(generuj(5))
# from Anitka.pokemoni.uloha import parne_pozicie




# def coho_je_viac(z:list)->str:
#     zoz_par = []
#     zoz_nepar = []
#     for prvok in z:
#         if prvok % 2 == 0:
#             zoz_par.append(prvok)
#         else:
#             zoz_nepar.append(prvok)
#     if len(zoz_par)>len(zoz_nepar):
#         return 'parne'
#     elif len(zoz_par)==len(zoz_nepar):
#         return 'rovnako'
#     else:
#         return 'neparne'
# print (coho_je_viac([1,2,3,4,5,6]))


# def nie_cisla(z:list)->list:
#     list_nie_cisla = []
#     for i in z:
#         if type(i) != int and type(i) != float:
#             list_nie_cisla.append(i)
#     return list_nie_cisla
# print(nie_cisla(['kuk', 5, 'ahoj', -1, 2.5, 4, None, 7, [2,-12], 8, 'servus',11]))




# def spolu_do_retazca(z:list)-> str:
#     vystup = ''
#     for x in z:
#         vystup += str(x)
#     return vystup
# print(spolu_do_retazca(['ahoj', 12, -3, 'kukuk', 6.45, True]))


# def zoznam_mocnin(n:int)->list:
#     zoz_mocnin = []
#     for i in range(0,n):
#         zoz_mocnin.append((i+1)**2)
#     return zoz_mocnin
# print(zoznam_mocnin(5))
# from math import pi
# def ludolf(n:int)->list:
#     if n <= 15:
#         zoz = []
#         for i in range(1,n+1):
#             zoz.append(round(pi,i))
#         return zoz
#     else:
#         return False
# print(ludolf(15))
# print(ludolf(20))


# def je_usp(z:list)->bool:
#     for i in range (len(z)-1):
#         if z[i]>=z[i+1]:
#             return False
#     return True
# print(je_usp([1,5,7,12,8]))

#
# def maxx(z:list)->int:
#    maximum = z[0]
#    for i in range (1,len(z)):
#        if z[i] > maximum:
#            maximum = z[i]
#    return maximum
# print(maxx([4,8,5,1]))

def ktory_min(z:int)->int:
    minimum = 0
    for i in range (1,len(z)):
        if z[i] < z[minimum]:
            minimum = i
    return minimum
print(ktory_min([4, 1, 5, 27, -7,12]))

def p_n(z:list)->list:
    parne = []
    neparne = []
    for i in z:
        if i % 2 == 0:
            parne.append(i)
        else:
            neparne.append(i)
    return parne, neparne
print(p_n([2,3,5,2,1,4,6,5,3,7]))