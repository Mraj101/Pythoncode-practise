with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\logfile.txt") as f:
  content= f.read().lower()
if 'python' in content:
    print("yes python is present")
else:
    print("no")