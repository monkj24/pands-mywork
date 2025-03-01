# Program modified to tell user if choosen number is to high or to low


numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else: 
        print("Too high")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was", numberToGuess)