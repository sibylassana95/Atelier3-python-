from tkinter import *

gui = Tk()
var = StringVar()
label = Label(gui, textvariable=var, relief=RAISED)

var.set("Bienvenue Siby!")
label.pack()
gui.mainloop()
