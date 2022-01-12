a = int(input("add meg az első számot"))
b = int(input("add meg az második számot"))
if a >= 0 and b >= 0:
    print("mindkét számod baba")
elif a < 0 and b < 0:
    print("egyik számod se baba")
elif a > 0 and b < 0:
    print("az első számod baba, de a második gány")
elif a < 0 and b > 0:
    print("az első számod gány, de a második baba")