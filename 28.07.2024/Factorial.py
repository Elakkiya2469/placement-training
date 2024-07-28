def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input("Enter a number: "))  
print(f"Factorial (Recursive) of {num}: {factorial_recursive(num)}")  
print(f"Factorial (Iterative) of {num}: {factorial_iterative(num)}")  
