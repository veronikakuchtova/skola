for x in range(1,21):
 if x == 3:
    print(f"x = {x} funkcia nie je definovana")
 else:
     y = (x ** 2 - 1) / (x - 3)
     print(f"x = {x} y= {y}")