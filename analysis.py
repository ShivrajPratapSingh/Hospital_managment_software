import csv
import os
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from datetime import datetime

# Function to load the data from multiple CSV files
def load_data_from_files(base_filename):
    data = {}
    for filename in os.listdir():
        if filename.startswith(base_filename) and filename.endswith('.csv'):
            date_str = filename.replace(base_filename, '').replace('.csv', '')
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            with open(filename, mode='r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    doctor_id = row['doctor_id']
                    if doctor_id not in data:
                        data[doctor_id] = []
                    row['date'] = date
                    data[doctor_id].append(row)
    return data

# Function to calculate individual parameter scores
def calculate_parameter_scores(data):
    parameter_columns = ['stress_level', 'workload', 'sleep_quality', 
                         'physical_activity', 'support_system', 
                         'nutrition', 'job_satisfaction', 
                         'anxiety_level', 'depression_level', 
                         'burnout_level']
    
    scores = []
    for row in data:
        score = [float(row[col]) for col in parameter_columns if col in row]
        scores.append(score)
    return scores

# Function to calculate overall rating
def calculate_overall_rating(parameter_scores):
    overall_ratings = []
    for scores in parameter_scores:
        if scores: 
            overall_rating = sum(scores) / len(scores) * 10 
        else:
            overall_rating = 0
        overall_ratings.append(overall_rating)
    return overall_ratings

# Function to plot doctor scores over time
def plot_doctor_scores(doctor_data, doctor_id):
    dates = [row['date'] for row in doctor_data]
    scores = calculate_parameter_scores(doctor_data)
    
    overall_ratings = calculate_overall_rating(scores)
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, overall_ratings, marker='o')
    plt.title(f'Mental Health Ratings Over Time for Doctor ID {doctor_id}')
    plt.xlabel('Date')
    plt.ylabel('Overall Rating')
    plt.xticks(rotation=45)
    plt.ylim(0, 100) 
    plt.grid()
    plt.tight_layout()
    plt.show()

# Function to display the overall rating and plot data
def display_rating():
    selected_doctor = doctor_combobox.get()
    if selected_doctor:
        doctor_data = data.get(selected_doctor, [])
        if doctor_data:
            plot_doctor_scores(doctor_data, selected_doctor)
        else:
            messagebox.showerror("Error", "No data found for Doctor ID!")
    else:
        messagebox.showerror("Error", "Please select a Doctor ID!")

# Function to run the Tkinter application
def run_mental_health_app(base_filename):
    global data, doctor_combobox

    data = load_data_from_files(base_filename)

    root = tk.Tk()
    root.title("Doctor Mental Health Rating")

    label = tk.Label(root, text="Select Doctor ID:")
    label.pack(pady=10)

    doctor_combobox = ttk.Combobox(root)
    if data:
        doctor_combobox['values'] = list(data.keys())
    doctor_combobox.pack(pady=10)

    button = tk.Button(root, text="Display Rating", command=display_rating)
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    base_filename = 'doctor_mental_health_'  # Base filename without date
    run_mental_health_app(base_filename)
