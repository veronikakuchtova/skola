a = int(input("zaciatok intervalu: "))
b= int(input("koniec intervalu: "))
for i in range(a,b+1):
    print(i, round(i**0.5, 2))