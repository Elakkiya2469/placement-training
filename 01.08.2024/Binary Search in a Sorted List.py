def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = binary_search(arr, 7)
print(index)