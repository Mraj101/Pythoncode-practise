class Number:
    def __init__(self,txt):
        self.txt=txt
    
    def __add__(self,a):
        print("Lets add")
        return self.num+a.num

    # def __mul__(self,o):
    #     print("Lets multiply")
    #     return self.num*o.num

n1 = Number("geek ")
n2 = Number("6")
# mul=n1*n2
print(n1+n2)