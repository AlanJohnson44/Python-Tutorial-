import tkinter as tk
import re

def check_strength():
    password = pwd_entry.get()
    
    # Conditions
    has_length = len(password) >= 8
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    score = has_length + has_digit + has_special
    
    if score == 3:
        result_label.config(text="Strength: Strong", fg="green")
    elif score == 2:
        result_label.config(text="Strength: Moderate", fg="orange")
    else:
        result_label.config(text="Strength: Weak", fg="red")

root = tk.Tk()
root.title("Password Checker")
root.geometry("300x150")

tk.Label(root, text="Enter Password:").pack(pady=5)
pwd_entry = tk.Entry(root, show="*")
pwd_entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_strength).pack(pady=5)

result_label = tk.Label(root, text="Strength: ", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

if __name__ == "__main__":
    root.mainloop()
