from itertools import product
a=map(int,input().split())
b=map(int,input().split())
k=list(product(a,b))
for i in k:
    print(i,end=" ")
