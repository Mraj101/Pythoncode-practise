class Employee:
    company="google"
    ecode= 120
class Freelancer:
    company="Fiverr"

class programmer(Employee,Freelancer):
    name="Hasnain"
    level=0
    def upgradeLevel(self):
        self.level=self.level+1

p=programmer()
print(p.company)
p.upgradeLevel()
print(p.level)