from tkinter import *

root = Tk()
root.title("Registration Form")
root.geometry("444x555")

file = open("data.txt","a")
def Values():
    # print("hellloooo")
    file.write("helloooooo")
# f1 = Frame(root, bg="gray", borderwidth=6, relief=SUNKEN)
# f1.pack(side=TOP, fill=X)
# l = Label(f1, text="Registration Form")
# l.pack(padx=143)

Label(root, text="First Name:").grid(row=1,column=0)
Label(root, text="Last Name:").grid(row=2,column=0)
Label(root, text="Phone Number:").grid(row=3,column=0)

FirstName = StringVar
LastName = StringVar
Phone = IntVar

Entry(root, textvariable = FirstName).grid(row=1, column=1)
Entry(root, textvariable = LastName).grid(row=2, column=1)
Entry(root, textvariable = Phone).grid(row=3, column=1)

Button(root, fg="blue", text="Register", command=Values).grid(row=4,column=0)


file.close()



root.mainloop()
