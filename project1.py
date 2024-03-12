####import sqlite3
####comm=sqlite3.connect('BJSR.DB')
####print("opened database succesfully")
####comm.execute('''Create table project1
####(id int primary key not null,
####name character(20) not null,
####dob date not null,
####MobileNo bigint not null);''')
####print("Table create succesfully")
##
##import tkinter as tk
##import sqlite3
##
##conn=sqlite3.connect('project1.db')
##def on_button_click():
##
##        name = entry2.get()
##        print("User entered:", name)
##
##        address=entry3.get()
##        print("user entered Name:",address)
##
##        phone = entry4.get()
##        print("User entered:", phone)
##
##        email=entry5.get()
##        print("user entered Name:",email)
##
##
##        #user
##def ADD():
##    # Create the main window
##    root = tk.Tk()
##    root.title("User Input Example")
##    # Create a Label widget
##    label=tk.Label(root,text="Enter Name")
##    label.pack(pady=10)
##    entry2 = tk.Entry(root)
##    entry2.pack(pady=10)
##    label=tk.Label(root,text="Enter Address")
##    label.pack(pady=10)
##    entry3 = tk.Entry(root)
##    entry3.pack(pady=10)
##    label=tk.Label(root,text="Enter Phone")
##    label.pack(pady=10)
##    entry4 = tk.Entry(root)
##    entry4.pack(pady=10)
##    label = tk.Label(root, text="Enter Email.:")
##    label.pack(pady=10)
##    entry5 = tk.Entry(root)
##    entry5.pack(pady=10)
##
##    print("user entered Name:",entry5)
##
##    button2 = tk.Button(root, text="Print", command=on_button_click)
##    button2.pack()
##    
##    # Create an Entry widget for text input
####    entry = tk.Entry(root)
####    entry.pack(pady=10)
##    root.mainloop()
##
##
##
## #Create the main window
##window = tk.Tk()
##
## #Create a button
##button1 = tk.Button(window, text="New User!", command=ADD)
####button2 = tk.Button(window, text="List Contact!", command=on_button_click)
####button3 = tk.Button(window, text="Update Contact!", command=Update)
####button4 = tk.Button(window, text="Delete Contact!", command=on_button_click)
####button5 = tk.Button(window, text="Exit!", command=on_button_click)
##
## #Pack the button into the window
##button1.pack()
####button2.pack()
####button3.pack()
####button4.pack()
####button5.pack()
##
##
### Start the main event loop
##window.mainloop()
#
import sqlite3
import tkinter as tk
from tkinter import messagebox

# Create a SQLite database and table
conn = sqlite3.connect('contact_book.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        address TEXT,
        phone TEXT,
        email TEXT
    )
''')
conn.commit()

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone:  # Check if name and phone are provided
        conn.execute('''
            INSERT INTO contacts (name, address, phone, email)
            VALUES (?, ?, ?, ?)
        ''', (name, address, phone, email))
        conn.commit()
        messagebox.showinfo("Contact Book", "Contact added successfully")
        clear_entries()
        display_contacts()
    else:
        messagebox.showwarning("Contact Book", "Name and Phone are required")

# Function to display contacts in the listbox
def display_contacts():
    contacts_listbox.delete(0, tk.END)
    for row in conn.execute('SELECT * FROM contacts'):
        contacts_listbox.insert(tk.END, f"{row[1]} - {row[3]}")

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Create and place entry widgets
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

tk.Label(root, text="Address:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
address_entry = tk.Entry(root)
address_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

tk.Label(root, text="Phone:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

# Create and place buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=3, pady=10)

# Create and place listbox to display contacts
contacts_listbox = tk.Listbox(root, width=40, height=10)
contacts_listbox.grid(row=5, column=0, columnspan=3, pady=5)

# Display initial contacts
display_contacts()

# Run the Tkinter main loop
root.mainloop()

# Close the SQLite connection when the GUI is closed
conn.close()




