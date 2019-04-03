from tkinter import *
import sqlite3
import Login
import homepage
import login_db
import loc_fin
import order_db
#================submit function==============================
def submit():
    if (str(entry1.get())!='') and (str(entry2.get())!='')and (str(entry3.get())!='') and (str(entry4.get())!='')and (str(entry5.get())!='')and (str(entry6.get())!='')and (str(entry7.get())!='') and (str(entry8.get())!='')  :
        
        order_db.insert(entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get())
        var.set("Order placedSuccessfully")
        for i in [entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8]:
            i.delete(0,END)
            
            
        
    else :
        var.set("Please fill all entry")
        
#=========================================================

#==================function definiton===============================

def pcalc():
    def cal():
        var.set("Total amount to be paid is :"+str(int(e1.get())*25)+"$410.")
    pcal=Toplevel()
    pcal.title("Price Calculator")
    pcal.geometry("300x300+550+250")
    pcal.resizable(0, 0)
    
    p1=PhotoImage(file="limage//lbackground.png")
    i1=p1.subsample(2, 2)
    l1=Label(pcal,image=i1)
    l1.place(x=0,y=0)
    
    var=StringVar()
    
    Label(pcal,text="Weight",font=("Arial",10,"bold italic"),bg="grey").place(x=15,y=51)
    e1=Entry(pcal,bd=3)
    e1.place(x=100,y=51)
    
    Label(pcal,text="Description",font=("Arial",10,"bold italic"),bg="grey").place(x=15,y=100)
    e2=Entry(pcal,bd=3)
    e2.place(x=100,y=100)
    
    Button(pcal,text="Calculate",font=("Arial",10,"bold italic"),bg="red",fg="black",command=cal).place(x=100,y=200)
    
    Label(pcal,textvariable=var,bg="white",fg="red",font=("helvetica",10,"bold italic")).place(x=80,y=150)
    
    
    pcal.mainloop()
    
#======================Function of booking========
def booking():
    booking=Toplevel()
    booking.title("Booking")
    booking.resizable(0, 0)
    booking.geometry("500x300")
    p1=PhotoImage(file="limage//lbackground.png")
    i1=p1.subsample(1, 1)
    l1=Label(booking,image=i1)
    l1.place(x=0,y=0)
   
    #==================sender details=============================
    
    label0=Label(booking,text="Sender's Details",height=2,width=43,font='times 16 bold',bg="grey",fg="black")
    
    label1=Label(booking,text="Name",anchor=W,font='times 12 bold',bg="grey",fg="black")
    label2=Label(booking,text="Mobile No.",anchor=W,font='times 12 bold',bg="grey",fg="black")
    label3=Label(booking,text="City",anchor=W,font='times 12 bold',bg="grey",fg="black")
    label4=Label(booking,text="Pin-Code",anchor=W,font='times 12 bold',bg="grey",fg="black")
    label5=Label(booking,text="Receiver's Details",bg="grey",fg="black",font='times 16 bold',height=2,width=43)
    label6=Label(booking,text="Name",anchor=W,font='times 12 bold',bg="grey",fg="black")
    label7=Label(booking,text="City",anchor=W,font='times 12 bold',bg="grey",fg="black")
    label8=Label(booking,text="Pin-Code",anchor=W,font='times 12 bold',bg="grey",fg="black")
    label9=Label(booking,text="Mobile No",anchor=W,font='times 12 bold',bg="grey",fg="black")
    
    global entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8
    
    
    entry1=Entry(booking,bd=3)
    entry2=Entry(booking,bd=3)
    entry3=Entry(booking,bd=3)
    entry4=Entry(booking,bd=3)
    entry5=Entry(booking,bd=3)
    entry6=Entry(booking,bd=3)
    entry7=Entry(booking,bd=3)
    entry8=Entry(booking,bd=3)
    
    
    
    
    label0.grid(row=0,columnspan=6)
    label1.grid(row=1,column=0)
    label2.grid(row=1,column=4)
    label3.grid(row=2,column=0)
    label4.grid(row=2,column=4)
    label5.grid(row=5,columnspan=6)
    label6.grid(row=6,column=0)
    label7.grid(row=7,column=0)
    label8.grid(row=7,column=4)
    label9.grid(row=6,column=4)
    
    
    entry1.grid(row=1,column=2)
    entry2.grid(row=1,column=5)
    entry3.grid(row=2,column=2)
    entry4.grid(row=2,column=5)
    entry5.grid(row=6,column=2)
    entry6.grid(row=6,column=5)
    entry7.grid(row=7,column=2)
    entry8.grid(row=7,column=5)
    global var
    var=StringVar()
    Label(booking,textvariable=var,bg="red",fg="white").grid(row=10,column=2)
                                                                              
    b1=Button(booking,text="Submit",font=("arial",10,"bold italic"),bg="red",fg="black",command=submit)
    b1.grid(row=12,column=3)
    #==============================================================
    booking.mainloop()
#===================================================================
def main ():
    #=======destroying of previous window==============================
    #Login.login.destroy()
    
    #==================================================================
    
    
    
    
    #===================panel declartion ===========================
    panel=Toplevel()#tk should be replaced with toplevel
    panel.title("Panel")
    panel.geometry("700x500+400+100")
    panel.resizable(0, 0)
    #================================================================
    
    
    
    #===========================frame declartion===================================
    f1=Frame(panel,bg="red",width=700,height=100)
    f1.place(x=0,y=0)
    f2=Frame(panel,bg="purple",width=700,height=400)
    f2.place(x=0,y=100)
    #========================================================================
    
    #===============frame data==============================================
    p1=PhotoImage(file="pimage//pback.png")
    i1=p1.subsample(3, 3)
    l1=Label(f1,image=i1)
    l1.place(x=0,y=0)
    
    global tt
    tt=StringVar()
    
    
    
    l2=Label(f1,textvariable=tt,font=('helvetica',20,'bold'))
    l2.place(x=20,y=30)
    tt.set("Welcome "+login_db.name)
    
    p2=PhotoImage(file="pimage//logout.png")
    i2=p2.subsample(8, 8)
    b1=Button(f1,image=i2,activebackground="black",command=panel.destroy)
    b1.place(x=600,y=20)
    
    #========================================================================
    
    
    
    #=================fram2 data===========================================
    p3=PhotoImage(file="pimage//b3.png")
    i3=p3.subsample(1, 1)
    l4=Label(f2,image=i3)
    l4.place(x=0,y=0)
    #image part completed
    
    
    
    #=============================button 1===================================
    p4=PhotoImage(file="pimage//pcalculator.png")
    i4=p4.subsample(3, 3)
    b2=Button(f2,image=i4,command=pcalc)
    b2.place(x=230 ,y=250)
    #========================================================================
    #+==============button 2=============================================
    p5=PhotoImage(file="pimage//booking.png")
    i5=p5.subsample(4, 4)
    b3=Button(f2,image=i5,command=booking)
    b3.place(x=100,y=50)
    
    #======================================================================
    #=================button 3==========================================
    p6=PhotoImage(file="pimage//loc_fin.png")
    i6=p6.subsample(2, 2)
    b4=Button(f2,image=i6,command=loc_fin.main)
    b4.place(x=500,y=50)
    
    
    
    
    
    
    
    #=======================================================================
    
    
    
    #==========continous loop===============================================

    panel.mainloop()



    
    
    

