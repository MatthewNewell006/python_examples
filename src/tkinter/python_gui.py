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



from tkinter import *

top = Tk()
L1 = Label(top, text = "User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)

top.mainloop()
