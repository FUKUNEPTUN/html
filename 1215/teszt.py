import sys

def teszt(tesztEset):
    sorszam = sys._getframe(1).f_lineno
    if tesztEset:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = "A(z) {0}. sorban álló teszt sikertelen.".format(sorszam)

    print(msg)