z = int(input("zaciatok: "))
k = int(input("koniec: "))
p = 0
for i in range(z,k+1):
    if i % 8 == 0:
        p += 1
print(p)