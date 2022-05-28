from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",15,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\white.jpg")
        img_top=img_top.resize((1530,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=700)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=0,y=0,width=1530,height=800)

        img_top1=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\student1.jpeg")
        img_top1=img_top1.resize((250,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=500,y=70,width=550,height=200)

        dev_lbl=Label(main_frame,text="Details:",font=("times new roman",20,"bold"),bg="violet",fg="white")
        dev_lbl.place(x=700,y=275)

        dev_lbl=Label(main_frame,text="Hi,I am Suhasini",font=("times new roman",20,"bold"),bg="violet",fg="white")
        dev_lbl.place(x=700,y=315)

        dev_lbl=Label(main_frame,text="I am pursuing B.TECH,ECE in",font=("times new roman",20,"bold"),bg="violet",fg="white")
        dev_lbl.place(x=700,y=355)

        dev_lbl=Label(main_frame,text="BVRIT,Telangana",font=("times new roman",20,"bold"),bg="violet",fg="white")
        dev_lbl.place(x=700,y=395)

        img_top2=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\suhasini.jpg")
        img_top2=img_top2.resize((450,400),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(self.root,image=self.photoimg_top2)
        f_lbl.place(x=400,y=280,width=250,height=300)

        












if __name__ == '__main__':
   root=Tk()
   obj=Developer(root)
   root.mainloop()
