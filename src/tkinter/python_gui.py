import tkinter as tk

window = tk.Tk()
label = tk.Label(text = 'Name')
entry = tk.Entry()

label.pack()
entry.pack()

name = entry.get()
name

entry.delete(0)

window.mainloop()

