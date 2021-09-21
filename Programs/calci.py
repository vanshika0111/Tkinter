# calculator

from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Calculator")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if (scvalue.get().isdigit()):
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar= scvalue, font="lucida 40 bold")
screen.pack(fill = "x", ipadx = 7, pady = 9, padx = 10)

# first line
f = Frame(root, bg="grey")
b = Button(f, text="9", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="8", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="7", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

# second line
f = Frame(root, bg="grey")
b = Button(f, text="6", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="5", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="4", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

# third line
f = Frame(root, bg="grey")
b = Button(f, text="3", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="2", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="1", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

# fourth line
f = Frame(root, bg="grey")
b = Button(f, text="0", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="-", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="*", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

# fifth line
f = Frame(root, bg="grey")
b = Button(f, text="/", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="%", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="=", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

# sixth line
f = Frame(root, bg="grey")
b = Button(f, text="+", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="c", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b = Button(f, text="DEL", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()



root.mainloop()