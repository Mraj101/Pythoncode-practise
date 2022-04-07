file1="copy.txt"
file2="this.txt"
with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\copy.txt") as f:
    f1=f.read()
with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\this.txt") as f:
    f2=f.read()
if f1==f2:
    print("they are same")
else:
    print("not same")