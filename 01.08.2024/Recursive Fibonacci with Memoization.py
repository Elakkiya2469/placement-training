def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
n = 10
fib_sequence = [fibonacci(i) for i in range(n)]
print(fib_sequence)
