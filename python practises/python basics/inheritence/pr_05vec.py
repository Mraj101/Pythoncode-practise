class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __add__(self,vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i]+vec2.vec[i])
        return Vector(newlist)

    def __str__(self):
        out=""
        index=0
        for i in self.vec:
            out=out+f"{i}a{index} +"
            index+=1
        return out[:-1]
    def __mul__(self,vec2):
        sum=0
        for i in range(len(self.vec)):
         sum=sum+self.vec[i]*vec2.vec[i]
        return sum

v1=Vector([1, 2, 3])
v2=Vector([4, 5, 8])
print(v1+v2)
print()
print(v1*v2)
