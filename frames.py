from tkinter import *
root = Tk()
root.geometry("555x333")
f1 = Frame(root, bg="gray", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)
l = Label(f1, text="project")
l.pack(pady=143)

f2 = Frame(f1, bg="gray", borderwidth=9, relief=SUNKEN)
#to make separate frame write root instead of f1
f2.pack(side=TOP, fill=X)
l = Label(f2, text="welcome", font="Helvetica 16 bold", fg="brown", pady=9 )
l.pack()
root.mainloop()