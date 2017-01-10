from tkinter import *

class TaxCalculator(Frame):
    netSal = 0
    totalTax = 0

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, text = "Enter your Salary: ")
        self.label.grid(row = 0, column = 0, sticky = W)
        self.salary = Entry(self)
        self.salary.grid(row = 0, column = 1, sticky = W)
        
        self.incTax = Label(self, text = "Income Tax: ")
        self.incTax.grid(row = 5, column = 0, sticky = W)
        
        self.prsi = Label(self, text = "PRSI: ")
        self.prsi.grid(row = 6, column = 0, sticky = W)
        
        self.usc = Label(self, text = "USC: ")
        self.usc.grid(row = 7, column = 0, sticky = W)

        self.calc_button = Button(self, text = "Calculate", command = self.calculate)
        self.calc_button.grid(row = 4, column = 1, sticky = W)

    def calculate(self):
        wage = float(self.salary.get())
        
        prsiC = wage * 0.04
        uscC = 0
        incC = 0
        lowRate = 0.20
        highRate = 0.40
        taxCred = 3300
		
        if(wage < 13000):
            prsiC = 0
            totalTax = 0
        elif(wage > 13000 and wage < 18772):
            uscC = (12012 * 0.005) + ((wage - 12012) * 0.025)
            incC = (wage * lowRate) - taxCred
            prsiC = 0
            if(incC < 0):
                incC = 0
	
        elif(wage > 18772 and wage < 33800):
            uscC = (12012 * 0.005) + (6760 * 0.025) + ((wage - 18772) * 0.05)
            incC = (wage * lowRate) - taxCred
			
        elif(wage > 33800 and wage < 70044):
            uscC = (12012 * 0.005) + (6760 * 0.025) + ((wage - 18772) * 0.05)
            incC = (((33800 * lowRate) - taxCred) + ((wage - 33800) * highRate))			
			
        elif(wage > 70044):
            uscC = (12012 * 0.005) + (6760 * 0.025) + (15028 * 0.05) + ((wage - 70044) * 0.08)
            incC = (((33800 * lowRate) - taxCred) + ((wage - 33800) * highRate))		
    
    
        totalTax = incC + prsiC + uscC
        netSal = wage - totalTax

        self.incTax1 = Label(self , text = str(incC))
        self.incTax1.grid(row = 5, column = 1, sticky = W)
        self.prsi1 = Label(self , text = str(prsiC))
        self.prsi1.grid(row = 6, column = 1, sticky = W)
        self.usc1 = Label(self , text = str(round(uscC,2)))
        self.usc1.grid(row = 7, column = 1, sticky = W)

        self.outputLabel1 = Label(self , text = "Your net salary for 2017 is: " + "€" + str(netSal))
        self.outputLabel1.grid(row = 9, column = 0, columnspan = 2, sticky = W)
        self.outputLabel2 = Label(self , text = "Your Monthly take home pay for 2017 is: " + "€" + str(round(netSal / 12,2)))
        self.outputLabel2.grid(row = 10, column = 0, columnspan = 2, sticky = W)
        self.outputLabel3 = Label(self , text = "Your total tax paid for 2017 will be: " + "€" + str(totalTax))
        self.outputLabel3.grid(row = 8, column = 0, columnspan = 2, sticky = W)

#create the window
root = Tk()

#modify root window
root.title("Tax Calculator")
root.geometry("350x200")
app = TaxCalculator(root)

#event loop
root.mainloop()
