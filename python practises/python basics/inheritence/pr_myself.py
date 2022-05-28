class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def __add__(self,other):
     return Student(self.m1 + other.m1,self.m2 + other.m2)

    def __str__(self):
       return f"m1 is{self.m1} and m2 is{self.m2}"
s1=Student(12, 15)
s2=Student(13, 14)
print(s1+s2)
