from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def update_time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, update_time)

label = Label(root, font= ("ds-digital", 80), background= "black", foreground = "#e90555")
label.pack(anchor = "center")
update_time()

mainloop()