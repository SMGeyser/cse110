country = []
code = []
year = []
age = []
data = []

with open("life-expectancy.csv") as line:
    next(line)
    for data in line:
        data = data.split(",")
        country.append(data[0])
        code.append(data[1])
        year.append(int(data[2]))
        age.append(float(data[3]))

select_year = int(input("Select a year you want to learn about: "))
in_year = []
in_country = []
in_age = []
for i in range(len(year)):
    if year[i] == select_year:
        in_year.append(year[i])
        in_country.append(country[i])
        in_age.append(age[i])
print(f"The average life expectancy across all countries in {select_year} was {(sum(in_age)/len(in_age)):.3f}")
in_most_age = 0
for i in range(len(in_age)):
    if in_age[i] > in_most_age:
        in_most_age = in_age[i]
        in_most_country = in_country[i]
        in_most_year = in_year[i]
in_least_age = in_most_age
for i in range(len(in_age)):
    if in_age[i] < in_least_age:
        in_least_age = in_age[i]
        in_least_country = in_country[i]
        in_least_year = in_year[i]
print(f"The maximum life expectancy in {in_most_year} comes from {in_most_country}. It is {in_most_age}.")
print(f"The minimum life expectancy in {in_least_year} comes from {in_least_country}. It is {in_least_age}.")


most_age = 0
for i in range(len(age)):
    if age[i] > most_age:
        most_age = age[i]
        most_country = country[i]
        most_year = year[i]
        most_code = code[i]

least_age = most_age
for i in range(len(age)):
    if age[i] < least_age:
        least_age = age[i]
        least_country = country[i]
        least_year = year[i]
        least_code = code[i]

print(f"\nThe maximum overall life expectancy comes from {most_country} in {most_year}. It is {most_age}.")
print(f"The minimum overall life expectancy comes from {least_country} in {least_year}. It is {least_age}.")
