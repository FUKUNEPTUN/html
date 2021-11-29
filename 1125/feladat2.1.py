c = int(10000)
r = 0.08
m = int(12)
t = int(input("évek száma:   "))


fv = c * (1 + r / m) ** ( m * t)
print(fv)
