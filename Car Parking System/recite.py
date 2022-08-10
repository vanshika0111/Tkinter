from tkinter import *
from datetime import datetime
import pywhatkit
from s4 import pno

root=Tk()

root.title("Bill")
root.geometry("900x700")
root.config(bg='light blue')

def wp():
    mob_no = "+91 " + pno"
    current_time = datetime.now()
    time_hr = int(current_time.strftime("%H"))
    time_min = int(current_time.strftime("%M")) + 2
    
    pywhatkit.sendwhatmsg(mob_no, "Your slot is booked!", time_hr, time_min, 30, True, 10)

btn1=Button(text="Bill",font=("times new roman",15,"bold"),bg="gray",fg="white",cursor="hand2",command=wp)
btn1.place(x=350,y=200)

root.mainloop()