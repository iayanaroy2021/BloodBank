import mysql.connector
from PIL import ImageTk,Image
import tkinter
from  tkinter import *
from  tkinter import ttk
from tkinter import messagebox



'''----------------------------------------------------------------------SEARCH BY BLOOD GROUP-------------------------------------------------'''
def scrBlgrp():
    root = Tk()
    root.title("search By Blood Group")
    fram = Frame(root)
    global  edit1
    Label(fram, text='Blood Group').pack(side=LEFT)
    edit1 = Entry(fram)
    edit1.pack(side=LEFT, fill=BOTH, expand=1)
    edit1.focus_set()
    butt = Button(fram, text='Search',command=searchbybldgrp,bg="#8A0707",fg="white")
    butt.pack(side=RIGHT)
    fram.pack(side=TOP)


def searchbybldgrp():
    view = Tk()
    view.geometry("750x750")
    view.title("Search Result")

    label_admin = Label(view, text="Search Results", width=50, fg="White", font=("bold", 25), bg="teal")
    label_admin.grid(row=0, column=0, columnspan=20)

    lb_name = Label(view, text="Name", font="time 15 bold", fg="teal")
    lb_name.grid(row=1, column=1, padx=10, pady=10)

    lb_age = Label(view, text="Age", font="time 15 bold", fg="teal")
    lb_age.grid(row=1, column=2, padx=10, pady=10)

    lb_gender = Label(view, text="Gender", font="time 15 bold", fg="teal")
    lb_gender.grid(row=1, column=3, padx=10, pady=10)

    lb_phone = Label(view, text="Phone", font="time 15 bold", fg="teal")
    lb_phone.grid(row=1, column=4, padx=10, pady=10)

    lb_bg = Label(view, text="Blood Group", font="time 15 bold", fg="teal")
    lb_bg.grid(row=1, column=5, padx=10, pady=10)

    lb_rh = Label(view, text="Rh", font="time 15 bold", fg="teal")
    lb_rh.grid(row=1, column=6, padx=10, pady=10)

    conbld = mysql.connector.connect(user='root', password="", host="localhost", database="blood_db")
    curbld = conbld.cursor()
    bloodgrp=edit1.get()
    print(bloodgrp)

    curbld.execute("SELECT * FROM bld_register where reg_bloodgrp='" + bloodgrp + "'")
    record1 = curbld.fetchall()
    num = 2
    for i in record1:
        name = Label(view, text=i[1], font="time 12 bold", fg="#8A0707")
        name.grid(row=num, column=1, padx=10, pady=10)

        age = Label(view, text=i[2], font="time 12 bold", fg="#8A0707")
        age.grid(row=num, column=2, padx=10, pady=10)

        gender=Label(view,text=i[3],font="time 12 bold", fg="#8A0707")
        gender.grid(row=num, column=3, padx=10, pady=10)

        phone = Label(view, text=i[4], font="time 12 bold", fg="#8A0707")
        phone.grid(row=num, column=4, padx=10, pady=10)

        bloodgrp = Label(view, text=i[5], font="time 12 bold", fg="#8A0707")
        bloodgrp.grid(row=num, column=5, padx=10, pady=10)

        rhval = Label(view, text=i[6], font="time 12 bold", fg="#8A0707")
        rhval.grid(row=num, column=6, padx=10, pady=10)

        num = num + 1

    conbld.commit()
    conbld.close()


'''------------------------------------------------------------------SEARCH BY PHONE ----------------------------------------------'''
def scrPhone():
    root = Tk()
    root.title("search by phone")
    fram = Frame(root)
    global  edit
    Label(fram, text='Phone Number').pack(side=LEFT)
    edit = Entry(fram)
    edit.pack(side=LEFT, fill=BOTH, expand=1)
    edit.focus_set()
    butt = Button(fram, text='Search',command=searchbyphone,bg="#8A0707",fg="white")
    butt.pack(side=RIGHT)
    fram.pack(side=TOP)


