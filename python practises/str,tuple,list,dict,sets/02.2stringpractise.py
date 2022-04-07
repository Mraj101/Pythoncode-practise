Name=input("Enter your name:")
print("Good Afternoon, "+Name)

letter='''Dear <|Name|>,
I love you so much.
<|date|>'''

print(letter)
name=input("enter your name: ")
name=input("enter date: ")
letter=letter.replace("<|Name|>","Hasnain")
letter=letter.replace("<|date|>","14th september")
print(letter)