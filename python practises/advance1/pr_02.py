a = [2, 3, 7, 12, 34, 56, 87, 99]
for index, items in enumerate(a):
    if index == 2 or index==4 or index==6:
     print(f"{items}, {index} This is {index+1} position")
