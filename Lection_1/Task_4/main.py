a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter thrid number: "))
print("Your equathion:")
if b > 0:
    firstHalf = (str(a) + "x^2" + "+" + str(b) + "x")
elif b < 0:
    firstHalf = (str(a) + "x^2" + str(b) + "x")
if c < 0:
    print(firstHalf + str(c) + " = 0")
elif c > 0:
    print(firstHalf + "+" + str(c) + " = 0")
descriminant = ((b**2) - (4 * a * c))
print("D = " + str(descriminant))
if int(descriminant) > 0:
    x1 = (-b + (descriminant ** (1/2))) / (2 * a)
    print(x1)
    x2 = (-b - (descriminant ** (1/2))) / (2 * a)
    print(x2)
elif int(descriminant) < 0:
    print("Your equathion have no roots")
elif int(descriminant) == 0:
    x = (-b / (2 * a))
    print(x)
