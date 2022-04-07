def readFile(fname):
    try:
     with open(fname,'r') as f:
         print(f.read())
    except FileNotFoundError:
        print(f"file {fname} is not found")


readFile("1.txt")
readFile("2.txt")
readFile("3.txt")

    