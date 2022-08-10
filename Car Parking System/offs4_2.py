from tkinter import *
from tkinter import ttk
import customtkinter

#from s4 import form

w = customtkinter.CTk()

w.geometry("750x750")
w.title("Block 2")

customtkinter.set_appearance_mode("dark")

def submit():
    w.destroy()
    import s4
    
def back():
    w.destroy()
    import offs3


listb = Listbox(w, selectmode='multiple')
listb.pack(fill=BOTH, pady=50,expand=True)

# scrollbar = Scrollbar(listb)
# scrollbar.pack(side=RIGHT, fill=Y)

for i in range(1, 26):
    listb.insert(END, 'Slot' + str(i))

#listb.config(yscrollcommand=scrollbar.set)

#scrollbar.config(command=listb.yview)

'''
listBox = Listbox(w)

scrollbar = Scrollbar(listBox)
scrollbar.pack(side=RIGHT, fill=Y)

listBox = Listbox(w, yscrollcommand=scrollbar.set)

for i in range(51):
    listBox.insert(END, f"Item {i}")
    # if i==10 or i==15 or i==30:
    #     listBox.config(state=DISABLED)

listBox.pack(fill="both", padx=22, pady=30)
scrollbar.config(command=listBox.yview)
'''

button2 = customtkinter.CTkButton(w, text="Next", command=submit, width=190,height=40)
button2.pack(pady=50,side=customtkinter.RIGHT)

button1 = customtkinter.CTkButton(w, text="Back", command=back, width=190,height=40)
button1.pack(pady=200,side=customtkinter.LEFT)
#scrollbar.config(command=Text.yview)

w.mainloop()