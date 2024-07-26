def simple_interest(p,r,t):
    si = (p * r * t)/100
    return si
p=int(input("Enter principal amount"))
r=int(input("Enter rate of interest"))
t=int(input("Enter time period"))
print('The Simple Interest is', simple_interest(p, r, t))
