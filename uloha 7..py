a = int(input("prve cislo:"))
b = int(input("druhe cislo:"))
if a > b:
    print(a, "je vacsie ako", b)
elif a == b:
    print("cisla su rovnake")
else:
    print(b, "je vacsie ako", a)