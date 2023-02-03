from tkinter import *

# Creating and initializing a container
container = Tk()


def on_click_button():
    label = Label(container, text=f'Hello {e.get()}', borderwidth=5)
    label.pack()


# Creating an entry box widget
e = Entry(container, width=50, fg='#248810')
# Attaching it to the container
e.pack()
e.insert(index=0, string='Enter your name: ')

# Creating a button widget
button = Button(container, text='Click Me', command=on_click_button, fg='#FFFFFF', bg='#248810')
# Attaching it to the container
button.pack()

container.mainloop()
