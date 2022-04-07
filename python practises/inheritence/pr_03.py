class Employee:
    salary=1000
    increament=1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increament

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment=sai/self.salary

e=Employee()
print(e.increament)
e.salaryAfterIncrement=2000
print(e.increment)