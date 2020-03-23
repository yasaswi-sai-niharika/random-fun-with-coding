from tkinter import*

def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4,bg="#7FFFD4") 
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'amitale 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Basic Calculator')

        display = StringVar()
        Entry(self, relief=RIDGE,
              textvariable=display,justify='right',bd=30,bg="#7FFFD4").pack(side=TOP, expand=YES, fill=BOTH) # #808080#C0C0C0 
        for clearBut in(["CE"],["c"]):
            erase = iCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar,lambda storeObj=display, q=ichar: storeObj.set(''))

        for NumBut in ("789/", "456*", "123-", "0.+"):
            FunctionNum = iCalc(self, TOP)
            for iEquals in NumBut:
                button(FunctionNum, LEFT, iEquals,lambda storeObj=display, q=iEquals: storeObj.set(storeObj.get() + q))

        EqualsButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals is '=':
                btniEquals = button(EqualsButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>',lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals = button(EqualsButton, LEFT, iEquals,lambda storeObj=display, s=' %s '%iEquals: storeObj.set(storeObj.get()+s))
                

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

if __name__ == '__main__':
    app().mainloop()
    

        
              
