import random

computer_guess = random.randint(1,100)
print(computer_guess)

user_name = input("Give me your name, human:\n")

print("Prepare to lose,", user_name, ". I am thinking of a number between 1 and 100.")

def guessing():
    guess = int(input("Your guess: "))
    if guess > computer_guess:
        print("Your guess is too high. Try again")
        guessing()
    elif guess < computer_guess:
        print("Your guess is too low. Try again")
        guessing()
    elif guess == computer_guess:
        print("You guessed it. You are the superior being")

guessing()