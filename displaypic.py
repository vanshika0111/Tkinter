from tkinter import *

#imprt the following module to display jpg images
from PIL import Image, ImageTk
import os

#creates basic gui  #Tk is an object
root = Tk()  

#to set the size of window ("widthxheight")
root.geometry("160x220")

#to display image in the window with extension of png
photo = PhotoImage(file="1.png")
label = Label(image=photo)
label.pack()

#to display image in the window with extension jpg
image = Image.open("vanshika.jpg")
photo2 = ImageTk.PhotoImage(image)
label = Label(image=photo2)
label.pack()

#creates event loop 
root.mainloop()   

