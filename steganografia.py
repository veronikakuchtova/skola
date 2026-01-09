
#kodovanie = prepis spravy do inej abecedy ale kluc poznam
# sifrovanie = prepis spravy do inej abecedy ale kluc sa utajuje - symetricke: jeden kluc, asymetricke: dva kluce(sukromny a verejny)
# steganografia = schovam spravu, aby nepriatel vedel, ze sa nebavime, budeme spravu skryvat do obrazku
# obrazok sa zmeni minimalne
# princip:
# clovek je najviac citlive na green, a najmenej na blue
# budeme to skryvat do modrej, iba ascii znaky ( ziadne dlzne, makcene )
# znaku 'a' priradim nejaku ascii hodnotu, kedze je to cislo, vieme ho previest do dvojkovej sustavy
# ak pocet znakov v dvoj. sustave je  mensie ako 7 (dohodli sme sa na 7-mice), treba ich doplnit nulami, budem potrebovat 7 pixelov
# jedno pismenko vydrtim do 7-mich pixelov
# ake je binarna hodnota blue, a binarna hodnota mojho pismenka = od konca blue a od zaciatku pismenka a menime ich, poslednu cislicu prepisem
# na hodnotu pismenka
# [x,y] x = pozicia%sirka, y = pozicia//sirka

from PIL import Image
message=input('Zadaj mi spravu na steganografiu:')
pic = Image.open('pzthon obrayok.png')

def codingMessage(message):
    output =''
    message +="#"
    for znak in message:
        temp = bin(ord(znak))[2::]
        if len(temp) < 7:
            zeros = 7 - len(temp)
            temp = '0'*zeros + temp
        output += temp
    return output

def hideMessage(output,pic):
    pixels = pic.load() # vytvori 2D  pole pixelov
    for i in range(len(output)):
        x = i % pic.size[0]
        y = i // pic.size[0]
        pixel = pixels[x,y] # toto uz je RGB konkretneho pixelu napr. (170,10,223) - tuple
        red = pixel[0]
        green = pixel[1]
        blue = bin(pixel[2])[2:-1:] # odtrhnem prv0 dve lebo 0b a odtrhnem aj poslednu
        new_blue = int(blue+output[i],2)
        pixels[x,y] = (red,green,new_blue)
#    pic.show()
    pic.save('newpzthon obrayok.png')
ou= codingMessage(message)
hideMessage(ou,pic)


from PIL import Image
pic = Image.open('pzthon obrayok.png')
def picture_unshreder(pic):
    pixels = pic.load()
    buffer = ''
    for y in range(pic.size[1]):
         for x in range(pic.size[0]):
             buffer += bin(pixels[x,y][2])[-1]
             if len(buffer) == 7:
                znak = chr(int(buffer,2))
                buffer =''
                print (znak, end='')
                if znak =="#":
                    return
ou= codingMessage(message)
hideMessage(ou,pic)

pic1 = Image.open('pzthon obrayok.png')
picture_unshreder(pic1)
