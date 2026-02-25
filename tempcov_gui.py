import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        # Update the read-only field
        result_var.set(f"{fahrenheit:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x150")

tk.Label(root, text="Celsius:").grid(row=0, column=0, padx=10, pady=10)
celsius_entry = tk.Entry(root)
celsius_entry.grid(row=0, column=1)

tk.Button(root, text="Convert to Fahrenheit", command=convert_temperature).grid(row=1, column=0, columnspan=2, pady=10)

tk.Label(root, text="Fahrenheit:").grid(row=2, column=0, padx=10, pady=10)
result_var = tk.StringVar()
# state='readonly' prevents user typing
result_entry = tk.Entry(root, textvariable=result_var, state='readonly') 
result_entry.grid(row=2, column=1)

if __name__ == "__main__":
    root.mainloop()
