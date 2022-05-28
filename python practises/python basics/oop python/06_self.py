class Employee:
    company="google"
    def getsalary(self):
        print(f"salary is {self.salary}k")
hasnain=Employee()
hasnain.salary=100
hasnain.getsalary() #Employee.getsalary(hasnain)