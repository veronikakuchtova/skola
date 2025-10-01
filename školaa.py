import math
a = int(input("Strana a:"))
b = int(input("Strana b:"))
c = int(input("Strana c:"))
d = (a+b+c)
s = (a+b+c)/2
S = math.sqrt(s*(s-a)*(s-b)*(s-c))
e = (2*S)/a
o = (2*S)/b
g = (2*S)/c
alpha = math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
beta = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
gamma = math.degrees(math.acos((b**2+a**2-c**2)/(2*b*a)))
r= S/s
R = a*b*c/ 4*S
ta = 0.5 * math.sqrt(2 * b**2 + 2 * c**2 - a**2)
tb = 0.5 * math.sqrt(2 * a**2 + 2 * c**2 - b**2)
tc = 0.5 * math.sqrt(2 * a**2 + 2 * b**2 - c**2)
print(f"obvod: {d}")
print(f"obsah: {S:.2f}")
print(f"vyska a: {e:.2f}")
print(f"vyska b: {o:.2f}")
print(f"vyska c: {g:.2f}")
print(f"taznica na stranu a: {ta:.2f}")
print(f"taznica na stranu b: {tb:.2f}")
print(f"taznica na stranu c: {tc:.2f}")
print(f"u. alpha: {alpha:.2f}")
print(f"u. beta: {beta:.2f}")
print(f"u. gamma: {gamma:.2f}")
print(f"polomer vpisanej kruznice: {r:.2f}")
print(f"polomer opisanej kruznice: {R:.2f}")
if a==b and c < b and c < a or b==c and a < b and a < c or a==c and b < c and b < a:
    print("trojuholnik je rovnorameny")
elif a==b and b==c and a==c:
    print("trojuholnik je rovnostrany")
else:
    print("trojuholnik je roznostrany")



