with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\myfile.txt") as f:
    content=f.read()

content=content.replace("donkey","$%!^@%")
with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\Fileinpython\\myfile.txt",'w') as f:
    content=f.write(content)