def romb(space, stars = 1):
    print(" " * space, "*" * stars)
    if stars <= space:
        romb(space-1, stars + 2)
    print(" " * space, "*" * stars)


size = int(input("Size: "))
romb(size)
