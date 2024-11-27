# You are given an array containing n distinct numbers ranging from 0 to n. Find the missing number.

def missing_number(nums):
    n = len(nums)
    current_sum = 0
    total_sum = n * (n+1)//2

    for num in nums:
        current_sum += num
    
    return total_sum - current_sum


nums = [0, 1, 3, 4, 5, 6]
print(missing_number(nums))