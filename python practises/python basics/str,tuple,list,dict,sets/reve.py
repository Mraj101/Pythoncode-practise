string="hello hasnain"
revstring=string[::-1]
print("slice it",revstring)
print("_______________Another method_______________\n")
funcstring="".join(reversed(string))
print("use .join"+funcstring)
print("_______________Another method_______________\n")
recfuncstring=string
next(recfuncstring)
