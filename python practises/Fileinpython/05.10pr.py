import os
with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\copy.txt") as f:
    content=f.read()

with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\renamed_by_python.txt",'w') as f:
    content=f.write(content)
os.remove("copy.txt")
