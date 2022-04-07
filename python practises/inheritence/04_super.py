class Person:
    def __init__(self):
        print("INITializing person")
    country="Bangladesh"
    def takeBreath(self):
        print("I am breathing....")

class Employee(Person):
    company="google"
    
    def __init__(self):
        super().__init__()
        print("Initialiazing employee")
    @staticmethod    
    def getSalary():
        print(f'''salary is "someting" ''')
    
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am breating..")

class Programmer(Employee):
    company="Fiverr"
    def getSalary(self):
        print(f"No salary to programmers")
    def __init__(self):
        super().__init__()
        print("Initializing programmer\n")
    def takeBreath(self):
        super().takeBreath()
        print("I am a programmer, and am taking breath.")
pr=Programmer()
pr.takeBreath()
