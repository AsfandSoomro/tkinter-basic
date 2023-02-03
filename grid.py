from tkinter import *

# Initializing a Tkinter object (A container)
container = Tk()

# Creating a Label Widgets
label = Label(container, text='Hello World')
# Fitting label to the frame with grid() method it has rows and columns
label.grid(row=0, column=0)

# Initializing the event loop or main loop
container.mainloop()