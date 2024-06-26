import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import input_parameters as ip
import analysis as an
import credits
import registor  as rs
def solution():
    pass
def  registor():
    rs.main()
def situation():
    ip.main()


def analysis():
    file_path = 'doctor_mental_health.csv'  # Path to your CSV file

    an.run_mental_health_app(file_path)

def credit():
    credits.main()
# Initialize the main window
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("800x600")
root.resizable(False, False)

# Apply a modern theme
style = ttk.Style()
style.theme_use('clam')  # Use the 'clam' theme for a modern look

# Frame for the header (logo and title)
header_frame = ttk.Frame(root)
header_frame.pack(pady=20)

# Load and display the logo
logo_path = "logo.png"  # replace with your logo file path
try:
    logo_image = Image.open(logo_path)
    logo_image = logo_image.resize((150, 150), Image.Resampling.LANCZOS)  # Updated attribute
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = ttk.Label(header_frame, image=logo_photo)
    logo_label.image = logo_photo  # keep a reference to avoid garbage collection
    logo_label.pack(side=tk.LEFT, padx=10)
except Exception as e:
    print(f"Error loading logo: {e}")

# Title Label
title_label = ttk.Label(header_frame, text="Hospital Management System", font=("Helvetica", 24, "bold"))
title_label.pack(side=tk.LEFT, padx=10)

# Frame for buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

# Button styling
style.configure("TButton", font=("Helvetica", 16), padding=10)

# Buttons
buttons = [
    ("Registor Doctors", registor),
    ("Situation Of Doctors", situation),
    ("Mental Analysis", analysis),
    ("Made By",credit),
    

  
]

for text, command in buttons:
    button = ttk.Button(button_frame, text=text, command=command)
    button.pack(pady=10, fill='x', expand=True)

# Run the application
root.mainloop()
