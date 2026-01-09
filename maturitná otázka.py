vstup = 'maturujeme v pythone'
kluc = 'abc'
novy_kluc = kluc*(len(vstup)//len(kluc))+kluc[:len(vstup)%len(kluc)] # v jednom riadku vypocet
vystup = ''
# inicializovali sme premennu vystup
for i in range(len(vstup)):
    if 97<=ord(vstup[i]) and ord(vstup[i])<=122:
        posun = ord(novy_kluc[i])-96
        vystup = chr((ord(vstup[i])-97+posun)%26+97)
    else:
        vystup += vstup[i]
print(vystup)


