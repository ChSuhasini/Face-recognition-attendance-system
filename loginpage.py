from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from developer import Developer
from help import Help
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from main import Face_Recognition_System



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("face recognition system")


        #self.bg=ImageTk.PhotoImage(file=r'C:\Users\Sony\Desktop\face recognition system\college_images\bg2.jpeg')
        #lbl_bg=Label(self.root,image=self.bg)
        #lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg='pink')
        frame.place(x=510,y=100,width=340,height=450)


        #img1=Image.open(r"C:\Users\Sony\Desktop\login\college_images\login1.jpg")
       # img1=img1.resize((1530,710),Image.ANTIALIAS)
        #self.photoimg1=ImageTk.PhotoImage(img1)
        #lblimg1=Label(self.root,image=self.photoimg1)
        #lblimg1.place(x=620,y=130,width=150,height=150)

        get_str=Label(frame,text='Login Page',font=('times new roman',30,'bold'),fg='white',bg='orange')
        get_str.place(x=70,y=30)

        username=lbl=Label(frame,text='User Name',font=('times new roman',20,'bold'),fg='white',bg='blue')
        username.place(x=0,y=110)

        self.txtuser=ttk.Entry(frame,font=('times new roman',20,'bold'))
        self.txtuser.place(x=0,y=170,width=240)

        password=lbl=Label(frame,text='Password',font=('times new roman',20,'bold'),fg='white',bg='blue')
        password.place(x=0,y=220)

        self.txtpass=ttk.Entry(frame,font=('times new roman',20,'bold'))
        self.txtpass.place(x=0,y=270,width=240)

        #login button
        loginbtn=Button(frame,text='login',command=self.login,font=('times new roman',20,'bold'),bd=3,relief=RIDGE,fg='white',bg='green',activeforeground='white',activebackground='red')
        loginbtn.place(x=90,y=330,width=170,height=40)

       # fpbtn=Button(frame,text='forget password',font=('times new roman',15,'bold'),bd=3,borderwidth=0,fg='white',bg='black',activeforeground='white',activebackground='red')
        #fpbtn.place(x=0,y=350,width=160)

       # nubtn=Button(frame,text='new user register',font=('times new roman',15,'bold'),bd=3,borderwidth=0,fg='white',bg='black',activeforeground='white',activebackground='red')
        #nubtn.place(x=0,y=400,width=160)
    def face(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition_System(self.new_window)
  
    def login(self):
             if self.txtuser.get()=='' or self.txtpass.get=='':
                 messagebox.showerror('Error','all field are required')
             elif self.txtuser.get()=='suhasini' or self.txtpass.get=='1234':
                 messagebox.showinfo('success','successful login')
                 command=self.face()
             else:
                messagebox.showerror('Error','Incorrect username or password')


            


       







        
          



if __name__ =="__main__":
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()
