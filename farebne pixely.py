from PIL import Image

img = Image.open("moj obrazok")
pixels = img.load()

def find_closest_palette_color(oldpixel):
    temp = (oldpixel[0]+oldpixel[1]+oldpixel[2])/3
    if temp >=127:
        return 255,255,255
    else:
        return 0,0,0
def odpocet(old, new):
    return old[0]-new[0], old[1]-new[1], old[2]-new[2]
def process_tuple(tuple1, tuple2, number):
    return int(tuple2[0]*number + tuple1[0]), int(tuple2[1]*number + tuple1[1]), int(tuple2[2]*number + tuple1[2])

for y in range(img.size[1]):
    for x in range(img.size[0]):
        oldpixel = pixels[x,y]
        newpixel= find_closest_palette_color(pixels[x,y])
        pixels[x,y] = newpixel
        quant_error = odpocet(oldpixel,newpixel)
        if x>0 and x<img.size[0]-1 and y < img.size[1]-1:
            pixels[x+1,y] = process_tuple( pixels[x + 1,y    ] , quant_error , 7 / 16)
            pixels[x - 1,y + 1] = process_tuple(pixels[x - 1,y + 1] , quant_error , 3 / 16)
            pixels[x,y + 1] = process_tuple
img.show()