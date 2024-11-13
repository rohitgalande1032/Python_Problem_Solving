def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [3, 5, 2 ,9, 7, 1, 8]
print(selection_sort(arr))