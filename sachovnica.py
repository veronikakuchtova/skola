# zoznam v zozname na sachovnicu = kniznica je na to NUMPY -> silna kniznica na matematiku
from PIL import Image, ImageDraw
chessboard = []
counter = 0

def createImage():
    obrazok = Image.new("RGB", (400, 400), "white")
    kreslenie = ImageDraw.Draw(obrazok)
    for riadok in range(8):
        for stlpec in range(8):
            if (riadok + stlpec) % 2 == 0:
                kreslenie.rectangle((stlpec * 50, riadok * 50, stlpec * 50 + 50, riadok * 50 + 50), fill="black")
    return obrazok

def create_chessboard():
    global chessboard
    row = [0]*8
    #  chessboard = [row] * 8 Maxi Pruser nikdy takto!!!!!!!!
    for i in range(8):
        row = [0] * 8
        chessboard.append(row)

def checkit(x,y):
    for i in range(0,8):
        if chessboard[y][i] == 1:
            return False
        if chessboard[i][x] == 1:
            return False
    for i in range(0,8):
        for j in range(0,8): #y
            if i + j == x+y:  #x
                if chessboard[i][j] == 1:
                    return False
            if i - j == y - x:
                if chessboard[i][j] == 1:
                    return False
    return True

def queens(n):
    global chessboard
    global counter
    if n == 8:
        counter += 1
        print(chessboard)
        print('------------------------')
        Drawqueens()
    else:
        for i in range(8):
            if checkit(i,n):
                chessboard[n][i] = 1
                queens(n+1)
                chessboard[n][i] = 0

def Drawqueens():
    obrazok = createImage()
    dama = Image.open("damaplsuz.png")
    dama = dama.resize((40, 40))
    for riadok in range(8):
        for stlpec in range(8):
            if chessboard[riadok][stlpec] == 1:
                obrazok.paste(dama,(stlpec * 50 + 5, riadok * 50 + 5), dama)
    obrazok.save("riesenie" + str(counter) + ".png")

#tgransparent queen
create_chessboard()
queens(0)





