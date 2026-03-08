import math
print("Let's find the velocity of an object! please enter the following info.")

m = float(input("Mass (Kg): "))
g = float(input("Gravity in m/s\u00B2: "))
t = float(input("Time (seconds): "))
p = float(input("Density of fluid (in Kg/m\u00B3, 1.3 for air, 1000 for water: ): "))
A = float(input("Cross sectional area (in m\u00B2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

c= (1/2) * p * A * C
v = math.sqrt((m * g) / c) * (1 - math.exp((-1 * t * math.sqrt(m * g * c)) / m))

print(f"Inner c value is: {round(c, 3)}")
print(f"The Velocity after {round(t, 1)} sec is: {round(v, 3)} m/s")