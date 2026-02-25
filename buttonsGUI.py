import tkinter as tk

def clear_action():
    display_label.config(text="")
    clear_btn.config(state=tk.DISABLED)
    restore_btn.config(state=tk.NORMAL)

def restore_action():
    display_label.config(text="Python GUI Demo")
    restore_btn.config(state=tk.DISABLED)
    clear_btn.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Clear & Restore Demo")
root.geometry("300x150")

display_label = tk.Label(root, text="Python GUI Demo", font=("Arial", 14))
display_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

clear_btn = tk.Button(button_frame, text="Clear", command=clear_action)
clear_btn.pack(side=tk.LEFT, padx=10)

restore_btn = tk.Button(button_frame, text="Restore", state=tk.DISABLED, command=restore_action)
restore_btn.pack(side=tk.LEFT, padx=10)

if __name__ == "__main__":
    root.mainloop()
