# Number-guessing-game
#This project is created using python programming language
import random
random_number = random.randrange(1,100) #To genrate a random number for the game.
chances = 0
level = input("Choose the level 'easy' or 'hard' ? ")
if level=="easy":
    chances = 10
    guess = None
    print("Easy Level so you will get 10 chances....")
    while guess!=random_number:
        guess = int(input("Guess a number : "))
        if (guess > random_number):
            print("Oops the number is too high !!")
            print("Guess Again")
            print(f"Only {chances} chances remaining")
            print("\n\n")
        elif (guess < random_number):
            print("Oops the number is too low !!")
            print("Guess Again")
            print(f"Only {chances} chances remaining")
            print("\n\n")
        elif (guess == random_number):
            print("Yes you got it !!!!....")
        if chances==0:
            print("No more chances left...")
            break
        chances -= 1

elif level=="hard":
    chances = 5
    guess = None
    print("Hard Level so you will get 5 chances....")
    while guess!=random_number:
        guess = int(input("Guess a number : "))
        if (guess > random_number):
            print("Oops the number is too high !!")
            print("Guess Again")
            print(f"Only {chances} chances remaining")
            print("\n\n")
        elif (guess < random_number):
            print("Oops the number is too low !!")
            print("Guess Again")
            print(f"Only {chances} chances remaining")
            print("\n\n")
        elif(guess==random_number):
            print("Yes you got it !!!!....")
        if chances==0:
            print("No more chances left...")
            break
        chances -= 1







