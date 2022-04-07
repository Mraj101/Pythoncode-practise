def game():
    return 64
score=game()
with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\highscore.txt") as f:
    hiscore=int(f.read())

if hiscore<score:
    with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\Fileinpython\\highscore.txt",'w') as f:
        f.write(str(score))
