from PIL import Image
pic = Image.open("imagesinfo.jpg")
fw = open("obr.txt","w", encoding="utf-8")
fw.write(str(pic.size[0])+" "+str(pic.size[1])+"\n")
pixels = pic.load()
for y in range(pic.size[1]):
    for x in range(pic.size[0]):
        red = hex(pixels[x, y][0])[2::]
        green = hex(pixels[x, y][1])[2::]
        blue = hex(pixels[x, y][2])[2::]
        if len(red) < 2:
            red = '0'+red
        if len(green) < 2:
            green = '0'+green
        if len(blue) < 2:
            blue = '0'+blue
        fw.write(red+green+blue)
    fw.write('\n')
fw.close()

fr = open("obr (1).txt","r",encoding="utf-8")
width, height = map(int,fr.readline().split())
img = Image.new("RGB",(width,height))
pixels = img.load()
for y in range(height):
    line = fr.readline().strip()
    for x in range(width):
        h_colour = line[x*6:(x+1)*6]
        red = int(h_colour[0:2], 16)
        green = int(h_colour[2:4], 16)
        blue = int(h_colour[4:6], 16)
        pixels [x,y] = (red,green,blue)
img.show()
