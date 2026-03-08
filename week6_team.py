
height_one = int(input("How tall are you? (in inches) "))
age_one = int(input("How old are you? "))

if age_one < 18 and age_one >= 12:
    pass_one = input("do you have the golden passport?? (YES or NO) ")
    if pass_one.lower().strip() == "yes":
        age_one = 18

preg_one = input("Are you pregnant? (YES or NO) ")
if age_one >= 60:
    print("Sorry boomer. We don't want you to break your back...")
elif preg_one.lower().strip() == "yes":
    print("You should probably go home and no hurt your baby then")
else:
    riders = input("Is there going to be a second rider? (YES or NO) ")

    if riders.lower().strip() == "no":
        if height_one < 36:
            print("Sorry short stuff. You can't ride :(")
        elif height_one >= 62 and age_one >= 18:
            print("Welcome! Please keep your hands and feet inside the ride at all times. (P.S. don't die)")
        else:
            print("Sorry, you may not ride by yourself.")
    else:
        height_two = int(input("How tall is the second rider? "))
        age_two = int(input("How old is the second rider? "))
        if age_two < 18 and age_two >= 12:
            pass_two = input("Does the second rider have a golden passport? (YES or NO) ")
            if pass_two.lower().strip() == "yes":
                age_two = 18
        preg_two = input("Is the second rider pregnant?? (YES or NO) ")
        if age_two >= 60:
            print("Sorry, probably send Grandpa home before you ride")
        elif preg_two.lower().strip() == "yes":
            print("Yeah... So she can't ride then.")
        elif height_one < 36 or height_two < 36:
            print("Sorry short stuff. You can't ride")
        elif age_one >= 18 or age_two >= 18:
            print("Welcome! Please keep your hands and feet inside the ride at all times.")
        elif age_one and age_two < 18:
            if (age_one and age_two > 12) and (height_one and height_two >= 52):
                print("You're young, but you will be fine going together")
            elif (age_one and age_two >= 14) and (age_one or age_two >= 16):
                print("Welcome teens. don't do anything dumb")
            else:
                print("Sorry kiddos. you got to be this tall to ride")
        
        else:
            print("Sorry you must have an adult to ride with you.")