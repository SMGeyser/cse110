import math
side = int(input("pick a length for the sid of your objects: "))

square = side ** 2
cube = side ** 3
circle = math.pi * (side**2)
sphere = 4 * math.pi * (side**2)

print(f"with a side length of {side}in. you could make a square with an area of {round(square, 2)}in\u00b2")
print(f"having a side length of {side}in. your cube would have a volume of {round(cube, 2)}in\u00b3")
print(f"if the radius of a circle was {side}in. the area of the circle would be {round(circle, 2)}in\u00b2")
print(f"if we had a sphere with the radius of {side}in. it's volume would then be {round(sphere, 2)}in\u00b3")

side2 = int(input("now pick another side length: "))

rectangle = side * side2

print(f"ok. with sides of {side}in. and {side2}in. you can make a rectangle with an area of {round(rectangle, 2)}in\u00b2")

side_ft = side / 12
cube_ft = side_ft ** 3
sphere_ft = 4 * math.pi * (side_ft**2)

print(f"that cube with the first side would have a volume of {round(cube_ft, 2)}ft\u00b3")
print(f"the sphere's volume in feet is {round(sphere_ft,2)}ft\u00b3")