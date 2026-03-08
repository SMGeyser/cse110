import random

words = ["nephi", "sarah", "ammon", "zenos", "jesus", "ether", "jacob", "lehi", "alma", "moroni", "mormon", "teancum", "mosiah", "abinadi", "samuel"]
cont = True

while cont:
    word = random.choice(words)
    word_list = list(word)
    word_len = len(word)
    win = False
    game = int(input("How many guesses would you like? "))
    print(f"Hint: ","_ " * word_len)
    g = 0
    for guesses in range(game):
        if win == True:
            win = True
        else:
            g = g + 1
            guess = input("What is your guess? ")
            guess_len = len(guess)
            guess_list = list(guess.lower())
            if guess_len != word_len:
                print("No! your guess needs to be the same length as the secret word")   
            elif guess.lower() == word:
                if g > 1:
                    print(f"YES! That is the word. It took you {g} guesses!")
                else:
                    print(f"YES! That is the word. It took you {g} guess!")
                win = True
            else:
                h = -1
                hint = []
                for n in range(word_len):
                    hint.insert(1,"_")
                for i in word_list:
                    h = h + 1
                    if i == guess_list[h]:
                        hint[h] = guess_list[h].upper()
                    elif guess_list[h] in word_list:
                        hint[h] = guess_list[h].lower()
                print("Hint:", " ".join(hint))

    if win != True:
        print("You ran out of guesses 😭\nBetter luck next time...")
    again = input("Would you like to play again? (Y or N) ")
    if again.lower() == "n":
        cont = False
    
print("goodbye!")

