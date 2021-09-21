# tips/tricks/functions

from tkinter import *
root = Tk()
root.geometry("500x400")
root.title("GUI")

# to change the icon of the page (initially, its feather)
root.wm_iconbitmap("1.jpg")

# to set the background of the GUI
root.configure(background="grey")

# to check the height and width of the screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height}")

# to destroy/close thw GUI window
Button(text="Close", command= root.destroy).pack()

root.mainloop()
