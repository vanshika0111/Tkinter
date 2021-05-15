from tkinter import *

#creates basic gui  #Tk is an object
root = Tk()  

#gui logic

#to make the title of the window
root.title("hello")

#to set the size of window ("widthxheight")
root.geometry("160x220")

#to set the minimum size of window (width,height)
root.minsize(200,100)

#to set the maximum size of window (width,height)
root.maxsize(1200,900)

#to make the label
label = Label(text="Hello. Welcome to this GUI")
#always pack the attribute or else program will runs but wont diplay the respective attributes
#there are three ways to pack the tags.
# 1. .pack() 2. .grid() 3. .place()
label.pack()


#creates event loop 
root.mainloop()   


