from PIL import Image
pic = Image.new("RGB", (100, 100), "white")
pixels = pic.load()

a_cords = input("coordinates of the first point(x,y) ").split(",")
b_cords = input("coordinates of the second point(x,y) ").split(",")

a1, a2 = int(a_cords[0]), int(a_cords[1])
b1, b2 = int(b_cords[0]), int(b_cords[1])

if a2 > b2:
    a2 , b2 = b2 , a2
if a1 > b1:
    a1, b1 = b1, a1

pixels[a1,a2] = (0,0,0)
pixels[b1,b2] = (0,0,0)

if a1 == b1:
    for y in range(a2,b2):
        x = a1
        pixels[x,y] = (0,0,0)
else:
    a = (a2 - b2) / (a1 - b1)
    b = a2 - (a2 - b2) / (a1 - b1) * a1
    if abs(b1-a1) >= abs(b2-a2):
        for x in range(a1,b1):
            y = int(a*x + b)
            pixels[x,y] = (0,0,0)
    elif abs(b1-a1) < abs(b2-a2):
        for y in range(a2,b2):
            x = int((y-b)/a)
            pixels[x,y] = (0,0,0)
pic.show()