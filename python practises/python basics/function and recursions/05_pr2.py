def mysum(n):
    if n==1 or n==0:
        return 1
    else:
        return n+mysum(n-1)

print(mysum(5))