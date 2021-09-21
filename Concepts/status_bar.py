# status bar

from tkinter import *

def upload():
    status_variable.set("Busy...")
    status_bar.update()
    import time
    time.sleep(2)
    status_variable.set("Ready now...")

root = Tk()
root.geometry("700x600")
root.title("Introducing scroll-bars")

status_variable = StringVar()
status_variable.set("Ready")
status_bar = Label(root, textvariable= status_variable, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command= upload).pack()
root.mainloop()
