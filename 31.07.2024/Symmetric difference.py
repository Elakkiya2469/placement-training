m=input()
m1=set(map(int,input().split()))
n=input()
n1=set(map(int,input().split()))
k=sorted(set.symmetric_difference(n1,m1))
for i in k:
    print(i)
