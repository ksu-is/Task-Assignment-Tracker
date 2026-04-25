import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create the main application window
window = tk.Tk()
window.title("Task/Assignment Tracker")
window.geometry("500x720")

#Title at the top of the window
title_label = tk.Label(window, text="Task/Assignment Tracker", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

# Assignment name
name_label = tk.Label(window, text="Assignment Name:", font=("Arial", 12))
name_label.pack()
name_entry = tk.Entry(window, font=("Arial", 12), width=30)
name_entry.pack(pady=5)

# Class
class_label = tk.Label(window, text="Class:", font=("Arial", 12))
class_label.pack()
class_entry = tk.Entry(window, font=("Arial", 12), width=30)
class_entry.pack(pady=5)

# Due date
due_label = tk.Label(window, text="Due Date (MM/DD/YYYY):", font=("Arial", 12))
due_label.pack()
due_entry = tk.Entry(window, font=("Arial", 12), width=30)
due_entry.pack(pady=5)

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

# Submit function
def submit():
    name = name_entry.get()
    class_name = class_entry.get()
    due = due_entry.get()
    priority = priority_box.get()
    notes = notes_entry.get()
    type_name = type_box.get()

    # Make sure nothing is empty
    if name == "" or class_name == "" or due == "" or priority == "" or type_name == "":
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        messagebox.showinfo("Success", f"Added: {name}\nType: {type_name}\nNotes: {notes if notes else 'None'}")
        # Clear the fields after submission
        name_entry.delete(0, tk.END)
        class_entry.delete(0, tk.END)
        due_entry.delete(0, tk.END)
        priority_box.set("")
        type_box.set("")
        notes_entry.delete(0, tk.END)

# Submit button
submit_button = tk.Button(window, text="Submit", font=("Arial", 12, "bold"), command=submit)
submit_button.pack(pady=20)

# Start the window
window.mainloop()



