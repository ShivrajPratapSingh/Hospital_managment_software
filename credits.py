import tkinter as tk

def show_credits():
    # Create the main Tkinter window
    credits_window = tk.Tk()
    credits_window.title("Credits")
    
    # Add a label for the title
    title_label = tk.Label(credits_window, text="Credits", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)
    
    # Add the credits information
    credits_text = """
    Project Title: Mental Health Evaluation of Doctors

    Developed by:
    - Developer 1: SHIVRAJ PRATAP SINGH
    - Developer 2: NEEV DiVAN
    - Developer 3: AADI KOHAR

    Acknowledgements:
    We would like to thank everyone who supported us during this project.
    """
    
    credits_label = tk.Label(credits_window, text=credits_text, justify="left")
    credits_label.pack(pady=10)
    
    # Add a button to close the credits window
    close_button = tk.Button(credits_window, text="Close", command=credits_window.destroy)
    close_button.pack(pady=10)
    
    # Run the Tkinter event loop for the credits window
    credits_window.mainloop()

def main():
    # Call show_credits to display the credits directly
    show_credits()

if __name__ == "__main__":
    main()
