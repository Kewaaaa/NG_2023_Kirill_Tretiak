def romb(n, empty=5):
    print(" " * empty, "*" * n)
    if n < 10:
        romb(n + 2, empty - 1)
    print(" " * empty, "*" * n)


romb(1)
