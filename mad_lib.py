
user = input("Hey there! What's your name? ")
print(f"Hi {user.title()}! We are going to make a story together!!\nI just need your help with some of the words. Okay?")

noun1 = input("Give me a random animal. ")
pverb1 = input("OK, now a past tense verb. ")
noun2 = input("now a random noun. ")
adj1 = input("Can you give me your favorite adjective? ")
pnoun1 = input("Sweet! Can I get a plural noun? ")
pnoun2 = input("And another plural noun to go with it? ")
emotion1 = input("Name an emotion. ")
## pverb2 = input("Ok ok, another past tense verb. ") decided i didn't want it
noun3 = input("Now think of another noun. ")
food = input("What is your favorite food? ")
verb1 = input("Oooo, that's a good one! Now what's a good verb? ")
noun4 = input("Can you give me one more noun? ")
pnoun3 = input("And a final plural noun? ")
## pverb3 = input("Almost done. give me another past tense verb. ") could do w/out it we'll see
## noun5 = input("Ok, to finish off the story. one last noun! ") didn't need this one either

ready = input("Alright! are you ready?? ").lower().strip()
if ready == "yes":
    print("OK! here it is!!")
else:
    print("Ready or not here is your story!!")


print(f"the {noun1} {pverb1} the {noun2} and went to buy {adj1} {pnoun1} and {pnoun2}.\nWhen the {noun1} got there he found all of the {pnoun2} were gone!\nThe {noun1} was filled with {emotion1}!!\nInstead of eating {food} that night, he decided to just {verb1} his {noun4}.\nWhen suddenly {pnoun3} broke into the house and stole all of his stuff!")