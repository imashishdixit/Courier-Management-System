from tkinter import *
import sqlite3



def show(i,mob):
    conn=sqlite3.connect('login.db')
    cur=conn.cursor()
    cur.execute("select id,sname,rcity from order1 where (id=?) or(smob=?)  ",(i,mob))
    row=cur.fetchall()
        
    conn.commit()
    conn.close()
    return row
def find():
    t=show(e1.get(),e2.get())
    for i in t:
        l1.insert(END,i)

def main ():
    track=Tk()
    track.title("Track Your Order")
    track.geometry("500x250+250+25")
    track.resizable(0, 0)
    
    
    Label(track,text="Order ID").grid(row=4,column=4)
    Label(track,text="Mobile No").grid(row=6,column=4)
    global e1,e2
    e1=Entry(track,bd=3)
    e1.grid(row=4,column=5)
    e2=Entry(track,bd=3)
    e2.grid(row=6,column=5)
    global l1
    l1=Listbox(track,width=100,height=10)
    l1.grid(row=8,column=4,columnspan=4,rowspan=4)
    b1=Button(track,text="Track",command=find)
    b1.grid(row=6,column=6)
    track.mainloop()
    
