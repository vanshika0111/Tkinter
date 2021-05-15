from tkinter import *

#imprt the following module to display jpg images
from PIL import Image, ImageTk
import os

#creates basic gui  #Tk is an object
root = Tk()  

#to set the size of window ("widthxheight")
root.geometry("160x220")

#to display image in the window with extension jpg
image_no_1 = ImageTk.PhotoImage(Image.open("1.jpg"))
image_no_2 = ImageTk.PhotoImage(Image.open("2.jpg"))
image_no_3 = ImageTk.PhotoImage(Image.open("3.jpg"))
image_no_4 = ImageTk.PhotoImage(Image.open("4.jpg"))
image_no_5 = ImageTk.PhotoImage(Image.open("5.jpg"))
image_no_6 = ImageTk.PhotoImage(Image.open("6.jpg"))
image_no_7 = ImageTk.PhotoImage(Image.open("7.jpg"))
image_no_8 = ImageTk.PhotoImage(Image.open("8.jpg"))

#list of traverse images
List_images = [image_no_1, image_no_2, image_no_3, image_no_4, image_no_5, image_no_6, image_no_7, image_no_8]

label = Label(image=image_no_1)
  
#to mark a grid
label.grid(row=1, column=0, columnspan=3)
label.pack()
  
#to create three buttons for forword, exit, back
button_back = Button(root, text="Back", command=back, state=DISABLED)
  
# root.quit for closing the app
button_exit = Button(root, text="Exit", command=root.quit)
  
button_forward = Button(root, text="Forward", command=lambda: forward(1))
  
# grid function is for placing the buttons in the frame
button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)

#creates event loop 
root.mainloop()   