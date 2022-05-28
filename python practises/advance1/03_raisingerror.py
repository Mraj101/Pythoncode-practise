# def increment(num):

#     try:
#         return int(num)+1
#     except:
#         raise ValueError("This is value error hasnain")
# a=increment('365a')
# print(a)
while True:
    def increment(num):
        try:
            return int(num)+1
        # except Exception as e:
        #     raise ValueError("this is value error")
        except Exception as e:
            raise TypeError("this is type error")
    a=input("enter something")
    print(increment(a))
