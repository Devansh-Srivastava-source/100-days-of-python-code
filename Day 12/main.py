from art import logo
import random

print(logo)
print("Welcome to the game! There is a random number from 1 to 100 and you have to guess.")
#First block ---------
difficulty = input("Choose the difficulty: Easy or Hard?\n").lower()
attempts = 0
while True:
    if difficulty == "easy":
        attempts = 10
        break
    elif difficulty == "hard":
        attempts = 5
        break
    else:
        print("Invalid choice! Try again.")
        continue
print(f"Great! You have {attempts} lives.")
#-------------------
#Second Block -----------------
ran_num = random.randint(1,100)
while attempts != 0:
    guess = int(input("Guess number: "))
    if guess == ran_num:
        print("Bravo! You got it right.")
        break
    elif guess < ran_num:
        print("Too low")
    elif guess > ran_num:
        print("Too high")
    attempts -= 1. #Every chance decreases the attempts
    print(f"You have {attempts} guesses left.")

if attempts == 0:
    print("You lose! All lives are over.")