def searchbyphone():
    win4 = Tk()
    win4.geometry("750x750")
    win4.title("Search result")

    label_admin = Label(win4, text="Search Results", width=50, fg="White", font=("bold", 25), bg="teal")
    label_admin.grid(row=0, column=0, columnspan=20)

    lb_name = Label(win4, text="Name", font="time 15 bold",fg="teal")
    lb_name.grid(row=1, column=1, padx=10, pady=10)

    lb_age = Label(win4, text="Age", font="time 15 bold",fg="teal")
    lb_age.grid(row=1, column=2, padx=10, pady=10)

    lb_gender = Label(win4, text="Gender", font="time 15 bold",fg="teal")
    lb_gender.grid(row=1, column=3, padx=10, pady=10)

    lb_phone = Label(win4, text="Phone", font="time 15 bold", fg="teal")
    lb_phone.grid(row=1, column=4, padx=10, pady=10)


    lb_bg = Label(win4, text="Blood Group", font="time 15 bold",fg="teal")
    lb_bg.grid(row=1, column=5, padx=10, pady=10)

    lb_rh = Label(win4, text="Rh", font="time 15 bold",fg="teal")
    lb_rh.grid(row=1, column=6, padx=10, pady=10)
    opt7 = edit.get()
    #print(opt7)

    con7 = mysql.connector.connect(user='root', password="", host="localhost", database="blood_db")
    cur7 = con7.cursor()
    cur7.execute("SELECT * FROM bld_register where reg_mobile='" + opt7 + "'")
    #cur7.execute(sql7, (opt7,))
    rows = cur7.fetchall()
    num1 = 8

    # print(rows)
    for i in rows:
        name2 = Label(win4, text=i[1], font="time 12 bold", fg="#8A0707")
        name2.grid(row=num1, column=1, padx=10, pady=10)
        age2 = Label(win4, text=i[2], font="time 12 bold", fg="#8A0707")
        age2.grid(row=num1, column=2, padx=10, pady=10)
        gender2 = Label(win4, text=i[3], font="time 12 bold", fg="#8A0707")
        gender2.grid(row=num1, column=3, padx=10, pady=10)

        phone2 = Label(win4, text=i[4], font="time 12 bold", fg="#8A0707")
        phone2.grid(row=num1, column=4, padx=10, pady=10)
        bloodgrp2 = Label(win4, text=i[5], font="time 12 bold", fg="#8A0707")
        bloodgrp2.grid(row=num1, column=5, padx=10, pady=10)
        rhval2 = Label(win4, text=i[6], font="time 12 bold", fg="#8A0707")
        rhval2.grid(row=num1, column=6, padx=10, pady=10)
        num1=num1+1
    con7.commit()
    con7.close()


