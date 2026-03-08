grade = float(input("What grade percentage do you have in this class? (don't include %) "))

if grade >= 90:
    letter = "a"
elif grade >= 80:
    letter = "b"
elif grade >= 70:
    letter = "c"
elif grade >= 60:
    letter = "d"
else:
    letter = "f"

last_digit = grade % 10
if last_digit >= 7 and letter != "a" and letter != "f":
    modify = "+"
elif last_digit <= 3 and letter != "f":
    modify = "-"
else:
    modify = ""

print(f"So you have a {letter.title()}{modify} in this class!")