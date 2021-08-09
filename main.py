
from tkinter import *
from tkinter import ttk
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='yellow',fg='red')
        title.pack(side=TOP,fill=X)
        #====================Variables======================
        self.roll=StringVar()
        self.name=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.cont=StringVar()
        self.dob=StringVar()
        self.searchby=StringVar()
        self.searchtxt=StringVar()

#================Manage Frame===========================================
        manage_fr=Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
        manage_fr.place(x=20,y=100,width=450,height=590)
        m_title=Label(manage_fr,text='Manage Students',font=("times new roman",30,'bold'),bg='crimson',fg='white')
        m_title.grid(row=0,columnspan=2,pady=20)

        roll=Label(manage_fr,text="Roll No:",bg='crimson',fg='white',font=('times new roman',20,'bold'))
        roll.grid(row=1,column=0,padx=10,pady=10,sticky='w')
        txt_roll=Entry(manage_fr,textvariable=self.roll,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,padx=10,pady=10)

        name=Label(manage_fr,text="Name:",bg='crimson',fg='white',font=('times new roman',20,'bold'))
        name.grid(row=2,column=0,padx=10,pady=10,sticky='w')
        txt_na=Entry(manage_fr,textvariable=self.name,bd=5,relief=GROOVE,font=("times new roman",15,'bold'))
        txt_na.grid(row=2,column=1,padx=10,pady=10)

        email = Label(manage_fr, text="Email:", bg='crimson', fg='white', font=('times new roman', 20, 'bold'))
        email.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txt_em = Entry(manage_fr, bd=5, relief=GROOVE,textvariable=self.email, font=("times new roman", 15, 'bold'))
        txt_em.grid(row=3, column=1, padx=10, pady=10)

        gender = Label(manage_fr, text="Gender:", bg='crimson', fg='white', font=('times new roman', 20, 'bold'))
        gender.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        combo=ttk.Combobox(manage_fr,textvariable=self.gender,font=("times new roman",13,'bold'),state='readonly')
        combo['values']=("Male","Female","Other")
        combo.grid(row=4,column=1,padx=20,pady=10)

        cont = Label(manage_fr, text="Contact:", bg='crimson', fg='white', font=('times new roman', 20, 'bold'))
        cont.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        txt_cont = Entry(manage_fr,textvariable=self.cont,bd=5, relief=GROOVE, font=("times new roman", 15, 'bold'))
        txt_cont.grid(row=5, column=1, padx=10, pady=10)

        dob = Label(manage_fr, text="D.O.B.:", bg='crimson', fg='white', font=('times new roman', 20, 'bold'))
        dob.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        txt_dob = Entry(manage_fr, bd=5, relief=GROOVE,textvariable=self.dob, font=("times new roman", 15, 'bold'))
        txt_dob.grid(row=6, column=1, padx=10, pady=10)

        add = Label(manage_fr, text="Address:", bg='crimson', fg='white', font=('times new roman', 20, 'bold'))
        add.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        self.txt_add=Text(manage_fr,width=30,height=4,font=("",10),bd=5,relief=GROOVE)
        self.txt_add.grid(row=7,column=1,padx=10,pady=10,sticky='w')
        #===========Button Frame============
        butt=Frame(manage_fr,bd=4,relief=RIDGE,bg='crimson')
        butt.place(x=15,y=525,width=420)

        add_bt=Button(butt,text="Add",command=self.add_st,width=10).grid(row=0,column=0,padx=10,pady=10)
        upd_bt=Button(butt,text="Update",command=self.update,width=10).grid(row=0,column=1,padx=10,pady=10)
        clr_bt=Button(butt,text="Clear",command=self.clear,width=10).grid(row=0,column=2,padx=10,pady=10)
        delt_bt=Button(butt,text="Delete",width=10,command=self.delete_d).grid(row=0,column=3,padx=10,pady=10)




        #======================Detail frame===========================
        det_fr=Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
        det_fr.place(x=500,y=100,width=800,height=590)

        search=Label(det_fr,text="Search By",font=('times new roman',20,'bold'),bg='crimson',fg='white')
        search.grid(row=0,column=0,padx=10,pady=20,sticky='w')

        serc=ttk.Combobox(det_fr,font=('times new roman',13,'bold'),textvariable=self.searchby,width=10,state='readonly')
        serc['values']=("Roll_no","Name","Contact")
        serc.grid(row=0,column=1,padx=20,pady=10)

        txt_sear=Entry(det_fr,width=20,textvariable=self.searchtxt,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        txt_sear.grid(row=0,column=2,padx=20,pady=10,sticky='w')

        sear_but=Button(det_fr,text="Search",command=self.search_d,width=10,pady=5).grid(row=0,column=3,padx=20,pady=10)
        show_b=Button(det_fr,text="Show All",command=self.fetch_d,width=10,pady=5).grid(row=0,column=4,padx=20,pady=10)

        #===========Table Frame====================================
        table=Frame(det_fr,bd=4,relief=RIDGE,bg='crimson')
        table.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(table,orient=HORIZONTAL)
        scroll_y=Scrollbar(table,orient=VERTICAL)
        self.std_t=ttk.Treeview(table,columns=("Roll No","Name","email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.std_t.xview)
        scroll_y.config(command=self.std_t.yview)
        self.std_t.heading("Roll No",text="Roll No.")
        self.std_t.heading("Name", text="Name")
        self.std_t.heading("email", text="Email")
        self.std_t.heading("Gender", text="Gender")
        self.std_t.heading("Contact", text="Contact")
        self.std_t.heading("DOB", text="D.O.B.")
        self.std_t.heading("Address", text="Address")
        self.std_t['show']=('headings')
        self.std_t.column("Roll No",width=100)
        self.std_t.column("Name",width=100)
        self.std_t.column("email",width=100)
        self.std_t.column("Gender",width=100)
        self.std_t.column("Contact",width=100)
        self.std_t.column("DOB",width=100)
        self.std_t.column("Address",width=150)

        self.std_t.pack(fill=BOTH,expand=1)
        self.std_t.bind("<ButtonRelease-1>",self.get_cur)
        self.fetch_d()

    def add_st(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll.get(),
                                                                         self.name.get(),
                                                                         self.email.get(),
                                                                         self.gender.get(),
                                                                         self.cont.get(),
                                                                         self.dob.get(),
                                                                         self.txt_add.get('1.0',END)
                                                                         ))
        con.commit()
        self.fetch_d()
        self.clear()
        con.close()
    def fetch_d(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.std_t.delete(*self.std_t.get_children())
            for row in rows:
                self.std_t.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.roll.set("")
        self.name.set("")
        self.cont.set("")
        self.email.set("")
        self.gender.set("")
        self.dob.set("")
        self.txt_add.delete('1.0',END)
    def get_cur(self,ev):
        cursor_row=self.std_t.focus()
        contents=self.std_t.item(cursor_row)
        row=contents['values']
        self.roll.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.gender.set(row[3])
        self.cont.set(row[4])
        self.dob.set(row[5])
        self.txt_add.delete('1.0', END)
        self.txt_add.insert(END,row[6])
    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (
                                                                                                                    self.name.get(),
                                                                                                                    self.email.get(),
                                                                                                                    self.gender.get(),
                                                                                                                    self.cont.get(),
                                                                                                                    self.dob.get(),
                                                                                                                    self.txt_add.get('1.0', END),
                                                                                                                    self.roll.get()
                                                                                                                    ))
        con.commit()
        self.fetch_d()
        self.clear()
        con.close()
    def delete_d(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.roll.get())
        con.commit()
        con.close()
        self.fetch_d()
        self.clear()

    def search_d(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students where"+str(self.searchby.get())+"LIKE '% "+(str(self.searchtxt.get()))+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.std_t.delete(*self.std_t.get_children())
            for row in rows:
                self.std_t.insert('',END,values=row)
            con.commit()
        con.close()

root=Tk()
ob=Student(root)
root.mainloop()