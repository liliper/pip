import tkinter as tk
from tkinter import messagebox
import math


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except NameError:
        messagebox.showinfo('Внимание', 'Нужно вводить только цифры!')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль дилить нельзя!')
        calc.insert(0, 0)


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)


def add_sqrt():
    value = calc.get()
    value = float(value)
    value = math.sqrt(value)
    calc.delete(0, tk.END)
    calc.insert(0, value)


def add_pow():
    value = calc.get()
    value = float(value)
    value = math.pow(value, 2)
    calc.delete(0, tk.END)
    calc.insert(0, value)


def add_factorial():
    value = calc.get()
    value = int(value)
    value = math.factorial(value)
    calc.delete(0, tk.END)
    calc.insert(0, value)


def add_log():
    value = calc.get()
    value = float(value)
    value = math.log10(value)
    calc.delete(0, tk.END)
    calc.insert(0, value)


def make_digit_button(digit):
    return tk.Button(text=digit, bd=1, font=('arial', 13),
                     command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=1, font=('arial', 13),
                     command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=1, font=('arial', 13),
                     command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=1, font=('arial', 13),
                     command=clear)


def make_sqrt_button(operation):
    return tk.Button(text=operation, bd=1, font=('arial', 13),
                     command=add_sqrt)


def make_pow_button(operation):
    return tk.Button(text=operation, bd=1, font=('arial', 13),
                     command=add_pow)


def make_factorial_button(operation):
    return tk.Button(text=operation, bd=1, font=('arial', 13),
                     command=add_factorial)


def make_log_button(operation):
    return tk.Button(text=operation, bd=1, font=('arial', 13),
                     command=add_log)


win = tk.Tk()
win.geometry(f"400x400+100+200")
win['bg'] = '#000000'
win.title('Калькулятор')

win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 23), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=5, stick='wens')

make_digit_button('1').grid(row=1, column=0, stick='wens')
make_digit_button('2').grid(row=1, column=1, stick='wens')
make_digit_button('3').grid(row=1, column=2, stick='wens')
make_digit_button('4').grid(row=2, column=0, stick='wens')
make_digit_button('5').grid(row=2, column=1, stick='wens')
make_digit_button('6').grid(row=2, column=2, stick='wens')
make_digit_button('7').grid(row=3, column=0, stick='wens')
make_digit_button('8').grid(row=3, column=1, stick='wens')
make_digit_button('9').grid(row=3, column=2, stick='wens')
make_digit_button('0').grid(row=4, column=1, stick='wens')

make_operation_button('+').grid(row=1, column=3, stick='wens')
make_operation_button('-').grid(row=2, column=3, stick='wens')
make_operation_button('*').grid(row=3, column=3, stick='wens')
make_operation_button('/').grid(row=4, column=3, stick='wens')

make_calc_button('=').grid(row=4, column=2, stick='wens')
make_clear_button('C').grid(row=4, column=0, stick='wens')

make_sqrt_button('√').grid(row=2, column=4, stick='wens')

make_pow_button('^2').grid(row=1, column=4, stick='wens')

make_factorial_button('!').grid(row=3, column=4, stick='wens')

make_log_button('log10').grid(row=4, column=4, stick='wens')

win.grid_columnconfigure(0, minsize=80)
win.grid_columnconfigure(1, minsize=80)
win.grid_columnconfigure(2, minsize=80)
win.grid_columnconfigure(3, minsize=80)
win.grid_columnconfigure(4, minsize=80)

win.grid_rowconfigure(0, minsize=80)
win.grid_rowconfigure(1, minsize=80)
win.grid_rowconfigure(2, minsize=80)
win.grid_rowconfigure(3, minsize=80)
win.grid_rowconfigure(4, minsize=80)

win.mainloop()
