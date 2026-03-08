print("put the numbers in the list. ok?")
zero = False
list = []

while not zero:
    num = int(input("Enter a number: "))
    if num == 0:
        zero = True
    else:
        list.append(num)

sum = 0
for item in list:
    sum += item
print(f"The sum is: {sum}")

print(f"The average is: {sum/len(list)}")

max = list[0]
for item in list:
    if item > max:
        max = item
print(f"The max number is: {max}")

min = list[0]
for item in list:
    if (item > 0) and (item < min):
        min = item
print(f"The min number is: {min}")

for item in sorted(list):
    print(item)