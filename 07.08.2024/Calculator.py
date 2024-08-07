a=int(input("Enter a number 1:"))
b=int(input("Enter a number 2:"))
c=str(input("Enter operator(+,-,*,/):"))
if (c=='+'):
    print("Sum of",a,"and",b,"is:",a+b)
elif (c=='-'):
    print("Difference of",a,"and",b,"is:",a-b)
elif (c=='*'):
    print("Product of",a,"and",b,"is:",a*b)
elif (c=='/'):
    print("Division of",a,"and",b,"is:",a/b)
else:
    print("operator is invalid")
