from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        #   first IMAGE
        img = Image.open(r"Images\Images16.jpg")
        img = img.resize((513, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=513, height=130)

        #   second Image
        img1 = Image.open( r"Images\Images17.jpg")
        img1 = img1.resize((513, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=513, y=0, width=513, height=130)

        # third Image
        img2 = Image.open(r"Images\Images18.jpeg")
        img2 = img2.resize((513, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1026, y=0, width=513, height=130)

        # bg image
        img3 = Image.open(r"Images\Images1.jpg")
        img3 = img3.resize((1540, 790), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, relwidth=1, relheight=1)

        title_lbl = Label(bg_img, text="FACE Recognition Based ATTENDANCE SYSTEM", font=("times new roman", 25, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1540, height=45)

        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',18,'bold'),background='black',foreground='red')
        lbl.place(x=0,y=0,width=150,height=50)
        time()

        # student button
        img4 = Image.open(r"Images\Images8.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=186, y=100, width=150, height=150)

        b2 = Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b2.place(x=186, y=250, width=150, height=20)

        # Detect Face button
        img5 = Image.open(r"Images\Images9.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b1.place(x=522, y=100, width=150, height=150)

        b2 = Button(bg_img, text="Face Detector", cursor="hand2",  command=self.face_data, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b2.place(x=522, y=250, width=150, height=20)

        # Attendance button
        img6 = Image.open(r"Images\Images10.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b1.place(x=858, y=100, width=150, height=150)

        b2 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b2.place(x=858, y=250, width=150, height=20)

        # Help Desk button
        img7 = Image.open( r"Images\Images11.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.help_data)
        b1.place(x=1194, y=100, width=150, height=150)

        b2 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.help_data, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b2.place(x=1194, y=250, width=150, height=20)

        # Train face button
        img8 = Image.open(r"Images\Images12.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b1.place(x=186, y=375, width=150, height=150)

        b2 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b2.place(x=186, y=525, width=150, height=20)

        # Captures
        img9 = Image.open(r"Images\Images13.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=522, y=375, width=150, height=150)

        b2 = Button(bg_img, text="Captures", cursor="hand2", command=self.open_img,font=("times new roman", 15, "bold"), bg="black", fg="white")
        b2.place(x=522, y=525, width=150, height=20)

        # Developer button
        img10 = Image.open(r"Images\Images14.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_data)
        b1.place(x=858, y=375, width=150, height=150)

        b2 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b2.place(x=858, y=525, width=150, height=20)

        # Exit face button
        img11 = Image.open(r"Images\Images15.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b1.place(x=1194, y=375, width=150, height=150)

        b2 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b2.place(x=1194, y=525, width=150, height=20)



        #Functions Buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def open_img(self):
        os.startfile("Data")

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit?", parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

        


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
