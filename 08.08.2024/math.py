    import math
    n=int(input("Enter n: "))
    r=int(input("Enter r: "))
    nCr=math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
    print(f"nCr={nCr}")
