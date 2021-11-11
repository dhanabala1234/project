from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
from student import Student
class Face_Recognition:
      def __init__(self,root):
            self.root=root
            self.root.geometry("1530x790")
           
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

            Label(bg_img,text="FACIAL RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="black",fg="red").place(x=-50,y=0,width=1500,height=45)

            img5=Image.open("C:/Users/Administrator/Desktop/college_images/smart-attendance.jpg")
            img5=img5.resize((220,220))
            self.photoimg5=ImageTk.PhotoImage(img5)

            b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.student_details)
            b1.place(x=110,y=50,width=220,height=220)

            b2=Button(bg_img,text="Student Details",font=("times new roman",15,"bold"),command=self.student_details,bg="black",fg="white",cursor="hand2")
            b2.place(x=110,y=240, width=220, height=30)

            
            img6=Image.open("C:/Users/Administrator/Desktop/college_images/face_detector1.jpg")
            img6=img6.resize((220,220))
            self.photoimg6=ImageTk.PhotoImage(img6)

            b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
            b3.place(x=410,y=50,width=220,height=220)
             
            
            b4=Button(bg_img,text="Face Detector",font=("times new roman",15,"bold"),bg="black",fg="white",cursor="hand2")
            b4.place(x=410,y=240, width=220, height=30)
            
            img8=Image.open("C:/Users/Administrator/Desktop/college_images/student.jpeg")
            img8=img8.resize((220,220))
            self.photoimg8=ImageTk.PhotoImage(img8)

            b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
            b5.place(x=710,y=50,width=220,height=220)

            
            b6=Button(bg_img,text="Attendance",font=("times new roman",15,"bold"),bg="black",fg="white",cursor="hand2")
            b6.place(x=710,y=240, width=220, height=30)

            img7=Image.open("C:/Users/Administrator/Desktop/college_images/help.jpg")
            img7=img7.resize((220,220))
            self.photoimg7=ImageTk.PhotoImage(img7)

            b7=Button(bg_img,image=self.photoimg7,cursor="hand2")
            b7.place(x=990,y=50,width=220,height=220)

            
            b8=Button(bg_img,text="Help Desk",font=("times new roman",15,"bold"),bg="black",fg="white",cursor="hand2")
            b8.place(x=990,y=240, width=220, height=30)

            img9=Image.open("C:/Users/Administrator/Desktop/college_images/Train.jpg")
            img9=img9.resize((220,220))
            self.photoimg9=ImageTk.PhotoImage(img9)

            b9=Button(bg_img,image=self.photoimg9,cursor="hand2")
            b9.place(x=110,y=320,width=220,height=220)

            b10=Button(bg_img,text="Train Faces",font=("times new roman",15,"bold"),bg="black",fg="white",cursor="hand2")
            b10.place(x=110,y=510, width=220, height=30)

            
            img10=Image.open("C:/Users/Administrator/Desktop/college_images/teaser.png")
            img10=img10.resize((220,220))
            self.photoimg10=ImageTk.PhotoImage(img10)

            b11=Button(bg_img,image=self.photoimg10,cursor="hand2")
            b11.place(x=410,y=320,width=220,height=220)
             
            
            b12=Button(bg_img,text="Photos",font=("times new roman",15,"bold"),bg="black",fg="white",cursor="hand2")
            b12.place(x=410,y=510, width=220, height=30)
            
            img11=Image.open("C:/Users/Administrator/Desktop/college_images/attendance.jpg")
            img11=img11.resize((220,220))
            self.photoimg11=ImageTk.PhotoImage(img11)

            b13=Button(bg_img,image=self.photoimg11,cursor="hand2")
            b13.place(x=710,y=320,width=220,height=220)

            
            b14=Button(bg_img,text="Developer",font=("times new roman",15,"bold"),bg="black",fg="white",cursor="hand2")
            b14.place(x=710,y=510, width=220, height=30)

            img12=Image.open("C:/Users/Administrator/Desktop/college_images/exit.jpg")
            img12=img12.resize((220,220))
            self.photoimg12=ImageTk.PhotoImage(img12)

            b15=Button(bg_img,image=self.photoimg12,cursor="hand2")
            b15.place(x=990,y=320,width=220,height=220)

            
            b16=Button(bg_img,text="Exit",font=("times new roman",15,"bold"),bg="black",fg="white",cursor="hand2")
            b16.place(x=990,y=510, width=220, height=30)
      def student_details(self):
            self.new_window=Toplevel()
            self.app=Student(self.new_window)
     
if __name__== "__main__":
      root=Tk()
      obj=Face_Recognition(root)
      obj.root.mainloop()

      