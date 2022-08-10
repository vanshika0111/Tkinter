import tkinter
from tkinter import *
import customtkinter
from tkhtmlview import HTMLLabel
from PIL import ImageTk, Image

r = customtkinter.CTk()
r.title("Car Parking System")
r.geometry("900x700")

customtkinter.set_appearance_mode("dark")

def available():
    r.destroy()
    choice = clicked.get()
    if choice == "Block 1":
        import offs4_1

    elif choice == "Block 2":
        import offs4_2



options = ["Block 1", "Block 2"]
fnt = ('Helvetica',25)

clicked = StringVar()
clicked.set("Enter location")
drop = customtkinter.CTkOptionMenu(master=r, variable=clicked, values=options, text_font=fnt)
drop.pack(pady=100)


img = ImageTk.PhotoImage(Image.open("WhatsApp Image 2022-08-05 at 6.36.51 PM.jpeg").resize((50, 20), Image.Resampling.LANCZOS))

button = customtkinter.CTkButton(r, image=img, text="See available parking slots", command=available, width=190,
                                height=40)
button.pack(pady=150)

r.mainloop()