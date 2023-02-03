from tkinter import *

# Initializing a Tkinter object (A container)
container = Tk()

# Creating a Label Widget
label = Label(container, text='Hello World')
# Fitting label to the frame with pack() method
label.pack()

# Initializing the event loop or main loop
container.mainloop()
