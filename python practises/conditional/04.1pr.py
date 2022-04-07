num=int(input("enter you number to check grade: "))
if num>90:
    grade="Ex"
elif num>=80:
    grade="A"
elif num>=70:
    grade="B"
elif num>=60:
    grade="C"
elif num>=50:
    grade="D"
else:
    grade="Fail"

print("Your grade is:",grade)