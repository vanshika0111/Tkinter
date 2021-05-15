from tkinter import *
root = Tk()
root.geometry("444x555")
frame = Frame(root, borderwidth=8, bg="gray", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

def hello():
    print("Welcome")

def name():
    print("Vanshika")

def age():
    print("18")

def year():
    print("2021")

b1 = Button(frame, fg="blue", text="Now", command=hello)
#here function is not called thus () ie arguments are not fixed here 
#just function name is written here
#command just executes the given function in the output console
b1.pack(side=LEFT, padx=10)

b2 = Button(frame, fg="blue", text="Then", command=name)
b2.pack(side=LEFT, padx=10)

b3 = Button(frame, fg="blue", text="Now", command=age)
b3.pack(side=LEFT, padx=10)

b3 = Button(frame, fg="blue", text="Now", command=year)
b3.pack(side=LEFT, padx=10)

root.mainloop()