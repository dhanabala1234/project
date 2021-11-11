from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import mysql.connector
from PIL import Image,ImageTk


class Student:
      def __init__(self,root):
            self.root=root
            self.root.geometry("1530x790")
            self.root.title("Student Management System")

            self.name1=StringVar()
            self.roll1=StringVar()
            self.dep1=StringVar()
            self.gender1=StringVar()
            self.year1=StringVar()
            im=Image.open("C:/Users/Administrator/Desktop/college_images/dev.jpg")
            im=im.resize((500,130))
            self.photoimg1=ImageTk.PhotoImage(im)
            Label(self.root,image=self.photoimg1).place(x=0,y=0,width=500,height=130)

            im1=Image.open("C:/Users/Administrator/Desktop/college_images/facialrecognition.png")
            im1=im1.resize((400,130))
            self.photoimg2=ImageTk.PhotoImage(im1)
            Label(self.root,image=self.photoimg2).place(x=500,y=0,width=400,height=130)

            im2=Image.open("C:/Users/Administrator/Desktop/college_images/news.jpg")
            im2=im2.resize((600,130))
            self.photoimg3=ImageTk.PhotoImage(im2)
            Label(self.root,image=self.photoimg3).place(x=900,y=0,width=600,height=130)

           
            bg=Image.open("C:/Users/Administrator/Desktop/college_images/bg45.jpg")
            bg=bg.resize((1530,790))
            self.photoimg4=ImageTk.PhotoImage(bg)
            bg_img=Label(self.root,image=self.photoimg4)
            bg_img.place(x=0,y=130,width=1530,height=790)

            Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="red").place(x=-50,y=0,width=1500,height=45)
            main_frame=Frame(bg_img)
            main_frame.place(x=0,y=50,width=1450,height=600)
            #left_frame
            left_frame=LabelFrame(main_frame,text="Student Details",bg="white",font=("times new roman",15,"bold"))
            left_frame.place(x=10,y=10,width=675,height=500)

            
            im_left=Image.open("C:/Users/Administrator/Desktop/college_images/facialrecognition.png")
            im_left=im_left.resize((675,175))
            self.photoimg_left=ImageTk.PhotoImage(im_left)
            my_label= Label(main_frame,image=self.photoimg_left)
            my_label.place(x=15,y=30,width=675,height=110)

            course_frame=LabelFrame(left_frame,text="Course Details",bg="white",font=("times new roman",15,"bold"))
            course_frame.place(x=0,y=110,width=675,height=120)

            dep_label=Label(course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
            dep_label.grid(column=0,row=0,padx=10)
           
           
                   


            optionsimp=ttk.Combobox(course_frame,values=["Select Course","BE","ME"],state="readonly",font=("times new roman",12,"bold"))
            optionsimp.current(0) 
            optionsimp.grid(column=1,row=0,padx=5,pady=10)
           


            dep_label=Label(course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
            dep_label.grid(column=2,row=0,padx=10)

            options=ttk.Combobox(course_frame,textvariable=self.dep1,  values=["Select Department","ECE","CSE","MECH","EEE"],state="readonly",font=("times new roman",12,"bold"))
            options.current(0)
            options.grid(column=3,row=0,padx=5,pady=10)

            dep_label=Label(course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
            dep_label.grid(column=0,row=1,padx=10)
            
            options2=ttk.Combobox(course_frame,state="readonly",font=("times new roman",12,"bold"))
         
            options2.grid(column=1,row=1,padx=5,pady=10)

            dep_label=Label(course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
            dep_label.grid(column=2,row=1,padx=10)

            options=ttk.Combobox(course_frame,values=["Select Department","ECE","CSE","MECH","EEE"],state="readonly",font=("times new roman",12,"bold"))
            options.current(0)
            options.grid(column=3,row=1,padx=5,pady=10)

            
            student_frame=LabelFrame(main_frame,text="Students' Information",bg="white",font=("times new roman",15,"bold"))
            student_frame.place(x=10,y=270,width=675,height=240)

            details_label=Label(student_frame,text="Student's Name",font=("times new roman",12,"bold"),bg="white")
            details_label.grid(column=0,row=0,padx=10,pady=10)

            e1=Entry(student_frame,textvariable=self.name1, width=30)
            e1.grid(row=0, column=1)

            details_label=Label(student_frame,text="Roll No",font=("times new roman",12,"bold"),bg="white")
            details_label.grid(column=2,row=0,padx=10,pady=10)

            e1=Entry(student_frame,textvariable=self.roll1,  width=30)
            e1.grid(row=0, column=3)

            details_label=Label(student_frame,text="Phone No",font=("times new roman",12,"bold"),bg="white")
            details_label.grid(column=0,row=1,padx=10,pady=10)

            e1=Entry(student_frame,width=30)
            e1.grid(row=1, column=1)

            details_label=Label(student_frame,text="Email Id",font=("times new roman",12,"bold"),bg="white")
            details_label.grid(column=2,row=1,padx=10,pady=10)

            e1=Entry(student_frame,width=30)
            e1.grid(row=1, column=3)

            
            details_label=Label(student_frame,text="Age",font=("times new roman",12,"bold"),bg="white")
            details_label.grid(column=0,row=2,padx=10,pady=10)

            e1=Entry(student_frame,width=30)
            e1.grid(row=2, column=1)

            details_label=Label(student_frame,text="Date of Birth",font=("times new roman",12,"bold"),bg="white")
            details_label.grid(column=2,row=2,padx=10,pady=10)

            e1=Entry(student_frame,width=30)
            e1.grid(row=2, column=3)

            btns_frame=Frame(student_frame)
            btns_frame.place(x=0,y=140,width=675,height=70)

            btn1=Button(btns_frame,width=13,font=("times new roman",15,"bold"),text="SAVE",cursor="hand2",command=self.add_data,bg="blue",fg="white")
            btn1.grid(row=0, column=0)
            btn1=Button(btns_frame,width=13,font=("times new roman",15,"bold"),command=self.update_data,text="UPDATE",bg="blue",fg="white")
            btn1.grid(row=0, column=1)
            btn1=Button(btns_frame,width=13,font=("times new roman",15,"bold"),command=self.delete_data,text="DELETE",bg="blue",fg="white")
            btn1.grid(row=0, column=2)
            btn1=Button(btns_frame,width=14,font=("times new roman",15,"bold"),text="RESET",command=self.reset_data,bg="blue",fg="white")
            btn1.grid(row=0, column=3)
            btns_frame1=Frame(student_frame)
            btns_frame1.place(x=0,y=180,width=675,height=30)

            btn1=Button(btns_frame1,width=27,font=("times new roman",15,"bold"),text="TAKE PHOTO SAMPLE",bg="blue",fg="white")
            btn1.grid(row=0, column=0)
            btn1=Button(btns_frame1,width=28,font=("times new roman",15,"bold"),text="UPDATE PHOTO SAMPLE",bg="blue",fg="white")
            btn1.grid(row=0, column=1)
         
            #right_frame
            right_frame=LabelFrame(main_frame,text="Student Details",bg="white",font=("times new roman",15,"bold"))
            right_frame.place(x=685,y=10,width=725,height=500)

            im_right=Image.open("C:/Users/Administrator/Desktop/college_images/di.jpg")
            im_right=im_right.resize((675,175))
            self.photoimg_right=ImageTk.PhotoImage(im_right)
            my_label= Label(main_frame,image=self.photoimg_right)
            my_label.place(x=690,y=30,width=675,height=110)

            student_rframe=LabelFrame(main_frame,text="Students' Information",bg="white",font=("times new roman",15,"bold"))
            student_rframe.place(x=690,y=140,width=675,height=360)

            scroll_x=ttk.Scrollbar(student_rframe,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(student_rframe,orient=VERTICAL)

            self.student_table=ttk.Treeview(student_rframe,column=("Name","Dept","Roll No","Gender", "Year"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)

            scroll_x.config(command=self.student_table.xview)
            scroll_y.config(command=self.student_table.yview)

            self.student_table.heading("Name",text="Student's Name")
            self.student_table.heading("Dept",text="Department")
            self.student_table.heading("Roll No",text="Roll Number")
            self.student_table.heading("Gender",text="Gender")
            self.student_table.heading("Year",text="Year")


            self.student_table.column("Name",width=17)
            self.student_table.column("Dept",width=17)
            self.student_table.column("Roll No",width=17)
            self.student_table.column("Gender",width=17)
            self.student_table.column("Year",width=17)
            self.student_table["show"]="headings"
            self.student_table.pack(fill=BOTH, expand=1)
            self.show_data()
            self.student_table.bind("<ButtonRelease>",self.get_cursor)

      def add_data(self):
            if self.dep1.get()=="Select Department" or self.name1.get()=="" or self.roll1.get()=="":
                  messagebox.showerror("Error","Please fill all the fields",parent=self.root)
            else:
                 conn=mysql.connector.connect(host="localhost",
                 username="root", password="",database="Dhana"
                 )
                 mycursor=conn.cursor()
                 mycursor.execute("INSERT INTO `studentinfo` VALUES(%s,%s,%s,%s)",(self.name1.get(),self.dep1.get(),self.year1.get(),self.roll1.get() ))
                 conn.commit()
                 conn.close()
                 messagebox.showinfo("success","Okay",parent=self.root)
                 self.show_data()

      def show_data(self):
                 conn=mysql.connector.connect(host="localhost",
                 username="root", password="",database="Dhana"
                 )
                 mycursor=conn.cursor()
                 mycursor.execute("SELECT * FROM STUDENTINFO")
                 data=mycursor.fetchall()
                 if(len(data)!=0):
                       self.student_table.delete(*self.student_table.get_children())
                       for i in data:
                             self.student_table.insert("",END,values=i)
                       conn.commit()
                 conn.close()
      def get_cursor(self, event=""):   
            selected=self.student_table.focus()  
            values=self.student_table.item(selected,'values')
            self.name1.set(values[0])
            self.dep1.set(values[1])
            self.year1.set(values[2])
            self.roll1.set(values[3])
      def update_data(self):
            if self.dep1.get()=="Select Department" or self.name1.get()=="" or self.roll1.get()=="":
                   messagebox.showerror("Error","Please fill all the fields",parent=self.root)
            else:
                 conn=mysql.connector.connect(host="localhost",
                 username="root", password="",database="Dhana"
                 )
                 mycursor=conn.cursor()
                 mycursor.execute("UPDATE STUDENTINFO SET NAME=%s,DEPT=%s,YEAR=%s,ROLLNO=%s WHERE NAME=%s",(self.name1.get(),self.dep1.get(),self.year1.get(),self.roll1.get(),self.name1.get() ))
                 conn.commit()
                 conn.close()
                 messagebox.showinfo("success","Update Success",parent=self.root)
                 self.show_data()
      def delete_data(self):
            if self.dep1.get()=="Select Department" and self.name1.get()==""and self.roll1.get()=="":
                  messagebox.showerror("Error","Please fill any one of the fields",parent=self.root)
            else:
                  delete=messagebox.askyesno("Deletion","Do you want to delete",parent=self.root)
                  if delete>0:
                        conn=mysql.connector.connect(host="localhost",
                        username="root", password="",database="Dhana"
                        )
                        mycursor=conn.cursor()
                        mycursor.execute("DELETE FROM STUDENTINFO WHERE NAME=%s",(self.name1.get(),))
                        conn.commit()
                        self.show_data()
                        conn.close ()
                  else:
                        if not delete:
                              return
      def reset_data(self):
            self.name1.set("")      
            self.dep1.set("")
            self.year1.set("")
            self.roll1.set("")
      def generate_data(self):
            

if __name__== "__main__":
      root=Tk()
      obj=Student(root)
      obj.root.mainloop()