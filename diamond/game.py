
diamond = int(input("enter "))  
for x in range(diamond):
    print(" " * (diamond-x), "*"*(x * 2 + 1))
for x in range(diamond-2, -1, -1):
    print(" "*(diamond-x), "*"*(x*2+1))