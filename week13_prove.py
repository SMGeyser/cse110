import math

def wind_chill(T, V):
    F = 35.74 + 0.6215*T - 35.75*(V**0.16) + 0.4275*T*(V**0.16)
    return F

def convert(T):
    F = T*(9/5) + 32
    return F

done = False
while not done:

    temp = float(input("What is the temperature? "))
    type = input("Is it in °F or °C? (F/C) ")

    if type.lower() == "c":
        temp = convert(temp)

    final = 1
    for i in range(5, 61, 5):
        print(f"At {temp}°F and a windspeed of {i}MPH, the windchill will be {wind_chill(temp, i):.2F}°F")

    finished = input("Would you like to test another temperature? (Y/N) ")
    if finished.lower().strip() == "n":
        done = True