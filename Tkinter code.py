import tkinter as tk
from tkinter import messagebox

def add_student():
    email = email_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    course_id = course_id_entry.get()
    grade = grade_entry.get()
    
    if email and first_name and last_name and course_id and grade:
        messagebox.showinfo("Success", f"Student {first_name} {last_name} added!")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

def logout():
    root.destroy()

# Initialize main window
root = tk.Tk()
root.title("Dashboard - CheckMyGrade")
root.geometry("400x400")

tk.Label(root, text="Dashboard", font=("Arial", 16)).pack()
tk.Button(root, text="Logout", command=logout).pack()

# Student Management Section
tk.Label(root, text="Student Management", font=("Arial", 14)).pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="First Name:").pack()
first_name_entry = tk.Entry(root)
first_name_entry.pack()

tk.Label(root, text="Last Name:").pack()
last_name_entry = tk.Entry(root)
last_name_entry.pack()

tk.Label(root, text="Course ID:").pack()
course_id_entry = tk.Entry(root)
course_id_entry.pack()

tk.Label(root, text="Grade:").pack()
grade_entry = tk.Entry(root)
grade_entry.pack()

tk.Button(root, text="Add Student", command=add_student).pack()

root.mainloop()
