N = 5
for i in range(1, N + 1):
        for j in range(1, i):
                print(" ", end="")
        for j in range(1, N - i + 2):
                print("*", end="")
        print()
