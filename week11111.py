from breezypythongui import EasyFrame
 
class Calculator(EasyFrame):

    def __init__(self, title="SIMPLE CALCULARO", width=500, height=200, background="white", resizable=True):
        EasyFrame.__init__(self, title, width, height, background, resizable)

        self.addLabel(text="Enter the first number", row=0,column=0)
        self.txtNum1 = self.addIntegerField(value=0,row=0,column=1,width=10)

        self.addLabel(text="Enter the second number", row=1,column=0)
        self.txtNum2 = self.addIntegerField(value=0,row=1,column=1,width=10)

        self.txtResult = self.addTextField(text="0",row=2,column=0,columnspan=2,state="readonly")

        self.addButton(text="+", row=3,column=0,columnspan=1,command=self.sum)
        self.addButton(text="-",row=3,column=0,columnspan=3,command=self.difference)
        self.addButton(text="x", row=3,column=0,columnspan=6,command=self.quotient)
        self.addButton(text="/", row=3,column=1,columnspan=4,command=self.float)
        self.addButton(text="//", row=3,column=4,columnspan=1,command=self.product)
        self.addButton(text="%", row=3,column=5,columnspan=1,command=self.modulo)
        self.addButton(text="**", row=3,column=6,columnspan=1,command=self.exponent)
        

    def sum(self):
        num1=self.txtNum1.getNumber()
        num2=self.txtNum2.getNumber()

        result = num1 + num2
        self.txtResult.setText(f"the sum is {result}")

    def difference(self):
        num1=self.txtNum1.getNumber()
        num2=self.txtNum2.getNumber()

        result = num1 - num2
        self.txtResult.setText(f"the difference is {result}")

    def quotient(self):
        num1=self.txtNum1.getNumber()
        num2=self.txtNum2.getNumber()

        result = num1 * num2
        self.txtResult.setText(f"the quotient is {result}")

    def product(self):
        num1=self.txtNum1.getNumber()
        num2=self.txtNum2.getNumber()

        result = num1 // num2
        self.txtResult.setText(f"the product is {result}")

    def float(self):
        num1=self.txtNum1.getNumber()
        num2=self.txtNum2.getNumber()

        result = num1 / num2
        self.txtResult.setText(f"the float product is {result}")

    def modulo(self):
        num1=self.txtNum1.getNumber()
        num2=self.txtNum2.getNumber()

        result = num1 % num2
        self.txtResult.setText(f"the modulo is {result}")

    def exponent(self):
        num1=self.txtNum1.getNumber()
        num2=self.txtNum2.getNumber()

        result = num1 % num2
        self.txtResult.setText(f"the exponentiation is {result}")  

    

        

Calculator().mainloop()