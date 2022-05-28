from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        #=============================================variables=============================================================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
    

       #first image
        img=Image.open(r"college_images\student1.jpeg")
        img=img.resize((700,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=700,height=100)
        #second image
        img1=Image.open(r"college_images\student2.jpeg")
        img1=img1.resize((600,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=700,y=0,width=600,height=100)
#bg image
        img3=Image.open(r"college_images\bg2.jpeg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",15,"bold"),bg="green",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=35,width=1480,height=600)

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=530)

        img_left=Image.open(r"C:\Users\Sony\Desktop\face recognition system\college_images\student1.jpeg")
        img_left=img_left.resize((500,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
       

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=600,height=100)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=105,width=650,height=300)
        #LABEL ENTRY
        #ATTENDANCE ID

        attendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

    #student name
        roll_label=Label(left_inside_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

    #time
        time_label=Label(left_inside_frame,text="time:",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
    

#name
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

    #date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

         # attendance status
        att_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",13,"bold"),bg="white")
        att_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        att_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",13,"bold"))
        att_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        self.att_combo=ttk.Combobox(left_inside_frame,font=("times new roman",13,"bold"),state='readonly',width=20)
        self.att_combo["values"]=('status','present','absent')
        self.att_combo.current(0)
        self.att_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text='Import csv',command=self.importCsv,width=15,font=('times new roman',13,'bold'),bg='blue',fg='white')
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text='Export csv',command=self.exportCsv,width=15,font=('times new roman',13,'bold'),bg='blue',fg='white')
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text='Update',width=15,font=('times new roman',13,'bold'),bg='blue',fg='white')
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text='reset',command=self.reset_data,width=15,font=('times new roman',13,'bold'),bg='blue',fg='white')
        reset_btn.grid(row=0,column=3)


        







#right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Attendance details",font=("times new roman",12,"bold"))
        right_frame.place(x=670,y=10,width=590,height=530)


        table_frame=Frame(right_frame,bd=2,bg='white',relief=RIDGE)
        table_frame.place(x=5,y=5,width=575,height=455)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=('id','roll','name','department','time','date','attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading('id',text='Attendance ID')
        self.AttendanceReportTable.heading('roll',text='Roll')
        self.AttendanceReportTable.heading('name',text='Name')
        self.AttendanceReportTable.heading('department',text='Department')
        self.AttendanceReportTable.heading('time',text='time')
        self.AttendanceReportTable.heading('date',text='Date')
        self.AttendanceReportTable.heading('attendance',text='attendance')
        self.AttendanceReportTable['show']='headings'



        self.AttendanceReportTable.column('id',width=100)
        self.AttendanceReportTable.column('roll',width=100)
        self.AttendanceReportTable.column('name',width=100)
        self.AttendanceReportTable.column('department',width=100)
        self.AttendanceReportTable.column('time',width=100)
        self.AttendanceReportTable.column('date',width=100)
        self.AttendanceReportTable.column('attendance',width=100)
        

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind('<ButtonRelease>',self.get_cursor)

        #=====================================================fetch data=================================================================

    def fetchData(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert('',END,values=i)

    def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title='open CSV',filetypes=(('CSV File','*.csv'),('ALl File','*.*')),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=',')
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror('No Data','No Data found to export',parent=self.root)
                return False
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title='open CSV',filetypes=(('CSV File','*.csv'),('ALl File','*.*')),parent=self.root)
            with open(fln,mode='w',newline='') as myfile:
              exp_write=csv.writer(myfile,delimiter=',')
              for i in mydata:
                exp_write.writerow(i)
              messagebox.showinfo('Data Export','Your data exported to'+os.path.basename(fln)+'successfully')
        except Exception as es:
          messagebox.showerror('error',f'Due To:{str(es)}',parent=self.root)

    def get_cursor(self,event=''):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        self.var_atten_id.set(rows[7])


    def reset_data(self):
        self.var_atten_id.set('')
        self.var_atten_roll.set('')
        self.var_atten_name.set('')
        self.var_atten_dep.set('')
        self.var_atten_time.set('')
        self.var_atten_date.set('')
        self.var_atten_attendance.set('')
        self.var_atten_id.set('')





    
        




        
            


        
            




if __name__ == '__main__':
   root=Tk()
   obj=Attendance(root)
   root.mainloop()
