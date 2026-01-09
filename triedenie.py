# list []
# tuple () -> nevieme v nim menit hodnoty
# dic {1:'joozo'}
# set {} -> mnozina
# okrem listu coming soon
# list = [1,10,7,100,8] = funkcia sort = utriedim jednym prikazom
# ak zoznam ma n prvkov tak to bude n**2 => najrychlejsi algoritmus n.log(n)
#bubble sort
# import random
# def generuj(dlzka:int)->list:
#     zoz=[]
#     for i in range(dlzka):
#         zoz.append(random.randint(1,101 ))
#     return zoz
# zoz = generuj(15)
# print(zoz)
#
# def vybublaj(zoz:list,n:int):
#     for i in range(n-1):
#         if zoz[i] > zoz[i+1]:
#             zoz[i],zoz[i+1] = zoz[i+1],zoz[i]
#
# for i in range(len(zoz),1,-1):
#     vybublaj(zoz,i)
#
# # for y in range(len(zoz),1,-1):
# #     for i in range(y-1):
# #         if zoz[i] > zoz[i+1]:
# #             zoz[i],zoz[i+1] = zoz[i+1],zoz[i] -> cyklus v cykle
#
# print(zoz)
# same shit different way
# triedenie vkladanim
# import random
# def generuj(dlzka:int)->list:
#     zoz=[]
#     for i in range(dlzka):
#         zoz.append(random.randint(1,101 ))
#     return zoz
# zoz = generuj(15)
# print(zoz)
#
# def maximum_index(list):
#     maximum = list[0]
#     poz_max = 0
#     for i in range(1,len(list)):
#         if list[i] > maximum:
#             maximum = list[i]
#             poz_max = i
#     return poz_max
#
# def same_shit(zoz:list):
#      for y in range(len(zoz),1,-1):
#          hightest = maximum_index(zoz[:y])
#          zoz[hightest],zoz[y-1]= zoz[y-1],zoz[hightest]
# same_shit(zoz)
# print(zoz)

# vonkajsi for vnutorny while
# zaciname od 2. prvku =>vonkajsi for
# vnutorny = > while, ak si vacsi a ak nie si mimo
# triedenie priamim vyberom
# import random
# def generuj(dlzka:int)->list:
#     zoz=[]
#     for i in range(dlzka):
#         zoz.append(random.randint(1,101 ))
#     return zoz
# zoz = generuj(15)
# print(zoz)

