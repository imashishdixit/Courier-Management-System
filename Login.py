from tkinter import *
import login_db
import panel

def log():
    


#================login declaration=======================================
    global login
    login=Toplevel()
    login.attributes("-alpha",0.98)

    login.title("Login")
    login.geometry("400x400+500+100")
    login.resizable(False, False)
#=======================================================================

#=======================image in login ================================================
    p1=PhotoImage(file="limage//b1.png")
    i1=p1.subsample(1, 1)
    l1=Label(login,image=i1)
    l1.grid(row=0,column=0)
    
    
#=======================================================================


#===================Frame Declariton===========================
    f1=Frame(login,width=300,height=300,relief=GROOVE)
    f1.place(x=50,y=70)
#=============================================================

#====================================frame data============================
    p2=PhotoImage(file="limage//lbackground.png")
    i2=p2.subsample(1, 1)
    l2=Label(f1,image=i2)
    l2.place(x=0,y=0)
#==========================================================================





#===============Entry page================================================
    global e1,e2
    e1=Entry(f1,width=33,bd=2)
    e1.insert(END, "Enter Username")
    e1.place(x=60,y=125)
    e2=Entry(f1,width=33,show="*",bd=2)
    e2.insert(END, "Enter Password")
    e2.place(x=60,y=200)
#==========================================================

#================login button===============================
    p2=PhotoImage(file="limage//LOGIN.png")
    i2=p2.subsample(6,6)
    b1=Button(f1,image=i2,activebackground="blue",relief=RAISED,command=login_db.verify)
    b1.place(x=90,y=250)
#==========================================================

#=============login logo======================================
    p3=PhotoImage(file="limage//Loginlogo.png")
    i3=p3.subsample(2, 2)
    l3=Label(login,image=i3,bg="#450011")
    l3.place(x=150,y=50)
    
    p4=PhotoImage(file="limage//username.png")
    i4=p4.subsample(20, 22)
    l4=Label(f1,image=i4)
    l4.place(x=10,y=120)
    
    p5=PhotoImage(file="limage//pass.png")
    i5=p5.subsample(22, 23)
    l5=Label(f1,image=i5)
    l5.place(x=10,y=190)
    
#=============================================================

#================label for error================================
    global error
    error=StringVar()
    
    l6=Label(f1,textvariable=error,fg="red")
    l6.place(x=57,y=220)




#===============================================================

#====================end of structure=====================================
    login.mainloop()
    

