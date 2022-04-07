while(True):
    print("press q to quit")
    a = input("Enter a number: ")
    if a=="q" or a=="Q":
        print("you quit")
        break
   
    try:  
        a=int(a)
        if a>6:
          print("you entered a number greater than 6")
    except Exception as e:
        print("cool: ",e)

    