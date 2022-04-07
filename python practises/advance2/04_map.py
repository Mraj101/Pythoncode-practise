def square(num):
    return num*num
l=[1,2,4,4,4,4]
l2=[]
#mehtod1
for item in l:
    l2.append(square(item))
print(l2)

#Mehod2
print(list(map(square,l)))
