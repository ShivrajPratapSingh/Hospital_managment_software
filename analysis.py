import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to load the data from CSV
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        required_columns = ['doctor_id', 'name', 'stress_level', 'workload', 'sleep_quality', 'physical_activity', 'support_system', 'nutrition', 'job_satisfaction', 'anxiety_level', 'depression_level', 'burnout_level']
        
        # Check if all required columns are present
        for col in required_columns:
            if col not in data.columns:
                raise ValueError(f"Missing required column: {col}")
        return data
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

# Function to calculate individual parameter scores
def calculate_parameter_scores(data):
    parameter_columns = ['stress_level', 'workload', 'sleep_quality', 'physical_activity', 'support_system', 'nutrition', 'job_satisfaction', 'anxiety_level', 'depression_level', 'burnout_level']
    parameter_scores = data[parameter_columns]
    return parameter_scores

# Function to calculate overall rating
def calculate_overall_rating(parameter_scores):
    overall_rating = parameter_scores.mean(axis=1) * 10  # Scale the average score to 100
    return overall_rating

# Function to load and process the data
def load_and_process_data(file_path):
    data = load_data(file_path)
    if data is not None:
        parameter_scores = calculate_parameter_scores(data)
        overall_ratings = calculate_overall_rating(parameter_scores)
        data['overall_rating'] = overall_ratings
    return data

# Function to display the overall rating for the selected doctor
def display_rating():
    selected_doctor = doctor_combobox.get()
    if selected_doctor:
        doctor_data = data[data['doctor_id'] == int(selected_doctor)]
        if not doctor_data.empty:
            doctor_name = doctor_data['name'].values[0]
            rating = doctor_data['overall_rating'].values[0]
            messagebox.showinfo("Overall Rating", f"Overall Mental Health Rating for Dr. {doctor_name} (ID: {selected_doctor}): {rating:.2f}/100")
        else:
            messagebox.showerror("Error", "Doctor ID not found!")
    else:
        messagebox.showerror("Error", "Please select a Doctor ID!")

# Function to run the Tkinter application
def run_mental_health_app(file_path):
    global data, doctor_combobox

    # Load and process the data
    data = load_and_process_data(file_path)

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Doctor Mental Health Rating")

    # Create a label for the combobox
    label = tk.Label(root, text="Select Doctor ID:")
    label.pack(pady=10)

    # Create a combobox for selecting doctor IDs
    doctor_combobox = ttk.Combobox(root)
    if data is not None:
        doctor_combobox['values'] = data['doctor_id'].tolist()
    doctor_combobox.pack(pady=10)

    # Create a button to display the rating
    button = tk.Button(root, text="Display Rating", command=display_rating)
    button.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()

# Example usage
if __name__ == "__main__":
    file_path = 'doctor_mental_health.csv'  # Path to your CSV file
    run_mental_health_app(file_path)
