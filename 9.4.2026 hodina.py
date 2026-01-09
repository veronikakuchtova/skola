from PIL import Image
img = Image.new("RGB", (300,300), 'white')
bod_a = input("Zadaj mi suradnice bodu A (x,y): ")
x1, y1 = map(int, bod_a.split(","))
bod_b = input("Zadaj mi suradnice bodu B (x,y): ")
x2, y2 = map(int, bod_b.split(","))
pixels = img.load()
if x1 != x2:
    a = (y1-y2)/(x1-x2)
    b = y1 -((y1-y2)/(x1-x2))*x1
    if abs(x1-x2) > abs(y1-y2):
        for x in range(x1,x2+1):
            y = round(a*x+b)
            pixels[x,y] = (0,0,0)
    else:
        for y in range(y1,y2+1):
            x= round((y-b)/a)
            pixels[x,y] = (0,0,0)
