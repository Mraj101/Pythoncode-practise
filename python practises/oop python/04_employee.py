class Employee:
    company="google"
    salary=100
hasnain = Employee()
rajni=Employee() 
hasnain.salary=300
rajni.salary=400
print(Employee.company)
Employee.company="youtube"
print(hasnain.company)
print(hasnain.salary)
print(rajni.salary)
print("BUT EMPLOYEE SALARY IS THE SAME: ",Employee.salary)