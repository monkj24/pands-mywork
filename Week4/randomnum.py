# Generate random number from 0 to 100

#Author: Joanna Mnich

# Import the random module
import random

# Generate a random number between 0 and 100
secret_number = random.randint(0, 100)

# Initialize the number of attempts
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 0 and 100. Can you guess it?")

# Loop until the user guesses the correct number
while True:
    # Ask the user to guess
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Check if the guess is correct
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break

    