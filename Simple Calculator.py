import tkinter as tk
from math import *

root = tk.Tk()
root.title("Simple Calculator")

def show_num(text):
    display.insert("end", text)

def evaluate():
    print(display.get())
    event = str(eval(str(display.get())))
    print(event)
    display.delete(0, "end")
    display.insert(0, event)

def clear_input():
    display.delete(0, "end")


input_equal = tk.Frame(master=root)

display = tk.Entry(master=input_equal, width=28)
equal = tk.Button(master=input_equal, width=5, text="=", bg="orange", command=lambda: evaluate())
equal.grid(row=0, column=1, padx=10)
display.grid(row=0, column=0, padx=8, pady=4)
display.bind(equal, evaluate)

input_equal.grid(row=0, column=0, padx=4, pady=5)

operators = tk.Frame(master=root)

digit7 = tk.Button(master=operators, width=7, height=2, text=7, command=lambda: show_num(7))
digit7.grid(row=0, column=0, padx=2, pady=2)
digit8 = tk.Button(master=operators, width=7, height=2, text=8, command=lambda: show_num(8))
digit8.grid(row=0, column=1, padx=2)
digit9 = tk.Button(master=operators, width=7, height=2, text=9, command=lambda: show_num(9))
digit9.grid(row=0, column=2, padx=2)
digit4 = tk.Button(master=operators, width=7, height=2, text=4, command=lambda: show_num(4))
digit4.grid(row=1, column=0, pady=2)
digit5 = tk.Button(master=operators, width=7, height=2, text=5, command=lambda: show_num(5))
digit5.grid(row=1, column=1)
digit6 = tk.Button(master=operators, width=7, height=2, text=6, command=lambda: show_num(6))
digit6.grid(row=1, column=2)
digit1 = tk.Button(master=operators, width=7, height=2, text=1, command=lambda: show_num(1))
digit1.grid(row=2, column=0, pady=2)
digit2 = tk.Button(master=operators, width=7, height=2, text=2, command=lambda: show_num(2))
digit2.grid(row=2, column=1)
digit3 = tk.Button(master=operators, width=7, height=2, text=3, command=lambda: show_num(3))
digit3.grid(row=2, column=2)
digit0 = tk.Button(master=operators, width=7, height=2, text=0, command=lambda: show_num(0))
digit0.grid(row=3, column=1)
clear = tk.Button(master=operators, width=7, height=2, text="C", command=clear_input)
clear.grid(row=3, column=0, pady=2)
dot = tk.Button(master=operators, width=7, height=2, text=".", command=lambda: show_num("."))
dot.grid(row=3, column=2)
plus = tk.Button(master=operators, width=7, height=2, text="+", command=lambda: show_num("+"))
plus.grid(row=0, column=3)
minus = tk.Button(master=operators, width=7, height=2, text="-", command=lambda: show_num("-"))
minus.grid(row=1, column=3)
multiply = tk.Button(master=operators, width=7, height=2, text="x", command=lambda: show_num("*"))
multiply.grid(row=2, column=3)
divide = tk.Button(master=operators, width=7, height=2, text="÷", command=lambda: show_num("÷"))
divide.grid(row=3, column=3)
operators.grid(row=1, column=0)

root.mainloop()
