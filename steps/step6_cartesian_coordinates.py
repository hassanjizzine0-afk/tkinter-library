import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Пример - Декартовы координаты")
root.geometry("400x300")

# Create the box
coord_frame = ttk.LabelFrame(root, text="Декартовы координаты")
coord_frame.pack(padx=10, pady=10, fill="x")

# X input
ttk.Label(coord_frame, text="X:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
x_entry = ttk.Entry(coord_frame)
x_entry.grid(row=0, column=1, padx=5, pady=5)

# Y input
ttk.Label(coord_frame, text="Y:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
y_entry = ttk.Entry(coord_frame)
y_entry.grid(row=1, column=1, padx=5, pady=5)

# Z input
ttk.Label(coord_frame, text="Z:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
z_entry = ttk.Entry(coord_frame)
z_entry.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()