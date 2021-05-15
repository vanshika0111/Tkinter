from tkinter import *

userValue = StringVar
pwdValue = StringVar

root = Tk()
root.geometry("333x444")

user= Label(root, text="Username")
user.grid()
pwd = Label(root, text="Password")
pwd.grid(row=1)

#widgets are the input tag boxes where user can enter the data
# Entry widget

#types of variable class in tkinter
# 1. BooleanVar 2. DoubleVar 3. IntVar 4. StringVar

userEntry = Entry(root, textvariable = userValue)
pwdEntry = Entry(root, textvariable = pwdValue)

userEntry.grid(row=0, column=1)
pwdEntry.grid(row=1, column=1)

def getValue():
    print(f"The username is {userValue.get()}")
    print(f"The password is {pwdValue.get()}")
    #print(userValue.get())
    #print(pwdValue.get())
    #pass

Button(text="Submit", command=getValue).grid()
root.mainloop()