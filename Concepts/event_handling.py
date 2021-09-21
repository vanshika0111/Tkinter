# event handling

from tkinter import *

def handling(event):
    print(f"Subscribed at {event.x}, {event.y}")
root = Tk()
root.title("Event handling in tkinter")
root.geometry("600x300")

widget = Button(root, text = "Click here to subscribe").pack()
widget.bind('<Button-1>', handling)
widget.bind('<Double-1>', handling)
root.mainloop()