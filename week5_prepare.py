first = int(input("Pick a number: "))
second = int(input("Pick another number: "))

if first > second:
    print(f"{first} is greater than {second}!")
else:
    print(f"{first} is not greater than {second}...")

if second > first:
    print(f"{second} is greater than {first}!!")
else:
    print(f"{second} is NOT greater than {first}.")

if first == second:
    print(f"{first} is the SAME as {second}")
else:
    print("Those numbers are not equal.")

animal = input("What is your favorite animal?? ")

if animal.lower().strip() == "platypus":
    print("No way!! Platypus is my favorite animal too!")
else:
    print(f"Sorry. I don't like {animal}s...")