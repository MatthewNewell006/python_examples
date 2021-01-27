import tkinter as tk

window = tk.Tk()

label = tk.Label(text = 'Hello, Tkinter', foreground = 'white', background = 'blue', width = 10, height = 10) # Can also use hexidecimal color codes
label.pack()

button = tk.Button(text = 'Click Me', width = 25, height = 5, fg = 'black', bg = 'blue')
button.pack()

window.mainloop() # This executes the code so the window appears
