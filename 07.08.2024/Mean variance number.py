import numpy as np

array = np.array([[0, 1, 2], [3, 4, 5]])
mean = np.mean(array, axis=1)
std_dev = np.std(array, axis=1)
variance = np.var(array, axis=1)

print("Original array:", array)
print("Mean:", mean)
print("Standard deviation:", std_dev)
print("Variance:", variance)
