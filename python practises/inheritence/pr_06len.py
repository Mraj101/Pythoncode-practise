class Vector:
    def __init__(self,vec):
        self.vec=vec
    
    def __len__(self):
        return len(self.vec)
    # # def __str__(self):
    # #     return f""
v1=Vector([1, 2, 3])
v2=Vector([4, 5, 8])
print(len(v1))