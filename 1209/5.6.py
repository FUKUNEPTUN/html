xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
def jegyertekelo():
    for i in xs:
        if (i >= 90):
            print("ötös")
        elif  (i >= 80):
            print("négyes")
        elif (i >= 70):
            print("Hármas")
        elif (i >= 60):
            print("kettes")
        else:
            print("egyes")
jegyertekelo()