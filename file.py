from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title('File opener program')
# Get the user's screen resolution
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}')


def ask_for_file():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir='./images/travel/',
                                               title='Open File',
                                               filetypes=(('jpg files', '*.jpg'), ('all files', '*.*'))
                                               )
    Label(root, text=f'{root.filename}').pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename).resize((screen_width-30, screen_height-200)))
    Label(root, image=my_img).pack()


Button(root, text='Open Image', command=ask_for_file).pack()

root.mainloop()
