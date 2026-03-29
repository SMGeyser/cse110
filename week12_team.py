scripture = []
chapters = []
book = []

with open("books_and_chapters.txt") as line:
    for data in line:
        data = data.strip().split(":")
        scripture.append(data[2])
        chapters.append(int(data[1]))
        book.append((data[0]))

for i in range(len(scripture)):
    print(f"Scripture: {scripture[i]}, Book: {book[i]}, Chapters: {chapters[i]}")

high = chapters[0]
for i in range(len(chapters)):
    if high < chapters[i]:
        high = chapters[i]
        high_book = book[i]

print(f"The highest amount of chapters is from the book of {high_book} with {high} chapters.")

choice = input("Which book would you like to learn more about? (BoM, OT, NT, D&C, PoGP) ")

if choice.strip().lower() == "bom":
    bom = []
    bom_chap = []
    high_bom = 0
    for i in range(len(scripture)):
        if scripture[i].strip().lower() == "book of mormon":
            bom.append(book[i])
            bom_chap.append(chapters[i])
    for i in range(len(bom)):
        if high_bom < bom_chap[i]:
            high_bom = bom_chap[i]
            high_bom_book = bom[i]
    print(f"The book with the most chapters in the Book of Mormon is {high_bom_book} with {high_bom} chapters")
if choice.strip().lower() == "ot":
    ot = []
    ot_chap = []
    high_ot = 0
    for i in range(len(scripture)):
        if scripture[i].strip().lower() == "old testament":
            ot.append(book[i])
            ot_chap.append(chapters[i])
    for i in range(len(ot)):
        if high_ot < ot_chap[i]:
            high_ot = ot_chap[i]
            high_ot_book = ot[i]
    print(f"The book with the most chapters in the Old Testament is {high_ot_book} with {high_ot} chapters")
if choice.strip().lower() == "nt":
    nt = []
    nt_chap = []
    high_nt = 0
    for i in range(len(scripture)):
        if scripture[i].strip().lower() == "new testament":
            nt.append(book[i])
            nt_chap.append(chapters[i])
    for i in range(len(nt)):
        if high_nt < nt_chap[i]:
            high_nt = nt_chap[i]
            high_nt_book = nt[i]
    print(f"The book with the most chapters in the New Testament is {high_nt_book} with {high_nt} chapters")
if choice.strip().lower() == "d&c":
    dc = []
    dc_chap = []
    high_dc = 0
    for i in range(len(scripture)):
        if scripture[i].strip().lower() == "doctrine and covenants":
            dc.append(book[i])
            dc_chap.append(chapters[i])
    for i in range(len(dc)):
        if high_dc < dc_chap[i]:
            high_dc = dc_chap[i]
            high_dc_book = dc[i]
    print(f"The book with the most chapters in the Doctrine and Covenants is {high_dc_book} with {high_dc} chapters")
if choice.strip().lower() == "pogp":
    pogp = []
    pogp_chap = []
    high_pogp = 0
    for i in range(len(scripture)):
        if scripture[i].strip().lower() == "pearl of great price":
            pogp.append(book[i])
            pogp_chap.append(chapters[i])
    for i in range(len(pogp)):
        if high_pogp < pogp_chap[i]:
            high_pogp = pogp_chap[i]
            high_pogp_book = pogp[i]
    print(f"The book with the most chapters in the Pearl of Great Price is {high_pogp_book} with {high_pogp} chapters")

        