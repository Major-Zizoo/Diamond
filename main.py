def print_diamond(n):
    for i in range(1,n+1):
     for j in range(n-i):
        print("",end="")
        for k in range(1,i*2):
           print(k, end="")
        print()

    for i in range(n-1,0,-1):
     for j in range(n-i):
        print("",end="")
        for k in range(1,i*2):
           print(k, end="")
        print()     