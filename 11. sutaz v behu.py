fr = open("sutaz_vbehu.txt" , "r")
pocet = 0
first = fr.readline().split()
best_t = int(first[1])
best_n = ''
for line in fr:
    x = line.split()
    if int(x[1]) < best_t:
        best_t = int(x[1])
        best_n = x[0]
    print(f"Súťažiaci {x[0]} dobehol do cieľa za {x[1]} sekund")
    pocet += 1
print ("Počet zúčastnených športovcov:",pocet)
print(f"najlepší súťažiaci: {best_n}, {best_t//60} min. {best_t%60} sec. ")