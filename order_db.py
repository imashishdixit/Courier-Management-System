import sqlite3





def create ():
    conn=sqlite3.connect('login.db')
    cur=conn.cursor()
    cur.execute('create table if not exists order1(id integer not null primary key autoincrement,sname text,smob text ,scity text, spin text,rname text,rmob text ,rcity text, rpin text)')
    conn.commit()
    conn.close()
    
create()
def insert(sname,smob,scity,spin,rname,rmob,rcity,rpin):
    
    conn=sqlite3.connect('login.db')
    cur=conn.cursor()
    cur.execute("insert into order1(sname,smob,scity,spin,rname,rmob,rcity,rpin) values(?,?,?,?,?,?,?,?)",(sname,smob,scity,spin,rname,rmob,rcity,rpin))
    conn.commit()
    conn.close()
    
