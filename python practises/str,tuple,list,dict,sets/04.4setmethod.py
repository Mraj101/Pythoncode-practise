b=set()
print(type(b))

b.add(4)
b.add(4)
b.add(4)
b.add(5)
print(b)
#non repitetive

# b.add([2,3,4,5])#we can not put list in a set 
b.add((2,3,4))
print(b)
print(len(b))#prints the lenght of this set
b.remove(5)
print(b)
print(b.pop())

