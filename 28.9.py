# zo 16stkovej sustavy do 10tkovej
def hextodec(cislo:str)->int:
    prevod = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,'A':10, 'B':11, 'C':12, 'D': 13, 'E':14, 'F':15}
    suma = 0
    index = 0
    for znak in cislo[::-1]:
        suma += prevod[znak]*16**index
        index += 1
    return suma
print(hextodec('AA'))

#dectohec du
