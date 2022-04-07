# def divBy_5(x):
#     if x%5==0:
#         return True
#     else:
#         return False
#         #or
divB_5=lambda num:num%2==0
li=[1,2,3,4,5,6,7,7,8,9,10,25,30,34,35]
print(list(filter(divB_5,li)))