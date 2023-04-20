# This program ask some elements and add to list when you push 'Enter'
# and you can finish program type 'end'


def countElem(lst):
    return len(lst)


def main():
    bufferList = []
    print("Type 'end' to end the program, or 'search' to the search element")
    while True:
        askElement = input("Enter a word: ")
        if askElement == "end":
            break
        bufferList.append(askElement)
        if askElement == "search":
            searchElem = input("Element you want to see: ")
            if searchElem in bufferList:
                index = bufferList.index(searchElem)
                print(bufferList)
                print(f"{searchElem} - {index + 1} index")
    print("Your list - ", bufferList)
    print("Elements: ", countElem(bufferList))


main()
