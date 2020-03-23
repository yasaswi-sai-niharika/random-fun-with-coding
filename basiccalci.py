from tkinter import *

window = Tk()
window.title("Calci the Basic Calcualtor")
window.geometry("312x402+120+120")


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

expr = ""
input_text = StringVar()

input_frame = Frame(window, width = 312, height = 50, bd = 10, highlightbackground = "azure", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('Helvetica', 18, 'bold'), textvariable = input_text, width = 50, bg = "SlateGray3", bd = 30, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

btns_frame = Frame(window, width = 312, height = 200, bg = "azure")
btns_frame.pack()


_clear_ = Button(btns_frame, text = "C", fg = "black", width = 22, height = 3, bd = 0, bg = "SlateGray3", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)
_modulus_ = Button(btns_frame, text = "%", fg = "black", width = 10, height = 3, bd = 0, bg = "SlateGray3", command = lambda: on_btn_click("%")).grid(row = 0, column = 2, padx = 1, pady = 1)
_divide_ = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "SlateGray3", command = lambda: on_btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
_seven_ = Button(btns_frame, text = "7", fg = "black", width = 11, height = 3, bd = 0, bg = "SlateGray1", command = lambda: on_btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
_eight_ = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "SlateGray1", command = lambda: on_btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
_nine_ = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "SlateGray1", command = lambda: on_btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
_multiply_ = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "SlateGray3", command = lambda: on_btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
_four_ = Button(btns_frame, text = "4", fg = "black", width = 11, height = 3, bd = 0, bg = "SlateGray1", command = lambda: on_btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
_five_ = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "SlateGray1", command = lambda: on_btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
_six_ = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "SlateGray1", command = lambda: on_btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
_minus_ = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "SlateGray3", command = lambda: on_btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
_one_ = Button(btns_frame, text = "1", fg = "black", width = 11, height = 3, bd = 0, bg = "SlateGray1", command = lambda: on_btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
_two_ = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "SlateGray1", command = lambda: on_btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
_three_ = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "SlateGray1", command = lambda: on_btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
_plus_ = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "SlateGray3", command = lambda: on_btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
_zero_ = Button(btns_frame, text = "0", fg = "black", width = 22, height = 3, bd = 0, bg = "SlateGray1", command = lambda: on_btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
_point_ = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "SlateGray3", command = lambda: on_btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
_equals_ = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "SlateGray3", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)


window.mainloop()
