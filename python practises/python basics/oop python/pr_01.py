class Programmer:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getDetails(self):
        print(f"The name of the {self.company}programmer is {self.name}")
        print(f"I work in {self.product}\n")
hasnain=Programmer("Hasnain","Skype")
magenta=Programmer("Azra","Github")
samantha=Programmer("Samantha","Youtube")
juli=Programmer("Juli","Google")
juli.getDetails()
magenta.getDetails()
