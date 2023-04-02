firstNumberForCalc = int(input("Enter first number: "))
secondNumberForCalc = int(input("Enter second number: "))
symbolForCalc = input("Which operation u want: ")
match symbolForCalc:
    case "+":
        result = firstNumberForCalc + secondNumberForCalc
    case "-":
        result = firstNumberForCalc - secondNumberForCalc
    case "*":
        result = firstNumberForCalc * secondNumberForCalc
    case "^":       # "^" - exponentiation
        result = firstNumberForCalc ** secondNumberForCalc
    case "/":
        try:
            result = firstNumberForCalc / secondNumberForCalc
        except ZeroDivisionError:
            result = "You can't division by zero"
    case "&":       # "&" - root of number
        result = firstNumberForCalc ** (1/secondNumberForCalc)
print("Result: " + str(result))
