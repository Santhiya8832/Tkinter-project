from tkinter import *
from tkinter import ttk,messagebox
from tkinter.font import Font
from tkinter.messagebox import showinfo

from PIL import Image, ImageTk
import mysql.connector
from pyexpat.errors import messages

mysql=mysql.connector.connect(host="localhost",user="root",passwd="",database="lms")

tk=Tk()
tk.geometry("200x200")
tk.config(bg="#D2691E")

def add_book():
    subject_code=e1.get()
    title_of_the_book=e2.get()
    author=e3.get()
    publisher=e4.get()
    prize=e5.get()
    mycursor = mysql.cursor()
    data = (subject_code, title_of_the_book, author, publisher, prize)
    sql = "insert into admin(subject_code,title_of_the_book,author,publisher,prize) values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql, data)
    mysql.commit()
    clear1()

def clear1():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0,END)

def register():
    member_name = en1.get()
    member_phone= en2.get()
    member_address= en3.get()
    mycursor1 = mysql.cursor()
    data1 = (member_name,member_phone,member_address)
    sql = "insert into member(member_name,member_phone,member_address) values(%s,%s,%s)"
    mycursor1.execute(sql, data1)
    mysql.commit()
    clear2()
    mem_code()

def mem_code():
    mycursor1 = mysql.cursor()
    sql = "select max(member_code)from member"
    mycursor1.execute(sql)
    result=mycursor1.fetchone()
    result1=result[0]
    a="Your Member Code:"+str(result1)
    messagebox.showinfo("Register",a)
def clear2():
    en1.delete(0,END)
    en2.delete(0,END)
    en3.delete(0,END)

framei=Frame(tk,height=407,width=807)
framei.place(x=280,y=10)
image_path=r"C:\Users\Hp\Desktop\python\libraryim.webp"
image1 = Image.open(image_path)
image11 = ImageTk.PhotoImage(image1)

l=Label(framei,image=image11)
l.place(x=0,y=0)

def admin():
    new=Toplevel(tk)
    new.geometry("700x400")
    new.config(bg="white")
    myfont = Font(family="times", size=15)
    l1 = Label(new, text="Subject Code", font=myfont)
    l1.place(x=50, y=20)
    l2 = Label(new, text="Title of the Book", font=myfont)
    l2.place(x=50, y=70)
    l3 = Label(new, text="Author", font=myfont)
    l3.place(x=50, y=120)
    l4 = Label(new, text="Publisher", font=myfont)
    l4.place(x=50, y=170)
    l5 = Label(new, text="Price", font=myfont)
    l5.place(x=50, y=220)
    global e1,e2,e3,e4,e5
    e1 = Entry(new, width=30, font=("times", 20))
    e1.place(x=200, y=20)
    e2 = Entry(new, width=30, font=("times", 20))
    e2.place(x=200, y=70)
    e3 = Entry(new, width=30, font=("times", 20))
    e3.place(x=200, y=120)
    e4 = Entry(new, width=30, font=("times", 20))
    e4.place(x=200, y=170)
    e5 = Entry(new, width=30, font=("times", 20))
    e5.place(x=200, y=220)

    sub = Button(new, text="ADD BOOK", bg="navy blue", fg="white", padx=2, pady=2, width=10,
                 font=("times", 20, "bold"),command=add_book)
    sub.place(x=150, y=300)

