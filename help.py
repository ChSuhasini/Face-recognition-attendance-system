from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")


        title_lbl=Label(self.root,text="help desk",font=("times new roman",15,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\develop.jpeg")
        img_top=img_top.resize((1530,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=700)

        dev_lbl=Label(f_lbl,text="Email:suhaisinichinni158@gmail.com",font=("times new roman",15,"bold"),bg="red",fg="white")
        dev_lbl.place(x=600,y=400)

       









if __name__ == '__main__':
   root=Tk()
   obj=Help(root)
   root.mainloop()