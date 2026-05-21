import tkinter as tk

# Create main window
root = tk.Tk()
root.title("My First GUI")
root.geometry("400x300")

# Create a label (text display)
label = tk.Label(root, text="Hello! Thisdf

# Place the label in the window
label.pack()                                         #With pack(): The label appears in the window

# Run the program
root.mainloop()
