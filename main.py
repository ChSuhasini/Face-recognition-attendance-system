from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from developer import Developer
from help import Help
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer


class Face_Recognition_System:
   def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        #first image
        img=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\img2.jpg.png")
        img=img.resize((400,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=100)
        #second image
        img1=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\firstimage.jpg")
        img1=img1.resize((500,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=500,height=100)
        #third image
        img2=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\img1.jpg.jpg")
        img2=img2.resize((500,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=500,height=100)

       #bg image
        img3=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\bg2.jpeg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        #student button
        img4=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\studentt.jpg")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="student details",command=self.student_details,cursor="hand2",font=("times new roman",10,"bold"),bg="green",fg="white")
        b1_1.place(x=100,y=250,width=150,height=40)

        #detect face button
        img5=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\facedetectt.jpg")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=300,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="face detector",command=self.face_data,cursor="hand2",font=("times new roman",10,"bold"),bg="green",fg="white")
        b1_1.place(x=300,y=250,width=150,height=40)


        #attendance
        img6=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\attendancee.jpg")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=500,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="face attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",10,"bold"),bg="green",fg="white")
        b1_1.place(x=500,y=250,width=150,height=40)

    

        #help desk
        img7=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\help desk.jpg")
        img7=img7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=700,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="help desk",cursor="hand2",command=self.help_data,font=("times new roman",10,"bold"),bg="green",fg="white")
        b1_1.place(x=700,y=250,width=150,height=40)


        #train data
        img8=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\train data.jpg")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=900,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="train data",cursor="hand2",command=self.train_data,font=("times new roman",10,"bold"),bg="green",fg="white")
        b1_1.place(x=900,y=250,width=150,height=40)  

        #photos
       # img9=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\photos.jpg")
       # img9=img9.resize((150,150),Image.ANTIALIAS)
        #self.photoimg9=ImageTk.PhotoImage(img9)

        #b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        #b1.place(x=1100,y=100,width=150,height=150)

        #b1_1=Button(bg_img,text="photos",cursor="hand2",font=("times new roman",10,"bold"),bg="green",fg="white")
        #b1_1.place(x=1100,y=250,width=150,height=40)    

        #developer
        img10=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\developerr.jpeg")
        img10=img10.resize((150,150),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=200,y=300,width=150,height=150)

        b1_1=Button(bg_img,text="developer",cursor="hand2",command=self.developer_data,font=("times new roman",10,"bold"),bg="green",fg="white")
        b1_1.place(x=200,y=450,width=150,height=40)    

       #exit
        img11=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\exit.jpeg")
        img11=img11.resize((150,150),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=400,y=300,width=150,height=150)

        b1_1=Button(bg_img,text="exit",cursor="hand2",command=self.iExit,font=("times new roman",10,"bold"),bg="green",fg="white")
        b1_1.place(x=400,y=450,width=150,height=40)  

   def iExit(self):
      self.iExit=messagebox.askyesno('Face Recognition','Are you sure exit this project',parent=self.root)
      if self.iExit >0:
              self.root.destroy()
      else:
               return



#============function buttons=======================================

   def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

   def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)

   def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)

   def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)

   def developer_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Developer(self.new_window)

   def help_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Help(self.new_window)
         
         
   






if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


