import sqlite3

# Function to initialize the database and create a contacts table
def initialize_database():
    conn = sqlite3.connect('contact_book.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            phone TEXT,
            email TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Function to add a new contact
def add_contact(name, address, phone, email):
    conn = sqlite3.connect('contact_book.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO contacts (name, address, phone, email) VALUES (?, ?, ?, ?)', (name, address, phone, email))

    conn.commit()
    conn.close()

    print(f"Contact {name} added successfully!")

# Function to list all contacts
def list_contacts():
    conn = sqlite3.connect('contact_book.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()

    if not contacts:
        print("No contacts found.")
    else:
        print("\nList of Contacts:")
        print("ID    Name        Address           Phone           Email  ")                                                              
        for contact in contacts:
            print(f"{contact[0]},{contact[1]},{contact[2]},{contact[3]}, {contact[4]}")

    conn.close()

# Function to update contact information
def update_contact(contact_id, new_name, new_address, new_phone, new_email):
    conn = sqlite3.connect('contact_book.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE contacts
        SET name=?, address=?, phone=?, email=?
        WHERE id=?
    ''', (new_name, new_address, new_phone, new_email, contact_id))

    conn.commit()
    conn.close()

    print(f"Contact with ID {contact_id} updated successfully!")

# Function to delete a contact
def delete_contact(contact_id):
    conn = sqlite3.connect('contact_book.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM contacts WHERE id=?', (contact_id,))

    conn.commit()
    conn.close()

    print(f"Contact with ID {contact_id} deleted successfully!")

# Main function to interact with the user
def insert_data():
    initialize_database()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            add_contact(name, address, phone, email)

        elif choice == '2':
             list_contacts()

        elif choice == '3':
             contact_id = input("Enter Contact ID to update: ")
             new_name = input("Enter New Name: ")
             new_address = input("Enter New Address: ")
             new_phone = input("Enter New Phone: ")
             new_email = input("Enter New Email: ")
             update_contact(contact_id, new_name, new_address, new_phone, new_email)

        elif choice == '4':
            contact_id = input("Enter Contact ID to delete: ")
            delete_contact(contact_id)

        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

insert_data()






