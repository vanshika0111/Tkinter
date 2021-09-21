# list box

from tkinter import *

root=Tk()
root.geometry("500x400")
root.title("List boxes")

def add():
    global i
    list_box.insert(ACTIVE, f"{i}")
    i += 1

i=0
list_box = Listbox(root)
list_box.insert(END, "First")
list_box.pack()

Button(root, text="Add Items", command=add).pack()

root.mainloop()