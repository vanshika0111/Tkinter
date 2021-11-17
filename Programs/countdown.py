from tkinter import *
import time
import playsound

root = Tk()
root.title("Clock")
root.geometry("400x400")
root.resizable(0,0)  #to prevent resizing
root.config(bg ='blanched almond')

Label(root, text = 'Clock Timer',  bg="cyan", font="Aesthetic 19", relief=SUNKEN).pack()

Label(root, font ='arial 15 bold', text = 'Current Time :', bg = 'papaya whip').place(x = 40 ,y = 70)
def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)
curr_time =Label(root, font ='arial 15 bold', text = '', fg = 'gray25' ,bg ='papaya whip')
curr_time.place(x = 190 , y = 70)
clock()


root.mainloop()