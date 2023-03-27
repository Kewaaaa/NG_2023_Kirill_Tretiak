# This program ask some elements and add to list when you push 'Enter'
# and you can finish program type 'end'

def countElem(lst):
    return len(lst)


def main():
    bufferList = []
    num = 1
    while True:
        askElem = input(
            "Enter some info, or type 'end' to end the program: ")
        if askElem == "end":
            break
        bufferList.append(askElem)
    num += 1
    print("Your list - ", bufferList)
    print("Elements: ", countElem(bufferList))


main()
