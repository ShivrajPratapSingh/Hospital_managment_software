import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import input_parameters as ip
import analysis as an
import credits


def situation():
    ip.main()


def analysis():
    base_filename = 'doctor_mental_health_'

    data = an.load_data_from_files('doctor_mental_health_')
    an.run_mental_health_app(base_filename)

def credit():
    credits.main()


root = tk.Tk()
root.title("Hospital Management System")
root.geometry("800x800")
root.resizable(True, True)



style = ttk.Style()
style.theme_use('clam') 



header_frame = ttk.Frame(root)
header_frame.pack(pady=20)




logo_path = "logo.png" 
try:
    logo_image = Image.open(logo_path)
    logo_image = logo_image.resize((150, 150), Image.Resampling.LANCZOS) 
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = ttk.Label(header_frame, image=logo_photo)
    logo_label.image = logo_photo  
    logo_label.pack(side=tk.LEFT, padx=10)
except Exception as e:
    print(f"Error loading logo: {e}")


title_label = ttk.Label(header_frame, text="Hospital Management System", font=("Helvetica", 24, "bold"))
title_label.pack(side=tk.LEFT, padx=10)

button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

style.configure("TButton", font=("Helvetica", 16), padding=10)


buttons = [
    ("Situation Of Doctors", situation),
    ("Mental Analysis", analysis),
    ("Made By",credit),
 
]
for text, command in buttons:
    button = ttk.Button(button_frame, text=text, command=command)
    button.pack(pady=10, fill='x', expand=True)



root.mainloop()
