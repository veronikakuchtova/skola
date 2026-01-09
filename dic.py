# modulo=7 => vzysok po delenni 7 => %
# zaokruhlim smerom na dol
# round(4.75,2) => co na kolko => pthon funkcia
 #zellerov vzorec

# from math import floor
# datum = input('zadaj mi datum: ten v nasoch tvare DD.MM.YYYY: ')
# parts = datum.split('.') #funkcia (list)
# q = int(parts[0])
# m = int(parts[1])
# K = int(parts[2])%100
# if m == 1 or m == 2:
#     K = K-1
#     m+=12
# J = floor(int(parts[2])/100)
# h = (q+floor(13*(m+1)/5)+K+floor(K/4)+(J/4)-2*J)%7
# print(q,m,K,J)
# zoz = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
# print(zoz[int(h)])

#A[r,alpha] => kartezianske suradnice
#A[1,1] => polarne suradnice

import math
a = int(input('zadaj litre nadrze:'))
b = a*2.5
print(b)
# ram je pamat energeticky zavisla, rychlejsia ako hard disk
# na hard disk sa ukladaju veci vo forme suborov - pripona (txt)
# citanie/zapisovanie = r/w