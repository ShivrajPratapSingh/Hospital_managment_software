import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime

base_filename = 'doctor_mental_health_' 
parameters = [
    'doctor_id', 
    'name', 
    'stress_level', 
    'workload', 
    'sleep_quality', 
    'physical_activity', 
    'support_system', 
    'nutrition', 
    'job_satisfaction', 
    'anxiety_level', 
    'depression_level', 
    'burnout_level'
]

current_date = datetime.now().date()
# Function to get the filename for the current date
def get_filename(date):
    return f"{base_filename}{date}.csv"

# Function to create CSV file if it doesn't exist
def create_csv(date):
    filename = get_filename(date)
    if not os.path.isfile(filename):
        with open(filename, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(parameters)

# Function to load data from CSV
def load_data(date):
    create_csv(date)
    filename = get_filename(date)
    with open(filename, mode='r', newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)

# Function to save data to CSV
def save_data(data, date):
    filename = get_filename(date)
    with open(filename, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=parameters)
        writer.writeheader()
        writer.writerows(data)

# Function to refresh Treeview with updated data
def refresh_treeview(tree, date):
    data = load_data(date)
    tree.delete(*tree.get_children())
    for index, row in enumerate(data):
        tree.insert("", "end", text=index, values=list(row.values()))

# Function to handle data submission
def submit_data(entries, window, tree, date):
    new_data = {param: entry.get() for param, entry in entries.items()}
    data = load_data(date)
    data.append(new_data)
    save_data(data, date)
    messagebox.showinfo("Success", "Data saved successfully!")
    window.destroy()
    refresh_treeview(tree, date)

# Function to open input form
def open_input_form(tree, date):
    input_window = tk.Toplevel()
    input_window.title("Input Data")

    entries = {}
    for param in parameters:
        row = tk.Frame(input_window)
        row.pack(pady=5)
        label = tk.Label(row, text=param, width=20, anchor='w')
        label.pack(side=tk.LEFT)
        entry = tk.Entry(row, width=30)
        entry.pack(side=tk.RIGHT, padx=5)
        entries[param] = entry

    submit_button = tk.Button(input_window, text='Submit', command=lambda: submit_data(entries, input_window, tree, date))
    submit_button.pack(pady=10)

# Function to update the date and refresh the Treeview
def update_date(tree, date_entry):
    global current_date
    date_str = date_entry.get()
    try:
        current_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        refresh_treeview(tree, current_date)
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")

# Main function to create the main menu
def main():
    global current_date
    root = tk.Tk()
    root.title("Hospital Management System")
    menu_frame = tk.Frame(root)
    menu_frame.pack(pady=20)
    date_label = tk.Label(menu_frame, text="Select Date (YYYY-MM-DD):")
    date_label.grid(row=0, column=0)

    date_entry = tk.Entry(menu_frame, width=15)
    date_entry.insert(0, str(current_date))
    date_entry.grid(row=0, column=1)

    update_button = tk.Button(menu_frame, text="Update Date", command=lambda: update_date(tree, date_entry))
    update_button.grid(row=0, column=2)

    input_button = tk.Button(menu_frame, text="Input Data", command=lambda: open_input_form(tree, current_date))
    input_button.grid(row=1, column=0, padx=10)

    tree_frame = tk.Frame(root)
    tree_frame.pack(pady=20)

    tree = ttk.Treeview(tree_frame, columns=parameters, show='headings')
    for col in parameters:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor='center')

    refresh_treeview(tree, current_date)
    tree.pack(expand=True, fill='both')
    root.mainloop()

if __name__ == "__main__":
    main()
