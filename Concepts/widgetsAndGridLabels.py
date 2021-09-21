# widget and grid labels

from tkinter import *

def getValue():
    print(f"The username is {userValue.get()}")
    print(f"The password is {pwdValue.get()}")
    # print(userValue.get())
    # print(pwdValue.get())
    return

# def getValue():
#     user = userValue.get()
#     pwd = pwdValue.get()
#     print("The username is " + user)
#     print("The password is " + pwd)
#     userValue.set("")
#     pwdValue.set("")

root = Tk()
root.geometry("333x444")

user= Label(root, text="Username")
password = Label(root, text="Password")
user.grid()
password.grid(row=1)

#widgets are the input tag boxes where user can enter the data
# Entry widget

userValue = StringVar()
pwdValue = StringVar()

"""
Types of variable class in tkinter
1. BooleanVar 
2. DoubleVar 
3. IntVar 
4. StringVar
"""

userEntry = Entry(root, textvariable = userValue)
pwdEntry = Entry(root, textvariable = pwdValue)

userEntry.grid(row=0, column=1)
pwdEntry.grid(row=1, column=1)

Button(text="Submit", command=getValue).grid()

root.mainloop()