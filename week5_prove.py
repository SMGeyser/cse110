end = "yes"
name = input("What is your name adventurer? ")
print(f"Welcome to Faerun, {name.title()}! Prepare to embark on an adventure.")

while end.lower().strip() == "yes":
    # C means choice. i.e. C1 = choice 1, C2 = choice 2, etc...
    move_on = False #I'll use this to determine if they said a real option

    C1 = input("You find yourself in the tavern awaiting some fun adventure to come your way!\n\nYou have been waiting a while, so you could either LEAVE or go talk with the man in the CORNER.\nWhat is your choice? ")
    while not move_on:
        if "leave" == C1.lower().strip():
            C2 = input("\nYou walk outside the Tavern and notice a man watching you as you get up.\nHe gets up to follow you as you leave the Tavern.\nAre you going to RUN when you get out the door or CONFRONT the man outside the door? ")
            while not move_on:
                if "run" == C2.lower().strip():
                    C3 = input("\nYou begin to run away like a coward and the man chases after you.\nDo you run FASTER? or stop and FIGHT? ")
                    while not move_on:
                        if "faster" == C3.lower().strip():
                            print(f"Wow {name.title()}! You are a coward. You get away I guess, but that wasn't fun at all!!")
                            move_on = True
                        elif "fight" == C3.lower().strip():
                            C4 = input("\nYes! You turn and confront your foe head on!! This battle will be Epic.\nDo you draw your BOW, your short SWORD, or DAGGERS? ")
                            while not move_on:
                                if "bow" == C4.lower().strip():
                                    print("You pull out your bow, but the man is too close for it to be useful!\nOH NO!! He jumps you and you get unalived...")
                                    move_on = True
                                elif "sword" == C4.lower().strip():
                                    print("Yes!! You pull your sword from its sheath and disarm (literally) the man. YOU WIN!!!!")
                                    move_on = True
                                elif "daggers" == C4.lower().strip():
                                    print(f"Exellent choice {name.title()}! You quikcly throw one dagger distracting the man and then jab with the other!\nYou take down the man and the city is safe again!")
                                    move_on = True
                                else:
                                    move_on = False
                                    C4 = input("Invalid answer. Try again: ")
                        else:
                            move_on = False
                            C3 = input("Invalid answer. Try again: ")
                elif "confront" == C2.lower().strip():
                    C3 = input("\nYou confront your enemy and gain the initiative!\nDo you step back to pull out your BOW, draw your short SWORD, or pull out your DAGGERS? ")
                    while not move_on:
                        if "bow" == C3.lower().strip():
                            C4 = input("\nYou step back to draw out your bow and the man rushes you.\nShoot your bow from CLOSE range or try to fun back to get a shot from FAR away? ")
                            while not move_on:
                                if "close" == C4.lower().strip():
                                    print("Quick thinking! you are able to wound him and he run down an alleyway instead of trying anymore funny buisness.\nYOU WIN!!")
                                    move_on = True
                                elif "far" == C4.lower().strip():
                                    print("You try to step back further to get a good shot on your foe, but he rushes forward with inhuman speed.\nHe quickly stuns you with a small ornate dagger and you are left powerless...")
                                    move_on = True
                                else:
                                    move_on = False
                                    C4 = input("Invalid answer. Try again: ")
                        elif "sword" == C3.lower().strip():
                            print("Using your sword you are able to knock a small ornate dagger from the man's hand and he puts up his hands in surrender.\nYOU WIN!!!")
                            move_on = True
                        elif "daggers" == C3.lower().strip():
                            C4 = input("\nWith your daggers you are able to jab at your foe, but his armor blocks your blow. He draws his sword.\nDo you STRIKE again or side step to DODGE his sword? ")
                            while not move_on:
                                if "strike" == C4.lower().strip():
                                    print("You go in to strike again, but his armor seems relentless.\nAs you attempt to pierce his side, he knocks you down with the hilt of his sword.\nYou are now under his power...")
                                    move_on = True
                                elif "dodge" == C4.lower().strip():
                                    print("You narrowly avoid his sword strike and see an opening in the side of his armor!\nYou plunge in your dagger and stun your foe.\nYOU WIN!")
                                    move_on = True
                                else:
                                    move_on = False
                                    C4 = input("Invalid answer. Try again: ")
                        else:
                            move_on = False
                            C3 = input("Invalid answer. Try again: ")
                else:
                    move_on = False
                    C2 = input("Invalid answer. Try again: ")
        elif "corner" == C1.lower().strip():
            C2 = input("\nYou aproach the man in the corner and he asks you what you seek.\nDo you want HONOR or an ADVENTURE? ")
            while not move_on:
                if "honor" == C2.lower().strip():
                    C3 = input("\nThe man tells you that you must do something great to find honor in this world.\nHe asks if you would like to join him to defend the city from an upcoming attack.\nWill you HELP him or DENY him? ")
                    while not move_on:
                        if "help" == C3.lower().strip():
                            print(f"He thanks you for your willingness and asks you to follow him.\nYou find yourself in a life of service to the people of the city!")
                            move_on = True
                        elif "deny" == C3.lower().strip():
                            print(f'"\nIf you want true honor, {name.title()}, you must be willing to sacrifice for something\ngreater than yourself" the man tells you.\n"Come back when you are ready"')
                            C4 = input("Will you LEAVE or apologize and ACCEPT his offer? ")
                            while not move_on:
                                if "leave" == C4.lower().strip():
                                    print("Your loss...")
                                    move_on = True
                                elif "accept" == C4.lower().strip():
                                    print("Wonderful. You follow your new found mentor to a life of service!")
                                    move_on = True
                                else:
                                    move_on = False
                                    C4 = input("Invalid answer. Try again: ")
                        else:
                            move_on = False
                            C3 = input("Invalid answer. Try again: ")
                elif "adventure" == C2.lower().strip():
                    C3 = input("\nFantastic! I love a good adventure.\nWhat are you seeking in return for your quest?\nFAME, GOLD, MAGIC items, or KNOWLEDGE? ")
                    while not move_on:
                        if "fame" == C3.lower().strip():
                            C4 = input("\nI am going with my band of adventurers to slay the black dragon that has been tormenting our city.\nWould you like to join us and find the fame you seek?\nYES or NO? ")
                            while not move_on:
                                if "yes" == C4.lower().strip():
                                    print("Exellent! We will leave in the morning.")
                                    move_on = True
                                elif "no" == C4.lower().strip():
                                    print("Ok. Then why did you come to me?\nHave a good day sir.")
                                    move_on = True
                                else:
                                    move_on = False
                                    C4 = input("Invalid answer. Try again: ")
                        elif "gold" == C3.lower().strip():
                            C4 = input("\nI am going with my band of adventurers to slay the black dragon.\nI can promise you 500gp as a reward for helping us. Will you accept?\nYES or NO? ")
                            while not move_on:
                                if "yes" == C4.lower().strip():
                                    print(f"Exellent {name.title()}! We will leave at daybreak.")
                                    move_on = True
                                elif "no" == C4.lower().strip():
                                    print("Ok. Then why did you come to me?\nHave a good day sir.")
                                    move_on = True
                                else:
                                    move_on = False
                                    C4 = input("Invalid answer. Try again: ")
                        elif "magic" == C3.lower().strip():
                            C4 = input("\nI am going with my band of adventurers to slay the tormenting black dragon.\nI can promise you a great prize of magic in the dragon's horde! Will you accept?\nYES or NO? ")
                            while not move_on:
                                if "yes" == C4.lower().strip():
                                    print("Amazing! We will leave at dawn.")
                                    move_on = True
                                elif "no" == C4.lower().strip():
                                    print("Ok. Then why did you come to me?\nHave a good day sir.")
                                    move_on = True
                                else:
                                    move_on = False
                                    C4 = input("Invalid answer. Try again: ")
                        elif "knowledge" == C3.lower().strip():
                            C4 = input("\nI am leaving to slay the black dragon with my small band of adventurers.\nI have this tome of greater knowledge as a reward for you to help us.\nWill you help us? YES or NO? ")
                            while not move_on:
                                if "yes" == C4.lower().strip():
                                    print(f"Exellent {name.title()}! We will leave after this night.")
                                    move_on = True
                                elif "no" == C4.lower().strip():
                                    print("Ok. Then why did you come to me?\nHave a good day sir.")
                                    move_on = True
                                else:
                                    move_on = False
                                    C4 = input("Invalid answer. Try again: ")
                        else:
                            move_on = False
                            C3 = input("Invalid answer. Try again: ")
                else:
                    move_on = False
                    C2 = input("Invalid answer. Try again: ")
        else:
            move_on = False
            C1 = input("Invalid answer. Try again: ")

    print("------------THE END------------")

    end = input("\nWould you like to play again?\nYES or NO? ")
    if "yes" == end.lower().strip():
        print("\nOk! Let's go again!\n")
    else:
        print(f"Goodbye {name.title()}!!")