'''----------------------------------------------------------------Register User List[Admin]--------------------------------------------'''
def viewRegUsr():
    view = Tk()
    view.geometry("750x750")
    view.title("Registered Users")

    label_admin = Label(view, text="Registered Users List", width=50, fg="White", font=("bold", 25), bg="Teal")
    label_admin.grid(row=0, column=0, columnspan=20)

    lb_name = Label(view, text="Name", font="time 15 bold",fg="teal")
    lb_name.grid(row=1, column=1, padx=10, pady=10)

    lb_age = Label(view, text="Age", font="time 15 bold",fg="teal")
    lb_age.grid(row=1, column=2, padx=10, pady=10)

    lb_gender = Label(view, text="Gender", font="time 15 bold",fg="teal")
    lb_gender.grid(row=1, column=3, padx=10, pady=10)

    lb_phone = Label(view, text="Phone", font="time 15 bold",fg="teal")
    lb_phone.grid(row=1, column=4, padx=10, pady=10)

    lb_bg = Label(view, text="Blood Group", font="time 15 bold",fg="teal")
    lb_bg.grid(row=1, column=5, padx=10, pady=10)

    lb_rh = Label(view, text="Rh", font="time 15 bold",fg="teal")
    lb_rh.grid(row=1, column=6, padx=10, pady=10)

    con = mysql.connector.connect(user='root', password="", host="localhost", database="blood_db")
    cur = con.cursor()

    cur.execute("SELECT * FROM bld_register")
    records = cur.fetchall()
    num = 2
    for i in records:
        name = Label(view, text=i[1], font="time 12 bold", fg="#8A0707")
        name.grid(row=num, column=1, padx=10, pady=10)

        age = Label(view, text=i[2], font="time 12 bold", fg="#8A0707")
        age.grid(row=num, column=2, padx=10, pady=10)

        #val2=i[3]
        gender=Label(view,text=i[3],font="time 12 bold", fg="#8A0707")
        gender.grid(row=num, column=3, padx=10, pady=10)

        phone = Label(view, text=i[4], font="time 12 bold", fg="#8A0707")
        phone.grid(row=num, column=4, padx=10, pady=10)

        bloodgrp = Label(view, text=i[5], font="time 12 bold", fg="#8A0707")
        bloodgrp.grid(row=num, column=5, padx=10, pady=10)

        rhval = Label(view, text=i[6], font="time 12 bold", fg="#8A0707")
        rhval.grid(row=num, column=6, padx=10, pady=10)

        num = num + 1

    con.commit()
    con.close()


'''--------------------------------------------------------Function Login---------------------------------------------------------------'''
def login():
        global res2
        global res3

        user = entry_usr.get()
        u = (user,)
        pas = entry_password.get()
        p = (pas,)

        db = mysql.connector.connect(user='root', password="", host="localhost", database="blood_db")
        mycursor = db.cursor()


        '''user_check=("SELECT bl_id from bld_login where bld_login.bl_user=%s and bld_login.bl_pass=%s")
        val=[(u,p)]

        mycursor.execute(user_check, val)
        res1 = mycursor.fetchone()'''

        query = "SELECT  bl_id from bld_login where bld_login.bl_user = '" + user + "' AND bld_login.bl_pass = '" + pas + "'"
        #print(query)  # implement sql Sentence
        mycursor.execute(query)
        res1=mycursor.fetchone()
        print(res1)

        if res1 is None:
            messagebox.showinfo("Login Failed", "Not Registered")

#Admin_Login[username='admin,password='admin']

        elif (res1 == (1,)):
            Top3 = Toplevel()

            Top3.geometry("750x750")
            Top3.title("Admin DashBoard")



            label_wel = Label(Top3, text="WELCOME ADMIN", width=50, fg="#8A0707", font=("bold", 20))
            label_wel.place(x=5, y=20)
            label_wel = Label(Top3, text="------------------------------", width=50, fg="Teal", font=("bold", 20))
            label_wel.place(x=5, y=50)


            menu = Menu(Top3)
            Top3.config(menu=menu,bg='#A0A0A0')
            addmenu= Menu(menu)
            viewmenu = Menu(menu)
            menu.add_cascade(label="Add",menu=addmenu,font="time 12 bold")
            addmenu.add_command(label="Add Users",command=reg,font="time 10 bold")
            menu.add_cascade(label='View', menu=viewmenu,font="time 12 bold")
            viewmenu.add_command(label='Registered Users',command=viewRegUsr,font="time 10 bold")
            #filemenu.add_command(label='Open...')
            viewmenu.add_separator()
            viewmenu.add_command(label='Exit',command=Top3.quit,font="time 10 bold")
            searchmenu = Menu(menu)
            menu.add_cascade(label='Search', menu=searchmenu,font="time 12 bold")
            searchmenu.add_command(label=' By Phone',command=scrPhone,font="time 10 bold")
            searchmenu.add_separator()
            searchmenu.add_command(label=" By Blood Group",command=scrBlgrp ,font="time 10 bold")

        #User_Login
        else:
            sq1 = ("SELECT reg_name from bld_register where reg_id=%s")

            mycursor.execute(sq1, res1)
            res2 = mycursor.fetchone()

            # str1 =''.join(res2)
            # ss=str(str1)


            #m1 =  res2[0]

            Top2 = Toplevel()

            Top2.geometry("500x500")
            Top2.title("User DashBoard")

            Label_1 = Label(Top2, width=20, font=("bold", 20))
            Label_1.place(x=40, y=60)

            Label_2 = Label(Top2, text="Welcome to ABC Blood Typing Test", width=40, font=("bold", 10))
            Label_2.place(x=40, y=120)

            # Label_3=Label(Top2,text=m2+s3,width=30,font=("bold",12))
            # Label_3.place(x=40,y=180)
            db.commit()
            db.close()


