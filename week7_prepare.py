negative = True

while negative:
    number = float(input("Pick a positive number: "))
    if number >= 0:
        print(f"your number is {number}")
        negative = False
    else:
        print("No, pick a postitive number.")

