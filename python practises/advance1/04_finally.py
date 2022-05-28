try:
    i=int(input("enter a number: "))
    c=1/i
    print(c)
except Exception as e:
    exit() #even after exiting finally will execute
    print(e)
finally:
    print("finallY: we were succesfull")

print("this wont be printed")