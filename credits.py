import tkinter as tk

#Main function to create the credit menu
def show_credits():
    credits_window = tk.Tk()
    credits_window.title("Credits")
       
    title_label = tk.Label(credits_window, text="Credits", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)

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
    
    
    close_button = tk.Button(credits_window, text="Close", command=credits_window.destroy)
    close_button.pack(pady=10)
    
    credits_window.mainloop()

def main():

    show_credits()

if __name__ == "__main__":
    main()
