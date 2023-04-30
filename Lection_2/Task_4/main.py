library = {
    "Book_1": {
        "Title": "Sherlock Holmes",
        "Author": "Arthur Conan Doyle",
        "Pages": "1392",
        "Genre": "Crime, Thriller & Mystery",
        "Book binding": "Soft",
    },
    "Book_2": {
        "Title": "Harry Potter",
        "Author": "Joanne Rowling",
        "Pages": "300",
        "Genre": "Fantasy",
        "Book binding": "Hard",
    },
    "Book_3": {
        "Title": "Biblia",
        "Author": "Jesus",
        "Pages": "666",
        "Genre": "Fantasy, thriller",
        "Book binding": "Hard",
    },
}
print("Your library")
for books, booksInfo in library.items():
    print(books)
    booksName = booksInfo["Title"]
    authorName = booksInfo["Author"]
    booksPages = booksInfo["Pages"]
    booksGenre = booksInfo["Genre"]
    booksBinding = booksInfo["Book binding"]
    print(f"Title - {booksName}")
    print(f"Author - {authorName}")
    print(f"Pages - {booksPages}")
    print(f"Genre - {booksGenre}")
    print(f"Binding - {booksBinding}")
print("Menu:\n1.Add book.\n2.Delete book.\n3.Edit book.\n4.Find book.")
choise = int(input("Choose the action[choose number]: "))
if choise < 0 or choise > 4:
    print("You chose wrons action!")

bufferDict = {}
count = len(library) + 1
match choise:
    case 1:
        while True:
            name = input("Enter the title of the book: ")
            bufferDict["Title"] = name
            author = input("Enter the author: ")
            bufferDict["Author"] = author
            page = input("Enter numer of pages: ")
            bufferDict["Pages"] = page
            genre = input("Enter a genre of book: ")
            bufferDict["Genre"] = genre
            binding = input("Enter a boob binding (soft/hard): ")
            bufferDict["Book binding"] = binding
            getAnswer = input("If you add all books please type 'exit': ")
            newKey = f"Book_{count}"
            count += 1
            library[newKey] = bufferDict
            bufferDict = {}
            if getAnswer == "exit":
                break
    case 2:
        deleteBook = input("Which book you want to delete[number of book]: ")
        del library[f"Book_{deleteBook}"]
    case 3:
        editBook = input("Which book you want to edit[number of book]: ")
        print(library[f"Book_{editBook}"])
        editBookContent = input(
            "What you want to change[enter like 'Title']: ")
        if editBookContent == "Title":
            editTitle = input("Enter new title: ")
            library[f"Book_{editBook}"]["Title"] = editTitle
            for k, v in library[f"Book_{editBook}"].items():
                print(k, "-", v)
        if editBookContent == "Author":
            editAuthor = input("Change author: ")
            library[f"Book_{editBook}"]["Author"] = editAuthor
            for k, v in library[f"Book_{editBook}"].items():
                print(k, "-", v)
        if editBookContent == "Pages":
            editPages = input("Change number of pages: ")
            library[f"Book_{editBook}"]["Pages"] = editPages
            for k, v in library[f"Book_{editBook}"].items():
                print(k, "-", v)
        if editBookContent == "Genre":
            editGenre = input("Change genre: ")
            library[f"Book_{editBook}"]["Genre"] = editGenre
            for k, v in library[f"Book_{editBook}"].items():
                print(k, "-", v)
    case 4:
        for i in range(1, len(library) + 1):
            print("-------------")
            print(
                library[f"Book_{i}"]["Title"], "-", library[f"Book_{i}"]["Pages"], "pages"
            )
        print("-------------")
        findBook = input(
            "Whick book you want to see all information[enter number]: ")
        for k, v in library[f"Book_{findBook}"].items():
            print(k, "-", v)
        print("--------------------")
print("Your library")
for books, booksInfo in library.items():
    print(books)
    booksName = booksInfo["Title"]
    authorName = booksInfo["Author"]
    booksPages = booksInfo["Pages"]
    booksGenre = booksInfo["Genre"]
    booksBinding = booksInfo["Book binding"]
    print(f"Title - {booksName}")
    print(f"Author - {authorName}")
    print(f"Pages - {booksPages}")
    print(f"Genre - {booksGenre}")
    print(f"Binding - {booksBinding}")
