content=True
i=1
with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\line.txt") as f:

 while content:
      i+=1
      content = f.readline()
      
      if 'python' in content.lower():
        print(content)
        print("yes pyton is present <--------------------")
        print(i)