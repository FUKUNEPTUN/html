ak = int(input("hány óra van:   "))
ker = int(input("hány óra mulva szóljon?:   "))
if (ak + ker < 24):
    eredm = ak + ker
    print(eredm) 
else: 
    eredm1 = ( ak + ker ) % 24
    print(eredm1)
