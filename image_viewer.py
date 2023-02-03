# Built-in modules
import os
from tkinter import *

# Third-party module
from PIL import Image, ImageTk

# Global Variables
current_image = 0
status_bar = None


def main():
    root = Tk()
    root.title('Asfand\'s Image Viewer App')

    # List of travel images names
    travel_images_list = os.listdir(f'{os.getcwd()}/images/travel/')

    frame = Frame(root, bg='#9F8080')
    frame.grid(row=0, column=0)

    # Contains the list image objects for all the travel images
    my_images = [
        ImageTk.PhotoImage(Image.open(f'./images/travel/{img}').reduce((8, 8))) for img in travel_images_list
    ]
    # Contains the labels as images ready to be attached on the frame
    my_images_labels = [
        Label(frame, image=the_img) for the_img in my_images
    ]

    # Attaching the first image on the frame
    my_images_labels[0].grid(row=0, column=0, columnspan=3)

    # Creating the status bar object
    global status_bar
    status_bar = Label(frame, text=f'1 of {len(my_images_labels)}', bd=3, relief=SUNKEN, anchor=E)

    # Function invokes when the user clicks on backward button
    def backward():
        global current_image
        if current_image == 1:
            my_buttons['backward'] = Button(frame, text='<<', command=backward, state=DISABLED)
            my_buttons['backward'].grid(row=1, column=0)
        my_images_labels[current_image].grid_forget()
        current_image -= 1
        my_images_labels[current_image].grid(row=0, column=0, columnspan=3)
        update_status()

    # Function invoked when the user clicks on the forward button
    def forward():
        global current_image
        if current_image == len(my_images_labels) - 2:
            my_buttons['forward'] = Button(frame, text='>>', command=forward, state=DISABLED)
            my_buttons['forward'].grid(row=1, column=2)
        my_images_labels[current_image].grid_forget()
        current_image += 1
        my_images_labels[current_image].grid(row=0, column=0, columnspan=3)

        my_buttons['backward'] = Button(frame, text='<<', command=backward, state=NORMAL)
        my_buttons['backward'].grid(row=1, column=0)
        update_status()

    def update_status():
        global current_image
        global status_bar
        status_bar.grid_forget()
        status_bar = Label(frame, text=f'{current_image + 1} of {len(my_images_labels)}', bd=1, relief=SUNKEN, anchor=E)
        status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E)

    my_buttons = {
        'backward': Button(frame, text='<<', command=backward, state=DISABLED),
        'exit': Button(frame, text='Exit Program', command=root.quit),
        'forward': Button(frame, text='>>', command=forward)
    }
    my_buttons['backward'].grid(row=1, column=0)
    my_buttons['exit'].grid(row=1, column=1)
    my_buttons['forward'].grid(row=1, column=2, pady=10)

    status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E)

    root.mainloop()


if __name__ == '__main__':
    main()
