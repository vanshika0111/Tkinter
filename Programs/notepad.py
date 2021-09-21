# notepad

from posixpath import basename
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfilename
import os

# definitions
def newFile():
    global file
    root.title("Untitled-Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", 
                           filetypes= [("All Files", "*.*"),
                                       ("Text Documents", "*.txt"),])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile= 'Untitled.txt', defaultextension=".txt", 
                                                              filetypes= [("All Files", "*.*"),
                                                                          ("Text Documents", "*.txt"),])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "- Notepad")
            # print("File saved!")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def exitFile():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("About us", "Notepad by Vanshika")

# main function
if __name__ == '__main__':
    root = Tk()
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("1.png")
    root.geometry("644x788")

    # text area
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # to create menubar
    menuBar = Menu(root)

    # ------------ file menu ---------
    FileMenu = Menu(menuBar, tearoff=0)
    # to create new file, open an existing file, save file, SEPARATOR, exit file optoins
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=exitFile)

    # to attach menu bar to file menu
    menuBar.add_cascade(label="File", menu=FileMenu)

    # --------- edit menu -----------
    EditMenu = Menu(menuBar, tearoff=0)
    # cut, copy & paste options
    EditMenu.add_command(label = "Cut", command= cut)
    EditMenu.add_command(label = "Copy", command= copy)
    EditMenu.add_command(label = "Paste", command= paste)
    menuBar.add_cascade(label="Edit", menu= EditMenu)

    # --------- help menu -----------
    HelpMenu = Menu(menuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    menuBar.add_cascade(label="Help", menu=HelpMenu)

    # scroll-bar
    scrollbar = Scrollbar(TextArea)
    scrollbar.pack(side=RIGHT, fill=Y)
    # TextArea.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=TextArea.yview)
    
    # to configure menu bar
    root.config(menu=menuBar)

    root.mainloop()