scripture = []
chapters = []
book = []

with open("books_and_chapters.txt") as line:
    next(line)
    for data in line:
        data = data.split(":")
        scripture.append(data[0])
        chapters.append(data[1])
        book.append(int(data[2]))

for i in range(len(scripture)):
    print(f"Scripture: {scripture[i]}, Book: {book[i]}, Chapters: {chapters[i]}")