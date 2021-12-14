from uniteszt import teszt
def abszolut(p):
    if (p >= 0): return p
    else: return -p

#tesztkészlet megadása
teszt(abszolut(0) == 0)
teszt(abszolut(-1) == 1)
teszt(abszolut(1) == 1)
teszt(abszolut(10) == 10)
teszt(abszolut(-10) == 10)