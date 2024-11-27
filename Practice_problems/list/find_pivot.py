#Find the pivot index where the sum of the numbers to the left equals the sum of the numbers to the right.

def pivot(nums):
    total_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        if left_sum == total_sum - left_sum - num:
            return i
        left_sum += num
    return -1


nums = [1, 7, 3, 6, 5, 6]
print("pivot index is ", pivot(nums))