def member():
    new=Toplevel(tk)
    new.geometry("700x400")
    new.config(bg="white")
    mynote=ttk.Notebook(new)
    mynote.pack(pady=15)
    frame1 = Frame(mynote,highlightthickness=1,highlightcolor="black",width=1000, height=1000)
    frame1.place(x=10,y=10)

    frame2 = Frame(mynote,highlightthickness=1,highlightcolor="black", width=1000, height=1000)
    frame2.place(x=10,y=10)

    mynote.add(frame1, text="New Member")
    mynote.add(frame2, text="Existing Member")

    myfont = Font(family="times", size=15)
    la4=Label(frame1,text="Are you a new member?Register",font=("times",10))
    la4.place(x=70,y=10)
    la1 = Label(frame1, text="Member Name", font=myfont)
    la1.place(x=50, y=40)
    la2 = Label(frame1, text="Member Phone", font=myfont)
    la2.place(x=50, y=90)
    la3 = Label(frame1, text="Member Address", font=myfont)
    la3.place(x=50, y=140)


    global en1,en2,en3
    en1 = Entry(frame1, width=30, font=("times", 20))
    en1.place(x=200, y=40)
    en2 = Entry(frame1, width=30, font=("times", 20))
    en2.place(x=200, y=90)
    en3 = Entry(frame1, width=30, font=("times", 20))
    en3.place(x=200, y=140)
    sub = Button(frame1, text="Register", bg="navy blue", fg="white", padx=2, pady=2, width=10,font=("times", 20, "bold"), command=register)
    sub.place(x=280, y=200)

    global admin1
    scroll_y = ttk.Scrollbar(frame2, orient=VERTICAL)
    admin1 = ttk.Treeview(frame2, columns=("accession_number","subject_code","title_of_the_book","author","publisher","prize"),yscrollcommand=scroll_y.set)
    scroll_y.configure(command=admin1.yview)
    scroll_y.pack(side=RIGHT, fill=Y)

    admin1.heading("accession_number", text="Accession Number")
    admin1.heading("subject_code", text="Subject Code")
    admin1.heading("title_of_the_book", text="Title of the Book")
    admin1.heading("author", text="Author")
    admin1.heading("publisher", text="Publisher")
    admin1.heading("prize", text="Prize")
    admin1['show'] = 'headings'

    admin1.column("accession_number", width=200)
    admin1.column("subject_code", width=200)
    admin1.column("title_of_the_book", width=200)
    admin1.column("author",width=200)
    admin1.column("publisher", width=200)
    admin1.column("prize", width=200)
    admin1.pack()
    data()

    myfont = Font(family="times", size=15)
    ml1=Label(frame2,text="Member Code",font=myfont)
    ml1.place(x=100,y=300)
    me1=Entry(frame2,width=30,font=myfont)
    me1.place(x=270,y=300)
    ml2 = Label(frame2, text="Member Name", font=myfont)
    ml2.place(x=100, y=350)
    me2 = Entry(frame2, width=30, font=myfont)
    me2.place(x=270, y=350)
    ml3 = Label(frame2, text="Accession Number", font=myfont)
    ml3.place(x=100, y=400)
    me3 = Entry(frame2, width=30, font=myfont)
    me3.place(x=270, y=400)

    def order():
        def available():
            c2=mysql.cursor()
            b2=me3.get()
            sql4="select available from admin where accession_number= %s "
            c2.execute(sql4,(b2,))
            x2=c2.fetchone()
            if x2[0]==1:
                messagebox.showinfo("warning","This book is not available")
            else:
                def limit():
                    c1 = mysql.cursor()
                    b1 = me1.get()
                    sql3 = "select number_of_books_issued from member where member_code= %s "
                    c1.execute(sql3,(b1,))
                    x1 = c1.fetchone()
                    if x1[0] > 3:
                        messagebox.showinfo("warning", "you have reached your maximum limit")
                limit()
        available()
        mycursor = mysql.cursor()
        b = me3.get()
        sql2 = "update admin set available=1 where accession_number= %s"
        mycursor.execute(sql2, (b,))
        mysql.commit()

        def book():
            mycursor = mysql.cursor()
            b = me1.get()
            sql2 = "update member set number_of_books_issued=number_of_books_issued+1 where member_code= %s"
            mycursor.execute(sql2, (b,))
            mysql.commit()

        book()
        me1.delete(0,END)
        me2.delete(0, END)
        me3.delete(0, END)
    sub = Button(frame2, text="Order", bg="navy blue", fg="white", padx=2, pady=2, width=10,font=("times", 20, "bold"),command=order)
    sub.place(x=200, y=500)

def data():
    mycursor=mysql.cursor()
    sql1="select * from admin"
    mycursor.execute(sql1)
    my_result = mycursor.fetchall()
    for i in my_result:
        admin1.insert("", END, values=i)

frame4=Frame(tk,background="#D2691E",height=175,width=190)
frame4.place(x=385,y=450)
image_path1=r"C:\Users\Hp\Desktop\admin.jfif"
image_path = Image.open(image_path1)
bgimage = ImageTk.PhotoImage(image_path)
lab1=Label(frame4,image=bgimage)
lab1.place(x=0,y=0)
ad=Button(text="ADMIN",fg="black",padx=2,pady=2,width=10,font=("times",20,"bold"),command=admin)
ad.place(x=387,y=630)
frame5=Frame(tk,height=175,width=190,background="#D2691E")
frame5.place(x=800,y=450)
image_path2=r"C:\Users\Hp\Desktop\member.jfif"
image_path3 = Image.open(image_path2)
bgimage1 = ImageTk.PhotoImage(image_path3)
lab1=Label(frame5,image=bgimage1,height=170,width=170)
lab1.place(x=0,y=0)
mm=Button(text="MEMBER",fg="black",padx=2,pady=2,width=10,font=("times",20,"bold"),command=member)
mm.place(x=802,y=630)

tk.mainloop()
