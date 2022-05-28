# try:
#     i=int(input("enter a number: "))
#     c=1/i
#     print(c)
# except Exception as e:
#     print(e)
# else:
#     print("we were succesfull")

while True:
        try:
         i=int(input("enter a number: "))
         c=1/i
         print(c)
        except Exception as e:
         print(e)
        else:
         print("we are successfull")

        print("we made a mistake but we are out now")