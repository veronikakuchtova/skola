a = int(input("zaciatok intervalu a:"))
b = int(input("koniec intervalu b:"))
c = int(input("dane cislo:"))
if c > a and c < b:
    print("cislo patri do intervalu" , (a,b))
else:
    print("cislo nepatri do intervalu" , (a,b))