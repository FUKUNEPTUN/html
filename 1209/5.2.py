napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]

def nap(indulas, ejszakak):
    print(napok[indulas])
    akt_nap = indulas
    for i in range(ejszakak):
        if (akt_nap == 7):
            akt_nap = 0
        else:
            akt_nap += 1

    print(napok[akt_nap])
nap(2, 137)
