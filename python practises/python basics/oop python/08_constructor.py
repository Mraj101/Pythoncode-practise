class Employee:
    company = "google"
    name="Harry"
    salary=500

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getDetails(self):
        print(f'''Name of theemployee is {self.name}''')
        print(f'''salary of the employee  is {self.salary}''')
        print(f'''company of the employee is {self.subunit}''')
    @staticmethod
    def greet():
        print("Good morning sir")


hasnain = Employee("hasnain", 100, "Youtube")
hasnain.getDetails()
hasnain.greet()
print(hasnain.salary)
