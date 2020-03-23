from tkinter import *
"""import tkinter library"""
window = Tk()
window.title("Calci the Basic Calculator")
window.geometry("328x420+120+120")
"""window operations after creating tkinter window"""

def on_btn_click(clicked_item):
    global expr
    expr = expr + str(clicked_item)
    input_text.set(expr)
    return 

def btn_clear():
    global expr
    expr = ""
    input_text.set("")
    return

def btn_equal():
    global expr
    result = str(eval(expr)) 
    input_text.set(result)
    expr = ""
    return
"""different event handling functions"""
expr = ""
input_text = StringVar()

input_frame = Frame(window, width = 328, height = 50, bd = 10, highlightbackground = "azure", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('Helvetica', 18, 'bold'), textvariable = input_text, width = 50, bg = "SlateGray3", bd = 30, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

btns_frame = Frame(window, width = 328, height = 200, bg = "azure")
btns_frame.pack()


clear_btn = Button(btns_frame, text = "C", fg = "black", width = 22, height = 3, bg = "SlateGray3", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)
modulus_btn = Button(btns_frame, text = "%", fg = "black", width = 10, height = 3, bg = "SlateGray3", command = lambda: on_btn_click("%")).grid(row = 0, column = 2, padx = 1, pady = 1)
divide_btn = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bg = "SlateGray3", command = lambda: on_btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
seven_btn = Button(btns_frame, text = "7", fg = "black", width = 11, height = 3, bg = "SlateGray1", command = lambda: on_btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight_btn = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bg = "SlateGray1", command = lambda: on_btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine_btn = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bg = "SlateGray1", command = lambda: on_btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply_btn = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bg = "SlateGray3", command = lambda: on_btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
four_btn = Button(btns_frame, text = "4", fg = "black", width = 11, height = 3, bg = "SlateGray1", command = lambda: on_btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five_btn = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bg = "SlateGray1", command = lambda: on_btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six_btn = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bg = "SlateGray1", command = lambda: on_btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus_btn = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bg = "SlateGray3", command = lambda: on_btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
one_btn = Button(btns_frame, text = "1", fg = "black", width = 11, height = 3, bg = "SlateGray1", command = lambda: on_btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two_btn = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bg = "SlateGray1", command = lambda: on_btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three_btn = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bg = "SlateGray1", command = lambda: on_btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus_btn = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bg = "SlateGray3", command = lambda: on_btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
zero_btn = Button(btns_frame, text = "0", fg = "black", width = 22, height = 3, bg = "SlateGray1", command = lambda: on_btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point_btn = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bg = "SlateGray3", command = lambda: on_btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals_btn = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bg = "SlateGray3", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
""" above code is responsible for aligning the different buttons for different roles  """

window.mainloop()
