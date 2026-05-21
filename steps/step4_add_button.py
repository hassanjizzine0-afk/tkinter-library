import tkinter as tk

def button_clicked():
    """This function runs when button is clicked"""
    print("Button was clicked!")

root = tk.Tk()
root.title("Button Example")
root.geometry("400x300")

label = tk.Label(root, text="Click the button:")
label.pack()

entry = tk.Entry(root)
entry.pack()

# Create button that calls button_clicked() when pressed
button = tk.Button(root, text="Click Me!", command=button_clicked) #button = tk.Button(parent, text="button text", command=function_name)
button.pack()

root.mainloop()
