import tkinter as tk

fr = open('glider-gun.txt', 'r')
height = int(fr.readline().strip())
witdh = int(fr.readline().strip())
print(height,witdh)

cell_size = 20 # ako velka je ta bunka
win = tk.Tk()
canvas = tk.Canvas(win, width=witdh*cell_size, height=height*cell_size, bg='lightblue')
canvas.pack()
generation = 1


print(height)
print(witdh)

dish1 = []
dish2 = []

def create_grid():
    for y in range(0, height * cell_size, cell_size):
        canvas.create_line(0, y, witdh * cell_size, y, fill='white')
    for x in range(0, witdh * cell_size, cell_size):
        canvas.create_line(x, 0, x, height * cell_size, fill='white')

def draw_fish(dish):
    for y in range(height):
        for x in range(witdh):
            if dish1[y][x] == 1:
                canvas.create_rectangle(x*cell_size, y*cell_size, x*cell_size+cell_size, y*cell_size+cell_size, fill='black', outline='white')

def life():
    global generation
    canvas.delete('all')
    create_grid()
    if generation % 2 == 1:
        dish_sanitizer(dish2)
        copy_dishes(dish1, dish2)
        draw_fish(dish1)
    else:
        dish_sanitizer(dish1)
        copy_dishes(dish2, dish1)
        draw_fish(dish2)
    generation += 1
    canvas.after(100, life)



def create_dishes():
    global dish1, dish2 # global udrzuje zoznamy aby sa neskoncili ked sa skonci funkcia
    for i in range(height):
         # syntax sugar,urobi zoznam ktory bude mat *width hodnota ktora bude mat v []
        dish2.append([0]*witdh)
        dish1.append([0]*witdh)
        #dish1 = dish2 toto zlo, lebo su to smerniky na tu istu strukturu
    x = 0
    y = 0
    for riadok in fr:
        x=0
        for znak in riadok.strip():
            if znak != '-':
                dish1[y][x] = 1
            x+=1
        y+=1

def get_neighbors(dish,x,y):
    neighbors = 0
    if x > 0 and y > 0 and dish[y-1][x-1] == 1:
        neighbors += 1
    if y > 0 and dish[y-1][x] == 1:
        neighbors += 1
    if x < witdh-1 and y > 0 and dish[y-1][x+1] == 1:
        neighbors += 1
    if x > 0 and dish[y][x-1] == 1:
        neighbors += 1
    if x < witdh-1 and dish[y][x+1] == 1:
        neighbors += 1
    if x > 0 and y < height-1 and dish[y+1][x-1] == 1:
        neighbors += 1
    if y < height-1 and dish[y+1][x] == 1:
        neighbors += 1
    if y < height-1 and x < witdh-1 and dish[y+1][x+1] == 1:
        neighbors += 1
    return neighbors

def dish_sanitizer(dish):
    for y in range(height):
        for x in range(witdh):
            dish[y][x] = 0

def copy_dishes(source, destination):
    for y in range(height):
        for x in range(witdh):
            if source[y][x] == 1:
                if get_neighbors(source, x,y) < 2:
                    destination[y][x] = 0
                if get_neighbors(source, x,y) in (2,3): # dva alebo tri
                    destination[y][x] = 1
                if get_neighbors(source, x,y) > 3:
                    destination[y][x] = 0
            else:
                if get_neighbors(source, x,y) == 3:
                    destination[y][x] = 1


create_dishes()
print(dish1)
create_grid()
draw_fish(dish1)
life()
win.mainloop()
