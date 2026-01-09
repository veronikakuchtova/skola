import math,datetime as dt, tkinter as tk
win = tk.Tk()
win.title("Hodiny")
canvas = tk.Canvas(win, width=500, height=500, bg="hotpink")
canvas.pack()

mid_x = 250 #suradnice kde zacinaju rucicky- stred hodin
mid_y = 250
long_arm = 150 #dlzka velkej rucicky - m(inute)a(rm), sa
short_arm = long_arm //2 #dlzka hodinovej rucicky=ha
lw = 2 #(long arm width)
sw = 3


#natvrdo dam tu rucicky




#vzhlad
def apperance():
    canvas.create_oval(mid_x-long_arm - 50, mid_y-long_arm - 50, mid_x+long_arm + 50, mid_y+long_arm + 50, outline = "black", width= 5,) # lem hodin
    for i in range(12):
        canvas.create_text(mid_x + (long_arm+20)*math.sin(math.radians((i*30)-180)), mid_y + (long_arm+20)*math.cos(math.radians((i*30)-180)),text = 12-i,font =("Courier New", 20, "bold"), fill = "black") #cisla
    for i in range(12):
        canvas.create_line(mid_x,mid_y,mid_x + long_arm*math.sin(math.radians(i*30)), mid_y + long_arm*math.cos(math.radians(i*30)),width = 2, ) #hodinovy cifernik
    for i in range(60):
        canvas.create_line(mid_x,mid_y,mid_x + (long_arm-4)*math.sin(math.radians(i*6)), mid_y + (long_arm-4)*math.cos(math.radians(i*6)),width = 1,) #minutovy cifernik
    canvas.create_oval(mid_x-long_arm + 15, mid_y-long_arm + 15, mid_x+long_arm - 15, mid_y+long_arm - 15, fill = "",) #kruh na vrchu aby bolo vidno len vybezky
    canvas.create_oval(mid_x-long_arm + 20, mid_y-long_arm + 20, mid_x+long_arm - 20, mid_y+long_arm - 20, fill = "hotpink", outline = "",) #kruh na vrchu
    canvas.create_oval(mid_x-5, mid_y-5,mid_x+5, mid_y+5, fill = "black",)#stred


def clocks():
    canvas.delete("all") # toto vyhodim
    #cas
    ac_time = dt.datetime.now()
    #vzhlad
    apperance()
    #rucicky
    sa = canvas.create_line(mid_x, mid_y, mid_x + long_arm*math.cos(math.radians((6*ac_time.second)-90)),mid_y + long_arm*math.sin(math.radians((6*ac_time.second)-90)),width = lw,)
    ma = canvas.create_line(mid_x, mid_y, mid_x + long_arm*math.cos(math.radians((6*ac_time.minute)-90)),mid_y + long_arm*math.sin(math.radians((6*ac_time.minute)-90)),width = sw,)
    hm = canvas.create_line(mid_x, mid_y, mid_x + short_arm*math.cos(math.radians(30*ac_time.hour+ac_time.minute*0.5 -90)),mid_y + short_arm*math.sin(math.radians(30*ac_time.hour+ac_time.minute*0.5 -90)), width =sw, fill = "black",)
    #coords ako getter
    print(canvas.coords(sa))
    #coords ako setter
    canvas.coords(sa,(100,100,200,200)) # idem ovplzvnovat coordinaty ruciciek nie mazat cele platno, jebnem tam od mid_x do koca
    canvas.after(1000,clocks)

# tu dam appereance
win.after(0,clocks)
win.mainloop()