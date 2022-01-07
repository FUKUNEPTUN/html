a = input("add meg a könyvnek a címét, entert ha kilépnél             ")
def kalapacs(b):
    if b >= 150:
        print("A", a, "könyv hosszú terjedelmű")
    else:
        print("A ",a , " könyved rövid")
while a != "":
    kalapacs(int(input("add meg az oldalak számát         ")))
    a = input("add meg a könyvnek a címét, entert ha kilépnél             ")
print("A programból sikeresen kiléptél")
