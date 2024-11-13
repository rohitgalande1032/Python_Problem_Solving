def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j>0 and arr[j-1]>arr[j]: 
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
    return arr

arr = [4, 5, 3, 6, 2, 7, 1]
print(insertion_sort(arr))