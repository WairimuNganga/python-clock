from tkinter import *
from tkinter.ttk import *
from time import strftime

great = Tk()
great.title("CLOCK")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)

label = Label(great,font=("arial",80),background = "black",foreground = "cyan")
label.pack(anchor="center")
time()

mainloop()

