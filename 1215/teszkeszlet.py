from teszt import teszt
from feladat import paratlen_e, tenyezo_e, tobbszorose_e

if False:
    teszt(paratlen_e(2))
    teszt(paratlen_e(3))

if False:
    teszt(tenyezo_e(3, 12))
    teszt(not tenyezo_e(5, 12))
    teszt(tenyezo_e(7, 14))
    teszt(not tenyezo_e(7, 15))
    teszt(tenyezo_e(1, 15))
    teszt(tenyezo_e(15, 15))
    teszt(not tenyezo_e(25, 15))
if True:
    teszt(tobbszorose_e(12, 3))
    teszt(tobbszorose_e(12, 4))
    teszt(not tobbszorose_e(12, 5))
    teszt(tobbszorose_e(12, 6))
    teszt(not tobbszorose_e(12, 7))