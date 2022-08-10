from itertools import count
from tkinter import *

def click():
    global count
    count +=1
    print(count)
    print("Submitted")

def submit():
    name = entry.get()
    print(f"Hello {name}")

window = Tk()
window.geometry("520x520")
window.title("Log-in form")

icon = PhotoImage(file='C:\\Users\\VANSHIKA\\Desktop\\coding_world\\TKINTER\\Programs\\1.png')
window.iconphoto(True, icon)

window.config(background="grey")

label = Label(window, text="Name", padx=23, pady=10, font="Aesthetic 19")
label.pack()
entry = Entry(window, font=("Arial", 50))
entry.pack(side=LEFT)

Button(window, text="Submit", command=submit, font=("Comic Sans", 15), fg="#00FF00", state=ACTIVE).pack()

window.mainloop()