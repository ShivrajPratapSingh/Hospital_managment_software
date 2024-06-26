import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

filename = 'doctor_info.csv'  # The CSV file name where data will be stored

parameters = [
    'doctor_id', 
    'name', 
    'phone No.', 
    'Email ID',
    'Emergency Contact',
    ]




# Function to create CSV file if it doesn't exist
def create_csv():
    if not os.path.isfile(filename):  # Check if the file already exists
        df = pd.DataFrame(columns=parameters)  # Create a DataFrame with the specified columns
        df.to_csv(filename, index=False)  # Save the DataFrame to a CSV file

# Function to load data from CSV
def load_data():
    create_csv()  # Ensure the CSV file exists
    return pd.read_csv(filename)  # Load and return the data from the CSV file

# Function to save data to CSV
def save_data(data):
    data.to_csv(filename, index=False)  # Save the DataFrame to the CSV file

# Function to handle submission of new data
def submit_data(entries, window, tree):
    new_data = pd.DataFrame([entries])  # Create a new DataFrame with the submitted data
    df = load_data()  # Load existing data
    df = pd.concat([df, new_data], ignore_index=True)  # Append the new data to the existing data
    save_data(df)  # Save the updated data back to the CSV file
    messagebox.showinfo("Success", "Data saved successfully!")  # Show success message
    window.destroy()  # Close the input form
    refresh_treeview(tree)  # Refresh the Treeview to show the updated data

# Function to open input form for new data entry
def open_input_form(tree):
    input_window = tk.Toplevel()  # Create a new top-level window
    input_window.title("Input Doctor Mental Health Data")  # Set the title of the window

    entries = {}  # Dictionary to store entries
    for param in parameters:  # Loop through each parameter
        row = tk.Frame(input_window)  # Create a new frame for each parameter
        row.pack(pady=5)  # Add some padding around the frame
        label = tk.Label(row, text=param, width=20, anchor='w')  # Create a label for the parameter
        label.pack(side=tk.LEFT)  # Pack the label to the left
        entry = tk.Entry(row, width=30)  # Create an entry widget for the parameter
        entry.pack(side=tk.RIGHT, padx=5)  # Pack the entry to the right with some padding
        entries[param] = entry  # Add the entry to the dictionary

    submit_button = tk.Button(input_window, text='Submit', command=lambda: submit_data({param: entry.get() for param, entry in entries.items()}, input_window, tree))
    submit_button.pack(pady=10)  # Pack the submit button with some padding

# Function to open edit form for selected data entry
def open_edit_form(tree):
    selected_item = tree.focus()  # Get the selected item in the Treeview
    if not selected_item:
        messagebox.showerror("Error", "Please select an entry to edit.")  # Show error message if no item is selected
        return

    edit_window = tk.Toplevel()  # Create a new top-level window
    edit_window.title("Edit Doctor Mental Health Data")  # Set the title of the window

    selected_index = int(tree.item(selected_item)['text'])  # Get the index of the selected entry
    entries = {}  # Dictionary to store entries
    for i, param in enumerate(parameters):  # Loop through each parameter
        row = tk.Frame(edit_window)  # Create a new frame for each parameter
        row.pack(pady=5)  # Add some padding around the frame
        label = tk.Label(row, text=param, width=20, anchor='w')  # Create a label for the parameter
        label.pack(side=tk.LEFT)  # Pack the label to the left
        entry = tk.Entry(row, width=30)  # Create an entry widget for the parameter
        entry.insert(0, tree.item(selected_item)['values'][i])  # Insert the current value into the entry
        entry.pack(side=tk.RIGHT, padx=5)  # Pack the entry to the right with some padding
        entries[param] = entry  # Add the entry to the dictionary

    save_button = tk.Button(edit_window, text='Save', command=lambda: save_edit_data(entries, selected_index, edit_window, tree))
    save_button.pack(pady=10)  # Pack the save button with some padding

# Function to delete selected data entry
def delete_data(tree):
    selected_item = tree.focus()  # Get the selected item in the Treeview
    if not selected_item:
        messagebox.showerror("Error", "Please select an entry to delete.")  # Show error message if no item is selected
        return

    if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this entry?"):  # Confirm deletion
        selected_index = int(tree.item(selected_item)['text'])  # Get the index of the selected entry
        data = load_data()  # Load existing data
        data = data.drop(index=selected_index)  # Drop the selected entry
        save_data(data)  # Save the updated data back to the CSV file
        messagebox.showinfo("Success", "Entry deleted successfully!")  # Show success message
        refresh_treeview(tree)  # Refresh the Treeview to show the updated data

# Function to save edited data
def save_edit_data(entries, index, window, tree):
    data = load_data()  # Load existing data
    for param, entry in entries.items():  # Loop through each entry
        data.at[index, param] = entry.get()  # Update the data
    save_data(data)  # Save the updated data back to the CSV file
    messagebox.showinfo("Success", "Data updated successfully!")  # Show success message
    window.destroy()  # Close the edit form
    refresh_treeview(tree)  # Refresh the Treeview to show the updated data

# Function to refresh Treeview with updated data
def refresh_treeview(tree):
    data = load_data()  # Load existing data
    tree.delete(*tree.get_children())  # Clear the Treeview
    for index, row in data.iterrows():  # Loop through each row in the data
        tree.insert("", "end", text=index, values=list(row))  # Insert the row into the Treeview

# Main function to create the main menu
def main():
    root = tk.Tk()  # Create the main window
    root.title("Hospital Management System")  # Set the title of the window

    menu_frame = tk.Frame(root)  # Create a frame for the menu
    menu_frame.pack(pady=20)  # Pack the frame with some padding

    input_button = tk.Button(menu_frame, text="Input Data", command=lambda: open_input_form(tree))
    input_button.grid(row=0, column=0, padx=10)  # Create and pack the input button

    edit_button = tk.Button(menu_frame, text="Edit Data", command=lambda: open_edit_form(tree))
    edit_button.grid(row=0, column=1, padx=10)  # Create and pack the edit button

    delete_button = tk.Button(menu_frame, text="Delete Data", command=lambda: delete_data(tree))
    delete_button.grid(row=0, column=2, padx=10)  # Create and pack the delete button

    # Treeview for displaying data
    tree_frame = tk.Frame(root)  # Create a frame for the Treeview
    tree_frame.pack(pady=20)  # Pack the frame with some padding

    tree = ttk.Treeview(tree_frame, columns=parameters, show='headings')  # Create the Treeview
    for col in parameters:  # Loop through each parameter
        tree.heading(col, text=col)  # Set the heading for the column
        tree.column(col, width=150, anchor='center')  # Set the column properties

    refresh_treeview(tree)  # Initial refresh of Treeview

    tree.pack(expand=True, fill='both')  # Pack the Treeview

    root.mainloop()  # Start the Tkinter main loop

if __name__ == "__main__":
    main()
