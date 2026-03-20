name = []
id = []
job = []
pay = []

with open("hr_system.txt") as line:
    for items in line:
        items = items.split(" ")
        name.append(items[0])
        id.append(items[1])
        job.append(items[2])
        pay.append(items[3])

for i in range(len(name)):
    print(f"{name[i]:10} (ID: {id[i]}), {job[i]:10} - ${pay[i]}")