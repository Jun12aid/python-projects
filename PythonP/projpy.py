from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title('Employee Management System')

        #variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()

        lbl_title=Label(self.root,text='EMPLOYEE MANAGMENT SYSTEM',font=('Forte',37,'italic'),fg='black',bg='grey')
        lbl_title.place(x=0,y=0,width=1300,height=50)

        #logo
        img_logo=Image.open('empimg/logo.jpg')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=160,y=0,width=50,height=50)

        img_logo1=Image.open('empimg/logo 1.jpg')
        img_logo1=img_logo1.resize((50,50),Image.ANTIALIAS)
        self.photo_logo1=ImageTk.PhotoImage(img_logo)

        self.logo1=Label(self.root,image=self.photo_logo1)
        self.logo1.place(x=1100,y=0,width=50,height=50)

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='grey')
        img_frame.place(x=0,y=50,width=1630,height=160)

        #1st
        img1=Image.open('empimg/img1.jpg')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        #2nd
        img2=Image.open('empimg/img2.jpg')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=740,y=0,width=540,height=160)

        #3rd
        img5=Image.open('empimg/img5.jpg')
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photo5=ImageTk.PhotoImage(img5)

        self.img_5=Label(self.root,image=self.photo5)
        self.img_5.place(x=548,y=50,width=190,height=200) 
        #main
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='dark grey')
        Main_frame.place(x=10,y=210,width=1280,height=560)
        #upper
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='grey',text='Employee Information',font=('times new roman',11,'bold'),fg='darkblue')
        upper_frame.place(x=10,y=10,width=1255,height=270)
        #department
        lbl_dep=Label(upper_frame,textvariable=self.var_dep,text='Department',font=('arial',11,'bold'),fg='black',bg='dark grey')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,font=('arial',12,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Engineer','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #name
        lbl_Name=Label(upper_frame,font=('arial',12,'bold'),text="Name:",bg="dark grey")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)
        #designation
        lbl_Designation=Label(upper_frame,font=('arial',12,'bold'),text="Designation:",bg="dark grey")
        lbl_Designation.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designation=ttk.Entry(upper_frame,textvariable=self.var_designation,width=22,font=("arial",11,"bold"))
        txt_Designation.grid(row=1,column=1,sticky=W,padx=2,pady=7)
        #email
        lbl_Email=Label(upper_frame,font=('arial',12,'bold'),text="Email:",bg="dark grey")
        lbl_Email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_Email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        txt_Email.grid(row=1,column=3,padx=2,pady=7)
        #address
        lbl_Address=Label(upper_frame,font=('arial',12,'bold'),text="Address:",bg="dark grey")
        lbl_Address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_Address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_Address.grid(row=2,column=1,padx=2,pady=7)
        #married
        lbl_Married_Status=Label(upper_frame,font=('arial',12,'bold'),text="Married_Status:",bg="dark grey")
        lbl_Married_Status.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        com_txt_Married=ttk.Combobox(upper_frame,textvariable=self.var_married,state="readonly",width=18,font=("arial",11,"bold"))
        com_txt_Married['value']=("Married","UnMarried")
        com_txt_Married.current(0)
        com_txt_Married.grid(row=2,column=3,sticky=W,padx=2,pady=7)
        #dob
        lbl_DOB=Label(upper_frame,font=('arial',12,'bold'),text="DOB:",bg="dark grey")
        lbl_DOB.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_DOB=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        txt_DOB.grid(row=3,column=1,padx=2,pady=7)
        #doj
        lbl_DOJ=Label(upper_frame,font=('arial',12,'bold'),text="DOJ:",bg="dark grey")
        lbl_DOJ.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_DOJ=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("arial",11,"bold"))
        txt_DOJ.grid(row=3,column=3,padx=2,pady=7)
        #ID proof
        com_txt_IDproof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,state="readonly",width=18,font=("arial",11,"bold"))
        com_txt_IDproof['value']=("Select ID proof","PAN CARD","ADHAR CARD","DRIVING LICENCE")
        com_txt_IDproof.current(0)
        com_txt_IDproof.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        txt_DOJ=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        txt_DOJ.grid(row=4,column=1,padx=2,pady=7)
        #gender
        lbl_Gender=Label(upper_frame,font=('arial',12,'bold'),text="Gender:",bg="dark grey")
        lbl_Gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        com_txt_Gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state="readonly",width=18,font=("arial",11,"bold"))
        com_txt_Gender['value']=("Select Gender","Male","Female","Other")
        com_txt_Gender.current(0)
        com_txt_Gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)
        #phone
        lbl_Phone=Label(upper_frame,font=('arial',12,'bold'),text="Phone:",bg="dark grey")
        lbl_Phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_Phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_Phone.grid(row=0,column=5,padx=2,pady=7)
        #country
        lbl_Country=Label(upper_frame,font=('arial',12,'bold'),text="Country:",bg="dark grey")
        lbl_Country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_Country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=("arial",11,"bold"))
        txt_Country.grid(row=1,column=5,padx=2,pady=7)
        #CTC
        lbl_CTC=Label(upper_frame,font=('arial',12,'bold'),text="SalaryCTC:",bg="dark grey")
        lbl_CTC.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_CTC=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=("arial",11,"bold"))
        txt_CTC.grid(row=2,column=5,padx=2,pady=7)

        #mask image
        img_mask=Image.open('empimg/maskimg.png')
        img_mask=img_mask.resize((100,100),Image.ANTIALIAS)
        self.photo_mask=ImageTk.PhotoImage(img_mask)
        self.img_mask=Label(upper_frame,image=self.photo_mask)
        self.img_mask.place(x=790,y=120,width=150,height=150)
        #buttonframe
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='black')
        button_frame.place(x=1050,y=10,width=190,height=210)
        
        btn_add=Button(button_frame,text="Save",font=("Forte",15,"bold"),width=13,bg='black',fg='white')
        btn_add.grid(row=0,column=0,padx=8.5,pady=5)

        btn_Update=Button(button_frame,text="Update",font=("Forte",15,"bold"),width=13,bg='black',fg='white')
        btn_Update.grid(row=1,column=0,padx=8.5,pady=5)

        btn_Delete=Button(button_frame,text="Delete",font=("Forte",15,"bold"),width=13,bg='black',fg='white')
        btn_Delete.grid(row=2,column=0,padx=8.5,pady=5)

        btn_Clear=Button(button_frame,text="Clear",font=("Forte",15,"bold"),width=13,bg='black',fg='white')
        btn_Clear.grid(row=3,column=0,padx=8.5,pady=5)
        

        #lower
        lower_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='grey',text='Employee Information Table',font=('times new roman',11,'bold'),fg='darkblue')
        lower_frame.place(x=10,y=250,width=1255,height=290)
        #Search frame
        Search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,bg='grey',text='Search Employee Information',font=('times new roman',11,'bold'),fg='darkblue')
        Search_frame.place(x=0,y=0,width=1250,height=60)

        Search_by=Label(Search_frame,font=('arial',11,'bold'),text="Search By",fg="white",bg="dark green")
        Search_by.grid(row=0,column=0,sticky=W,padx=2)

        #search
        # self.var_com_Search=StringVar()
        com_txt_Search=ttk.Combobox(Search_frame,state="readonly",width=18,font=("arial",11,"bold"))
        com_txt_Search['value']=("Select option","Phone","ID_Proof")
        com_txt_Search.current(0)
        com_txt_Search.grid(row=0,column=1,sticky=W,padx=5)
        txt_Search=ttk.Entry(Search_frame,width=22,font=("arial",11,"bold"))
        txt_Search.grid(row=0,column=2,padx=5)
        btn__Search=Button(Search_frame,text="Search",font=("arial",11,"bold"),width=14,bg="dark grey")
        btn__Search.grid(row=0,column=3,padx=5)
        btn__ShowAll=Button(Search_frame,text="ShowAll",font=("arial",11,"bold"),width=14,bg="dark grey")
        btn__ShowAll.grid(row=0,column=4,padx=5)

        #Employee Data
        #table data
        Table_frame=Frame(lower_frame,bd=3,relief=RIDGE,bg='grey')
        Table_frame.place(x=0,y=60,width=1250,height=210)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
         
        self.employee_table=ttk.Treeview(Table_frame,column=("Dep","Name","Desig","Email","Add","Marr","Dob","Doj","IDproofcomb","gender","phone","country","salary"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('Dep',text='Department')
        self.employee_table.heading('Name',text='Name')
        self.employee_table.heading('Desig',text='Designation')
        self.employee_table.heading('Email',text='Email')
        self.employee_table.heading('Add',text='Address')
        self.employee_table.heading('Marr',text='Married Status')
        self.employee_table.heading('Dob',text='DOB')
        self.employee_table.heading('Doj',text='DOJ')
        self.employee_table.heading('IDproofcomb',text='ID proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')

        self.employee_table['show']='headings'

        self.employee_table.column("Dep",width=100)
        self.employee_table.column("Name",width=100)
        self.employee_table.column("Desig",width=100)
        self.employee_table.column("Email",width=100)
        self.employee_table.column("Add",width=100)
        self.employee_table.column("Marr",width=100)
        self.employee_table.column("Dob",width=100)
        self.employee_table.column("Doj",width=100)
        self.employee_table.column("IDproofcomb",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()


    # *******Function Declaration****
     
    def add_data(self):
            if self.var_dep.get()=="" or self.var_email=="":
                messagebox.showerror("Error","All fiels are required")           
            else:
                try:
                    conn=mysql.connector.connect(host='localhost',username='root',password='admin123',database='emp')    
                    my_cursor=conn.cursor()
                    my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                         
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_designation.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_married.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_idproofcomb.get(),
                    self.var_idproof.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_country.get(),
                    self.var_salary.get()     


                                                                                                              ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success ","Employee has been Added!",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)      
                    
    # fetch data
    def fetch_data(self):
            conn=mysql.connector.connect(host='localhost',username='root',password='admin123',database='emp')    
            my_cursor=conn.cursor()
            my_cursor.execute('select * from employee1')
            data=my_cursor.fetchall()
            if len(data)!=0:
                self.employee_table.delete(*self.employee_table.get_children())
                for i in data:
                    self.employee_table.insert("",END,values=i)
                conn.commit()
            conn.close()
         
    # get cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values'] 

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13]) 

# Update
    def update_data(self):
        if self.var_dep.get()=="" or self.var_email=="":
                messagebox.showerror("Error","All fiels are required")           
        else:
            try:
                update=messagebox.askyesno("update","are uh sure update this employee data?")
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='admin123',database='emp')    
                    my_cursor=conn.cursor()
                    my_cursor.execute('update employee1 set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,Id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where Id_Proof=%s',(
                         

                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_designation.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_married.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_idproofcomb.get(),

                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_country.get(),
                    self.var_salary.get(),   
                    self.var_idproof.get()

                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success",'Employee Succesfully updated',parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 

    def delete_data(self):
        if self.var_idproof.get()=="":
              messagebox.showerror("Error","All Things are Required")
        else:
            try:
                delete=messagebox.askyesno('Delete',"Are you Sure Uh want to DElete data?",parent=self.root)   
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='admin123',database='emp')    
                    my_cursor=conn.cursor() 
                    sql='delete from employee1 where id_proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                     if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success",'Employee Succesfully Deleted',parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)              


# reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designation.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")          

    # search
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror('error',"Please select option ")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='admin123',database='emp')    
                my_cursor=conn.cursor()            
                my_cursor.execute('select * from employee1 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))  
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())   
                    for i in rows:
                        self.employee_table.insert("",END,values=i)      
                conn.commit
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)         




if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()







        





if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()