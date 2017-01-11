from tkinter import *

class MortgageCalculator(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, text = "Principle: ")
        self.label.grid(row = 0, column = 0, sticky = W)
        self.prince = Entry(self)
        self.prince.grid(row = 0, column = 1, sticky = W)

        self.label = Label(self, text = "Term of Mortgage: ")
        self.label.grid(row = 1, column = 0, sticky = W)
        self.term = Entry(self)
        self.term.grid(row = 1, column = 1, sticky = W)

        self.label = Label(self, text = "Interest Rate: ")
        self.label.grid(row = 2, column = 0, sticky = W)
        self.rate = Entry(self)
        self.rate.grid(row = 2, column = 1, sticky = W)
        
        self.calc_button = Button(self, text = "Calculate", command = self.calculate)
        self.calc_button.grid(row = 3, column = 1, sticky = W)

    def calculate(self):
        princeC = float(self.prince.get())
        termC = float(self.term.get())
        rateC = float(self.rate.get())
        
        rateC = (rateC/100)/12
        powercalc = (1 - (pow((1 + rateC), (-termC * 12))))

        total = (rateC * princeC) / powercalc
        total = total * 100
        total = round(total, 2)
        total = total / 100

        totalInt = (total * (termC * 12) - princeC)
        totalInt = totalInt * 100
        totalInt = round(totalInt, 2)
        totalInt = totalInt / 100

        self.outputLabel1 = Label(self , text = "Your monthly repayments will be: " + "€" + str(total))
        self.outputLabel1.grid(row = 4, column = 0, columnspan = 2, sticky = W)
        self.outputLabel2 = Label(self , text = "Your total interest paid for the loan will be: " + "€" + str(totalInt))
        self.outputLabel2.grid(row = 5, column = 0, columnspan = 2, sticky = W)
        self.outputLabel3 = Label(self , text = "Total paid back to the bank: " + "€" +  str(totalInt + princeC))
        self.outputLabel3.grid(row = 6, column = 0, columnspan = 2, sticky = W)

#create the window
root = Tk()

#modify root window
root.title("Mortgage Calculator")
root.geometry("350x200")
app = MortgageCalculator(root)

#event loop
root.mainloop()
