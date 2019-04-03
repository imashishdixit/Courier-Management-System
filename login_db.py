from tkinter import *
import sqlite3
import Login
import panel
def create():
    conn=sqlite3.connect('Login.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS sign(id integer not null primary key autoincrement,name text,reg_no text,gender text,mob text,email_id text,password text,cpassword text)')
    conn.commit()
    conn.close()
create()

def insert(name,reg_no,gender,mob,email_id,password,cpassword):
    conn=sqlite3.connect('login.db')
    cur=conn.cursor()
    cur.execute("insert into sign(name,reg_no,gender,mob,email_id,password,cpassword) values(?,?,?,?,?,?,?)",(name,reg_no,gender,mob,email_id,password,cpassword))
    conn.commit()
    conn.close()

def verify():
    conn=sqlite3.connect('Login.db')
    cur=conn.cursor()
    
    cur.execute('SELECT * FROM sign where email_id=? and password=?',(Login.e1.get(),Login.e2.get()))
    global result
    result=cur.fetchall()
    if result:
        global name
        name=Login.e1.get()
        panel.main()
        
    
    else :
        Login.error.set("Email ID or Password is incorrect")


    