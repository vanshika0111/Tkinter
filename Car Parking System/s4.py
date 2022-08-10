from logging import exception
import sqlite3
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pywhatkit
from datetime import datetime
import pyautogui
import keyboard as k

global pno
class form:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1000x500+220+130")
        self.root.title("Booking Form")
        self.root.config(bg="lightblue")
        self.root.focus_force()

        #====variables==
        self.var_name=StringVar()
        self.var_v_no=StringVar()
        self.var_p_no=StringVar()
        self.var_t_f=StringVar()
        self.var_t_t=StringVar()

        #====Frame====
        # formframe=LabelFrame(self.root,text="Booking",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        # formframe.place(x=30,y=10,height=450,width=950)

        name=Label(text="Name",font=("times new roman",15,"bold"),bg="lightblue",fg="black")
        name.place(x=60,y=50)
        txt_name=Entry(textvariable=self.var_name,font=("times new roman",15,"bold"),bg="lightgray")
        txt_name.place(x=200,y=50)

        v_no=Label(text="Vehicle No.",font=("times new roman",15,"bold"),bg="lightblue",fg="black")
        v_no.place(x=60,y=100)
        txt_v_no=Entry(textvariable=self.var_v_no,font=("times new roman",15,"bold"),bg="lightgray")
        txt_v_no.place(x=200,y=100)

        p_no=Label(text="Phone No.",font=("times new roman",15,"bold"),bg="lightblue",fg="black")
        p_no.place(x=60,y=150)
        txt_p_no=Entry(textvariable=self.var_p_no,font=("times new roman",15,"bold"),bg="lightgray")
        txt_p_no.place(x=200,y=150)
        global pno
        pno=txt_p_no


        TF=Label(text="Time(From)",font=("times new roman",15,"bold"),bg="lightblue",fg="black")
        TF.place(x=480,y=50)
        txt_TF=Entry(textvariable=self.var_t_f,font=("times new roman",15,"bold"),bg="lightgray")
        txt_TF.place(x=620,y=50)

        TT=Label(text="Time(To)",font=("times new roman",15,"bold"),bg="lightblue",fg="black")
        TT.place(x=480,y=100)
        txt_TT=Entry(textvariable=self.var_t_t,font=("times new roman",15,"bold"),bg="lightgray")
        txt_TT.place(x=620,y=100)

        btn1=Button(text="Submit",command=self.sub,font=("times new roman",15,"bold"),bg="gray",fg="white",cursor="hand2")
        btn1.place(x=350,y=200)

        btn2=Button(text="Reset",command=self.reset,font=("times new roman",15,"bold"),bg="gray",fg="white",cursor="hand2")
        btn2.place(x=520,y=200)

        #===details====
        frame=Frame(self.root,bd=3,relief=RIDGE)
        frame.place(x=0,y=300,relwidth=1,height=200)

        scrolly=Scrollbar(frame,orient=VERTICAL)
        scrollx=Scrollbar(frame,orient=HORIZONTAL)

        self.table=ttk.Treeview(frame,columns=("name","v_no","p_no","t_f","t_t"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.table.xview)
        scrolly.config(command=self.table.yview)

        self.table.heading("name",text="Name")
        self.table.heading("v_no",text="Vehicle Number")
        self.table.heading("p_no",text="Phone Number")
        self.table.heading("t_f",text="Time(From)")
        self.table.heading("t_t",text="Time(to)")

        self.table["show"]="headings"

        self.table.column("name",width=100)
        self.table.column("v_no",width=100)
        self.table.column("p_no",width=100)
        self.table.column("t_f",width=100)
        self.table.column("t_t",width=100)
        self.table.pack(fill=BOTH,expand=1)
        self.table.bind("<ButtonRelease-1>")
        self.show()
        

#===========================================================
    def sub(self):
        con=sqlite3.connect(database=r"data.db")
        cur=con.cursor()
        try:
            if self.var_v_no.get()=="" and self.var_p_no.get()=="":
                messagebox.showerror("Error","Vehicle number is required",parent=self.root)
            
            else:
                cur.execute("Select * from form where v_no=?",(self.var_v_no.get(),))
                cur.execute("Insert into form(name,v_no,p_no,t_f,t_t) values(?,?,?,?,?)",(
                                            self.var_name.get(),
                                            self.var_v_no.get(),
                                            self.var_p_no.get(),
                                            self.var_t_f.get(),
                                            self.var_t_t.get(),
                ))
                con.commit()
                messagebox.showinfo("Success","Details Added Sucessfully",parent=self.root)
                self.show()
                self.reset()
                import whatsapp
                whatsapp.my_time()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r"data.db")
        cur=con.cursor()
        try:
                cur.execute("Select * from form ")
                rows=cur.fetchall()
                self.table.delete(*self.table.get_children())
                for row in rows:
                    self.table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)
            

    def reset(self):
        self.var_name.set("")
        self.var_v_no.set("")
        self.var_p_no.set("")
        self.var_t_f.set("")
        self.var_t_t.set("")
        
        self.show()

root=Tk()
obj=form(root)
root.mainloop()