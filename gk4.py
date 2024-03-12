#import module
import sqlite3

#connecting to sqlite
conn=sqlite3.connect('gfg1.db')

#creating to sqlite
conn=sqlite3.connect('gfg1.db')

#creating a cursor object using
#the cursor() method
cursor=conn.cursor()

#creating table
table="""create table if not exists employee
      (first_name varchar(255),
      last_name varchar(255),
      age int ,
      sex varchar(25),
      income int);"""
cursor.execute(table)

#qureis to insert records.
cursor.execute('''insert into employee(first_name,last_name,age,sex,income)values('Anand','choudery',25,'m',10000)''')
cursor.execute('''insert into employee(first_name,last_name,age,sex,income)values('Mukesh','Sharma',20,'m',90000)''')
cursor.execute('''insert into employee(first_name,last_name,age,sex,income)values('ankit','Pandey',24,'m',6300)''')
cursor.execute('''insert into employee(first_name,last_name,age,sex,income)values('subhdra','singh',26,'f',8000)''')
cursor.execute('''insert into employee(first_name,last_name,age,sex,income)values('Tanu','Mishra',24,'f',65000)''')
#display data inserted
print("employee table:")
data=cursor.execute('''select * from employee''')
for row in data:
    print(row)

#updating
    cursor.execute('''update employee set income=5000 where age<25;''')
    print('\nAfter updating\n')

#display data
    print("employee table:")
    data=cursor.execute('''select * from employee''')
    for row in data:
        print(row)
conn.commit()
conn.close()
