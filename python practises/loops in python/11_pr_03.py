num=int(input("Enter your  number: "))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
        break
if prime:
    print("The number is prime")
else:
    print("This number is not prime")