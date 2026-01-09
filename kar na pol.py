import math
x = int(input("Zadaj x-suradnicu: "))
y = int(input("Zadaj y-suradnicu: "))
r = (((x**2) + (y**2))**0.5)
aplha = math.degrees(math.atan2(y,x))
if x and y < 0:
    aplha += 360
print(r,aplha)
