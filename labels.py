from tkinter import *
root = Tk()
root.geometry("500x400")
root.title("Labels and Attributes")

#label operations
# text = adds texts
# bd = background
# fg = foreground
# font = sets the font of text
# 1. font=("Aesthetic",19, "bold")
# 2. font="Aesthetic 19 bold"
# padx = x padding or x co-ordinate
# pady = y padding or y co-ordinate
# relief = styling of border which are SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text = "Ready", 
    bg="cyan", fg="black", padx=23, pady=10, font="Aesthetic 19", borderwidth=10, relief=SUNKEN)
#title_label.pack()

#pack operations
#anchor = nw,ne,se,sw
#side = top, bottom,left,right
#by default side id top. For anchor "se" or "sw", specify the side as bottom
#title_label.pack(anchor="ne") #for ne and nw
#title_label.pack(side=BOTTOM, anchor="se")   #for se and sw
#fill = streches the box as per the specified co-ordinate
title_label.pack(side=BOTTOM, anchor="se", fill=X)
#title_label.pack(side=LEFT, fill=Y)
root.mainloop()