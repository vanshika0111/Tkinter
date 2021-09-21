# scroll bar

from tkinter import *

root = Tk()
root.geometry("700x600")
root.title("Introducing scroll-bars")

"""
To connect scroll-bar with a widget
1. widget()
2. scrollbar.config(command = widget.yview)
"""
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listBox = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(300):
    listBox.insert(END, f"Item {i}")
listBox.pack(fill = "both", padx=22, pady=30)
scrollbar.config(command = listBox.yview)

text = Text(root, yscrollcommand = scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command = text.yview)

root.mainloop()
