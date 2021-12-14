napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
indulas = int(input("add meg melyik nap indulsz"))
ejszakak = int(input("add meg hány nap múlva értél haza"))
akt_nap = indulas
k = indulas + ejszakak
for i in range(1):
 print(napok[k])