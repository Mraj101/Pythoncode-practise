class Employee:
    company="Titas Gas"
    salary=5600
    salarybonus=500
    @property
    def totalSalary(self):
        return self.salary+self.salarybonus
    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus=val-self.salary
    
e=Employee()
print(e.totalSalary)
print(e.salary)
print(e.salarybonus)
