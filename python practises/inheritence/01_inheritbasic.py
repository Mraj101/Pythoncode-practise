class Employee:        #base class
    company="google"
    def showDetails(self):
        print("this is an employee")

class Programmer(Employee): #child class
    language="python"
    company="youtube"
    def showDetails(self):
        print("this is an employee from child class")
    def getLanguage(self):
        print(f"The language is {self.language}")

e=Employee()
e.showDetails()
p=Programmer()
p.showDetails()
print(p.company)