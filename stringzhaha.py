# heslo = input('Zadaj mi heslo: ')
# status = True
# if len(heslo) >= 8:
#     velke_pismeno = 0
#     for znak in heslo:
#         if znak.isupper():
#             velke_pismeno += 1
#     if velke_pismeno > 0:
#         pismeno = 0
#         for znak in heslo:
#             if znak.isdigit():
#                 pismeno += 1
#         if pismeno > 0:
#             symbol = 0
#             for znak in heslo:
#                 if not znak.isalnum():
#                     symbol += 1
#             if symbol > 0:
#                 status = True
#             else:
#                 status = False
#         else:
#             status = False
#     else:
#         status = False
# else:
#     status = False
# print(status)

# heslo = input('heslo: ')
# poc_p = 0
# poc_c = 0
# poc_z = 0
# for znak in heslo:
#     if znak.isdigit():
#         poc_c += 1
#     if znak.isupper():
#         poc_p += 1
#     if not znak.isalnum():
#         poc_z += 1
# if len(heslo)>8 and poc_c>0 and poc_p>0 and poc_z>0:
#     print(True)
# else:
#     print(False)
# input.sk
# video

#
# def faktorial(n):
#     fak = 1
#     for i in range(2,n+1):
#         fak *= i
#     return fak
#
# def komcis(n,k):
#     return faktorial(n) // (faktorial(n-k)*faktorial(k))
#
# def pasctroj(velkost):
#     for riadok in range(0,velkost):
#         for cislo in range(0,riadok+1): #cyklus v cykle
#             print(komcis(riadok,cislo), end=' ')
#         print('')
# pasctroj(4)
