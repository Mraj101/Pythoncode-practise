# marks=[45,75,65,77]
# avg=(sum(marks)/400)*100

# marks2=[55,79,65,88]
# avg2=(sum(marks2)/400)*100
# print(avg,avg2)
def percent(marks):
    return ((mark[0]+mark[1]+mark[2]+mark[3])/400)*100

num1 =int(input("enter number num1 "))
num2 =int(input("enter number num2 " ))
num3 =int(input("enter number num3 ") )
num4 =int(input("enter number num4 ")) 

mark=[num1,num2,num3,num4]
print("mark is :",percent(mark))
