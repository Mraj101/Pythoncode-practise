import random
randNumber=random.randint(1,100)
userGuess=None
guesses=0
while(userGuess!=randNumber):
    userGuess=int(input("enter your guess: "))
    guesses+=1
    if(userGuess==randNumber):
        print("you guessed it right")
    else:
        if(userGuess>randNumber):
            print("you guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
    
    

print(f"You guessed the number in {guesses} guesses")
with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\inheritence\\hi.txt","r") as f:
    highscore=int(f.read())
if guesses>highscore:
    print("you hve broker high score")
    with open("C:\\Users\\HP\\OneDrive\\Documents\\code\\pythoncode\\Harry's python\\inheritence\\hi.txt","w") as f:
        f.write(str(guesses))