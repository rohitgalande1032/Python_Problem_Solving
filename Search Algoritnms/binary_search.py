# To use Binary search array must be in sorted order

def binary_search(arr, target):
    n= len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid
        
        elif target < arr[mid]:
            high = mid-1
        else:
            low = mid+1

    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 1
print(binary_search(arr, target))