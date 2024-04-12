from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import os

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Systtem | Developed By Adulwahab")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #=====Images=====
        
        self.im1=Image.open("Image/phone.png")
        self.im1=self.im1.resize((540,420), Image.LANCZOS)
        self.im1=ImageTk.PhotoImage(self.im1)
        
        self.lbl_im1=Label(self.root,image=self.im1, bd=0, relief=RAISED)
        self.lbl_im1.place(x=30,y=100)
        
        #========Login_Frame======
        self.employee_id=StringVar()
        self.password=StringVar()
        
        login_frame=Frame(self.root, bd=2, relief=RIDGE, bg="#fafafa")
        login_frame.place(x=650, y=90, width=350, height=460)
        
        title=Label(login_frame, text="Login System", font=("time new roman", 30, "bold"), bg="white").place(x=0, y=30, relwidth=1)
        
        lbl_user=Label(login_frame, text="Empployee ID", font=("goudy old style", 15, "bold"), bg="white", fg="#767171").place(x=50, y=100)
        txt_employee_id=Entry(login_frame, textvariable=self.employee_id, font=("time new roman", 15, "bold"), bg="lightyellow").place(x=50, y=130, width=250)
        
        lbl_pass=Label(login_frame, text="Password", font=("goudy old style", 15, "bold"), bg="white", fg="#767171").place(x=50, y=190)
        txt_pass=Entry(login_frame, textvariable=self.password, show="*",font=("time new roman", 15, "bold"), bg="lightyellow").place(x=50, y=220, width=250)
        
        btn_login=Button(login_frame, text="Log In", command=self.login, font=("time new roman", 15, "bold"), bg="#00B0F0",  fg="white",  cursor="hand2" ).place(x=50, y=300, width=250, height=40)
        
        hr=Label(login_frame, bg="lightgrey").place(x=50, y=380, width=250, height=2)
        or_=Label(login_frame, text="Or", font=("time new roman", 15, "bold"), bg="white", fg="lightgrey").place(x=150, y=365)
        
        btn_forget=Button(login_frame, text="Forget Password", command=self.forget_window, bd=0, font=("time new roman", 13, "bold"), bg="white", activebackground="white", fg="#00759E", cursor="hand2").place(x=100, y=395)

    
    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror('Error', "All Fields Are Reuired", parent=self.root)
            else:
                cur.execute("Select utype from employee WHERE eid=? AND pass=?", (self.employee_id.get(), self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror('Error', "Invalid User Name or Password", parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def forget_window(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.employee_id.get()=="":
                    messagebox.showerror('Error', "Employee ID Must Be Required", parent=self.root)
                else:
                    cur.execute("Select email from employee WHERE eid=?", (self.employee_id.get(),))
                    email=cur.fetchone()
                    if email==None:
                            messagebox.showerror('Error', "Invalid Employee ID, try again", parent=self.root)
                    else:
                        #======Forget Window=======
                        self.var_otp=StringVar()
                        self.var_new_pass=StringVar()
                        self.var_conf_pass=StringVar()
                        # call send _email_function()
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title('RESET PASSWORD')
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()
                        
                        title=Label(self.forget_win, text='Reset Password', font=('goudy old style', 15, "bold"), bg="#3f51b5", fg="white").pack(side=TOP, fill=X)
                        lbl_reset = Label(self.forget_win, text="Enter OTP Sent on Registered Email", font=("times new roman", 15)).place(x=20, y=60)
                        txt_reset=Entry(self.forget_win, textvariable=self.var_otp, font=("times new roman", 15), bg="lightyellow").place(x=20, y=100, width=200, height=30) 
                        self.btn_reset=Button(self.forget_win,  text="SUBMIT", font=("times new roman", 15), bg="lightblue", cursor="hand2")
                        self.btn_reset.place(x=240, y=99, width=100, height=30)
                        
                        lbl_new_pass = Label(self.forget_win, text="New Password", font=("times new roman", 15)).place(x=20, y=160)
                        txt_new_pass=Entry(self.forget_win, textvariable=self.var_new_pass, font=("times new roman", 15), bg="lightyellow").place(x=20, y=190, width=200, height=30) 
                        
                        lbl_c_pass = Label(self.forget_win, text="Confirm Password", font=("times new roman", 15)).place(x=20, y=225)
                        txt_c_pass=Entry(self.forget_win, textvariable=self.var_conf_pass, font=("times new roman", 15), bg="lightyellow").place(x=20, y=255, width=200, height=30)
                        
                        self.btn_update=Button(self.forget_win, text="UPDATE", state=DISABLED, font=("times new roman", 15), bg="lightgreen", cursor="hand2")
                        self.btn_update.place(x=150, y=300, width=100, height=30)
                        
                        
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}",parent=self.root)




root=Tk()
obj=Login_System(root)
root.mainloop()