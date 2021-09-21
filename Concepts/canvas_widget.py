# canvas widgets

from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
canvas_widget = Canvas(root, width= canvas_width, height = canvas_height)
canvas_widget.pack()

# line (x1,y1) to (x2,y2)
canvas_widget.create_line(0 , 0, 800, 400, fill="red")
canvas_widget.create_line(0 , 400, 800, 0)

# rectangle --> coordinates: (top left(s), bottom right(s))
canvas_widget.create_rectangle(3,5,700,300, fill="red")

# text --> (coordinates, text)
canvas_widget.create_text(200,200, text="Hello World")

# oval inside rectangle(select option)
canvas_widget.create_oval(344,233,244,355)
root.mainloop()