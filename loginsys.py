
import tkinter as tk
from tkinter import messagebox

def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    
    if not username or not password:
        messagebox.showwarning("Warning", "Username and password cannot be empty!")
    elif username == "admin" and password == "1234":  # Hardcoded valid credentials for testing
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid credentials. Try admin / 1234.")

root = tk.Tk()
root.title("Login Screen")
root.geometry("250x150")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_btn = tk.Button(root, text="Login", command=handle_login)
login_btn.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()
