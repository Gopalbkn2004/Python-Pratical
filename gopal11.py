#importing splite3 module
import sqlite3

#create connection by using object
#to connect with hotel-data database
connection=sqlite3.connect("hote2-data.db")

#query to create a table named food1
connection.execute('''create table if not exists hotel2
                   (find int primary key not null,
                    fname  text not null,
                    cost  int,
                    weight int);''')
#insert query to insert food details in
#the above table
connection.execute("insert into hotel2 values(1,'cakes',800,10)")
connection.execute("insert into hotel2 values(2,'biscuts',100,20)")
connection.execute("insert into hotel2 values(3,'chocos',1000,30)")

print("all data in food table\n")

#create a cousor object for select query
cursor=connection.execute("select find,fname from hotel2")

#dislay all data from hotel table
for row in cursor:
    print(row)
