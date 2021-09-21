# sliders

from tkinter import *
from tkinter import messagebox as tm

root = Tk()
root.geometry("400x500")
root.title("Sliders")

def coffee():
    print(f"Booked {slider2.get()} coffee")
    tm.showinfo("Booked", f"{slider2.get()} coffee booked")

# slider = Scale(root, from_=0, to=100)
# slider.pack()

Label(root, text="Rate yourself...").pack()
slider2 = Scale(root, from_=0, to=100, orient= HORIZONTAL, tickinterval=50)
# slider2.set(30)
slider2.pack()

Button(root, text="Get yourself a coffee", command=coffee).pack()
root.mainloop()