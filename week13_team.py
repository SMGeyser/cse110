import math

def compute_area(shape, side1, side2):
    if shape.lower() == "circle":
        print(f"The area is {((float(side1)**2) * math.pi)}")
    elif shape.lower() == "square":
        print(f"The area is {float(side1)**2}")
    elif shape.lower() == "rectangle":
        print(f"The area is {float(side1) * float(side2)}")
    elif shape.lower() == "triangle":
        print(f"The area is {(float(side1) * float(side2)) / 2}")
    else:
        print("Sorry that isn't a valid shape.")

done = False
while not done:
    choice = input("What shape do you want the area of? (Circle, Square, Rectangle, or Triangle) ")
    length1 = 1
    length2 = 1

    if choice.lower() == "circle" :
        length1 = input("How long is the radius? ")
    elif choice.lower() == "square":
        length1 = input("How long is the side? ")
    elif choice.lower() == ("rectangle" or "triangle"):
        length1 = input("How long is the base? ")
        length2 = input("How long is the height? ")

    compute_area(choice, length1, length2)

    finished = input("Would you like to compute the area of another shape? (Y/N) ")
    if finished.lower() == "n":
        done = True
print("Goodbye!")