'''-----------------------------------------insert Registration----------------------------------'''
def submit():
    name1 = entry_name.get()
    age1 = entry_age.get()
    phn1 = entry_phone.get()
    usr1=entry_uname.get()
    psw=entry_pass.get()
    r = v.get()
    if r == 1:
        n = "Male"
    if r == 2:
        n = "Female"
    print(r)
    bg = combo.get()
    rh = combo_rh.get()

    #check_counter = 0
    #warn = ""
    if name1 == "":
        messagebox.showerror("Error","Name can't be empty")
    elif age1=="":
        messagebox.showerror("Error","Age can't be empty")
    elif v.get() == 0:
        messagebox.showerror("Error", "Gender can't be empty")
    elif len(phn1)!=10:
        messagebox.showerror("Error","Enter 10 phone number")
    elif bg == "---Select---":
        messagebox.showerror( "Error","Select your blood group")
    elif rh == "---Select---":
        messagebox.showerror("Error","Select your rH factor")


    elif usr1 == "":
        messagebox.showerror("Error","Enter username")
    elif psw == "":
        messagebox.showerror("Error","Enter Password")
    else:
        myconn = mysql.connector.connect(user="root", password="", host="localhost", database="blood_db")
        cur = myconn.cursor()
        #mycursor = db.cursor()
        sql1 = "INSERT INTO bld_register(reg_name,reg_age,reg_sex,reg_mobile,reg_bloodgrp,reg_rh) values(%s,%s,%s,%s,%s,%s)"
        values = [(name1, age1,n, phn1, bg,rh)]
        cur.executemany(sql1, values)
        sql2 = "INSERT into bld_login(bl_user,bl_pass) values(%s,%s)"
        values = [(usr1, psw)]
        cur.executemany(sql2, values)
        myconn.commit()
        myconn.close()
        messagebox.showinfo('confirmation', "Registered successfully")




'''------------------------------Registration Form-------------------------------------'''

