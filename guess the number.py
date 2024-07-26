import random
print("Game: Guess the Number(1-100): ")
for i in range(10):
    b=random.randint(1,100)
    a=int(input("Enter a number: "))
    if a==b:
        print("You guessed it right")
        break
    else:
        print("You guessed it wrong")
print("Game Ends")