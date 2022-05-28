a=54 #Global varuable
def func1():
    global a
    print(f"print statement 1: {a}")     #local varibale
    a=8
    print(f"print statement 2: {a}")


func1()
print("setement 3:" ,a)