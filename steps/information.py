import tkinter
import tkinter.ttk as ttk

# See all modules in tkinter
print(dir(tkinter))

# See all classes in tkinter module
print([item for item in dir(tkinter) if not item.startswith('_')])

# See all classes in ttk module
print([item for item in dir(ttk) if not item.startswith('_')])

# See all methods of a specific class
print(dir(tkinter.Tk))  # Methods of Tk class
print(dir(ttk.LabelFrame))  # Methods of LabelFrame class