anormDict={
    "Magenta":"Azra",
    "Ami": "I",
    "Tumake":"you",
    "valobashi":"love"
}
print("options are:",anormDict.keys())
a=input("Enter the bangla word: ")
# print("The meaning of your word is: ",anormDict[a]) will throw
print("The meaning of your word is: ",anormDict.get(a))#wont throw an error