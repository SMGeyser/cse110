name = input("What is your name adventurer? ")
print(f"Welcome to Faerun, {name.title()}! Prepare to embark on an epic quest.")

move_on = False

# --- LEVEL 1: THE CALL TO ADVENTURE ---
C1 = input("\nYou are at the town gates. You can go to the JUNGLE, the MOUNTAINS, or the COAST.\nWhere do you travel? ")

while move_on == False:
    if "jungle" == C1.lower().strip():
        # --- LEVEL 2: THE RIVER ---
        print("\nThe jungle is humid and loud. You arrive at a raging river.")
        C2 = input("Do you attempt to SWIM across or chop trees to build a RAFT? ")
        
        while move_on == False:
            if "swim" == C2.lower().strip():
                print("The current is too strong! You are swept downstream and lose your gear. GAME OVER.")
                move_on = True
            elif "raft" == C2.lower().strip():
                # --- LEVEL 3: THE TEMPLE ENTRANCE ---
                print("\nYou build a sturdy raft and cross safely. You find a hidden Temple covered in vines.")
                C3 = input("The door is locked. Do you look for a KEY or try to PICK the lock? ")
                
                while move_on == False:
                    if "pick" == C3.lower().strip():
                        print("You trigger a poison needle trap in the lock mechanism. You faint. GAME OVER.")
                        move_on = True
                    elif "key" == C3.lower().strip():
                        # --- LEVEL 4: THE GUARDIAN ---
                        print("\nYou search the bushes and find a golden skull key! You enter the temple.")
                        C4 = input("A Stone Golem blocks the hallway! Do you FIGHT or SNEAK past it? ")
                        
                        while move_on == False:
                            if "fight" == C4.lower().strip():
                                print("Your weapons shatter against its stone skin. It crushes you. GAME OVER.")
                                move_on = True
                            elif "sneak" == C4.lower().strip():
                                # --- LEVEL 5: THE RIDDLE ROOM ---
                                print("\nYou crawl through the shadows. You enter a room with a magical talking door.")
                                C5 = input('The door asks: "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?" (Hint: A MAP)\nWhat is your answer? ')
                                
                                while move_on == False:
                                    if "map" != C5.lower().strip():
                                        print("The door laughs at you. The floor opens up and you fall into a pit. GAME OVER.")
                                        move_on = True
                                    elif "map" == C5.lower().strip():
                                        # --- LEVEL 6: THE ARTIFACT ---
                                        print("\nCorrect! The door creaks open. In the center of the room is the Crown of Command.")
                                        C6 = input("Do you put the crown on your HEAD or put it in your BAG? ")
                                        
                                        while move_on == False:
                                            if "head" == C6.lower().strip():
                                                # --- LEVEL 7: THE CURSE (FINAL) ---
                                                print("\nYou put the crown on. Ancient power flows through you!")
                                                C7 = input("The power is overwhelming. Do you CONTROL it or SUBMIT to it? ")
                                                
                                                while move_on == False:
                                                    if "control" == C7.lower().strip():
                                                        print(f"\nCongratulations {name.title()}! You mastered the artifact and became the new King of Faerun!\n------------ YOU WIN ------------")
                                                        move_on = True
                                                    elif "submit" == C7.lower().strip():
                                                        print("Your mind is erased. You become a slave to the crown forever. GAME OVER.")
                                                        move_on = True
                                                    else:
                                                        C7 = input("Invalid choice. CONTROL or SUBMIT? ")

                                            elif "bag" == C6.lower().strip():
                                                print(f"\nSmart move, {name.title()}. The crown was cursed. You sell it for 1,000,000 gold pieces!\n------------ YOU WIN ------------")
                                                move_on = True
                                            else:
                                                C6 = input("Invalid choice. HEAD or BAG? ")
                                    else:
                                        # This captures wrong riddle answers immediately if not using != logic
                                        pass 
                            else:
                                C4 = input("Invalid choice. FIGHT or SNEAK? ")
                    else:
                        C3 = input("Invalid choice. KEY or PICK? ")
            else:
                C2 = input("Invalid choice. SWIM or RAFT? ")

    elif "mountains" == C1.lower().strip():
        # A shorter path for variety
        print("\nYou climb the freezing peaks.")
        C2 = input("You find a cave. ENTER or PASS? ")
        while move_on == False:
            if "enter" == C2.lower().strip():
                print("It was a bear cave. You run away all the way back home.")
                move_on = True
            elif "pass" == C2.lower().strip():
                print("You freeze to death on the summit. GAME OVER.")
                move_on = True
            else:
                 C2 = input("Invalid choice. ENTER or PASS? ")

    elif "coast" == C1.lower().strip():
        # A shorter path for variety
        print("\nYou walk along the beautiful beach.")
        C2 = input("You see a pirate ship. SIGNAL them or HIDE? ")
        while move_on == False:
            if "signal" == C2.lower().strip():
                print("They capture you and make you scrub the deck. GAME OVER.")
                move_on = True
            elif "hide" == C2.lower().strip():
                print("They leave behind a chest of gold! You are rich!")
                move_on = True
            else:
                C2 = input("Invalid choice. SIGNAL or HIDE? ")
    
    else:
        # Loop resets if C1 is invalid
        C1 = input("Invalid answer. Please choose JUNGLE, MOUNTAINS, or COAST: ")

print("------------ GAME OVER ------------")