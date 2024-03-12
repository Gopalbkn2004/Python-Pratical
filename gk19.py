import sqlite3
conn=sqlite3.connect('gopal.db')
conn.execute('''create table if not exists text
            (sno int not null,
            questions varchar(200) not null,
            option1 varchar(255),
            option2 varchar(255),
            option3 varchar(255),
            option4 varchar(255),
            answer varchar(255),
            userans varchar(255));''')
for i in range(2):
    no=input("enter the number:")
    q=input("enter Question:")
    o1=input("enter 1 option :")
    o2=input("enter 2 option :")
    o3=input("enter 3 option :")
    o4=input("enter 4 option :")
    answer=input("enter the correct answer")


    conn.execute('''insert into text(sno,questions,option1,option2,option3,option4,answer)\
                 values(?,?,?,?,?,?,?)''',(no,q,o1,o2,o3,o4,answer))
data=conn.execute("select * from text");
for x in data:
    print(x)
conn.close()
    
     


