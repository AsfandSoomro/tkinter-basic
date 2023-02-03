from tkinter import *
from PIL import Image, ImageTk


def main():
    root = Tk()
    root.title('Program to show image on the container')
    root.iconbitmap('./icons/YouTube.ico')

    my_img = ImageTk.PhotoImage(Image.open('./images/body.jpg'))
    my_label = Label(root, image=my_img)
    my_label.pack()

    my_button = Button(root, image=my_img, width=50, height=50)
    quit_button = Button(root, text='Exit Program', command=root.quit)

    my_button.pack()
    quit_button.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
