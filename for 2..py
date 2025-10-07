a = int(input("zadaj cislo: "))
for i in range(1,a):
    print(i)

b = int(input("zadaj cislo: "))
for i in range(1,b):
    if i < b:
        print(i, end=",")
else:
    print(b, end=" ")