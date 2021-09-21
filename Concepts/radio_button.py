# radio buttons

from tkinter import *
from tkinter import messagebox as tm

root = Tk()
root.geometry("400x500")
root.title("Radio Button")

def order():
    tm.showinfo("Order Recieved", f"We've recieved your order of {var.get()}")

var = StringVar()
var.set("Radio")
# var = IntVar()
# var.set(1)

Label(root, text="What's your favourite dish?", font="lucida 19 bold", justify=LEFT, padx=14).pack()
radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Paneer", padx=14, variable=var, value="Paneer").pack(anchor="w")
radio = Radiobutton(root, text="Noodles", padx=14, variable=var, value="Noodles").pack(anchor="w")
radio = Radiobutton(root, text="Manchurian", padx=14, variable=var, value="Manchurian").pack(anchor="w")
radio = Radiobutton(root, text="Samosa", padx=14, variable=var, value="Samosa").pack(anchor="w")
radio = Radiobutton(root, text="Maggie", padx=14, variable=var, value="Maggie").pack(anchor="w")

Button(text="Order Now", command= order).pack()
# use for loop by creating list of menu
root.mainloop()