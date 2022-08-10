from tkinter import *
from PIL import ImageTk, Image
import time



r1=Tk()

width_of_window=427
height_of_window=250
screen_width=r1.winfo_screenwidth()
screen_height=r1.winfo_screenheight()
x_coordinate=(screen_width/2)-(width_of_window/2)
y_coordinate=(screen_width/2)-(width_of_window/2)
r1.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

#======New window====
def new_win():
    q=Tk()
    q.geometry("500x600+300+200")
    q.title("main window")
    q.mainloop()

Frame(r1,width=427,height=250,bg='#272727').place(x=0,y=0)
label1=Label(r1, text='PARKING SYSTEM',fg='white',bg='#272727')
label1.configure(font=("Game Of Squids",24,"bold"))
label1.place(x=40,y=90)

label2=Label(r1, text='Loading....',fg='white',bg='#272727')
label2.configure(font=("Calibri",11,"bold"))
label2.place(x=10,y=215)

image_a=ImageTk.PhotoImage(Image.open('c2.png'))


image_b=ImageTk.PhotoImage(Image.open('c1.png'))

for i in range(2):  #delay
    l1=Label(r1,image=image_a,border=0,relief=SUNKEN).place(x=180,y=145)
    l2=Label(r1,image=image_b,border=0,relief=SUNKEN).place(x=200,y=145)
    l3=Label(r1,image=image_a,border=0,relief=SUNKEN).place(x=220,y=145)
    l4=Label(r1,image=image_b,border=0,relief=SUNKEN).place(x=240,y=145)
    r1.update_idletasks()
    time.sleep(1.5)

    l1=Label(r1,image=image_b,border=0,relief=SUNKEN).place(x=180,y=145)
    l2=Label(r1,image=image_a,border=0,relief=SUNKEN).place(x=200,y=145)
    l3=Label(r1,image=image_b,border=0,relief=SUNKEN).place(x=220,y=145)

r1.destroy()

import offs2