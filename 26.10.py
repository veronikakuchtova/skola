# # import random, zozonam 1=auto, 0= koza, [1,0,1], pozicia 0..2, pop jednu, nemoze ta ktoru si vybral ani auto,pocet pozitivnych deleno pocet celkovych
# import random
# vyhra =0
# opakovanie = int(input('zadaj pocet opakovani: '))
# for i in range(opakovanie):
#     dvere = [0, 1, 0]
#     random.shuffle(dvere)
#     vyber = random.choice(dvere)
#     if dvere[vyber] == 1:
#         vyber = 0
#     else:
#         vyber = 1
#         vyhra += 1
# print('win rate', (vyhra/opakovanie)*100, '%')

names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
cisla = []
def spracuj_cisla():
    global cisla
    for cislo in names:
        fr = open('cislo/'+cislo+'.txt', 'r')
        for line in fr:
            print(line)
spracuj_cisla()