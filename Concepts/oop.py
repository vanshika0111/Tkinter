# using classes and objects to create GUIs

from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)
    def click(self):
        print("Button clicked")
    def button(self, inptext):
        Button(text = inptext, command= self.click).pack()

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.button("click me")
    window.mainloop()