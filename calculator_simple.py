from tkinter import *

# Constants
BUTTON_WIDTH = 60
BUTTON_HEIGHT = 20
BUTTON_BORDER_WIDTH = 2

COLOR_WHITE = '#FFFFFF'
COLOR_GREY = '#838383'
COLOR_DARK_GREY = '#3D3D3D'

# Globals
operand1 = None
operand2 = None
operator = None

# Flags
used_before = False


def main():
    container = Tk()
    container.title('Asfand\'s Calculator')

    frame = Frame(container, bg=COLOR_GREY)
    frame.grid(row=0, column=0)

    def on_click_num(number):

        global used_before
        global operand1
        global operator
        global operand2

        if used_before:
            on_click_clear()
            used_before = False

        current = e.get()
        e.delete(first=0, last=END)
        e.insert(0, current + number)

        if not operator:
            operand1 = int(current + number)
        elif operator:
            _, operand2 = (current + number).rsplit(f' {operator} ', maxsplit=1)
            operand2 = int(operand2)

    def on_click_clear():
        e.delete(first=0, last=END)
        global operand1
        operand1 = None
        global operand2
        operand2 = None
        global operator
        operator = None

    def on_click_equal():
        if operand1 and operand2:
            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand1 - operand2
            elif operator == 'x':
                result = operand1 * operand2
            elif operator == '/':
                result = operand1 / operand2
            current = e.get()
            on_click_clear()
            e.insert(0, f'{current} = {result}')
            global used_before
            used_before = True

    def on_click_operator(op):
        global operator
        if operand1 and not operand2 and not operator:
            operator = op
            current = e.get()
            e.delete(first=0, last=END)
            e.insert(0, f'{current} {operator} ')

    def create_buttons(master):
        buttons = {
            '7': Button(master, text='7', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_num('7')),
            '8': Button(master, text='8', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_num('8')),
            '9': Button(master, text='9', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_num('9')),

            '4': Button(master, text='4', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_num('4')),
            '5': Button(master, text='5', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_num('5')),
            '6': Button(master, text='6', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_num('6')),

            '1': Button(master, text='1', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_num('1')),
            '2': Button(master, text='2', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_num('2')),
            '3': Button(master, text='3', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_num('3')),

            '0': Button(master, text='0', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_num('0')),

            'CE': Button(master, text='CE', padx=BUTTON_WIDTH - 4, pady=BUTTON_HEIGHT, fg=COLOR_WHITE,
                         bg=COLOR_DARK_GREY, borderwidth=BUTTON_BORDER_WIDTH, command=on_click_clear),
            '=': Button(master, text='=', padx=BUTTON_WIDTH - 1, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=on_click_equal),

            '+': Button(master, text='+', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_operator('+')),
            '-': Button(master, text='-', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_operator('-')),
            'x': Button(master, text='x', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_operator('x')),
            '/': Button(master, text='/', padx=BUTTON_WIDTH, pady=BUTTON_HEIGHT, fg=COLOR_WHITE, bg=COLOR_DARK_GREY,
                        borderwidth=BUTTON_BORDER_WIDTH, command=lambda: on_click_operator('/'))
        }
        return buttons

    e = Entry(frame, width=60, borderwidth=6)
    e.grid(row=0, column=0, columnspan=5, rowspan=5)

    my_buttons = create_buttons(frame)

    # Starting row and column for buttons (i = row, j = column)
    i = 6
    j = 0

    # Attaching all the buttons to the calculator's container
    for button in my_buttons:
        my_buttons[button].grid(row=i, column=j)
        j += 1
        if j == 3:
            j = 0
            i += 1

    container.mainloop()


if __name__ == '__main__':
    main()
