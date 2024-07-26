a = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if a <= 0:
   print("Please enter a positive integer")
elif a == 1:
   print("Fibonacci sequence upto",a,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < a:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
