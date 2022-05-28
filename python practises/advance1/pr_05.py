n=int(input("enter a nubmer: "))
with open('mult.txt','a') as f:
    li =[i*n for i in range(1,11)]
    for mult in li:
     f.write(str(mult))
     f.write('\n')