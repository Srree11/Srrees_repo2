import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = task_list.curselection()
        task_list.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_all():
    task_list.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

# Create task list
task_list = tk.Listbox(root, width=50)
task_list.pack(pady=10)

# Create task entry
task_entry = tk.Entry(root, font=("Helvetica", 12))
task_entry.pack(pady=5)

# Create buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_all)
clear_button.grid(row=0, column=2)

root.mainloop()