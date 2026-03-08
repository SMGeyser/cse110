cont = True
import random

while cont:
    num = random.randint(1,100)
    guess = False
    n = 0
    while not guess:
        n = n + 1
        user = float(input("Guess the magic number!! "))
        if user == num:
            print(f"YES! {num} is the magic number!")
            print(f"It took you {n} guesses!")
            guess = True
        elif user > num:
            print("No, the number is lower.")
        else:
            print("No, the magic number is higher.")
    play = input("Would you like to play again? (Y or N) ")
    if play.lower().strip() == "n":
        cont = False

print("Goodbye!")
