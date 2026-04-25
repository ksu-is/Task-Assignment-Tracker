import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create the main application window
window = tk.Tk()
window.title("Task/Assignment Tracker")
window.geometry("500x720")

# Counter variable to keep track of the number of assignments added
counter = 0

# Creating a placeholder text for the entry fields
def add_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg='gray')

    def on_click(event):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def on_leave(event):
        if entry.get() == '':
            entry.insert(0, placeholder_text)
            entry.config(fg='gray')

    entry.bind("<FocusIn>", on_click)
    entry.bind("<FocusOut>", on_leave)

# Create a function to make sure the date is valid
def is_valid_date(date_str):
    # Check it's not empty or placeholder
    if date_str == "" or date_str == "e.g. 4/27/2026":
        return False

    # Split by "/" and check we get exactly 3 parts
    parts = date_str.split("/")
    if len(parts) != 3:
        return False

    # Check each part is a number
    for part in parts:
        if not part.isdigit():
            return False

    # Pull out month, day, year
    month = int(parts[0])
    day   = int(parts[1])
    year  = int(parts[2])

    # Check ranges make sense
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if year < 2000 or year > 2100:
        return False

    return True
#Title at the top of the window
title_label = tk.Label(window, text="Task/Assignment Tracker", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

# Assignment name
name_label = tk.Label(window, text="Assignment Name:", font=("Arial", 12))
name_label.pack()
name_entry = tk.Entry(window, font=("Arial", 12), width=30)
name_entry.pack(pady=5)
add_placeholder(name_entry, "e.g. Math Homework 5")

# Class
class_label = tk.Label(window, text="Class:", font=("Arial", 12))
class_label.pack()
class_entry = tk.Entry(window, font=("Arial", 12), width=30)
class_entry.pack(pady=5)
add_placeholder(class_entry, "e.g. Math 101")

# Due date
due_label = tk.Label(window, text="Due Date (MM/DD/YYYY):", font=("Arial", 12))
due_label.pack()
due_entry = tk.Entry(window, font=("Arial", 12), width=30)
due_entry.pack(pady=5)
add_placeholder(due_entry, "e.g. 4/27/2026")

#Type of assignment dropdown
type_label = tk.Label(window, text="Assignment Type:", font=("Arial", 12))
type_label.pack()
type_box = ttk.Combobox(window, values=["Homework", "Quiz", "Exam", "Project", "Lab", "Paper", "Reading", "Other"], font=("Arial", 12), width=28, state="readonly")
type_box.pack(pady=5)

# Priority dropdown
priority_label = tk.Label(window, text="Priority:", font=("Arial", 12))
priority_label.pack()
priority_box = ttk.Combobox(window, values=["Low", "Medium", "High"], font=("Arial", 12), width=28, state="readonly")
priority_box.pack(pady=5)

# Notes
notes_label = tk.Label(window, text="Notes (Optional):", font=("Arial", 12))
notes_label.pack()
notes_entry = tk.Entry(window, font=("Arial", 12), width=30)
notes_entry.pack(pady=5)
add_placeholder(notes_entry, "e.g. Chapters 5-7")

# Submit function
def submit():
    global counter

    name = name_entry.get()
    class_name = class_entry.get()
    due = due_entry.get()
    priority = priority_box.get()
    notes = notes_entry.get()
    if notes == "e.g. Chapters 5-7":
        notes = ""
    type_name = type_box.get()

    # Make sure nothing is empty
    if name == "" or name == "e.g. Math Homework 5" or class_name == "" or class_name == "e.g. Math 101" or due == "" or due == "e.g. 4/27/2026" or priority == "" or type_name == "":
        messagebox.showerror("Error", "Please fill in all fields.")
    elif not is_valid_date(due):
        messagebox.showerror("Invalid Date", "Please enter a valid date in MM/DD/YYYY format.")
    else:
        messagebox.showinfo("Success", f"Added: {name}\nType: {type_name}\nNotes: {notes if notes else 'None'}")
        # Clear the fields after submission
        name_entry.delete(0, tk.END)
        class_entry.delete(0, tk.END)
        due_entry.delete(0, tk.END)
        priority_box.set("")
        type_box.set("")
        notes_entry.delete(0, tk.END)
        # Increment the counter and update the label
        counter += 1
        counter_label.config(text=f"Assignments Added: {counter}")

# Counter label
counter_label = tk.Label(window, text=f"Assignments Added: 0", font=("Arial", 11), fg="gray")
counter_label.pack(pady=5)

# Submit button
submit_button = tk.Button(window, text="Submit", font=("Arial", 12, "bold"), command=submit)
submit_button.pack(pady=20)

# Start the window
window.mainloop()



