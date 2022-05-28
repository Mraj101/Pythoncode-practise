class Employee:
    company="google"
    salary=100
    def getsalary(self,signature):
        print(f"salary is {self.salary}\n{signature}")
    @staticmethod
    def greet(): 
        print("Good Morning, sir")
hasnain = Employee()

hasnain.salary=10000
hasnain.getsalary("thanks!")
hasnain.greet()