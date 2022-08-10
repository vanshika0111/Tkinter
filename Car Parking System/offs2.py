from tkinter import *
from tkhtmlview import HTMLLabel
from PIL import ImageTk, Image
import customtkinter


root = Tk()
root.title("Car Parking System")
root.geometry("900x700")
root.config(bg='light blue')

def slide3():
    root.destroy()
    import offs3

def getStarted():
    root.destroy()


# heading-top center
T = Text(root, height=5, width=52)
title = Label(root, text="Smart Parking System",
              bg="lightblue", font=('Helvetica', 25, 'bold italic'))

title.place(x=300, y=30)

# photo-left
photo = Image.open("bg2.jpg")
photo = photo.resize((400, 400))
photo1 = ImageTk.PhotoImage(photo)
label1 = Label(root, image=photo1)

label1.place(x=60, y=100)


T1 = Text(root, height=5, width=52)
title = Label(root, text="Need a Parking Space?",
              bg="lightblue", font=('Helvetica', 25, 'bold italic'))
title.place(x=500, y=200)
T2 = Text(root, height=5, width=52)
title = Label(root, text="      Don't Worry! We've got you.      ",
              bg="lightblue", font=('Helvetica', 15, 'bold italic'))
title.place(x=500, y=300)


# First button - below text

dwnd = PhotoImage(
    file='Picture1.png')
# dwnd = dwnd.resize((100, 100))
bt=Button(root, image=dwnd, command=slide3, borderwidth=0,
       bg="light blue").place(x=500, y=400)

root.mainloop()
