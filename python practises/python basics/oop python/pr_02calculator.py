class Calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"The square value of {self.num} is {self.num**2}\n")        
    def squareRoot(self):
        print(f"The squareRoot value of {self.num} is {pow(self.num,0.5)}\n")
    def cube(self):
         print(f"The cube value of {self.num} is {self.num**3}\n")
a=Calculator(9)
a.square()
a.squareRoot()
a.cube()
