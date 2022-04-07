from typing import final


n=int(input("enter a number:"))
try:
    a=1
    b=a/n
    c=40
except ZeroDivisionError as z:
    print("Infinite by handlding zeor division error")
