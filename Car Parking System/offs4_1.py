from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter
import sqlite3

#from s4 import *


#from s4 import form

w = customtkinter.CTk()

w.geometry("750x750")
w.title("Block 1")

customtkinter.set_appearance_mode("dark")

def submit():
    slts = []
    for i in listb.curselection():
        slts.append(listb.get(i))
    
    con=sqlite3.connect(database=r"slots.db")
    cur=con.cursor()

    try:
        cur.execute("Insert into slots(slts) values(?)",(slts))
        con.commit()
        messagebox.showinfo("Success","Slot Added Sucessfully",parent=w)

    except Exception as ex:
        messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=w)


    print(slts)

    w.destroy()
    import s4
    
def back():
    w.destroy()
    import offs3


listb = Listbox(w, selectmode='multiple')
listb.pack(fill=BOTH, pady=50,expand=True)

for i in range(1, 15):
    listb.insert(END, 'Slot' + str(i))

button2 = customtkinter.CTkButton(w, text="Next", command=submit, width=190,height=40)
button2.pack(pady=50,side=customtkinter.RIGHT)

button1 = customtkinter.CTkButton(w, text="Back", command=back, width=190,height=40)
button1.pack(pady=200,side=customtkinter.LEFT)
#scrollbar.config(command=Text.yview)

w.mainloop()

