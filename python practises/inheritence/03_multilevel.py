class Person:
    country="Bangladesh"
    def takeBreath(self):
        print("I am breathing....")

class Employee(Person):
    company="google"

    def getSalary(self):
        print(f"salary is {self.salary}")
    
    def takeBreath(self):
        print("I am an Employee so I am breating..")

class Programmer(Employee):
    company="Fiverr"
    
    def getSalary(self):
        print(f"No salary to programmers")
p=Person()
p.takeBreath()
e=Employee()
e.takeBreath()
pr=Programmer()
pr.takeBreath()
print(p.country)

