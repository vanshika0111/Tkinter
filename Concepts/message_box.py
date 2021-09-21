# Messagebox

from tkinter import *
from tkinter import messagebox as tm

root = Tk()
root.geometry("700x600")
root.title("Introducing menus and sub-menus")

def function():
    print("Inside menu function")

def help():
    print("This is for help")
    # a = tm.showinfo("Help", "Help yourself")
    # print(a)
    tm.showinfo("Help", "Help yourself")

def rate():
    print("Rate us")
    value = tm.askquestion("Experience", "How was your experience?")
    # print(value)
    if value == "yes":
        msg = "Great! Tell your friends about us."
    else:
        msg = "What's wrong?"
    tm.showinfo("Feedback", msg)

def friend():
    answer = tm.askretrycancel("Friends?", "Can we be friends??")
    if answer:
        print("I won't let you down.")
    else:
        print("Your loss!")

# to create drop-down menu
FileMenu = Menu(root)

m1 = Menu(FileMenu, tearoff=0)
m1.add_command(label = "Cancel", command= function)
m1.add_command(label = "Save", command= function)
m1.add_separator()
m1.add_command(label = "Save as", command= function)
root.config(menu= FileMenu)
FileMenu.add_cascade(label = "File", menu=m1)

m2 = Menu(FileMenu, tearoff=0)
m2.add_command(label = "Cut", command= function)
m2.add_command(label = "Copy", command= function)
m2.add_separator()
m2.add_command(label = "Paste", command= function)
root.config(menu= FileMenu)
FileMenu.add_cascade(label = "Operations", menu=m2)

m3 = Menu(FileMenu, tearoff=0)
m3.add_command(label = "Exit", command= help)
m3.add_command(label = "Rate", command= rate)
m3.add_command(label = "Friends", command= friend)
FileMenu.add_cascade(label = "End", menu=m3)

root.config(menu = FileMenu)
root.mainloop()

