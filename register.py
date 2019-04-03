from tkinter import *
from tkinter import messagebox
from sqlite3 import *
import login_db
def main():
    #!=!=!=!=!=!=!=!=!=!=!==register!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!==
    reg=Toplevel()
    reg.geometry("400x400+450+80")
    reg.resizable(0, 0)
    reg.title("Registration")
    
    reg.config(background="#8f9db5")
    #!=!=!=!=!=!=!==image in background!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=
    p1=PhotoImage(file="pimage//registerback.png")
    i1=p1.subsample(1, 1)
    Label(reg,image=i1).place(x=0,y=0)
    
    #!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=
    #!=!=!=!=!=!=!=!=!==frame declaration!=!=!=!=!=!=!=!=!=!=!=!=!==

    
    #!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=
    #!=!=!=!=!=!=!=!=!=!=!=!=registration form!=!=!=!=!=!=!=!=!=!=!=!=
    Label(reg,text="Name",font=("Helvetica",13,"bold italic"),bg="#e8e1e4",fg="#59203d").grid(row=2,column=2,padx=5,pady=5,stick=E)
    Label(reg,text="Reg.No",font=("Helvetica",13,"bold italic"),bg="#e8e1e4",fg="#59203d").grid(row=3,column=2,padx=5,pady=5,stick=E)
    Label(reg,text="Gender",font=("Helvetica",13,"bold italic"),bg="#e8e1e4",fg="#59203d").grid(row=4,column=2,padx=5,pady=5,stick=E)
    Label(reg,text="Mobile No",font=("Helvetica",13,"bold italic"),bg="#e8e1e4",fg="#59203d").grid(row=5,column=2,padx=5,pady=5,stick=E)
    Label(reg,text="Email Id",font=("Helvetica",13,"bold italic"),bg="#e8e1e4",fg="#59203d").grid(row=6,column=2,padx=5,pady=5,stick=E)
    global v
    v=StringVar()
    r1=Radiobutton(reg,text="Male",variable=v,value='M',font=("Helvetica",13,"bold italic"),bg="#e8e1e4",fg="#59203d")
    r1.grid(row=4,column=3,stick=W)
    r2=Radiobutton(reg,text="Female",variable=v,value='F',font=("Helvetica",13,"bold italic"),bg="#e8e1e4",fg="#59203d")
    r2.grid(row=4,column=4,stick=W)
    Label(reg,text="Password",font=("Helvetica",13,"bold italic"),bg="#e8e1e4",fg="#59203d").grid(row=8,column=2,stick=E,padx=5,pady=5)
    Label(reg,text="Confirm Password",font=("Helvetica",13,"bold italic"),bg="#e8e1e4",fg="#59203d").grid(row=9,column=2,stick=E,padx=5,pady=5)
    global e1,e2,e3,e4,e5,e6
    e1=Entry(reg,bd=3) #name
    e1.grid(row=2,column=3,columnspan=2)
    e2=Entry(reg,bd=3)#reg no
    e2.grid(row=3,column=3,columnspan=2)
    e3=Entry(reg,bd=3)#mobile no
    e3.grid(row=5,column=3,columnspan=2)
    e4=Entry(reg,bd=3)#email id
    e4.grid(row=6,column=3,columnspan=2)
    e5=Entry(reg,bd=3,show="*")#password
    e5.grid(row=8,column=3,columnspan=2)
    e6=Entry(reg,bd=3,show="*")#confirm password
    e6.grid(row=9,column=3,columnspan=2)

    b1=Button(reg,text="Submit",bg="lightblue",font=("Helvetica",13,"bold italic"),fg="#59203d",command=submit)
    b1.grid(row=20,column=3,padx=5,pady=5,columnspan=5)
    global var
    var=StringVar()
    Label(reg,textvariable=var,bg="white",fg="red").grid(row=10,column=2)
    
    e1.focus()
    
    
    #!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!==
    reg.mainloop()



def submit():
    if (str(e1.get())!='') and (str(e2.get())!='')and (str(e3.get())!='') and (str(e4.get())!='')and (str(e5.get())!='')and (str(e6.get())!='')and (str(v.get())!='') :
        if e5.get()==e6.get():#password and confirm password should be same
            login_db.insert(e1.get(),e2.get(),v.get(),e3.get(),e4.get(),e5.get(),e6.get())
            var.set("Data Saved Successfully")
            for i in [e1,e2,e3,e4,e5,e6]:
                i.delete(0,END)
            
            
        else :
            var.set("Password and Confirm Password is not same")
    else :
        var.set("Please fill all entry")
        
    
    