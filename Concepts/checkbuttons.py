# check buttons

from tkinter import *

# includes recordes.txt file

root = Tk()
root.geometry("600x500")

def Values():
    # print("Worked!")
    with open("records.txt","a") as f:
        f.write(f"{nameValue.get(), phoneValue.get(), genderValue.get(), ageValue.get(), subscriptionValue.get()}\n")
    
# top heading of the page
Label(root, text = "Welcome to the virtual world!", font = "comicsansms 13 bold", pady = 5).grid(row=0, column = 3)

# heading sf the content
name = Label(root, text = "Name: ")
phone = Label(root, text = "Phone: ")
gender = Label(root, text = "Gender: ")
age = Label(root, text = "Age: ")

# packing the headings of the page
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
age.grid(row=4, column=2)

# variables for storing the user-entered information
nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
ageValue = StringVar()
subscriptionValue = IntVar()    #checkbox --> either yes or no

# creating entries for headings
nameEntry = Entry(root, textvariable = nameValue)
phoneEntry = Entry(root, textvariable = phoneValue)
genderEntry = Entry(root, textvariable = genderValue)
ageEntry = Entry(root, textvariable = ageValue)

# packing the entry boxes 
nameEntry.grid(row=1, column=3)
phoneEntry.grid(row=2, column=3)
genderEntry.grid(row=3, column=3)
ageEntry.grid(row=4, column=3)

# creating & packing checkbox
Subscription = Checkbutton(text = "Do you want to subscribe?", variable = subscriptionValue)
Subscription.grid(row=5, column=3)

#creating & packing a button
Button(text = "Submit", command= Values).grid(row=6, column=3)
root.mainloop()