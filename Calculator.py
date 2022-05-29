from tkinter import *
from math import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width = 35, borderwidth = 5, bg = "Black", fg = "White")
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_sum():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
         e.insert(0, f_num + int(second_number))

    if math == "subtraction":
         e.insert(0, f_num - int(second_number))

    if math == "multiplication":
         e.insert(0, f_num * int(second_number))

    if math == "division":
         e.insert(0, f_num / int(second_number))
    
    if math == "sqrt":
         e.insert(0, sqrt(f_num))

    if math == "square":
         e.insert(0, f_num**2)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_sqrt():
    first_number = e.get()
    global f_num
    global math
    math = "sqrt"
    f_num = int(first_number)

def button_square():
    first_number = e.get()
    global f_num
    global math
    math = "square"
    f_num = int(first_number)
    
    


button1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda : button_click(1), bg = "#3b7fb9", fg = "White")
button2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda : button_click(2), bg = "#3b7fb9", fg = "White")
button3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda : button_click(3), bg = "#3b7fb9", fg = "White")
button4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda : button_click(4), bg = "#3b7fb9", fg = "White")
button5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda : button_click(5), bg = "#3b7fb9", fg = "White")
button6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda : button_click(6), bg = "#3b7fb9", fg = "White")
button7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda : button_click(7), bg = "#3b7fb9", fg = "White")
button8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda : button_click(8), bg = "#3b7fb9", fg = "White")
button9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda : button_click(9), bg = "#3b7fb9", fg = "White")
button0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda : button_click(0), bg = "#3b7fb9", fg = "White")

button_add = Button(root, text = "+", padx = 40, pady = 20, command = button_sum, bg = "#3b7fb9", fg = "White")
button_subtract = Button(root, text = "-", padx = 43, pady = 20, command = button_subtract, bg = "#3b7fb9", fg = "White")
button_multiply = Button(root, text = "*", padx = 43, pady = 20, command = button_multiply, bg = "#3b7fb9", fg = "White")
button_divide = Button(root, text = "/", padx = 43, pady = 20, command = button_divide, bg = "#3b7fb9", fg = "White")
button_sqrt = Button(root, text = "√x", padx = 39, pady = 20,  command = button_sqrt, bg = "#3b7fb9", fg = "White")
button_square = Button(root, text = "x²", padx = 39, pady = 20,  command = button_square, bg = "#3b7fb9", fg = "White")

button_equal = Button(root, text = "=", padx = 90, pady = 20, command = button_equal, bg = "#3b7fb9", fg = "White")
button_clear = Button(root, text = "Clear", padx = 80, pady = 20, command = button_clear, bg = "#3b7fb9", fg = "White")

button_information = Button(root, text = "Basic Calculator", state = DISABLED, padx = 1, pady = 20, bg = "Red", fg = "White")

button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)

button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)

button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)

button0.grid(row = 4, column = 0)


button_add.grid(row = 5, column = 0)
button_subtract.grid(row = 6, column = 0)
button_multiply.grid(row = 6, column = 1)
button_divide.grid(row = 6, column = 2)
button_sqrt.grid(row = 7, column = 0)
button_square.grid(row = 7, column = 1)

button_equal.grid(row = 5, column = 1, columnspan = 2)
button_clear.grid(row = 4, column = 1, columnspan = 2)
button_information.grid(row = 7, column = 2)

root.mainloop()

