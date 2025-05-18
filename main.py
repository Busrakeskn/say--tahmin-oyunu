import random


print("Welcome to the number guessing game! You have 5 attempts.")


number = random.randint(0,50)
number_of_guesses = 0

while number_of_guesses < 5:
    print("Guess a number between 1 and 50: ")
    guess = input()
    guess = int(guess)
    number_of_guesses +=1

    if guess == number:
        break 
    elif number_of_guesses == 5:
        break
    else:
        print("Nope! Try again.")


# clue
if guess == number:
    print("Correct! You guessed the number in " + str(number_of_guesses) + "tries.")
else:
    print("You did not guess the number! The number was " + str(number) + "." )