import tkinter as tk

def show_value():
    """Get text from entry and print it"""
    text = entry.get()  # Get what user typed
    print(f"You typed: {text}")

root = tk.Tk()
root.title("Get Input Value")
root.geometry("400x300")

label = tk.Label(root, text="Type something:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Show Value", command=show_value)
button.pack()

root.mainloop()
