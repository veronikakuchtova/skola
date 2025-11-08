import random
vowels = 'aeiouy'
consonants = 'qwrtpsdfghjklzxcvbnm'
def translation(vstup):
    counter = 0
    vystup = ''
    while counter < len(vstup):
        if vstup[counter] in consonants:
            vystup = vystup + vstup[counter] + random.choice(vowels)
            counter += 1
        elif vstup[counter] in vowels:
            vystup = vystup + (vstup[counter]*3)
            counter = counter + 1
        else:
            vystup = vystup + vstup[counter]
            counter = counter + 1
    return vystup
print(translation("hello"))