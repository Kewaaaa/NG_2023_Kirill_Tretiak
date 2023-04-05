def actionOfOperation(action, value1, value2):
    match action:
        case "+":
            result = value1 + value2
        case "-":
            result = value1 - value2
        case "*":
            result = value1 * value2
        case "^":
            result = value1 ** value2
        case "/":
            try:
                result = value1 / value2
            except ZeroDivisionError:
                result = "You can't division by zero"
        case "&":
            result = value1 ** (1/value2)
    return result


def askOperation(message):
    return input(message)


def askNums(message):
    return float(input(message))


def main():
    firstNum = askNums("Enter first value: ")
    secondNum = askNums("Enter second value: ")
    print("'+' - plus\n'-' - minus\n'*' - multiply\n'/' - divide\n'^' - exponentiation\n'&' - square root")
    operation = askOperation("Enter an operation: ")
    print(actionOfOperation(operation, firstNum, secondNum))


main()
