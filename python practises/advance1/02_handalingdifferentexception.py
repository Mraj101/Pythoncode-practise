while True:
    try:
        a=int(input("fool: "))
        print("cool"+a)
    except ValueError as e:
        print("this is value error")
        print("value: ",e)
    except ZeroDivisionError as e:
        print("zero divide error")
        print(e)
    except TypeError as e:
        print("this is type error")
        print("reallY:",e)
    else:
        print("Thanks for using this code")