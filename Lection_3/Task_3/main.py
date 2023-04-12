def addBook(addNewBook):
    print("Adding new book")
    name = input("Enter the title of the book: ")
    addNewBook["Title"] = name
    author = input("Enter the author: ")
    addNewBook["Author"] = author
    page = input("Enter number of pages: ")
    addNewBook["Pages"] = page
    genre = input("Enter a genre of book: ")
    addNewBook["Genre"] = genre
    binding = input("Enter a book binding (soft/hard): ")
    addNewBook["Book binding"] = binding
    return addNewBook


def deleteBook(delBook):
    deleteBook = input("Which book you want to delete: ")
    for i in range(1, len(delBook)+1):
        if deleteBook in delBook[f"Book_{i}"]["Title"]:
            del delBook[f"Book_{i}"]
            break
    return delBook


def editingBook(editBook):
    choose = input("Which book you want to edit: ")
    for i in range(1, len(editBook)+1):
        if choose in editBook[f"Book_{i}"]["Title"]:
            bookContent = input("Enter what you want to change: ")
            change = input("Rename: ")
            editBook[f"Book_{i}"][bookContent] = change
    return editBook


def findingBook(findBook):
    for i in range(1, len(findBook) + 1):
        print("-------------")
        print(findBook[f"Book_{i}"]["Title"],
              "-", findBook[f"Book_{i}"]["Pages"], "pages")
    print("-------------")
    find = input("Whick book you want to see: ")
    print("About book:")
    for i in range(1, len(findBook)+1):
        if find in findBook[f"Book_{i}"]["Title"]:
            print("Title -", findBook[f"Book_{i}"]["Title"])
            print("Author -", findBook[f"Book_{i}"]["Author"])
            print("Pages -", findBook[f"Book_{i}"]["Pages"])
            print("Genre -", findBook[f"Book_{i}"]["Genre"])
            print("Book binding -", findBook[f"Book_{i}"]["Book binding"])


# Func for check all keys in dict after deleted book
def checkAllKeys(lib):
    newDict = {}
    for j, key in enumerate(lib.keys()):
        newKey = f"Book_{j+1}"
        newDict[newKey] = lib[key]
    return newDict


# Func for showing all book in better view
def showAllBooks(allBooks):
    for books, booksInfo in allBooks.items():
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


def main():
    library = {

        "Book_1": {
            "Title": "Sherlock Holmes",
            "Author": "Arthur Conan Doyle",
            "Pages": "1392",
            "Genre": "Crime, Thriller & Mystery",
            "Book binding": "Soft"
        },

        "Book_2": {
            "Title": "Harry Potter",
            "Author": "Joanne Rowling",
            "Pages": "300",
            "Genre": "Fantasy",
            "Book binding": "Hard"
        },

        "Book_3": {
            "Title": "Biblia",
            "Author": "Jesus",
            "Pages": "666",
            "Genre": "Fantasy, thriller",
            "Book binding": "Hard"
        }

    }

    while True:
        try:
            print("Menu:\n1.Add book.\n2.Delete book.\n3.Edit book.\n4.Find book.")
            choise = int(input("Choose the action: "))
        except ValueError:
            print("Error: You entered wrong value!")
            exit(1)
        if choise == 1:
            correct_keys = checkAllKeys(library)
            library = correct_keys
            bufferDict = {}
            new_book = addBook(bufferDict)
            count = len(correct_keys) + 1
            library[f"Book_{count}"] = new_book
            showAllBooks(correct_keys)
        if choise == 2:
            correct_keys = checkAllKeys(library)
            showAllBooks(correct_keys)
            update_lib = deleteBook(correct_keys)
            library = update_lib
            showAllBooks(correct_keys)
        if choise == 3:
            correct_keys = checkAllKeys(library)
            showAllBooks(correct_keys)
            edit_book_in_lib = editingBook(correct_keys)
            library = edit_book_in_lib
            showAllBooks(correct_keys)
        if choise == 4:
            correct_keys = checkAllKeys(library)
            findingBook(correct_keys)


main()
