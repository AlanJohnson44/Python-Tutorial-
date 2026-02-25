import tkinter as tk
from tkinter import messagebox

def perform_operation(op):
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        
        if op == '+': result = num1 + num2
        elif op == '-': result = num1 - num2
        elif op == '*': result = num1 * num2
        elif op == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                messagebox.showerror("Math Error", "Cannot divide by zero!")
                return
                
        output_var.set(str(result))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers.")

root = tk.Tk()
root.title("Calculator")

tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

tk.Button(root, text="Add", command=lambda: perform_operation('+')).grid(row=2, column=0, pady=5)
tk.Button(root, text="Subtract", command=lambda: perform_operation('-')).grid(row=2, column=1, pady=5)
tk.Button(root, text="Multiply", command=lambda: perform_operation('*')).grid(row=2, column=2, pady=5)
tk.Button(root, text="Divide", command=lambda: perform_operation('/')).grid(row=2, column=3, pady=5)

tk.Label(root, text="Result:").grid(row=3, column=0, padx=5, pady=5)
output_var = tk.StringVar()
tk.Entry(root, textvariable=output_var, state='readonly').grid(row=3, column=1, columnspan=3, padx=5, pady=5)

if __name__ == "__main__":
    root.mainloop()
