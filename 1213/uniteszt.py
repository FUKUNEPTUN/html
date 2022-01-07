import sys
def teszt(teszteset):
    sorszam = sys._getframe(1).f_lineno #visszaadja a hívó sorának sorszámát.
    if teszteset:
        msg =" A(z) {0}. sorban álló teszt sikeres".format(sorszam)
    else:
        msg =" A(z) {0}. sorban álló teszt sikertelen".format(sorszam)
    print(msg)