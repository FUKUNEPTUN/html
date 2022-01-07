def paratlen_e(n):
    if n % 2 > 0:
        return True
    else:
        return False

def tenyezo_e(t, n):
    if n % t < 0:
        return "s"
    else:
        return "k"

def tobbszorose_e(t, n):
    return tenyezo_e(n, t)