def reg():
    global entry_uname
    global  entry_pass
    global  entry_name
    global entry_age
    global entry_phone
    global combo
    global combo_rh
    global  v
    global top
    top = Toplevel()
    top.config(bg='teal')
    v = IntVar()
    entry_name = StringVar()
    entry_phone = StringVar()
    entry_age = StringVar()
    entry_pass = StringVar()
    entry_uname = StringVar()
    top.geometry("750x750")
    top.title("REGISTRATION")
    label_reg = Label(top,
                  text="Registration Form",
                  width=20, fg="white",bg="teal",
                  font=("bold", 25)).place(x=90, y=53)
    label_name = Label(top,
                   text="Name",
                   width=20,
                   fg="white", bg="teal",
                   font=("bold", 12)).place(x=80, y=130)

    entry_name = Entry(top, width=23)
    entry_name.place(x=240, y=130)

    label_age = Label(top,
                  text="Age",
                  width=20,
                  fg="white", bg="teal",
                  font=("bold", 12)).place(x=75, y=180)
    entry_age = Entry(top, width=23)
    entry_age.place(x=240, y=180)

    gender = Label(top, text="Gender", width=20, font=("bold", 12),fg="white",bg="teal")
    gender.place(x=78, y=230)

    s1 = Radiobutton(top, text=" Male ", value=1, variable=v)
    s1.place(x=235, y=230)
    # s1.deselect()
    s2 = Radiobutton(top, text="Female", value=2, variable=v)
    s2.place(x=310, y=230)
    # s2.deselect()

    label_phone = Label(top, text="Phone", width=20, font=("bold", 12),fg="white",bg="teal",)
    label_phone.place(x=80, y=280)
    entry_phone = Entry(top, width=23)
    entry_phone.place(x=240, y=280)
    label_bg = Label(top, text="Blood group", width=20, font=('bold', 12),fg="white",bg="teal",)
    label_bg.place(x=80, y=330)
    combo = ttk.Combobox(top)
    combo['values'] = ("---Select---", 'A', 'B', 'AB', 'O')
    #print(combo['values'])
    combo.current(0)
    combo.place(x=240, y=335)
    label_rh = Label(top, text="Rh Factor", width=20, font=('bold', 12),fg="white",bg="teal",)
    label_rh.place(x=80, y=375)
    combo_rh = ttk.Combobox(top)
    combo_rh['values'] = ("---Select---",'A+','A-','B+','B-','O+','O-','AB+','AB-')
    combo_rh.current(0)
    combo_rh.place(x=240, y=380)
    label_uname = Label(top,
                       text="User Name",
                       width=20,
                       fg="white", bg="teal",
                       font=("bold", 12)).place(x=80, y=420)
    entry_uname = Entry(top, width=23)
    entry_uname.place(x=240, y=420)
    label_pass = Label(top,
                       text="Password",
                       width=20,
                       fg="white", bg="teal",
                       font=("bold", 12)).place(x=80, y=460)

    entry_pass = Entry(top, width=23,show="*")
    entry_pass.place(x=240, y=460)

    register = Button(top, text='Register', font=('bold', 12), bg="#8A0707", fg="white",  width=20,command=submit).place(x=180,
                                                                                                                y=530)

'''--------------page first--------------------------------------------------------------'''

mstr = tkinter.Tk()
mstr.geometry("750x750")
mstr.title("Blood Typing Test")


label_wel = Label(mstr, text="--------welcome to ABC Blood Typing Test-----------", width=50, fg="#8A0707", font=("bold", 25))
label_wel.place(x=3, y=1)

label_wel1 = Label(mstr, text="------------------------------", width=50, fg="Teal", font=("bold", 20))
label_wel1.place(x=3, y=40)


canvas = Canvas(mstr, width = 600, height = 600)
canvas.place(x=5,y=85)
#canvas.place(fill)
#img = ImageTk.PhotoImage("F:\python\lms\Lms-tkinter projct\sunshine.jpg")
#img = ImageTk.PhotoImage(file="F:\python\lms\lms-blood ref\blood.jpg")
#canvas.create_image(75, 75, anchor=NW, image=img)
f = ('Times', 14)
label_usr= Label( mstr,
    text="UserName",
    bg='white',
    font=f,width=15).place(x=200, y=280)

entry_usr = Entry(mstr, width=18,font=10)
entry_usr.place(x=400, y=280)

label_pass= Label( mstr,
    text="Password",
    bg='white',
    font=f,width=15).place(x=200, y=320)
entry_password = Entry(mstr, width=18,font=10,show="*")
entry_password.place(x=400, y=320)



btn_login = Button(mstr, text="Login", bg="#8A0707", fg="white", width=10, font=("bold", 10),command=login)
btn_login.place(x=420, y=370)

'''acc = Label(mstr, text="Don't have an Account? Register Now!  ",font=("bold", 10),bg="white",fg="black",height=1
            ).place(x=180, y=420)

btn_register = Button(mstr, text="Registration ", bg="Teal", fg="white", width=10, font=("bold", 10),command=reg)
btn_register.place(x=460, y=420)'''


mstr.mainloop()
