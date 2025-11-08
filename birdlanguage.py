def translation(vstup):
    vowels = 'aeiouy'
    consonants = 'qwrtpsdfghjklzxcvbnm'
    counter = 0
    vystup = ''
    while counter < len(vstup):
        if vstup[counter] in vowels:
            vystup += vstup[counter]
            counter += 3
        elif vstup[counter] in consonants:
            vystup += vstup[counter]
            counter += 2
        else:
            vystup += vstup[counter]
            counter += 1
    return vystup
print(translation("hieeelalaooo"))



