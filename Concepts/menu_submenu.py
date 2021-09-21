# menu and sub-menu

from tkinter import *

root = Tk()
root.geometry("700x600")
root.title("Introducing menus and sub-menus")

def function():
    print("Inside menu function")

# to create non-drop menu
# menu = Menu(root)
# menu.add_command(label = "File", command= "function")
# menu.add_command(label = "Exit", command= quit)

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
m2.add_command(label = "Cancel", command= function)
m2.add_command(label = "Save", command= function)
m2.add_separator()
m2.add_command(label = "Save as", command= function)
root.config(menu= FileMenu)
FileMenu.add_cascade(label = "File", menu=m2)

root.config(menu = FileMenu)
root.mainloop()
