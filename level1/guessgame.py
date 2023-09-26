# a Guess game with random numbers
import random

while True:
    print('>> I am thinking of a number from 1 to 10, try to guess!')
    randomNumber = random.randint(1, 10)
    
    try: guess = int(input("Your Guess: "))
    except: guess = 0
        
    if guess == randomNumber:
            print('Correct! You got it right!')
            break
    else:
            print('Too bad! Wrong guess!')
    
    play_again = input("Do you want to try again? (yes/no): ").lower()
    if play_again != "yes":
        break