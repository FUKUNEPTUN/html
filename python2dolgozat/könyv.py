a = input("Add meg a könyvnek a címét, entert ha kilépnél   ")
def kalapacs(b):
    if b >= 150:
        print("A(z)", a, "könyv hosszú terjedelmű")
    else:
        print("A(z) ",a , " könyved rövid")
while a != "":
    kalapacs(int(input("add meg az oldalak számát   ")))
    a = input("add meg a könyvnek a címét, entert ha kilépnél   ")
print("A programból sikeresen kiléptél")
