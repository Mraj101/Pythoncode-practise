f=open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\poem.txt")
a=f.read()
if "twinkle" in a:
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()