for i in range(2,21):
        with open(f"C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\multiply\\multiplication_of_{i}.txt",'w') as f:
           for j in range(1,11):
               f.write(f"{i}x{j}={i*j}\n")