def osszeg(n):
    ered = 0
    for i in range(n + 1):
        ered += i

    return ered

print(osszeg(10))
