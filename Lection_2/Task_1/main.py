# This program ask some elements and add to list when you push 'Enter'
# and you can finish program type 'end'

def countElem(lst):
    return len(lst)


def main():
    bufferList = []
    num = 1
    while True:
        askElement = input(
            "Enter some info, or type 'end' to end the program: ")
        if askElement == "end":
            break
        bufferList.append(askElement)
    num += 1
    print("Your list - ", bufferList)
    print("Elements: ", countElem(bufferList))


main()
