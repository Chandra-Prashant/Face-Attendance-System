from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 25, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1550, height=45)

        img_top = Image.open(r"Images\Images1.jpg")
        img_top = img_top.resize((1550, 790), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55,relwidth=1, relheight=1)

        dev_label = Label(f_lbl, text="Email:pc079105@gmail.com",font=("times new roman", 30, "bold"), fg="skyblue", bg="white")
        dev_label.place(x=500,y=365)






if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()