import random

def game(comp,you):
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
        elif comp=='g':
            return True
    elif comp=='w':
        if you=='s':
            return False
        elif you=='g':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
        
          
        return True
    



print("Com Turn: snake(s) Water (w) or Gun()?")


you=input("player 2 Turn: Snake(s) Water(w) or Gun(g): ")
randno=random.randint(1, 3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'
a=game(comp,you)
print(f"Computer choose {comp}")
print(f"computer chose {you}")
if a==None:
    print("the game is a tie")
elif a:
    print("you win")
else:
    print("you lose")