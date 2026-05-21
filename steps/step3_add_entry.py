import tkinter as tk

root = tk.Tk()
root.title("Input Example")
root.geometry("400x300")

# Create a label
label = tk.Label(root, text="Enter your name:")
label.pack()

# Create an entry field (where user types)
entry = tk.Entry(root)
entry.pack()

# Run
root.mainloop()
