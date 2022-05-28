def factorial(Num):
    if Num==1 or Num==0:
        return 1
    else:
        return Num*factorial(Num-1)

print(factorial(5))