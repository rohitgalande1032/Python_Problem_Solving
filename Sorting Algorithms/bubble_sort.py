# Algorithm :-

# Start with the first element in the array.
# Compare the current element with the next element.
# If the current element is greater than the next element, swap them.
# Move to the next element and repeat steps 2–3 until the end of the array.
# Repeat, the whole process for all elements, largest element "bubbles up" to its correct position at the end of the array with each pass.
# Continue until no more swaps are needed.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    arr = [4, 3, 5, 9, 8, 7, 2, 6, 1]
    print(f"Bubble Sort : {bubble_sort(arr)}")