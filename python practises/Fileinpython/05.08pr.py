with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\this.txt") as f:
    content=f.read()
with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\copy.txt",'w') as f:
    f.write(content)  