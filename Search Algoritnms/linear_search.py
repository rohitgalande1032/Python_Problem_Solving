def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [4, 3, 5, 9, 7, 1, 6]
target = 7
print(f"Element found at index - {linear_search(arr, target)}")
