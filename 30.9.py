fr = open('jozo txt', 'r', encoding='utf-8')
text = fr.read()
slovnik = {}
print(text)
slova = text.split(' ')
print(slova)
for slovo in slova:
# ak koncis bodkou tak ju z teba dostanem
    slovnik[slovo] = slovnik.get(slovo, 0)+ 1
# toto mi zjednodusi, nedam if