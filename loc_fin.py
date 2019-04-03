from tkinter import *
import sqlite3
def create():
    conn=sqlite3.connect('login.db')
    cur=conn.cursor()
    cur.execute('create table if not exists locf(id integer not null primary key autoincrement,pcode text ,location text)')
        
    conn.commit()
    conn.close()
def insert(p,l):
    create()
    conn=sqlite3.connect('login.db')
    cur=conn.cursor()
    cur.execute("insert into locf(pcode,location) values(?,?)",(p,l))
    conn.commit()
    conn.close()

def show(p):
    conn=sqlite3.connect('login.db')
    cur=conn.cursor()
    cur.execute("select * from locf where pcode=?",(p,))
    row=cur.fetchall()
        
    conn.commit()
    conn.close()
    return row
def find():
    t=show(e1.get())
    for i in t:
        l1.insert(END,i)

def main ():
    loc=Tk()
    loc.title("Location Finder")
    loc.geometry("400x200")
    loc.resizable(0, 0)
    
    
    Label(loc,text="PIN CODE").grid(row=4,column=4)
    global e1
    e1=Entry(loc,bd=3)
    e1.grid(row=4,column=5)
    global l1
    l1=Listbox(loc,width=40,height=40)
    l1.grid(row=5,column=4,columnspan=4,rowspan=4)
    b1=Button(loc,text="Find Location",command=find)
    b1.grid(row=5,column=11)
    loc.mainloop()
    



