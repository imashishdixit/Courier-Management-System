from tkinter import *

import Login
import register
import panel
import Track
def main():
#===========================home designing========

    global home
    home=Tk()
    #home.attributes('-alpha',0.8)
    home.title("Homepage")
    home.geometry("800x600+325+75")
    home.resizable(False, False)
#=================================================



#=============frame declaration===========================
    f1=Frame(home,width=800,height=140,bg="#4d94ff")
    f1.grid(row=0,column=0)
    f2=Frame(home,bg="blue",width=800,height=427)
    f2.grid(row=140,column=0)
    f3=Frame(home,width=800,height=33,bg="white")
    f3.grid(row=580,column=0)
#=======================================================



#=============Frame 1 Data=========================
    l1=Label(f1,text="DTDC Courier Services",font=("arial",20,"bold"),bg="#00b386",fg="#1a1a1a",bd=15)
    l1.place(x=10,y=40)
    p1=PhotoImage(file="himage//frameimage.png")
    i1=p1.subsample(2, 2)
    l2=Label(f1,image=i1)
    l2.place(x=400,y=10)


#=======================================================




#=============Frame 2 Data===============================
    p2=PhotoImage(file="himage//back.png")
    i2=p2.subsample(2, 2)
    l3=Label(f2,image=i2)
    l3.place(x=0,y=0)

    p3=PhotoImage(file="himage//Login.png")
    p4=PhotoImage(file="himage//Register.png")
    p5=PhotoImage(file="himage//track.png")

    i3=p3.subsample(2, 3)
    i4=p4.subsample(2, 2)
    i5=p5.subsample(2, 2)

    b1=Button(f2,image=i3,cursor="hand2",activebackground="blue",command=Login.log)
    b2=Button(f2,image=i4,cursor="hand2",activebackground="blue",command=register.main)
    b3=Button(f2,image=i5,cursor="hand2",activebackground="blue",command=Track.main)

    b1.place(x=150,y=150)
    b2.place(x=350,y=150)
    b3.place(x=550,y=150)








#=========================================================


#======================Fram 3 data=======================

    copy=Label(f3,text="Copyright (C) 2018 by Ashish Dixit\nAll Right Reserved",font=("times new roman",10,"bold"))
    copy.pack()

#========================================================


















    home.mainloop()

if __name__=="__main__":main()
