n = int(input("Enter number of rows:"))
start = 1
total = n * (n + 1) // 2
end = total + n
for i in range(n):
    print(' ' * (2 * i), end='')
    a = start + (n - i - 1)
    for num in range(start,a):
        print(num, end='*')
    start = a
    b = end - (n - i - 1)
    for num in range(b, end):
        print(num, end='*')
    end -= (n - i)
    print()
    start = end
