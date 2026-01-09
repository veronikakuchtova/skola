import tkinter as tk
win = tk.Tk()
win.title("window")

def sprav():
    color = canvas.itemcget(id_stvorec, "fill")
    if color == "red":
        canvas.itemconfig(id_stvorec, fill="blue")
        canvas.itemconfig(id_kruznica, fill="yellow")
    else:
        canvas.itemconfig(id_stvorec, fill="red")
        canvas.itemconfig(id_kruznica, fill="#9F9F9F")


canvas = tk.Canvas(win, width=400, height=400, bg="#9F9F9F")
canvas.pack() #uplaces the canvas on the window
button =tk.Button(win, text='Button 1', command=sprav)
button.pack()

id_stvorec = canvas.create_rectangle(10, 10, 90, 50, fill="red", outline="black", tags='obj1') #1
id_kruznica = canvas.create_oval(100, 100, 350, 350, fill="#9F9F9F", outline="gray",tags='obj2') #2

win.mainloop()