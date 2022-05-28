class Number:
    def __init__(self,num):
        self.num=num
    
    def __add__(self,num2):
        print("Lets add")
        return self.num+num2.num
    
    def __str__(self):
        return f"Decimal Number: {self.num}"

    def __len__(self):
        return 1
    # def __mul__(self,o):
    #     print("Lets multiply")
    #     return self.num*o.num
n1=Number(9)
print(n1)