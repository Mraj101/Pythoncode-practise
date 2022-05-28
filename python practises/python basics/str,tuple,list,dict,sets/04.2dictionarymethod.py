myDict={
"fast":"In a Quick Manner",
"hasnain": "A coder",
"marks": [1,2,5],
"anotherDict": {'Miraj':'player'},
1: 2
}
#dictionary methods.
# print(myDict.keys()) #return or shows keys
# print(myDict.values())#return values of the keys
# print(myDict.items())#prints the (key, value) for all contens in tuples
print(myDict)
updateDict={
      "lovish":"friend",
      "arif":"friend",
      "hasnain":"Not a dancer"
}
myDict.update(updateDict)#updates the dictionary
# print(myDict)

#difference between .get and [ ] sytnax.
print(myDict.get("hasnain2")) #does not trow error. and prints none
print(myDict['hasnain2'])#returns error
