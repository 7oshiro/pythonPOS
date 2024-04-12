from tkinter import*
from PIL import Image, ImageTk #pip Install Pillow
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time

class IMS:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By Abdulwahab")
        self.root.config(bg="white")
        
        #==Title====
        title=Label(self.root, text="Athar Textile POS", font=("time new roman", 40, "bold"), bg="black", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1,  height=70)
        
        #===btn_Logout====
        btn_logout=Button(self.root, text="Logout", command=self.logout, font=("times new roman", 20, "bold"), bg="white", fg="black",  cursor="hand2").place(x=1150, y=10, height=50, width=150)
        
        #===clock====
        self.lbl_clock=Label(self.root, text="Welcome to POS System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("time new roman", 15, ), bg="#CBCBCB", fg="black")
        self.lbl_clock.place(x=0, y=70, relwidth=1,  height=30)
        
        #===Left Menu===
        self.Menulogo=Image.open("Image/User_img.png")
        self.Menulogo=self.Menulogo.resize((200, 200))
        self.Menulogo=ImageTk.PhotoImage(self.Menulogo)
        
        LeftMenu=Frame(self.root, bd=2, relief=RIDGE, bg="#F0F0F0")
        LeftMenu.place(x=0,  y=102, width=300, height=1000)
        
        lbl_menuLogo=Label(LeftMenu, image=self.Menulogo)
        lbl_menuLogo.pack(side=TOP, fill=X)
        
        self.icon_side=PhotoImage(file="image/side.png")
        lbl_menu=Label(LeftMenu, text="Menu",  font=("times new roman", 20), bg="#009688", fg="black").pack(side=TOP, fill=X)
        
        btn_employee=Button(LeftMenu, text="Employee", command=self.employee, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20), bg="black", bd=3, cursor="hand2", fg="white",  highlightbackground="white").pack(side=TOP, fill=X)
        btn_supplier=Button(LeftMenu, text="Supplier", command=self.supplier , image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20), bg="black", bd=3, cursor="hand2", fg="white",  highlightbackground="white").pack(side=TOP, fill=X)
        btn_category=Button(LeftMenu, text="Category", command=self.category, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20), bg="black", bd=3, cursor="hand2", fg="white",  highlightbackground="white").pack(side=TOP, fill=X)
        btn_product=Button(LeftMenu, text="Product", command=self.product, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20), bg="black", bd=3, cursor="hand2", fg="white",  highlightbackground="white").pack(side=TOP, fill=X)
        btn_sales=Button(LeftMenu, text="Sales", command=self.sales, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20), bg="black", bd=3, cursor="hand2", fg="white",  highlightbackground="white").pack(side=TOP, fill=X)
        btn_exit=Button(LeftMenu, text="Exit", image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20), bg="black", bd=3, cursor="hand2", fg="white",  highlightbackground="white").pack(side=TOP, fill=X)
        
        # Content ===
        
        self.lbl_employee=Label(self.root,text="Total Employye\n [0]", bd=5, relief=RIDGE, bg="#33bbf9", font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=350, y=120, height=150, width=300)
        
        self.lbl_supplier=Label(self.root,text="Total Supplier\n [0]", bd=5, relief=RIDGE, bg="#33bbf9", font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=680, y=120, height=150, width=300)
        
        self.lbl_category=Label(self.root,text="Total Category\n [0]", bd=5, relief=RIDGE, bg="#33bbf9", font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1030, y=120, height=150, width=300)
        
        self.lbl_product=Label(self.root,text="Total Product\n [0]", bd=5, relief=RIDGE, bg="#33bbf9", font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=350, y=300, height=150, width=300)
        
        self.lbl_sales=Label(self.root,text="Total Sales\n [0]", bd=5, relief=RIDGE, bg="#33bbf9", font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=680, y=300, height=150, width=300)
        
         #===Footer====
        lbl_footer=Label(self.root, text="IMS-Inventory Management System | Developed By Abdulwahab\n For any Issue Contact: 880xxxxx13 ", font=("time new roman", 12, ), bg="#CBCBCB",fg="black").pack(side=BOTTOM, fill=X)
        
        self.update_content()
# ==============================================================================

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
    
    
    
    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            
            cur.execute("Select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[ {str(len(product))} ]')
            
            cur.execute("Select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[ {str(len(supplier))} ]')
            
            cur.execute("Select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[ {str(len(category))} ]')
            
            cur.execute("Select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[ {str(len(employee))} ]')
            
            self.lbl_sales.config(text=f'Total Sales\n[ {str(len(os.listdir('bill')))} ]')
            
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d:%m-:%Y")
            self.lbl_clock.config(text=f"Welcome to POS System\t\t Date: {str   (date_)}\t\t Time:{str(time_)}")
            self.lbl_clock.after(200, self.update_content)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
    
if __name__=="__main__":                
    root=Tk()
    obj=IMS(root)
    root.mainloop()