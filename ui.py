import sqlite3
from tkinter import *
from tkinter import messagebox

# Database setup
def setup_database():
    
    conn = sqlite3.connect('college_fest.sql')
    cursor = conn.cursor()
    
    # Creating tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE)''')
                        
    cursor.execute('''CREATE TABLE IF NOT EXISTS events (
                        id INTEGER PRIMARY KEY,
                        event_name TEXT NOT NULL,
                        event_date TEXT)''')
                        
    cursor.execute('''CREATE TABLE IF NOT EXISTS registrations (
                        id INTEGER PRIMARY KEY,
                        student_id INTEGER,
                        event_id INTEGER,
                        FOREIGN KEY (student_id) REFERENCES students (id),
                        FOREIGN KEY (event_id) REFERENCES events (id))''')
    conn.commit()
    conn.close()

# Add student to the database
def add_student():
    name = entry_name.get()
    email = entry_email.get()
    
    if not name or not email:
        messagebox.showwarning("Input Error", "Please fill all fields")
        return
    
    conn = sqlite3.connect('college_fest.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists.")
    conn.close()

# Register a student for an event
def register_for_event():
    student_id = entry_student_id.get()
    event_id = entry_event_id.get()
    
    if not student_id or not event_id:
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    conn = sqlite3.connect('college_fest.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO registrations (student_id, event_id) VALUES (?, ?)", (student_id, event_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Registration successful!")

# Create the Tkinter window
root = Tk()
root.title("College Fest Management System")

# Set up Database
setup_database()

# Student Registration Section
Label(root, text="Student Registration", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5, sticky=E)
entry_name = Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5, sticky=E)
entry_email = Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

Button(root, text="Add Student", command=add_student).grid(row=3, columnspan=2, pady=10)

# Event Registration Section
Label(root, text="Event Registration", font=("Arial", 14)).grid(row=4, columnspan=2, pady=10)

Label(root, text="Student ID").grid(row=5, column=0, padx=10, pady=5, sticky=E)
entry_student_id = Entry(root)
entry_student_id.grid(row=5, column=1, padx=10, pady=5)

Label(root, text="Event ID").grid(row=6, column=0, padx=10, pady=5, sticky=E)
entry_event_id = Entry(root)
entry_event_id.grid(row=6, column=1, padx=10, pady=5)

Button(root, text="Register for Event", command=register_for_event).grid(row=7, columnspan=2, pady=10)

root.mainloop()