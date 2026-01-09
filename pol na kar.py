import math
r = float(input("Zadaj r: "))
u = int(input("Zadaj uhol: "))
z = math.radians(u)
x = r*math.cos(z)
y = r*math.sin(z)
print(round(x,2), round(y,2))

