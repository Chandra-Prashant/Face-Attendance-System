from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from Test import Face_Recognition_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
        


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"Images\Images1.jpg")

        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="skyblue")
        frame.place(x=605,y=175,width=340,height=450)

        img1=Image.open(r"Images\Images2.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="skyblue",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="skyblue")
        get_str.place(x=100,y=100)

        #label
        username=lbl=Label(frame,text="UserName",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="PassWord",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #icon images

        img2=Image.open(r"Images\Images3.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimg2,bg="skyblue",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"Images\Images4.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimg3,bg="skyblue",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)

        #buttons
        #login
        loginbtn=Button(frame,text="Login",command=self.login,cursor="hand2",font=("times new roman",20,"bold"),borderwidth=0,fg="white",bg="red",activeforeground="skyblue",activebackground="green")
        loginbtn.place(x=110,y=300,width=120,height=35)
        #register
        registerbtn=Button(frame,text="New User Register",command=self.register_window,cursor="hand2",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="skyblue",activeforeground="white",activebackground="green")
        registerbtn.place(x=15,y=350,width=160)
        
        #forget
        forgotpassbtn=Button(frame,text="Forgot PassWord",command=self.forgot_password_window,cursor="hand2",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="skyblue",activeforeground="white",activebackground="green")
        forgotpassbtn.place(x=10,y=400,width=160)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields Required!!!",parent=self.root)
        elif self.txtuser.get()=="prashant" and self.txtpass.get()=="chandra":
            messagebox.showinfo("Success","Welcome to Face Rocognition System",parent=self.root)
            open_main=messagebox.askyesno("Yes/No","Access only admin",parent=self.root)
            if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition_System(self.new_window)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Umesh@123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                               self.txtuser.get(),
                                                                               self.txtpass.get()
                                                                                ))
            row=my_cursor.fetchone()
            #print(row)
            if row!=None:
                messagebox.showerror("Error","Invalid username or password",parent=self.root)
            else:
                open_main=messagebox.askyesno("Yes/No","Access only admin",parent=self.root)
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    #=======reset password =======
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter The New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Umesh@123",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter The Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.textuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showeinfo("Info","Your password has been reset,please login with new password",parent=self.root2)
                self.root2.destroy()



    #=========Forgot Password Window ==========#
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter The Email Address To Reset Password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Umesh@123",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter The Valid User Name ",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password ",font=("times new roman",20,"bold"),fg="white",bg="skyblue")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your GirlFriend Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
                security_A.place(x=50,y=150)

                self.txt_security_A=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security_A.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="skyblue",fg="white")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)











class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")
        
        #========Variable=======
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #bg image
        self.bg=ImageTk.PhotoImage(file=r"Images\Images1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #left image
        self.bg1=ImageTk.PhotoImage(file=r"Images\Images5.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        #main frame
        frame=Frame(self.root,bg="skyblue")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="white",bg="skyblue")
        register_lbl.place(x=20,y=20)

        #label and entry
        #row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
        fname.place(x=50,y=100)

        self.fname_enrty=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.fname_enrty.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        

        #row2
        contact=Label(frame,text="Contact Info",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email(remember it to use as UserName)",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #row3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your GirlFriend Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Select Security Answer",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
        security_A.place(x=370,y=240)

        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security_A.place(x=370,y=270,width=250)

        #row4
        pswd=Label(frame,text="PassWord",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm PassWord",font=("times new roman",15,"bold"),fg="white",bg="skyblue")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #checkbutton
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #======button=====
        img=Image.open(r"Images\Images6.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage= ImageTk.PhotoImage(img)

        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2") 
        b1.place(x=10,y=420,width=200)


        img1=Image.open(r"Images\Images7.jpg")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1= ImageTk.PhotoImage(img1)
        
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2") 
        b1.place(x=330,y=420,width=200)


    #=====Function Declaration ========
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms & condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Umesh@123",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register value(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                   self.var_fname.get(),
                                                                                   self.var_lname.get(),
                                                                                   self.var_contact.get(),
                                                                                   self.var_email.get(),
                                                                                   self.var_securityQ.get(),
                                                                                   self.var_securityA.get(),
                                                                                   self.var_pass.get()
                                                                               ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registered Success",parent=self.root)


    def return_login(self):
        self.root.destroy()


     







if __name__ == "__main__":
    main()