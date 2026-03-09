names = []

with open("books.txt") as lines:
    for i in lines:
        print(f"{i.strip()}")