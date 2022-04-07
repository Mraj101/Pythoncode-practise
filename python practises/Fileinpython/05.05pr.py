with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\myfile.txt") as f:
    content=f.read()
words=['donkey','monkey','funkey','stupid']
for word in words:
        content=content.replace(word,"$%!^@%")


with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\Fileinpython\\myfile.txt",'w') as f:
    content=f.write(content)
