from tkinter import *
import mysql.connector
def click():

    name=entryname.get()
    email=entryemail.get()
    age=entryage.get()
    PNR_NO=entryPNR_NO.get()
    state=entrystate.get()
    phn=entryphn.get()

    print(name,email,age,PNR_NO,state,phn)

    sql = "insert into record values( '{}','{}','{}','{}','{}','{}')".format(name, email, age, PNR_NO, state, phn)

    con = mysql.connector.connect(user='root',password="",host="localhost",database="record")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(name,"saved in database")

def click1():
    name = entryname.get()
    email = entryemail.get()
    age = entryage.get()
    PNR_NO = entryPNR_NO.get()
    state = entrystate.get()
    phn = entryphn.get()

    print(name, email, age, PNR_NO, state,phn)

    sql = "delete from  record where name = '{}'".format(name)

    con = mysql.connector.connect(user='root', password="", host="localhost", database="record")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(name, "delete in database")

def click2():
    name = entryname.get()
    email = entryemail.get()
    age = entryage.get()
    PNR_NO = entryPNR_NO.get()
    state = entrystate.get()
    phn = entryphn.get()

    print(name, email, age, PNR_NO, state, phn)

    sql = "select * from record"
    con = mysql.connector.connect(user='root', password="", host="localhost", database="record")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    rows = cursor.fetchall()

    for rows in rows:
        print(rows)

def click3():
    name = entryname.get()
    email = entryemail.get()
    age = entryage.get()
    PNR_NO = entryPNR_NO.get()
    state = entrystate.get()
    phn = entryphn.get()

    print(name, email, age, PRN_NO, state, phn)

    sql = "update record set PNR_NO = '{}' where name = '{}'".format(PNR_NO, name)

    con = mysql.connector.connect(user='root', password="", host="localhost", database="record")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(PNR_NO, "update in database")

def click4():
    name = entryname.get()
    email = entryemail.get()
    age = entryage.get()
    PNR_NO = entryPNR_NO.get()
    state = entrystate.get()
    phn = entryphn.get()

    print(name, email, age, PNR_NO, state, phn)

    sql = "update record set phn = '{}' where name = '{}'".format(phn, name)


    con = mysql.connector.connect(user='root', password="", host="localhost", database="record")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(phone, "update in database")

def click5():
    name = entryname.get()
    email = entryemail.get()
    age = entryage.get()
    PNR_NO = entryPNR_NO.get()
    state = entrystate.get()
    phn = entryphn.get()

    print(name, email, age, PNR_NO, state, phn)

    sql = "update record set age = '{}' where name = '{}'".format(age, name)

    con = mysql.connector.connect(user='root', password="", host="localhost", database="record")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(age, "update in database")

def click6():
    name = entryname.get()
    email = entryemail.get()
    age = entryage.get()
    PNR_NO = entryPNR_NO.get()
    state = entrystate.get()
    phn = entryphn.get()

    print(name, email, age, PNR_NO, state, phn)

    sql = "update record set state = '{}' where name = '{}'".format(state, name)

    con = mysql.connector.connect(user='root', password="", host="localhost", database="record")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(state, "update in database")

def click7():
    name = entryname.get()
    email = entryemail.get()
    age = entryage.get()
    PNR_NO = entryPNR_NO.get()
    state = entrystate.get()
    phn = entryphn.get()

    print(name, email, age, PNR_NO, state, phn)

    sql = "update record set email = '{}' where name = '{}'".format(email, name)

    con = mysql.connector.connect(user='root', password="", host="localhost", database="record")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

    print(email, "update in database")

window = Tk()

lbltitle = Label(window, text="railway record")
lbltitle.pack()

lblname = Label(window, text="enter the name")
lblname.pack()

entryname = Entry(window)
entryname.pack()

lblphn = Label(window, text="enter the phone number")
lblphn.pack()

entryphn = Entry(window)
entryphn.pack()

lblemail = Label(window, text="enter the email")
lblemail.pack()

entryemail = Entry(window)
entryemail.pack()

lblPNR_NO = Label(window, text="enter the PNR number")
lblPNR_NO.pack()

entryPNR_NO = Entry(window)
entryPNR_NO.pack()

lblage = Label(window, text="enter the age")
lblage.pack()

entryage = Entry(window)
entryage.pack()

lblstate = Label(window, text="enter the state")
lblstate.pack()

entrystate = Entry(window)
entrystate.pack()

btnsave = Button(window, text="save record", command=click)
btnsave.pack()

btndelete = Button(window, text="delete record", command=click1)
btndelete.pack()

btnselect = Button(window, text="view all record", command=click2)
btnselect.pack()

btnupdate1 = Button(window, text="update PNR number", command=click3)
btnupdate1.pack()

btnupdate2 = Button(window, text="update phone number", command=click4)
btnupdate2.pack()

btnupdate3 = Button(window, text="udape age", command=click5)
btnupdate3.pack()

btnupdate4 = Button(window, text="update state", command=click6)
btnupdate4.pack()

btnupdate5 = Button(window, text="update email", command=click7)
btnupdate5.pack()

window.mainloop()