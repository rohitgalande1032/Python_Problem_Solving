def merge_sort(arr):
    if len(arr) <=1:
        return arr
    
    mid = len(arr)//2
    
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    new = []
    i, j = 0, 0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i+=1
        else: 
            new.append(right[j])
            j+=1

    new.extend(left[i:])
    new.extend(right[j:])

    return new


arr = [5, 4, 6, 3, 7, 2, 8, 11, 9]
print(merge_sort(arr))

    