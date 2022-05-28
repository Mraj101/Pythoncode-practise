def remove_and_split(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()
this="    hi i am hasnain    "
print(remove_and_split(this,"hasnain"))
# print(this)
# print(this.strip())