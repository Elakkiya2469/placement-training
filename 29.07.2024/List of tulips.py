def sumOfTuples(lst):
    sum1 = sum(x[0] for x in lst)
    sum2 = sum(x[1] for x in lst)
    return sum1, sum2
lst = [(1, 2), (3, 4), (5, 6)]
print(sumOfTuples(lst))  # Output: (9, 12)
