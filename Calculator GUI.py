# A simple calculator GUI
from tkinter import *


def button_click(number):
    global expression
    expression = expression + str(number)
    input_var.set(expression)

def clear_button():
    global expression
    expression = ""
    input_var.set(expression)

def clear_one():
    global expression
    new_string = expression[:-1]
    input_var.set(new_string)
    expression = new_string

def equals_button():
    global expression
    try:
        result = str(eval(expression))
        input_var.set(result)
        if result == "0":
            expression = ""
        else:
            expression = result
    except SyntaxError:
        if expression == "":
            input_var.set(0)
        else:
            input_var.set("Syntax Error")
        expression = ""
    except ZeroDivisionError:
        input_var.set("Can't divide by Zero")
        expression = ""


calculator = Tk()
calculator.title("Calc")
calculator.geometry("205x365+600+150")
calculator.resizable(0,0) #To make sure the program keeps its shape and doesnt get resized.

input_var = StringVar()
expression = ""

frame1 = Frame(calculator, height = 50, bg = "powder blue")
frame1.pack(side = TOP)

frame2 = Frame(calculator, height = 50, bg = "powder blue")
frame2.pack()

frame3 = Frame(calculator, width = 1400, height = 530)
frame3.pack(side = BOTTOM)

my_Label = Label(frame1, text = "The cALcACER", bg = "powder blue", font = ("comic sans", 21, "italic"))
my_Label.pack()

entry = Entry(frame2, font = ("Cambria", 13), textvariable = input_var,
      bd = 3, width = 22, justify = "right")
entry.grid(row = 0, column = 0, ipady = 10)

# Adding the buttons
button7 = Button(frame3, text = 7, padx = 16, pady = 16, command = lambda: button_click(7))
button7.grid(row=2, column = 0)

button8 = Button(frame3, text = 8, padx = 16, pady = 16, command = lambda: button_click(8))
button8.grid(row=2, column = 1)

button9 = Button(frame3, text = 9, padx = 19, pady = 16, command = lambda: button_click(9))
button9.grid(row=2, column = 2)

button4 = Button(frame3, text = 4, padx = 16, pady = 16, command = lambda: button_click(4))
button4.grid(row=3, column = 0)

button5 = Button(frame3, text = 5, padx = 16, pady = 16, command = lambda: button_click(5))
button5.grid(row=3, column = 1)

button6 = Button(frame3, text = 6, padx = 19, pady = 16, command = lambda: button_click(6))
button6.grid(row=3, column = 2)

button3 = Button(frame3, text = 3, padx = 19, pady = 16, command = lambda: button_click(3))
button3.grid(row=4, column = 2)

button2 = Button(frame3, text = 2, padx = 16, pady = 16, command = lambda: button_click(2))
button2.grid(row=4, column = 1)

button1 = Button(frame3, text = 1, padx = 16, pady = 16, command = lambda: button_click(1))
button1.grid(row=4, column = 0)

button0 = Button(frame3, text = 0, pady = 16, width = 12, command = lambda: button_click(0))
button0.grid(row=5, columnspan = 2)

plus_button = Button(frame3, text = "+", padx = 17, pady = 16, command = lambda: button_click("+"))
plus_button.grid(row=1, column = 3)

minus_button = Button(frame3, text = "-", padx = 19, pady = 16, command = lambda: button_click("-"))
minus_button.grid(row=2, column = 3)

divide_button = Button(frame3, text = "/", padx = 19, pady = 16, command = lambda: button_click("/"))
divide_button.grid(row=4, column = 3)


times_button = Button(frame3, text = "x", padx = 19, pady = 16, command = lambda: button_click("*"))
times_button.grid(row=3, column = 3)

clear_btn = Button(frame3, text = "CE", width = 12, pady = 15, command = clear_button)
clear_btn.grid(row=1, columnspan = 2)

single_clear_btn = Button(frame3, text = "<-", padx = 16, pady = 16, command = clear_one)
single_clear_btn.grid(row=1, column= 2)

equals_btn = Button(frame3, text = "=", padx = 17, pady = 16, command = equals_button)
equals_btn.grid(row=5, column = 3)

decimal_button = Button(frame3, text = ".", padx = 20, pady = 16, command = lambda: button_click("."))
decimal_button.grid(row=5, column = 2)

calculator.mainloop()
