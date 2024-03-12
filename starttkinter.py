import tkinter as tk
import sqlite3
root=tk.Tk()

def insertdata():
##    id=entry_id.get()
##    name=entry_name.get()
##    dob=entry_dob.get()
##    Mobileno=entry_Mobileno.get()
##
##    cursor.execute('INSERT INTO your_table_name (id,name,dob,Mobileno) VALUES (?,?,?,?)', (id,name,dob,Mobileno))
##    conn.commit()
    # Create Tkinter window
    root = tk.Tk()
    root.title("Data Entry with Tkinter")

    # Connect to SQLite database
    conn = sqlite3.connect('project2.db')
    cursor = conn.cursor()

     # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS project2 (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')

    # Create and pack Tkinter widgets
    label_name = tk.Label(root, text="Name:")
    entry_name = tk.Entry(root)

    label_age = tk.Label(root, text="Age:")
    entry_age = tk.Entry(root)

    #insert_button = tk.Button(root, text="Insert Data", command=insert_data)

    label_name.pack()
    entry_name.pack()
    label_age.pack()
    entry_age.pack()
    insert_button.pack()

    # Run Tkinter event loop
    root.mainloop()

    # Close the database connection when the application exits
    conn.close()


     # Optional: Clear entry fields after inserting data
    entry_id.delete(0,tk.END)
    entry_name.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_Mobilno.delete(0, tk.END)
    
#main file

#create a button
button=tk.Button(root,text="ADD",command=insertdata)
button1=tk.Button(root,text="Find")
button.pack()
button1.pack()

#run the tkinter event loop
root.mainloop()

