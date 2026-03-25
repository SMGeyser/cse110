people = [["Michael", 23],["Grace", 8],["William", 10],["Jacob", 15],["Emily", 18],["Sam", 20],["Andrew", 25],["Josh", 49],["Cassie", 46],["Margret", 1]]

for i in people:
    print(f"{i[0]} is {i[1]} years old.")

low = 999
for i in people:
    if low > i[1]:
        low = i[1]
        name = i[0]

print(f"{name} is the youngest and is {low} years old.")