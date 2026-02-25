import tkinter as tk
from tkinter import messagebox

def generate_bill():
    try:
        price = float(price_entry.get())
        quantity = int(qty_entry.get())
        
        total = price * quantity
        
        # Apply 10% discount if over 1000
        if total > 1000:
            total = total - (total * 0.10)
            
        result_var.set(f"Final Amount: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Price must be a number and Quantity must be an integer.")

root = tk.Tk()
root.title("Billing System")
root.geometry("250x200")

tk.Label(root, text="Item Price:").pack(pady=2)
price_entry = tk.Entry(root)
price_entry.pack(pady=2)

tk.Label(root, text="Quantity:").pack(pady=2)
qty_entry = tk.Entry(root)
qty_entry.pack(pady=2)

tk.Button(root, text="Generate Bill", command=generate_bill).pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold"), fg="blue")
result_label.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()
