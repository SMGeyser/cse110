scripture = []
chapters = []
book = []

with open("books_and_chapters.txt") as line:
    for data in line:
        data = data.split(":")
        scripture.append(data[0])
        chapters.append(int(data[1]))
        book.append((data[2]))

for i in range(len(scripture)):
    print(f"Scripture: {scripture[i]}, Book: {book[i]}, Chapters: {chapters[i]}")