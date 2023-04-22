def romb(star, empty=5):
    print(" " * empty, "*" * star)
    if star < 10:
        romb(star + 2, empty - 1)
    print(" " * empty, "*" * star)


romb(1)
